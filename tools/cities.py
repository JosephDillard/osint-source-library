#!/usr/bin/env python3
"""Validate, search and render the 50-state city source library (standard library only)."""
import argparse
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import html
import json
from pathlib import Path
import re
import sys
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from catalog import unique_keys, valid_date, valid_url

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'catalog/cities.json'
REPORT = ROOT / 'catalog/city-link-check.json'
CATEGORIES = {'emergency', 'public-safety', 'water', 'power'}
KINDS = {'web-reference', 'alert-page', 'registration-portal', 'outage-reference', 'provider-portal'}
METHODS = {'official-directory-link', 'publisher-reference', 'publisher-search-evidence'}
STATES = {line.split(' ', 2)[0]: tuple(line.split(' ', 2)[1:]) for line in '''01 AL Alabama
02 AK Alaska
04 AZ Arizona
05 AR Arkansas
06 CA California
08 CO Colorado
09 CT Connecticut
10 DE Delaware
12 FL Florida
13 GA Georgia
15 HI Hawaii
16 ID Idaho
17 IL Illinois
18 IN Indiana
19 IA Iowa
20 KS Kansas
21 KY Kentucky
22 LA Louisiana
23 ME Maine
24 MD Maryland
25 MA Massachusetts
26 MI Michigan
27 MN Minnesota
28 MS Mississippi
29 MO Missouri
30 MT Montana
31 NE Nebraska
32 NV Nevada
33 NH New Hampshire
34 NJ New Jersey
35 NM New Mexico
36 NY New York
37 NC North Carolina
38 ND North Dakota
39 OH Ohio
40 OK Oklahoma
41 OR Oregon
42 PA Pennsylvania
44 RI Rhode Island
45 SC South Carolina
46 SD South Dakota
47 TN Tennessee
48 TX Texas
49 UT Utah
50 VT Vermont
51 VA Virginia
53 WA Washington
54 WV West Virginia
55 WI Wisconsin
56 WY Wyoming'''.splitlines()}
GENERATED = '<!-- Generated from catalog/cities.json and catalog/city-link-check.json; run python tools/cities.py build. -->'


def load(path=CATALOG):
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique_keys)


