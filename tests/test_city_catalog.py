"""Guard coverage and provenance when the city directory is maintained."""
from copy import deepcopy
import html
from pathlib import Path
import re
import sys
import unittest
from urllib.parse import unquote, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import cities


class CityCatalogChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = cities.load()
        cls.report = cities.load(cities.REPORT)

    def test_committed_catalog_is_complete(self):
        self.assertEqual(cities.validate(self.catalog), [])
        self.assertEqual(cities.validate_report(self.catalog, self.report), [])

    def test_missing_state_or_duplicate_place_cannot_pass(self):
        for change in ['remove', 'duplicate']:
            with self.subTest(change=change):
                data = deepcopy(self.catalog)
                if change == 'remove':
                    data['cities'] = [c for c in data['cities'] if c['state_code'] != 'AK']
                else:
                    data['cities'][1] = deepcopy(data['cities'][0])
                self.assertTrue(cities.validate(data))

    def test_every_city_needs_each_source_category(self):
        for category in cities.CATEGORIES:
            with self.subTest(category=category):
                data = deepcopy(self.catalog)
                data['cities'][0]['sources'][category] = []
                self.assertTrue(cities.validate(data))

    def test_wrong_role_or_unknown_source_is_rejected(self):
        for replacement in ['unknown-source', self.catalog['cities'][0]['sources']['water'][0]]:
            with self.subTest(replacement=replacement):
                data = deepcopy(self.catalog)
                data['cities'][0]['sources']['power'] = [replacement]
                self.assertTrue(cities.validate(data))

    def test_rank_and_hawaii_vintage_are_preserved(self):
        data = deepcopy(self.catalog)
        data['cities'][0]['rank'], data['cities'][1]['rank'] = 2, 1
        self.assertTrue(cities.validate(data))
        data = deepcopy(self.catalog)
        next(c for c in data['cities'] if c['state_code'] == 'HI')['population_date'] = '2025-07-01'
        self.assertTrue(cities.validate(data))

    def test_credentials_cannot_enter_source_links(self):
        for url in ['https://example.com/feed?api_key=test-value', 'https://name:password@example.com/feed']:
            with self.subTest(url=url):
                data = deepcopy(self.catalog)
                data['sources'][0]['url'] = url
                self.assertTrue(cities.validate(data))

    def test_snapshot_must_cover_the_current_sources(self):
        report = deepcopy(self.report)
        report['checks'].pop()
        self.assertTrue(cities.validate_report(self.catalog, report))

    def test_blocked_retrieval_is_visible_without_discarding_source(self):
        report = deepcopy(self.report)
        check = report['checks'][0]
        check.update(status=403, result='http-error')
        self.assertEqual(cities.validate_report(self.catalog, report), [])
        self.assertIn('HTTP 403; review access', cities.render(self.catalog, report)[cities.ROOT / 'cities/SOURCES.md'])

    def test_generated_pages_are_current(self):
        for path, expected in cities.render(self.catalog, self.report).items():
            with self.subTest(path=path.name):
                self.assertEqual(path.read_text(encoding='utf-8'), expected)

    def test_internal_markdown_destinations_exist(self):
        root = cities.ROOT
        paths = [root / name for name in ['README.md', 'LIBRARY.md', 'CITIES.md', 'CONTRIBUTING.md', 'ROADMAP.md']]
        for directory in ['docs', 'sources', 'cities']:
            paths.extend((root / directory).rglob('*.md'))
        anchors = {}
        for path in paths:
            text = path.read_text(encoding='utf-8')
            for match in re.finditer(r'\]\(([^\s)]+)\)', text):
                target = match.group(1).strip('<>')
                parts = urlsplit(target)
                if parts.scheme or parts.netloc:
                    continue
                dest = (path.parent / unquote(parts.path)).resolve() if parts.path else path.resolve()
                with self.subTest(file=str(path.relative_to(root)), target=target):
                    self.assertTrue(dest.is_file(), f'Missing internal file: {target}')
                    if not parts.fragment or dest.suffix != '.md' or not dest.is_file():
                        continue
                    if dest not in anchors:
                        body = dest.read_text(encoding='utf-8')
                        explicit = re.findall(r'<a id="([^"]+)"', body)
                        headings = re.findall(r'^#{1,6} (.+)$', body, re.M)
                        anchors[dest] = set(explicit) | {re.sub(r'[^\w\- ]', '', html.unescape(h).lower()).replace(' ', '-') for h in headings}
                    self.assertIn(unquote(parts.fragment), anchors[dest], f'Missing anchor: {target}')


if __name__ == '__main__':
    unittest.main()
