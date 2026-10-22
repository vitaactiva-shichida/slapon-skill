"""Compatible updates, customer geometry preservation and possession checks."""
import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from resolve_kit import resolve,effective_design,safe_path
from verify_kit import binding,verify


def write(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value))


class SharedRuntimeTests(unittest.TestCase):
    def setUp(self):
        temp=tempfile.TemporaryDirectory();self.addCleanup(temp.cleanup)
        self.work=Path(temp.name);self.kit=self.work/'kit';self.repo=self.work/'repository'
        self.kit.mkdir();self.repo.mkdir()
        self.customer=dict(id='fixture',name='Fixture',runtime=dict(mode='shared-design-v1',
            compatibility_major=1,design_system='standard',github=dict(repository='https://github.com/example/slapon',
            registry_ref='main',compatibility_path='compatibility.json'),
            local=dict(overrides='overrides.json',license='license.json')))
        self.license=dict(schema_version=1,license_id='opaque-fixture-id',customer_id='fixture',
                          compatibility_major=1,design_system='standard',code='fixture-code-for-tests-only-1234567890')
        self.registry=dict(schema_version=1,licenses={self.license['license_id']:dict(status='active',binding_sha256=binding(self.license))})
        logo=self.kit/'logo.svg';logo.write_text('<svg xmlns="http://www.w3.org/2000/svg"/>')
        record=dict(file='logo.svg',sha256=hashlib.sha256(logo.read_bytes()).hexdigest())
        self.overrides=dict(schema_version=1,design_system='standard',resolvedTheme=dict(main='#123456'),
            logos=dict(color=record,white=record),logo_placements=dict(header=dict(box=[1400,20,160,45]),
            cover=dict(box=[90,80,210,60]),pages={},cover_watermark=dict(enabled=False,translate=[1300,870],opacity=.4)),
            spec_overrides={})
        write(self.kit/'customer.json',self.customer);write(self.kit/'license.json',self.license)
        write(self.kit/'overrides.json',self.overrides);write(self.repo/'licenses.json',self.registry)
        self.specs={'specs/design.json':dict(title_y=114),
                    'specs/components/header.json':dict(logo=[1466,23,104,29]),
                    'specs/components/cover-watermark.json':dict(enabled=True,translate=[1400,900],opacity=.2)}
        self.publish_specs()
        self.compat=dict(schema_version=1,license_registry='licenses.json',generations={'1':dict(status='active',ref='main',
             common='SKILL.md',catalog='catalog.json',design_systems={'standard':dict(source='design/index.html',manifest='design/manifest.json')})})
        write(self.repo/'compatibility.json',self.compat)
        (self.repo/'SKILL.md').write_text('Shared workflow')
        (self.repo/'design/index.html').write_text('<html>Fixture template</html>')

    def publish_specs(self):
        records=[]
        for key,data in self.specs.items():
            path=self.repo/'design'/key;write(path,data)
            records.append(dict(key=key,path='design/'+key,sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
        write(self.repo/'design/manifest.json',dict(specs=records))

    def run_job(self,name):return resolve(self.kit,self.work/name,self.repo)
    def effective(self,name):return json.loads((self.work/name/'effective-design.json').read_text())

    def test_new_job_gets_improvements_and_retains_customer_logo_geometry(self):
        first=self.run_job('first');before=self.effective('first')
        self.specs['specs/design.json']['title_y']=120
        self.specs['specs/components/header.json']['logo']=[1000,0,500,100]
        self.specs['specs/components/cover-watermark.json'].update(translate=[999,999],opacity=.1)
        self.publish_specs()
        second=self.run_job('second');after=self.effective('second')
        self.assertNotEqual(first['resolved_commit'],second['resolved_commit'])
        self.assertEqual(before['specs']['specs/design.json']['title_y'],114)
        self.assertEqual(after['specs']['specs/design.json']['title_y'],120)
        self.assertEqual(after['specs']['specs/components/header.json']['logo'],[1400,20,160,45])
        watermark=after['specs']['specs/components/cover-watermark.json']
        self.assertEqual(watermark['translate'],[1300,870]);self.assertEqual(watermark['opacity'],.4)
        self.assertFalse(watermark['enabled'])
        self.assertEqual(self.run_job('first'),first)
        self.assertEqual(self.effective('first'),before)

    def test_branch_mapping_changes_without_reinstalling_customer_kit(self):
        self.compat['generations']['1']['ref']='v1';write(self.repo/'compatibility.json',self.compat)
        result=self.run_job('old-generation')
        self.assertEqual(result['selected_ref'],'v1');self.assertEqual(result['compatibility_major'],1)

    def test_missing_wrong_cross_customer_and_revoked_codes_fail_closed(self):
        for change in [dict(code='wrong-code-which-is-at-least-32-characters'),dict(customer_id='another')]:
            bad={**self.license,**change}
            with self.assertRaises(ValueError):verify(self.customer,bad,self.registry)
        with self.assertRaises(ValueError):verify(self.customer,{},self.registry)
        revoked=copy.deepcopy(self.registry);revoked['licenses'][self.license['license_id']]['status']='revoked'
        with self.assertRaises(ValueError):verify(self.customer,self.license,revoked)
        write(self.kit/'license.json',{**self.license,'code':'wrong-code-which-is-at-least-32-characters'})
        with self.assertRaises(ValueError):self.run_job('blocked')
        self.assertFalse((self.work/'blocked').exists())

    def test_unsupported_generation_has_no_latest_fallback(self):
        self.customer['runtime']['compatibility_major']=2;write(self.kit/'customer.json',self.customer)
        with self.assertRaisesRegex(ValueError,'Unsupported kit generation'):self.run_job('blocked')
        self.assertFalse((self.work/'blocked').exists())

    def test_customer_logo_tampering_and_unknown_overrides_are_rejected(self):
        (self.kit/'logo.svg').write_text('replaced')
        with self.assertRaisesRegex(ValueError,'logo hash'):self.run_job('blocked')
        self.assertFalse((self.work/'blocked').exists())
        for relative in ['../outside','/tmp/outside','https://example.com','a\\b']:
            with self.assertRaises(ValueError):safe_path(relative)

    def test_snapshot_or_kit_edits_require_a_new_job(self):
        self.run_job('job');(self.work/'job/effective-design.json').write_text('{}')
        with self.assertRaisesRegex(ValueError,'runtime was modified'):self.run_job('job')
        self.overrides['resolvedTheme']['main']='#FFFFFF';write(self.kit/'overrides.json',self.overrides)
        with self.assertRaisesRegex(ValueError,'changed kit'):self.run_job('job')

    def test_public_license_record_contains_no_code_or_customer_identity(self):
        record=self.registry['licenses'][self.license['license_id']]
        self.assertEqual(set(record),{'status','binding_sha256'})
        text=json.dumps(record);self.assertNotIn(self.license['code'],text);self.assertNotIn('fixture',text)

    def test_unknown_customer_override_does_not_silently_override_future_schema(self):
        self.overrides['spec_overrides']={'specs/design.json':{'misspelled_title_y':20}}
        write(self.kit/'overrides.json',self.overrides)
        with self.assertRaisesRegex(ValueError,'Unknown customer design override'):self.run_job('blocked')


if __name__=='__main__':unittest.main()
