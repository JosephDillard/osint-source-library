# Water outages & water systems

<!-- Generated from catalog/sources.json; edit the catalog, then run python tools/catalog.py build. -->

[All categories](../LIBRARY.md) | [How to use this library](../docs/getting-started.md)

<a id="dc-water"></a>

## DC Water service alerts and outage map

**[Visit source](https://www.dcwater.com/service-alerts)** | [Provider documentation](https://www.dcwater.com/service-alerts)

- **Provider:** DC Water
- **Coverage:** DC Water service area, Washington, DC
- **Type / access:** `dashboard` / `open`
- **Formats:** Web alerts, Web map
- **Updates:** Incident-driven notices and utility updates.
- **Security use:** Water service interruptions, repairs and local operational awareness.
- **License / terms:** Public utility information; no supported public machine API validated here.
- **Limitations:** Confirm the applicable service area and advisory details. Absence from a map does not establish service.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://www.dcwater.com/service-alerts)
- **Catalog ID:** `dc-water`

<a id="epa-sdwis"></a>

## EPA drinking-water systems and compliance data

**[Visit source](https://www.epa.gov/waterdata/safe-drinking-water-information-system)** | [Provider documentation](https://echo.epa.gov/tools/data-downloads/sdwa-download-summary)

- **Provider:** US Environmental Protection Agency
- **Coverage:** United States public water systems
- **Type / access:** `periodic` / `open`
- **Formats:** Downloads, Search portal
- **Updates:** Periodic reporting; ECHO download documentation describes quarterly refreshes.
- **Security use:** Identify water systems and review reported compliance history.
- **License / terms:** Public EPA releases; consult data dictionaries and completeness caveats.
- **Limitations:** Historical compliance records do not establish current water safety or report active outages.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://echo.epa.gov/tools/data-downloads/sdwa-download-summary) · [Provider reference 2](https://www.epa.gov/waterdata/safe-drinking-water-information-system)
- **Catalog ID:** `epa-sdwis`

<a id="usgs-water"></a>

## USGS modern Water Data APIs

**[Visit source](https://api.waterdata.usgs.gov/)** | [Provider documentation](https://api.waterdata.usgs.gov/docs/ogcapi)

- **Provider:** US Geological Survey
- **Coverage:** United States monitoring locations
- **Type / access:** `live-feed` / `mixed`
- **Formats:** GeoJSON, JSON, OGC API
- **Updates:** Sensor and telemetry dependent; historical series also available.
- **Security use:** Streamflow, gauge height and water-resource conditions affecting sites and routes.
- **License / terms:** Public USGS data; consult current API-key, quota and service guidance for the selected endpoint.
- **Limitations:** Not a drinking-water outage feed. Prefer modern APIs; legacy WaterServices retirement is announced for early 2027.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://api.waterdata.usgs.gov/ogcapi/v0/collections/latest-continuous/items?limit=1). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://api.waterdata.usgs.gov/docs/ogcapi) · [Provider reference 2](https://waterdata.usgs.gov/blog/api-waterservices-decom)
- **Catalog ID:** `usgs-water`
