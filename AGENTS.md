# Agent guidance: OSINT Source Library

These instructions apply throughout this repository. Read [README.md](README.md), [CONTRIBUTING.md](CONTRIBUTING.md), and the relevant methodology before changing catalog records or tools.

## Purpose and scope

This is a curated OSINT source-discovery library for physical security, protective services, business continuity and government situational awareness. It prioritizes the United States and includes global sources. It is not a running collector, alerting service or monitoring dashboard.

The repository is independent of Open GEOINT Watch and other sibling projects. Use repository-relative paths; do not introduce dependencies on a particular user's checkout location.

## Editable files and generated views

- `catalog/sources.json`: national/global source records.
- `catalog/cities.json`: city selections, population provenance, local source records and city-to-source references.
- `catalog/city-link-check.json`: timestamped HTTP retrieval snapshot, separate from content review.
- `tools/catalog.py`: national/global validation, search and Markdown generation.
- `tools/cities.py`: city validation, search, link checks and Markdown generation.
- `tools/rank_cities.py`: reproduction of the Census annual-estimate rankings.
- `tests/`: offline validation and internal-link checks.
- `docs/`: methodology, data models, coverage and review limits.

Edit the catalogs, then regenerate their views. Do not hand-edit `LIBRARY.md`, `sources/*.md`, `CITIES.md`, `cities/SOURCES.md` or `cities/states/*.md` to change source content. Commit catalog changes and regenerated views together.

## Source and geography rules

- Prefer original publishers and official documentation. Record evidence URLs, access conditions, geographic limits and unresolved questions.
- A public webpage is not proof of an open license, a documented API or a working live feed. Preserve the distinction between reference pages, dashboards, historical data and feeds.
- Keep source IDs stable. Reuse shared source records rather than duplicating them for each city.
- Preserve the current selection: three places per state, 150 total. The 49-state ranking uses Census Vintage 2025 incorporated-place estimates; Hawaii uses 2020 Census CDPs. Follow [city-methodology.md](docs/city-methodology.md) for intentional changes.
- Keep Census FIPS identifiers as strings with leading zeros. Do not substitute metropolitan or consolidated-county populations for place populations.
- Utility service territories require address-level confirmation; a city reference is not proof of coverage for every address.
- HTTP success does not prove source accuracy or feed health. Retain blocked requests and failures as uncertainty. Do not advance content-review dates merely because a link check or build passed.
- Keep credentials, private facility inventories and downloaded working data out of tracked files. Existing ignore rules cover local research and outputs.

## Local commands and validation

Python 3.10+ and the standard library are sufficient; CI uses Python 3.12. Run commands from the repository root.

After changing catalogs or generators, rebuild the affected views:

```powershell
python tools/catalog.py build
python tools/cities.py build
```

For catalog, generator or validation changes, run the offline CI checks:

```powershell
python tools/catalog.py validate
python tools/catalog.py build --check
python tools/cities.py validate
python tools/cities.py build --check
python -m unittest discover -s tests
```

For documentation-only changes, check local links and `git diff --check`; runtime tests are unnecessary unless the edit changes documented behavior or commands.

When source URLs change, `python tools/cities.py check-links --missing-only` fetches newly added URLs. Without that flag, the command refreshes all source URLs. These commands contact external publishers and update the snapshot; use them as part of source maintenance, not as a routine offline test. Rebuild city pages after updating the snapshot.

Report the scope of changes, validation performed and remaining source-review limits. Do not describe HTTP reachability as a completed operational integration.