def validate(data):
    errors = []
    if not isinstance(data, dict) or set(data) != {'catalog_version', 'reviewed_on', 'methodology', 'categories', 'sources', 'cities'}:
        return ['City catalog has missing or unexpected fields.']
    if data['catalog_version'] != 1 or not valid_date(data['reviewed_on']):
        errors.append('Invalid catalog version or review date.')
    if not isinstance(data['categories'], dict) or set(data['categories']) != CATEGORIES:
        errors.append('Exactly four city-source categories are required.')
    method = data['methodology']
    if not isinstance(method, dict):
        return errors + ['methodology must be an object.']
    for key in ['population_source_url', 'population_layout_url', 'hawaii_source_url']:
        if not valid_url(method.get(key)):
            errors.append(f'Invalid methodology {key}.')
    if not re.fullmatch(r'[a-f0-9]{64}', str(method.get('population_file_sha256', ''))):
        errors.append('Missing population file SHA-256.')
    for key in ['selection', 'hawaii_exception', 'excluded']:
        if not isinstance(method.get(key), str) or not method[key].strip():
            errors.append(f'Missing methodology {key}.')
    if not isinstance(data['sources'], list) or not isinstance(data['cities'], list):
        return errors + ['sources and cities must be arrays.']
    sources = {}
    fields = {'id', 'name', 'category', 'url', 'evidence_url', 'review_method', 'review_note', 'resource_type', 'reviewed_on'}
    for source in data['sources']:
        if not isinstance(source, dict) or set(source) != fields or not all(isinstance(v, str) and v.strip() for v in source.values()):
            errors.append('Source must have exactly the documented nonempty string fields.')
            continue
        sid = source['id']
        if sid in sources or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', sid):
            errors.append(f'Duplicate or invalid source ID: {sid}')
        sources[sid] = source
        if source['category'] not in CATEGORIES or source['resource_type'] not in KINDS or source['review_method'] not in METHODS:
            errors.append(f'{sid}: invalid category, resource type or review method.')
        if not all(valid_url(source[k]) for k in ['url', 'evidence_url']):
            errors.append(f'{sid}: invalid URL or credential-like query parameter.')
        if not valid_date(source['reviewed_on']) or source['reviewed_on'] > data['reviewed_on']:
            errors.append(f'{sid}: invalid review date.')
    by_state = defaultdict(list)
    seen = set()
    used = set()
    city_fields = {'id', 'name', 'census_name', 'state', 'state_code', 'state_fips', 'place_fips', 'rank', 'population', 'population_date', 'population_source_url', 'geography_type', 'municipal_url', 'address_coverage_verified', 'coverage_notes', 'sources'}
    if len(data['cities']) != 150:
        errors.append('Exactly 150 city/place records are required.')
    for city in data['cities']:
        if not isinstance(city, dict) or set(city) != city_fields:
            errors.append('City record has missing or unexpected fields.')
            continue
        for key in ['id', 'name', 'census_name', 'state', 'state_code', 'state_fips', 'place_fips']:
            if not isinstance(city[key], str) or not city[key].strip():
                errors.append(f'City has invalid {key}.')
        cid = str(city['id'])
        fips = str(city['state_fips'])
        if cid in seen or cid != f"{fips}-{city['place_fips']}" or not re.fullmatch(r'\d{2}-\d{5}', cid):
            errors.append(f'Duplicate or invalid city FIPS ID: {cid}')
        seen.add(cid)
        if STATES.get(fips) != (city['state_code'], city['state']):
            errors.append(f'{cid}: state name/code/FIPS mismatch.')
        by_state[fips].append(city)
        if type(city['population']) is not int or city['population'] <= 0:
            errors.append(f'{cid}: population must be a positive integer.')
        if type(city['rank']) is not int or city['rank'] not in {1, 2, 3}:
            errors.append(f'{cid}: rank must be 1, 2 or 3.')
        hawaii = fips == '15'
        if city['population_date'] != ('2020-04-01' if hawaii else '2025-07-01'):
            errors.append(f'{cid}: unexpected population date for this catalog vintage.')
        if city['geography_type'] != ('census-designated-place' if hawaii else 'incorporated-place'):
            errors.append(f'{cid}: incorrect geography type.')
        expected_url = method.get('hawaii_source_url' if hawaii else 'population_source_url')
        if city['population_source_url'] != expected_url or not valid_url(city['municipal_url']):
            errors.append(f'{cid}: invalid population source or municipal URL.')
        if city['address_coverage_verified'] is not False:
            errors.append(f'{cid}: this directory has no address-level coverage validation.')
        if not isinstance(city['coverage_notes'], list) or not all(isinstance(n, str) and n.strip() for n in city['coverage_notes']):
            errors.append(f'{cid}: coverage_notes must be a list of nonempty strings.')
        if not isinstance(city['sources'], dict) or set(city['sources']) != CATEGORIES:
            errors.append(f'{cid}: all four source categories are required.')
            continue
        for category, refs in city['sources'].items():
            if not isinstance(refs, list) or not refs or not all(isinstance(r, str) for r in refs):
                errors.append(f'{cid}: {category} must contain source IDs.')
                continue
            if len(set(refs)) != len(refs):
                errors.append(f'{cid}: duplicate source reference in {category}.')
            for sid in refs:
                if sid not in sources or sources[sid]['category'] != category:
                    errors.append(f'{cid}: unknown or wrongly categorized source {sid}.')
                used.add(sid)
    if set(by_state) != set(STATES):
        errors.append('The catalog must cover all 50 states, without DC or territories.')
    for state, entries in by_state.items():
        if sorted(str(c['rank']) for c in entries) != ['1', '2', '3']:
            errors.append(f'{state}: exactly ranks 1, 2 and 3 are required.')
        elif all(type(c['population']) is int for c in entries):
            populations = [c['population'] for c in sorted(entries, key=lambda c: str(c['rank']))]
            if populations != sorted(populations, reverse=True):
                errors.append(f'{state}: ranks do not follow descending population.')
    if set(sources) - used:
        errors.append('Unreferenced sources: ' + ', '.join(sorted(set(sources) - used)))
    return errors


