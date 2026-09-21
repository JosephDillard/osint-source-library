#!/usr/bin/env python3
"""Reproduce the 147 incorporated-place selections from the official Vintage 2025 CSV."""
import argparse
from collections import defaultdict
import csv
import hashlib
import json
from pathlib import Path
import sys

from cities import CATALOG, STATES, load


def select(path):
    groups = defaultdict(list)
    with path.open(encoding='cp1252', newline='') as stream:
        for row in csv.DictReader(stream):
            state = row['STATE'].zfill(2)
            if row['SUMLEV'] != '162' or state not in STATES or state == '15':
                continue
            groups[state].append(dict(id=state + '-' + row['PLACE'].zfill(5),
                census_name=row['NAME'], population=int(row['POPESTIMATE2025'])))
    result = []
    for state in sorted(groups):
        entries = sorted(groups[state], key=lambda c: (-c['population'], c['id']))[:3]
        result.extend(dict(city, rank=rank) for rank, city in enumerate(entries, 1))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv', type=Path)
    parser.add_argument('--check', action='store_true', help='Compare hash and selected values against catalog/cities.json')
    args = parser.parse_args()
    try:
        selected = select(args.csv)
        if len(selected) != 147:
            raise ValueError(f'Expected 147 incorporated places, found {len(selected)}.')
        if args.check:
            catalog = load(CATALOG)
            if hashlib.sha256(args.csv.read_bytes()).hexdigest() != catalog['methodology']['population_file_sha256']:
                raise ValueError('CSV checksum differs from the catalog source. Review the input vintage/revision.')
            expected = [{k: c[k] for k in ['id', 'census_name', 'population', 'rank']} for c in catalog['cities'] if c['state_fips'] != '15']
            if sorted(selected, key=lambda c: c['id']) != sorted(expected, key=lambda c: c['id']):
                raise ValueError('Selected Census places differ from the catalog.')
            print('Verified source checksum and all 147 Vintage 2025 incorporated-place rankings. Hawaii is documented separately.')
        else:
            print(json.dumps(selected, indent=2, ensure_ascii=False))
        return 0
    except (OSError, ValueError, KeyError) as exc:
        print(f'Population selection error: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
