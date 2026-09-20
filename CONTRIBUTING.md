# Contributing sources

1. Find the original publisher's dataset page or official API documentation.
2. Copy a similar record in `catalog/sources.json` and assign a stable, unique lowercase ID.
3. Record geographic coverage, data type, access requirements, formats, update timing, limitations and specific security use.
4. Add the documentation and evidence links. Supply an endpoint only when it is documented; use `null` when none is established. Never store keys or tokens in URLs.
5. Read the provider's current usage terms. Describe uncertainty explicitly instead of assuming public access permits commercial reuse.
6. Set the actual review date and review status. A page title or search result alone does not establish a working feed.
7. Run:

```powershell
python tools/catalog.py validate
python tools/catalog.py build
python tools/catalog.py build --check
```

Commit the JSON and regenerated Markdown together. The CI workflow checks structure and synchronization without contacting providers.

## Review status

- `provider-documentation-reviewed`: publisher documentation or substantive provider material was reviewed; no claim of an authenticated integration test.
- `provider-metadata-reviewed`: the publisher's structured dataset metadata was inspected.
- `partial-review`: only part of the entry could be checked; record the limitation.

Do not advance review dates because a build or HTTP status check passed. Review quarterly and before an operational integration; this is a suggested maintenance practice, not a configured automated monitor.

## Good source records

Prefer direct publishers over copied lists. Distinguish event time, publication time and data retrieval time. Say whether geometry is a point, approximate block, route, polygon or broad administrative area when it matters.

For a local source, name the service territory or jurisdiction. Keep overlapping sources when they provide different evidence, but avoid duplicate URLs under different names.

For protests and public events, describe access, disruption and safety relevance without treating attendance or lawful assembly as evidence of a threat. Catalog event-level sources rather than personal dossiers.

## Report a broken or changed source

Use the source-request issue template to identify the source ID, link, observed date and specific failure or correction. Do not attach credentials, personal information or proprietary operational records.