def validate_report(data, report):
    if not isinstance(report, dict) or report.get('report_version') != 1 or not isinstance(report.get('checks'), list):
        return ['Invalid city link-check report.']
    checks = report['checks']
    urls = [c.get('url') for c in checks if isinstance(c, dict)]
    if len(urls) != len(checks) or len(set(urls)) != len(urls) or set(urls) != {s['url'] for s in data['sources']}:
        return ['Link report must contain exactly one check for every unique source URL. Run check-links.']
    errors = []
    for check in checks:
        result = check.get('result')
        status = check.get('status')
        if result not in {'reachable', 'http-error', 'request-error'}:
            errors.append(f"Unknown check result for {check['url']}.")
        elif result == 'reachable' and (type(status) is not int or not 200 <= status < 300):
            errors.append(f"Inconsistent reachable status for {check['url']}.")
        elif result == 'http-error' and (type(status) is not int or status < 400):
            errors.append(f"Inconsistent HTTP error status for {check['url']}.")
        elif result == 'request-error' and status is not None:
            errors.append(f"Inconsistent request error status for {check['url']}.")
        try:
            stamp = datetime.fromisoformat(check['checked_at'])
            if stamp.tzinfo is None or stamp > datetime.now(timezone.utc):
                raise ValueError()
        except (KeyError, ValueError, TypeError):
            errors.append(f"Invalid check timestamp for {check['url']}.")
    return errors


def md(text):
    return html.escape(str(text), quote=False).replace('|', '\\|').replace('[', '\\[').replace(']', '\\]').replace('\n', ' ')


def link(label, url):
    return f'[{md(label)}](<{url}>)'


def state_slug(state):
    return state.lower().replace(' ', '-')


def check_label(check):
    if check['result'] == 'reachable':
        return 'HTTP ' + str(check['status'])
    if check['result'] == 'http-error':
        return 'HTTP ' + str(check['status']) + '; review access'
    return 'Request failed; review access'


