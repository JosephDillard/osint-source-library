# Government & humanitarian information

<!-- Generated from catalog/sources.json; edit the catalog, then run python tools/catalog.py build. -->

[All categories](../LIBRARY.md) | [How to use this library](../docs/getting-started.md)

Original catalog text: Copyright (c) 2026 Joseph Dillard and contributors, [CC BY 4.0](../LICENSE-CONTENT). [Scope and attribution](../LICENSING.md). Provider material retains its own terms.

<a id="data-gov"></a>

## Data.gov catalog

**[Visit source](https://data.gov/)** | [Provider documentation](https://data.gov/)

- **Provider:** US General Services Administration and contributing agencies
- **Coverage:** United States federal, state and local contributors
- **Type / access:** `catalog` / `mixed`
- **Formats:** Catalog, Dataset-specific downloads
- **Updates:** Catalog and underlying datasets update separately.
- **Security use:** Discover local government, infrastructure and emergency-management sources.
- **License / terms:** Licenses and access conditions are dataset-specific; catalog inclusion is not blanket permission.
- **Limitations:** A catalog record is not an operational feed; validate the underlying publisher and resource.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://data.gov/)
- **Catalog ID:** `data-gov`

<a id="federal-register"></a>

## Federal Register API

**[Visit source](https://www.federalregister.gov/)** | [Provider documentation](https://www.federalregister.gov/developers/documentation/api/v1)

- **Provider:** Office of the Federal Register / Government Publishing Office
- **Coverage:** United States federal government
- **Type / access:** `periodic` / `open`
- **Formats:** JSON, XML, PDF
- **Updates:** Publication schedule; inspect dates and document status.
- **Security use:** Track agency notices, emergency declarations and infrastructure-related policy changes.
- **License / terms:** Public API without keys; linked source documents may have additional notices.
- **Limitations:** Text usually needs geographic interpretation; verify legal reliance against the linked official edition.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://www.federalregister.gov/api/v1/documents.json?per_page=1). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://www.federalregister.gov/developers/documentation/api/v1)
- **Catalog ID:** `federal-register`

<a id="openfema"></a>

## OpenFEMA disaster declarations and program data

**[Visit source](https://www.fema.gov/about/openfema)** | [Provider documentation](https://www.fema.gov/about/openfema/api)

- **Provider:** Federal Emergency Management Agency
- **Coverage:** United States and territories
- **Type / access:** `periodic` / `open`
- **Formats:** JSON, Downloads
- **Updates:** Dataset-specific administrative updates.
- **Security use:** Declared disasters, affected jurisdictions and recovery context.
- **License / terms:** Public OpenFEMA data; review dataset metadata and terms.
- **Limitations:** Declarations and aid records are not live evacuation or incident alerts. Documentation fetch returned 403 in this review.
- **Review:** 2026-09-20 — `partial-review`
- **API entrypoint / example:** [Open endpoint](https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://www.fema.gov/about/openfema/api) · [Provider reference 2](https://www.fema.gov/gu/about/reports-and-data/openfema)
- **Catalog ID:** `openfema`

<a id="reliefweb"></a>

## ReliefWeb reports and disasters API

**[Visit source](https://reliefweb.int/)** | [Provider documentation](https://apidoc.reliefweb.int/parameters)

- **Provider:** UN OCHA / ReliefWeb
- **Coverage:** Global humanitarian emergencies
- **Type / access:** `live-feed` / `approval`
- **Formats:** JSON
- **Updates:** Continuously curated reports; publication lag varies.
- **Security use:** Humanitarian situation reports and international operational context.
- **License / terms:** No API fee; pre-approved appname required since November 2025. Original publishers retain content rights.
- **Limitations:** Reports can reference broad areas and older events; distinguish reporting time from event time.
- **Review:** 2026-09-21 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://api.reliefweb.int/v2/reports). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://apidoc.reliefweb.int/) · [Provider reference 2](https://apidoc.reliefweb.int/parameters)
- **Catalog ID:** `reliefweb`
