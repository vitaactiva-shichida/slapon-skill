"""Resolve compatible shared definitions and apply customer-owned differences.

Only the public repository is fetched. Customer settings, logos and the kit code
remain local. A job is pinned once; new jobs resolve the current compatible ref.
"""
import argparse
import copy
import hashlib
import json
import re
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path, PurePosixPath

from verify_kit import verify


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def safe_path(value):
    p = PurePosixPath(value)
    if not value or p.is_absolute() or '..' in p.parts or '\\' in value or ':' in value:
        raise ValueError('Invalid relative path')
    return value


def local_path(root, relative):
    path = (root / safe_path(relative)).resolve()
    if not path.is_relative_to(root.resolve()) or not path.is_file():
        raise ValueError('Missing or outside kit file: '+relative)
    return path


class Repository:
    def __init__(self, url, local=None):
        match = re.fullmatch(r'https://github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+?)(?:\.git)?/?', url)
        if not match:
            raise ValueError('Only a configured public GitHub repository is supported')
        self.name = match[1]
        self.local = local.resolve() if local else None

    def get(self, url):
        request = urllib.request.Request(url, headers={'User-Agent': 'Slapon-compatible-kit/1'})
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.read()
        except (urllib.error.URLError, TimeoutError) as exc:
            raise ValueError('Cannot retrieve required shared definition; retry with a GitHub connector') from exc

    def resolve(self, ref):
        if re.fullmatch('[0-9a-f]{40}', ref):
            return ref
        if not re.fullmatch('[A-Za-z0-9_./-]+', ref) or '..' in ref:
            raise ValueError('Invalid compatibility ref')
        if self.local:
            # Local source is only used by release checks, never inferred at runtime.
            state=hashlib.sha256(ref.encode())
            for file in sorted(self.local.rglob('*')):
                if file.is_file() and not set(file.relative_to(self.local).parts)&{'.git','__pycache__'}:
                    state.update(file.relative_to(self.local).as_posix().encode())
                    state.update(hashlib.sha256(file.read_bytes()).digest())
            return state.hexdigest()[:40]
        data = json.loads(self.get('https://api.github.com/repos/'+self.name+'/commits/'+urllib.parse.quote(ref, safe='')))
        sha = data['sha']
        if not re.fullmatch('[0-9a-f]{40}', sha):
            raise ValueError('GitHub did not return a resolved commit')
        return sha

    def file(self, sha, path):
        safe_path(path)
        if self.local:
            return local_path(self.local, path).read_bytes()
        return self.get('https://raw.githubusercontent.com/'+self.name+'/'+sha+'/'+urllib.parse.quote(path, safe='/'))


def merge_known(target, changes):
    """Only explicitly supplied, existing fields override inherited definitions."""
    for key, value in changes.items():
        if key not in target:
            raise ValueError('Unknown customer design override: '+key)
        if isinstance(value, dict):
            if not isinstance(target[key], dict):
                raise ValueError('Design override type mismatch: '+key)
            merge_known(target[key], value)
        else:
            target[key] = copy.deepcopy(value)


def effective_design(specs, customer, overrides, kit):
    family = customer['runtime']['design_system']
    if overrides.get('schema_version') != 1 or overrides.get('design_system') != family:
        raise ValueError('Customer overrides use a different design system')
    result = copy.deepcopy(specs)
    for path, changes in overrides.get('spec_overrides', {}).items():
        if path not in result:
            raise ValueError('Unknown customer specification override: '+path)
        merge_known(result[path], changes)
    logos = overrides['logos']
    for variant in ['color', 'white']:
        record = logos[variant]
        logo = local_path(kit, record['file'])
        if digest(logo.read_bytes()) != record['sha256']:
            raise ValueError('Customer logo hash mismatch: '+variant)
    placements = copy.deepcopy(overrides['logo_placements'])
    for slot in ['header', 'cover']:
        box = placements[slot]['box']
        if len(box) != 4 or not all(isinstance(n, (int,float)) for n in box) or min(box[2:]) <= 0:
            raise ValueError('Invalid customer logo placement: '+slot)
    if family == 'standard':
        result['specs/components/header.json']['logo'] = placements['header']['box']
        for page in ['cover', 'message']:
            watermark = placements.get(page+'_watermark')
            if watermark:
                # An explicit false also survives future changes to shared defaults.
                result['specs/components/'+page+'-watermark.json'].update(copy.deepcopy(watermark))
    return dict(design_system=family, specs=result, resolvedTheme=overrides['resolvedTheme'],
                logos=logos, logo_placements=placements, tuning=overrides.get('tuning', {}),
                precedence=['current shared definition','explicit customer overrides','current job instructions'],
                customer_id=customer['id'])