def render(data, report):
    sources = {s['id']: s for s in data['sources']}
    checks = {c['url']: c for c in report['checks']}
    grouped = defaultdict(list)
    for city in data['cities']:
        grouped[city['state']].append(city)
    refs = sum(len(v) for c in data['cities'] for v in c['sources'].values())
    index = ['# Cities and local sources', '', GENERATED, '',
        f"**150 places · 50 states · {len(sources)} source records · {refs} city-to-source references.** Reviewed {data['reviewed_on']}.", '',
        '[National and global library](LIBRARY.md) · [Source details](cities/SOURCES.md) · [Selection and review method](docs/city-methodology.md)', '',
        'The three largest incorporated places in each state, ranked by Census Vintage 2025 population (July 1, 2025). Hawaii uses the three largest 2020 Census CDPs. These are city/place populations, not metro populations.', '',
        'Each profile has emergency-management or alert references, police/public-safety references, water-service information and electric-utility resources. Some references are directories or registration pages. No live feed collection is configured.', '',
        'Electric and water territories may split a city. Provider lists are starting points; confirm the provider for each facility address. Public viewing does not establish an API or commercial reuse rights.', '',
        '| State | #1 | #2 | #3 |', '| --- | --- | --- | --- |']
    pages = {}
    for state in sorted(grouped):
        cities = sorted(grouped[state], key=lambda c: c['rank'])
        slug = state_slug(state)
        path = f'cities/states/{slug}.md'
        index.append('| ' + f'[{state}]({path}) | ' + ' | '.join(f"[{md(c['name'])}]({path}#city-{c['id']})" for c in cities) + ' |')
        page = [f'# {state}: three largest places', '', GENERATED, '',
            '[All states](../../CITIES.md) · [Source details](../SOURCES.md) · [Methodology](../../docs/city-methodology.md)', '',
            'Rank uses incorporated-place population as of July 1, 2025 (Census Vintage 2025).' if state != 'Hawaii' else 'Hawaii exception: rank uses 2020 Census CDP population as of April 1, 2020. All three places are on Oahu.', '',
            'Sources are discovery references. Confirm utility service territory by address and check the publisher for current notices. HTTP results indicate retrieval only; they do not test live data, subscriptions or feed functionality.', '']
        for city in cities:
            page += [f'<a id="city-{city["id"]}"></a>', '', f"## {city['rank']}. {city['name']}", '',
                f"**Population:** {city['population']:,} ({city['population_date']}) · **Census place:** {md(city['census_name'])} · **FIPS:** `{city['id']}`", '',
                link('Population source', city['population_source_url']) + ' · ' + link('Municipal website', city['municipal_url']), '']
            page += [note + '\n' for note in city['coverage_notes']]
            page += ['| Category | Source | Resource type | Retrieval check |', '| --- | --- | --- | --- |']
            for category in data['categories']:
                for sid in city['sources'][category]:
                    source = sources[sid]
                    page.append(f"| {md(data['categories'][category])} | {link(source['name'], source['url'])} · [details](../SOURCES.md#{sid}) | {source['resource_type']} | {check_label(checks[source['url']])} |")
            page.append('')
        pages[ROOT / path] = '\n'.join(page).rstrip() + '\n'
    counts = Counter(c['result'] for c in report['checks'])
    index += ['', '## Review status', '',
        f"The link snapshot contains {len(checks)} distinct source URLs: {counts['reachable']} returned a successful HTTP response, {counts['http-error']} returned HTTP errors, and {counts['request-error']} had request/TLS/network errors.", '',
        'Blocked retrieval does not prove a source is unavailable. Successful retrieval does not prove the correct content loaded. See the [dated check report](catalog/city-link-check.json) and source-specific notes before using a link operationally.', '',
        '[Editable catalog](catalog/cities.json) · [Contribution guide](CONTRIBUTING.md#city-source-packs)', '']
    pages[ROOT / 'CITIES.md'] = '\n'.join(index)
    registry = ['# City source details', '', GENERATED, '', '[Browse states and cities](../CITIES.md) · [Review method](../docs/city-methodology.md)', '',
        'These entries are web references. No documented API, machine-readable feed, update cadence, comprehensive coverage or commercial reuse license is asserted by inclusion.', '',
        'Review methods describe how a reference was found. HTTP checks are separate and do not advance the content review date.', '']
    used_by = defaultdict(list)
    for city in data['cities']:
        for ids in city['sources'].values():
            for sid in ids:
                used_by[sid].append(city)
    for sid, source in sorted(sources.items()):
        check = checks[source['url']]
        registry += [f'<a id="{sid}"></a>', '', f"## {md(source['name'])}", '',
            link('Visit source', source['url']) + ' · ' + link('Publisher evidence', source['evidence_url']), '',
            f"- **ID / category:** `{sid}` / {source['category']}",
            f"- **Resource:** `{source['resource_type']}`",
            f"- **Review:** {source['reviewed_on']} · `{source['review_method']}`",
            f"- **Notes:** {md(source['review_note'])}",
            f"- **HTTP check:** {check_label(check)} · {check['checked_at']}",
            '- **Used by:** ' + ', '.join(f"[{md(c['name'])}, {c['state_code']}](states/{state_slug(c['state'])}.md#city-{c['id']})" for c in used_by[sid]), '']
    pages[ROOT / 'cities/SOURCES.md'] = '\n'.join(registry)
    return pages


