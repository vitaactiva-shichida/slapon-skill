#!/usr/bin/env python3
"""Inspect a final PPTX package. This does not certify appearance or editing."""
import argparse
import hashlib
import io
import json
import posixpath
import sys
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

NS = {
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'svg': 'http://schemas.microsoft.com/office/drawing/2016/SVG/main',
}
RID = '{' + NS['r'] + '}embed'


def inspect(path, expected_slides):
    findings, warnings, slides, media = [], [], [], []
    report = {
        'schema': 'slapon-package-audit.v1', 'file': str(path.resolve()),
        'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
        'claim_boundary': 'Package structure and image decoding only. Content accuracy, visual comparison, fonts in PowerPoint and edit operations require separate evidence.',
        'manual_checks_complete': False,
        'findings': findings, 'warnings': warnings, 'slides': slides, 'media': media,
    }
    try:
        from PIL import Image
    except ImportError:
        report.update(status='unverified', findings=['Pillow is required for full raster decoding.'])
        return report
    try:
        with zipfile.ZipFile(path) as z:
            names = z.namelist()
            if len(names) != len(set(names)):
                findings.append('Duplicate ZIP member names')
            bad = z.testzip()
            if bad:
                findings.append('ZIP CRC failure: ' + bad)
            name_set = set(names)
            roots, relations = {}, {}
            for name in names:
                if name.endswith(('.xml', '.rels', '.svg')):
                    try:
                        roots[name] = ET.fromstring(z.read(name))
                    except ET.ParseError as e:
                        findings.append(f'Invalid XML: {name}: {e}')
            for name, root in roots.items():
                if not name.endswith('.rels'):
                    continue
                folder, filename = name.rsplit('/_rels/', 1) if '/_rels/' in name else ('', name)
                owner = posixpath.join(folder, filename[:-5]) if folder else ''
                links = {}
                for rel in root:
                    rid, target = rel.get('Id'), rel.get('Target', '')
                    if rid in links:
                        findings.append(f'Duplicate relationship ID: {name}: {rid}')
                    if rel.get('TargetMode') == 'External':
                        links[rid] = None
                        continue
                    target = (target.lstrip('/') if target.startswith('/') else
                              posixpath.normpath(posixpath.join(folder, target)))
                    links[rid] = target
                    if target not in name_set:
                        findings.append(f'Missing relationship target: {name}: {target}')
                relations[owner] = links
            decoded = {}
            for name in names:
                if not name.startswith('ppt/media/'):
                    continue
                suffix = Path(name).suffix.lower()
                if suffix in ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tif', '.tiff', '.webp'):
                    try:
                        with Image.open(io.BytesIO(z.read(name))) as im:
                            im.load()
                            info = {'path': name, 'size': list(im.size), 'decode': 'pass'}
                            if 'A' in im.getbands():
                                info['fully_transparent'] = im.getchannel('A').getbbox() is None
                            decoded[name] = info
                            media.append(info)
                    except Exception as e:
                        findings.append(f'Raster decode failed: {name}: {e}')
                elif suffix == '.svg':
                    if name in roots:
                        if roots[name].tag.rsplit('}', 1)[-1] != 'svg':
                            findings.append(f'Not an SVG document: {name}')
                        media.append({'path': name, 'xml': 'pass'})
                else:
                    warnings.append(f'Media not decoded by this audit: {name}')
            pres = roots.get('ppt/presentation.xml')
            if pres is None:
                findings.append('Missing or invalid presentation.xml')
            else:
                slide_refs = pres.findall('p:sldIdLst/p:sldId', NS)
                if len(slide_refs) != expected_slides:
                    findings.append(f'Expected {expected_slides} slides; found {len(slide_refs)}')
                slide_size = pres.find('p:sldSz', NS)
                canvas = [int(slide_size.get(k)) for k in ('cx', 'cy')] if slide_size is not None else None
                report['slide_size_emu'] = canvas
                for page, ref in enumerate(slide_refs, 1):
                    target = relations.get('ppt/presentation.xml', {}).get(ref.get('{' + NS['r'] + '}id'))
                    root = roots.get(target)
                    if root is None:
                        findings.append(f'Missing slide content for page {page}')
                        continue
                    ids = [n.get('id') for n in root.findall('.//p:cNvPr', NS)]
                    if len(ids) != len(set(ids)):
                        findings.append(f'Duplicate object IDs on page {page}')
                    id_set = set(ids)
                    connectors = root.findall('.//p:cxnSp', NS)
                    for line in connectors:
                        nv = line.find('p:nvCxnSpPr/p:cNvPr', NS)
                        label = nv.get('name') if nv is not None else 'unnamed'
                        for side in ('stCxn', 'endCxn'):
                            end = line.find('p:nvCxnSpPr/p:cNvCxnSpPr/a:' + side, NS)
                            if end is None or end.get('id') not in id_set:
                                findings.append(f'Unbound connector {side}: page {page}, {label}. Use a native line for an intentional free arrow.')
                    fonts = sorted({n.get('typeface') for n in root.iter() if n.tag.rsplit('}', 1)[-1] in ('latin', 'ea', 'cs') and n.get('typeface')})
                    pictures = root.findall('.//p:pic', NS)
                    svg_count = 0
                    for pic in pictures:
                        blip = pic.find('.//a:blip', NS)
                        svg = pic.find('.//svg:svgBlip', NS)
                        links = relations.get(target, {})
                        if svg is not None:
                            svg_count += 1
                            svg_path = links.get(svg.get(RID))
                            png_path = links.get(blip.get(RID)) if blip is not None else None
                            png = decoded.get(png_path)
                            if not svg_path or not svg_path.endswith('.svg') or svg_path not in roots:
                                findings.append(f'Invalid SVG reference on page {page}')
                            if not png or not png_path.lower().endswith('.png'):
                                findings.append(f'SVG has no decoded PNG fallback on page {page}')
                            elif min(png['size']) <= 1 or png.get('fully_transparent'):
                                findings.append(f'Degenerate SVG PNG fallback on page {page}: {png_path}')
                        xf = pic.find('p:spPr/a:xfrm/a:ext', NS)
                        if xf is not None and canvas and all(int(xf.get(k, 0)) >= canvas[j] * .95 for j, k in enumerate(('cx', 'cy'))):
                            warnings.append(f'Near-full-slide image on page {page}: verify it is an approved clean background, not a completed slide under editable objects.')
                    slides.append({'page': page, 'part': target, 'native_text_runs': len(root.findall('.//a:t', NS)),
                                   'native_shapes': len(root.findall('.//p:sp', NS)), 'connectors': len(connectors),
                                   'pictures': len(pictures), 'svg_objects': svg_count, 'fonts': fonts})
    except (zipfile.BadZipFile, KeyError, OSError, ValueError) as e:
        findings.append(f'Package inspection failed: {e}')
    report['status'] = 'fail' if findings else 'package_pass_manual_checks_required'
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pptx', type=Path)
    parser.add_argument('--expected-slides', required=True, type=int)
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    if args.expected_slides < 1:
        parser.error('--expected-slides must be positive')
    if args.out and args.out.resolve() == args.pptx.resolve():
        parser.error('--out must not overwrite the input PowerPoint')
    try:
        result = inspect(args.pptx, args.expected_slides)
    except OSError as e:
        parser.exit(2, f'Cannot read input: {e}\n')
    output = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(output, encoding='utf-8')
    print(output, end='')
    return 0 if result['status'] == 'package_pass_manual_checks_required' else 2


if __name__ == '__main__':
    sys.exit(main())