def resolve(kit, output, repository_root=None):
    kit, output = kit.resolve(), output.resolve()
    customer = read(kit/'customer.json')
    runtime = customer['runtime']
    if runtime.get('mode') != 'shared-design-v1':
        raise ValueError('This loader requires a shared-design kit')
    if output == kit or output.is_relative_to(kit) or kit.is_relative_to(output):
        raise ValueError('Keep the job runtime outside the installed kit')
    local_files = [kit/'customer.json', local_path(kit, runtime['local']['overrides']),
                   local_path(kit, runtime['local']['license'])]
    overrides = read(local_files[1])
    for record in overrides['logos'].values():
        local_files.append(local_path(kit, record['file']))
    input_hashes = {str(p.relative_to(kit)):digest(p.read_bytes()) for p in local_files}
    if output.exists():
        lock = read(output/'runtime-lock.json')
        if lock['customer_id'] != customer['id'] or lock['kit_files_sha256'] != input_hashes:
            raise ValueError('Job runtime belongs to another or changed kit; start a new job snapshot')
        for path, sha in lock['files_sha256'].items():
            if digest(local_path(output,path).read_bytes()) != sha:
                raise ValueError('Job runtime was modified; do not mix revisions')
        return lock
    source = runtime['github']
    repo = Repository(source['repository'], repository_root)
    registry_sha = repo.resolve(source.get('registry_ref','main'))
    compatibility = json.loads(repo.file(registry_sha, source['compatibility_path']))
    if compatibility.get('schema_version') != 1:
        raise ValueError('Unsupported compatibility registry')
    generation = compatibility['generations'].get(str(runtime['compatibility_major']))
    if not generation or generation.get('status') != 'active':
        raise ValueError('Unsupported kit generation; do not fall back to the newest generation')
    selected = generation['ref']
    sha = registry_sha if selected == source.get('registry_ref','main') else repo.resolve(selected)
    families = generation['design_systems']
    family = runtime['design_system']
    if family not in families:
        raise ValueError('Design system is not available for this kit generation')
    # Check possession before downloading the production workflow and design.
    license_registry = json.loads(repo.file(registry_sha, compatibility['license_registry']))
    evidence = verify(customer, read(local_files[2]), license_registry)
    files = {}
    for path in [generation['common'], families[family]['manifest'], families[family]['source']]:
        files[safe_path(path)] = repo.file(sha,path)
    guide = families[family].get('guide')
    if guide:
        files[safe_path(guide)] = repo.file(sha,guide)
    manifest = json.loads(files[families[family]['manifest']])
    specs = {}
    for record in manifest['specs']:
        data = repo.file(sha,record['path'])
        if digest(data) != record['sha256']:
            raise ValueError('Shared design specification hash mismatch')
        files[record['path']] = data
        specs[record['key']] = json.loads(data)
    design = effective_design(specs, customer, overrides, kit)
    files['effective-design.json'] = (json.dumps(design,ensure_ascii=False,indent=2)+'\n').encode()
    files['license-check.json'] = (json.dumps(evidence,ensure_ascii=False,indent=2)+'\n').encode()
    lock = dict(schema_version=1,customer_id=customer['id'],compatibility_major=runtime['compatibility_major'],
                design_system=family,repository=source['repository'],selected_ref=selected,
                registry_commit=registry_sha,resolved_commit=sha,kit_files_sha256=input_hashes,
                files_sha256={p:digest(b) for p,b in files.items()},
                source_mode='local-release-check' if repository_root else 'github',
                shared_base_url='https://raw.githubusercontent.com/'+repo.name+'/'+sha+'/',
                design_source=families[family]['source'],catalog=generation['catalog'],
                access_valid=True,license_id=evidence['license_id'])
    output.mkdir(parents=True)
    for path, data in files.items():
        dest=output/safe_path(path);dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
    (output/'runtime-lock.json').write_text(json.dumps(lock,ensure_ascii=False,indent=2)+'\n')
    return lock


if __name__ == '__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--kit',type=Path,required=True)
    ap.add_argument('--output-dir',type=Path,required=True)
    ap.add_argument('--source-repo',type=Path,help='Explicit local release-check fixture only')
    args=ap.parse_args()
    try:
        result=resolve(args.kit,args.output_dir,args.source_repo)
        print(json.dumps({key:result[key] for key in ['customer_id','compatibility_major','design_system','resolved_commit','source_mode','access_valid']}))
    except (ValueError,KeyError,OSError) as exc:
        ap.exit(2,str(exc)+'\n')
