# Source reviews

## Service expansion — 2026-09-21

The [expanded shortlist](service-shortlist.md) contains 18 services and public sources. Eight were already cataloged; ten commercial services were added, bringing the national/global catalog to 47 sources across 15 categories. Existing records were improved where the new review supported a change. Individual review dates remain authoritative; the catalog date does not imply every source was re-reviewed.

- Added Factal, Samdesk, Dataminr for Corporate Security, Seerist, Riskline, Base Operations, Crisis24 Horizon, AlertMedia, Everbridge Risk Intelligence and Ontic.
- Recorded documented API, GIS and export capabilities separately from outbound integration questions. Commercial accounts, sample payloads and native GIS compatibility were not tested.
- Clarified that API or licensed export/ETL access is sufficient; a native GIS connector is not a prerequisite.
- Limited cybersecurity to major consequential breaches and incidents. Connectivity measurements do not establish a cyberattack by themselves.
- Corrected Cloudflare Radar licensing notes to reflect [CC BY-NC 4.0](https://developers.cloudflare.com/radar/). An API token does not resolve corporate operational-use rights.
- Retained Base Operations as periodic risk context, reflecting its [published update cadence](https://www.baseoperations.com/product/api), rather than an emergency alert feed.

Commercial capabilities are based on public provider material. Listing a service does not establish procurement approval or rights to its underlying sources. Contract terms, prices and delivery commitments remain to be confirmed. This expansion did not refresh the separate HTTP availability snapshot or city catalog.

## Initial review — 2026-09-20

Review date: **2026-09-20**.

The initial catalog was assembled from publisher documentation, official dataset metadata and public status pages. The source cards retain the supporting links and review method. This is a point-in-time research review, not an availability commitment or a complete API integration test.

## Findings incorporated

- [OpenSky terms](https://opensky-network.org/about/terms-of-use) require a written license for commercial entities and operational REST API use; [API documentation](https://openskynetwork.github.io/opensky-api/rest.html) specifies OAuth2.
- [ReliefWeb documentation](https://apidoc.reliefweb.int/) requires a pre-approved application name from November 2025.
- [USGS migration notice](https://waterdata.usgs.gov/blog/api-waterservices-decom) announces early-2027 retirement of legacy WaterServices; the catalog points to modern Water Data APIs.
- [Marine Cadastre's AccessAIS page](https://marinecadastre.gov/accessais/) reported its ordering service unavailable and directed users to bulk downloads. Historical AIS is therefore not described as a working live feed.
- [Chicago metadata](https://data.cityofchicago.org/api/views/ijzp-q8t2.json) describes daily updates, a seven-day exclusion and approximate locations. Its restrictions and cautions are reflected in the record.
- [NYC complaint metadata](https://data.cityofnewyork.us/api/views/5uac-w243.json) includes an old year in the description, despite more recent update metadata. The record directs users to check actual row dates.
- [NYC event metadata](https://data.cityofnewyork.us/api/views/tvpp-9vvx.json) covers approved events in the next month, with a specific inclusion limit for film permits.

## Verification boundaries

Provider documentation review does not mean a feed has been continuously tested. Paid or authenticated APIs were not accessed. Dashboard backend endpoints were not inferred from browser internals.

The FAA status site rendered insufficient text to inspect its operational content with the research tool. OpenFEMA documentation and the HDX portal returned access errors in that tool; other official provider material supports their discovery entries. These records are labeled `partial-review`.

Availability observations are stored separately in [link-check.json](../catalog/link-check.json) when a link check is run. A successful HTTP response is only a reachability observation; an error may be an anti-bot rule, rate limit or temporary failure rather than a dead source.

The initial HTTP check covered 69 distinct landing and documentation URLs: 60 returned successful responses, seven returned HTTP 403, and two IODA URLs failed certificate-chain validation in the local Python environment. TLS verification was retained. The report preserves the URL, time and result for each check; these outcomes do not change the separate documentation-review status.

No claim is made that this initial collection provides nationwide live crime, protest, utility outage or vessel coverage.
