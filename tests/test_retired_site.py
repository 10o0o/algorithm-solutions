"""The retired presentation layer must not return via a study checkpoint change."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class RetiredSiteTests(unittest.TestCase):
    def test_site_and_deploy_jobs_are_absent(self):
        self.assertFalse((ROOT / 'web').exists())
        workflow = (ROOT / '.github/workflows/validate.yml').read_text()
        for forbidden in ('deploy-pages', 'upload-pages-artifact', 'configure-pages',
                          'pages: write', 'id-token: write', 'working-directory: web'):
            self.assertNotIn(forbidden, workflow)
        for required in ('unittest discover', 'validate_notes.py', 'uv lock --check'):
            self.assertIn(required, workflow)

    def test_learning_sources_remain(self):
        for path in ('STATE.md', 'ROADMAP.md', 'knowledge', 'contests', 'atcoder',
                     'codeforces', 'cses', 'leetcode'):
            self.assertTrue((ROOT / path).exists(), path)
        self.assertNotIn('https://10o0o.github.io/algorithm-solutions/',
                         (ROOT / 'README.md').read_text())

if __name__ == '__main__':
    unittest.main()
