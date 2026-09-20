# Catalog data model

`catalog/sources.json` is the single editable source. `LIBRARY.md` and `sources/*.md` are generated views.

## Catalog fields

- `catalog_version`: integer format version; currently 1.
- `review_date`: date of this catalog review, not an operational freshness guarantee.
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
| `reviewed_on` | Actual date the record's supporting material was reviewed |
| `review_status` | Documentation reviewed, metadata reviewed or partial review |
| `evidence_urls` | Primary-source links supporting the record |

A provider may offer multiple products. A source record is a discovery entry, not a normalized event schema or a guarantee of coverage.

## Validation

The dependency-free helper checks required and unexpected fields, types, category membership, unique IDs and landing URLs, access and kind values, dates, nonempty lists, and HTTP(S) links without embedded user/password credentials.

It also flags common credential query parameters in stored links. That check is intentionally limited; reviewers must still ensure that no secret, personal data or proprietary material is committed.

`build --check` detects missing or stale generated Markdown, including obsolete category files. It does not make network calls or interpret third-party licenses.