def check_url(url):
    row = {'url': url, 'checked_at': datetime.now(timezone.utc).isoformat(timespec='seconds')}
    try:
        request = Request(url, headers={'User-Agent': 'OSINTSourceLibrary/0.2 (public-source-directory)'})
        with urlopen(request, timeout=12) as response:
            row.update(status=response.status, final_url=response.url, content_type=response.headers.get('Content-Type', ''))
            body = response.read(400000).decode('utf-8', 'replace')
        title = re.search(r'<title[^>]*>(.*?)</title>', body, re.I | re.S)
        row.update(result='reachable', title=html.unescape(re.sub(r'\s+', ' ', title.group(1))).strip() if title else '')
    except HTTPError as exc:
        row.update(status=exc.code, result='http-error')
    except Exception as exc:
        row.update(status=None, result='request-error', detail=str(exc)[:160])
    return row


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('validate', help='Offline checks for coverage, references and link-report structure')
    build = commands.add_parser('build', help='Generate CITIES.md and state/source pages')
    build.add_argument('--check', action='store_true')
    search = commands.add_parser('search', help='Search city and source metadata offline')
    search.add_argument('query', nargs='?', default='')
    search.add_argument('--state', default='', help='State name or two-letter abbreviation')
    search.add_argument('--category', choices=sorted(CATEGORIES))
    search.add_argument('--json', action='store_true')
    links = commands.add_parser('check-links', help='Fetch public source URLs once and replace the HTTP snapshot; no feed test')
    links.add_argument('--missing-only', action='store_true', help='Retain existing timestamps/results; fetch only newly added URLs')
    args = parser.parse_args()
    try:
        data = load()
        errors = validate(data)
        if errors:
            raise ValueError('\n'.join(errors))
        if args.command == 'check-links':
            urls = sorted({s['url'] for s in data['sources']})
            prior = {c['url']: c for c in load(REPORT)['checks']} if args.missing_only and REPORT.exists() else {}
            with ThreadPoolExecutor(max_workers=8) as pool:
                fresh = list(pool.map(check_url, [u for u in urls if u not in prior]))
            prior.update({c['url']: c for c in fresh})
            report = {'report_version': 1, 'method': 'GET, default TLS verification, 12-second timeout, up to 400000 response bytes. Reachability only; scripts, subscriptions and APIs not tested.', 'checks': [prior[u] for u in urls]}
            REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
            print(f'Snapshot saved: {len(urls)} URLs ({len(fresh)} fetched). Run build and review error statuses, titles and redirects.')
            return 0
        if args.command == 'search':
            source_map = {s['id']: s for s in data['sources']}
            matches = []
            for city in data['cities']:
                if args.state and args.state.casefold() not in {city['state'].casefold(), city['state_code'].casefold()}:
                    continue
                selected = {cat: [source_map[sid] for sid in refs] for cat, refs in city['sources'].items() if not args.category or cat == args.category}
                if args.query.casefold() not in json.dumps([city['name'], city['census_name'], city['id'], city['state'], selected]).casefold():
                    continue
                matches.append(dict(city, sources=selected))
            if args.json:
                print(json.dumps(matches, indent=2, ensure_ascii=False))
            else:
                for city in matches:
                    print(f"{city['name']}, {city['state_code']} | rank {city['rank']} | population {city['population']:,} ({city['population_date']})")
                    for category, sources in city['sources'].items():
                        for source in sources:
                            print(f"  {category}: {source['name']} — {source['url']}")
                print(f'{len(matches)} matching cities.')
            return 0
        report = load(REPORT)
        errors = validate_report(data, report)
        if errors:
            raise ValueError('\n'.join(errors))
        if args.command == 'validate':
            print(f"Valid: 150 places, 50 states, {len(data['sources'])} source records, four categories per place.")
            return 0
        pages = render(data, report)
        stale = []
        obsolete = set((ROOT / 'cities/states').glob('*.md')) - set(pages)
        if obsolete:
            raise ValueError('Unexpected state pages; review before removal: ' + ', '.join(str(p.relative_to(ROOT)) for p in sorted(obsolete)))
        for path, content in pages.items():
            if args.check:
                if not path.exists() or path.read_text(encoding='utf-8') != content:
                    stale.append(str(path.relative_to(ROOT)))
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding='utf-8')
        if stale:
            raise ValueError('Stale generated files: ' + ', '.join(stale))
        print(f"{'Checked' if args.check else 'Built'} {len(pages)} city library pages.")
        return 0
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(f'City catalog error: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
