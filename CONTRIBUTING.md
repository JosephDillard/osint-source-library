# Contributing sources

Original code contributions use MIT. Original catalog descriptions and prose contributions use CC BY 4.0. Follow the [licensing scope and attribution guidance](LICENSING.md), retain notices and identify any third-party material and its terms. Provider license notes remain separate from the license of your original catalog annotation.

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

The labels below apply to the national/global catalog. City references have their own narrower [review methods](docs/city-methodology.md#what-a-source-entry-establishes).

- `provider-documentation-reviewed`: publisher documentation or substantive provider material was reviewed; no claim of an authenticated integration test.
- `provider-metadata-reviewed`: the publisher's structured dataset metadata was inspected.
- `partial-review`: only part of the entry could be checked; record the limitation.

Do not advance review dates because a build or HTTP status check passed. Review quarterly and before an operational integration; this is a suggested maintenance practice, not a configured automated monitor.

## Good source records

Prefer direct publishers over copied lists. Distinguish event time, publication time and data retrieval time. Say whether geometry is a point, approximate block, route, polygon or broad administrative area when it matters.

For a local source, name the service territory or jurisdiction. Keep overlapping sources when they provide different evidence, but avoid duplicate URLs under different names.

For protests and public events, describe access, disruption and safety relevance without treating attendance or lawful assembly as evidence of a threat. Catalog event-level sources rather than personal dossiers.

Keep cybersecurity focused on [major events](docs/getting-started.md#major-cybersecurity-events), including consequential breaches and disruptions affecting people, operations or critical providers. Do not add routine vulnerability, exposed-service or account-monitoring feeds for their own sake.

Supported API, feed and licensed export/ETL access are all acceptable. Distinguish an inbound integration from an outbound data service; a vendor's integration claim alone does not establish export rights or a usable event feed.

## Report a broken or changed source

Use the source-request issue template to identify the source ID, link, observed date and specific failure or correction. Do not attach credentials, personal information or proprietary operational records.

## City source packs

Edit `catalog/cities.json`. Preserve stable FIPS city IDs and source IDs. Each city must reference at least one source in all four categories. Shared agencies and utilities can be referenced by several cities; do not duplicate the same source just to add another city. Separate providers can share a regional outage portal.

Keep population provenance, vintage and geography explicit. Do not replace place populations with metro or consolidated-county totals. The Hawaii exception must remain visible until an intentional methodology change.

Every reference needs a publisher URL, evidence URL, resource type, review method, date and notes. Do not label a page as a working API or assume a utility covers all city addresses. If a new source URL is added, refresh the snapshot for that URL:

```powershell
python tools/cities.py check-links --missing-only
python tools/cities.py validate
python tools/cities.py build
python tools/cities.py build --check
python -m unittest discover -s tests
```

`check-links` without the flag refreshes all source URLs. It changes HTTP timestamps only; content review dates require actual review. Commit the catalog, snapshot, `CITIES.md`, and generated `cities/` pages together. CI performs offline validation and generation checks; it does not contact providers.
