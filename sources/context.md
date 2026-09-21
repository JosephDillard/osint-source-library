# Maps, infrastructure & geographic context

<!-- Generated from catalog/sources.json; edit the catalog, then run python tools/catalog.py build. -->

[All categories](../LIBRARY.md) | [How to use this library](../docs/getting-started.md)

Original catalog text: Copyright (c) 2026 Joseph Dillard and contributors, [CC BY 4.0](../LICENSE-CONTENT). [Scope and attribution](../LICENSING.md). Provider material retains its own terms.

<a id="hdx"></a>

## Humanitarian Data Exchange

**[Visit source](https://data.humdata.org/)** | [Provider documentation](https://centre.humdata.org/ufaqs/about-the-humanitarian-data-exchange-api/)

- **Provider:** UN OCHA Centre for Humanitarian Data / contributing organizations
- **Coverage:** Global, with humanitarian-response focus
- **Type / access:** `catalog` / `mixed`
- **Formats:** CKAN API, Dataset downloads, Tabular Data Endpoints
- **Updates:** Dataset-specific; inspect source and last update.
- **Security use:** Find administrative boundaries, infrastructure and humanitarian baseline data.
- **License / terms:** Dataset-specific licenses and access conditions; tabular endpoints require an HDX API token.
- **Limitations:** Some datasets require access approval; country and dataset coverage varies. Portal fetch returned 403 in this review.
- **Review:** 2026-09-20 — `partial-review`
- **Evidence:** [Provider reference 1](https://centre.humdata.org/ufaqs/about-the-humanitarian-data-exchange-api/) · [Provider reference 2](https://centre.humdata.org/ufaqs/data-licenses/) · [Provider reference 3](https://centre.humdata.org/new-api-access-on-hdx-tabular-data-endpoints/)
- **Catalog ID:** `hdx`

<a id="openstreetmap"></a>

## OpenStreetMap

**[Visit source](https://www.openstreetmap.org/)** | [Provider documentation](https://www.openstreetmap.org/copyright)

- **Provider:** OpenStreetMap contributors / OpenStreetMap Foundation
- **Coverage:** Global community mapping; completeness varies
- **Type / access:** `reference` / `open`
- **Formats:** OSM PBF, OSM XML, Map data
- **Updates:** Continuously edited; extracts have their own snapshot dates.
- **Security use:** Road, building and place context for situational-awareness maps.
- **License / terms:** ODbL database license; attribution and applicable share-alike terms. Tile-server policies are separate.
- **Limitations:** Map features are not a live incident or verified critical-infrastructure inventory.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://www.openstreetmap.org/copyright)
- **Catalog ID:** `openstreetmap`

<a id="overture"></a>

## Overture Maps

**[Visit source](https://overturemaps.org/)** | [Provider documentation](https://docs.overturemaps.org/getting-data/)

- **Provider:** Overture Maps Foundation and contributors
- **Coverage:** Global, theme-dependent coverage
- **Type / access:** `reference` / `open`
- **Formats:** GeoParquet, GeoJSON
- **Updates:** Versioned releases; pin the release used.
- **Security use:** Buildings, transport and place context for facility exposure analysis.
- **License / terms:** Licensing and attribution vary by theme and source; inspect current attribution documentation.
- **Limitations:** Feature presence, geometry and business attributes can be incomplete or outdated.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://docs.overturemaps.org/getting-data/) · [Provider reference 2](https://docs.overturemaps.org/attribution/)
- **Catalog ID:** `overture`
