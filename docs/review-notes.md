# Initial source review

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
