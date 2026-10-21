"""Regression checks for broken image fallbacks and connector references."""
import importlib.util
import io
import tempfile
import unittest
import zipfile
from pathlib import Path
from PIL import Image

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/audit_pptx.py'
spec = importlib.util.spec_from_file_location('audit_pptx', SCRIPT)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


def fixture(path, raster=None, endpoint='2', missing_media=False):
    if raster is None:
        out = io.BytesIO()
        Image.new('RGBA', (16, 16), (0, 120, 200, 255)).save(out, format='PNG')
        raster = out.getvalue()
    a, p, r, svg = (audit.NS[k] for k in ('a', 'p', 'r', 'svg'))
    rel = 'http://schemas.openxmlformats.org/package/2006/relationships'
    files = {
        'ppt/presentation.xml': f'<p:presentation xmlns:p="{p}" xmlns:r="{r}"><p:sldIdLst><p:sldId id="256" r:id="r1"/></p:sldIdLst><p:sldSz cx="16000" cy="9000"/></p:presentation>',
        'ppt/_rels/presentation.xml.rels': f'<Relationships xmlns="{rel}"><Relationship Id="r1" Target="slides/slide1.xml"/></Relationships>',
        'ppt/slides/slide1.xml': f'<p:sld xmlns:p="{p}" xmlns:a="{a}" xmlns:r="{r}" xmlns:svg="{svg}"><p:cSld><p:spTree><p:sp><p:nvSpPr><p:cNvPr id="2" name="actor"/></p:nvSpPr></p:sp><p:cxnSp><p:nvCxnSpPr><p:cNvPr id="3" name="line"/><p:cNvCxnSpPr><a:stCxn id="2" idx="0"/><a:endCxn id="{endpoint}" idx="1"/></p:cNvCxnSpPr></p:nvCxnSpPr></p:cxnSp><p:pic><p:nvPicPr><p:cNvPr id="4" name="icon"/></p:nvPicPr><p:blipFill><a:blip r:embed="png"><a:extLst><a:ext><svg:svgBlip r:embed="svg"/></a:ext></a:extLst></a:blip></p:blipFill></p:pic></p:spTree></p:cSld></p:sld>',
        'ppt/slides/_rels/slide1.xml.rels': f'<Relationships xmlns="{rel}"><Relationship Id="png" Target="../media/icon.png"/><Relationship Id="svg" Target="../media/icon.svg"/></Relationships>',
        'ppt/media/icon.svg': '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"><rect width="16" height="16" fill="blue"/></svg>',
    }
    if not missing_media:
        files['ppt/media/icon.png'] = raster
    with zipfile.ZipFile(path, 'w') as z:
        for name, content in files.items():
            z.writestr(name, content)


class PackageAuditTest(unittest.TestCase):
    def result(self, expected=1, **kwargs):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'test.pptx'
            fixture(path, **kwargs)
            return audit.inspect(path, expected)

    def test_valid_package_does_not_claim_visual_or_edit_success(self):
        report = self.result()
        self.assertEqual(report['status'], 'package_pass_manual_checks_required')
        self.assertFalse(report['manual_checks_complete'])
        self.assertEqual(report['slides'][0]['svg_objects'], 1)

    def test_corrupt_png_is_rejected(self):
        self.assertTrue(any('Raster decode failed' in f for f in self.result(raster=b'broken PNG')['findings']))

    def test_one_pixel_placeholder_is_rejected(self):
        out = io.BytesIO()
        Image.new('RGBA', (1, 1), 'blue').save(out, format='PNG')
        self.assertTrue(any('Degenerate' in f for f in self.result(raster=out.getvalue())['findings']))

    def test_transparent_placeholder_is_rejected(self):
        out = io.BytesIO()
        Image.new('RGBA', (16, 16), (0, 0, 0, 0)).save(out, format='PNG')
        self.assertTrue(any('Degenerate' in f for f in self.result(raster=out.getvalue())['findings']))

    def test_missing_media_is_rejected(self):
        self.assertTrue(any('Missing relationship target' in f for f in self.result(missing_media=True)['findings']))

    def test_missing_connector_target_is_rejected(self):
        self.assertTrue(any('Unbound connector' in f for f in self.result(endpoint='999')['findings']))

    def test_wrong_page_count_is_rejected(self):
        self.assertTrue(any('Expected 5 slides' in f for f in self.result(expected=5)['findings']))


if __name__ == '__main__':
    unittest.main()
