# Catalog data model

`catalog/sources.json` is the editable national/global source catalog. `LIBRARY.md` and `sources/*.md` are generated views. The separate city catalog is described below.

## Catalog fields

- `catalog_version`: integer format version; currently 1.
- `review_date`: UTC calendar date of this catalog review, not an operational freshness guarantee. Date validation uses the current UTC date so local time zones do not reject same-day UTC reviews.
- `categories`: mapping from stable category ID to readable label.
- `sources`: list of source records.

## Source fields

| Field | Meaning |
| --- | --- |
| `id` | Stable lowercase identifier with hyphens |
| `name`, `provider` | Public source name and publisher |
| `category` | One primary category; cross-domain relevance can appear in descriptions |
| `coverage` | Geographic coverage, service territory and important gaps |
| `kind` | `live-feed`, `periodic`, `historical`, `dashboard`, `catalog`, `reference` or `mixed` |
| `access` | `open`, `registration`, `approval`, `commercial` or `mixed`; describes access, not an open-data license |
| `formats` | Available representations or delivery mechanisms |
| `url` | Publisher landing page or dataset |
| `documentation_url` | Official documentation, metadata or substantive provider page |
| `endpoint_url` | Documented API entrypoint or example; `null` when not established. Authentication, parameters or pagination may still be required |
| `update_frequency` | Published schedule or clearly stated uncertainty |
| `license_notes` | Reuse requirements and unresolved terms; this is not legal clearance |
| `security_use` | Concrete defensive or continuity use |
| `limitations` | Timing, coverage, interpretation and integration constraints |
| `reviewed_on` | UTC calendar date the record's supporting material was reviewed |
| `review_status` | Documentation reviewed, metadata reviewed or partial review |
| `evidence_urls` | Primary-source links supporting the record |

A provider may offer multiple products. A source record is a discovery entry, not a normalized event schema or a guarantee of coverage.

## Validation

The dependency-free helper checks required and unexpected fields, types, category membership, unique IDs and landing URLs, access and kind values, dates, nonempty lists, and HTTP(S) links without embedded user/password credentials.

It also flags common credential query parameters in stored links. That check is intentionally limited; reviewers must still ensure that no secret, personal data or proprietary material is committed.

`build --check` detects missing or stale generated Markdown, including obsolete category files. It does not make network calls or interpret third-party licenses.

## City catalog

`catalog/cities.json` contains `catalog_version`, `reviewed_on`, `methodology`, `categories`, `sources` and `cities`. The methodology preserves population-source URLs, source-file SHA-256, selection rules and the Hawaii exception.

Each city records its display name, original Census name, state name/abbreviation/FIPS, place FIPS, rank, population, population date/source, geography type, municipal URL and coverage notes. Its stable `id` is `SS-PPPPP`, the state and place FIPS separated by a hyphen. `sources` maps each of the four category IDs to a nonempty list of source IDs. All city records set `address_coverage_verified` to `false`.

Each city source has these fields:

| Field | Meaning |
| --- | --- |
| `id`, `name` | Stable identifier and readable publisher/reference name |
| `category` | `emergency`, `public-safety`, `water` or `power` |
| `url`, `evidence_url` | Source entry point and official supporting reference |
| `resource_type` | Web reference, alert page, registration portal, outage reference or provider portal |
| `review_method` | Official-directory link, publisher search evidence or publisher reference |
| `review_note` | Reference limitations, access uncertainty and geographic caveats |
| `reviewed_on` | Date of reference review, separate from HTTP retrieval |

Shared sources are reused by ID. Distinct electric providers can share the same regional outage URL. API availability, cadence and reuse rights have not been established by this reference schema; use the national/global schema when documenting an integration-ready dataset.

`catalog/city-link-check.json` is a timestamped HTTP snapshot keyed by unique source URL. It stores a result, status and, when available, final URL, content type, page title or error detail. The [city methodology](city-methodology.md) defines what these checks establish.

`python tools/cities.py validate` checks all 50 states, exactly three ranks per state, descending populations, geography/date rules, source references and complete snapshot coverage. `build --check` verifies `CITIES.md`, the 50 state pages and `cities/SOURCES.md`. `tools/rank_cities.py` separately reproduces the 147 annual-estimate selections from the Census CSV.
