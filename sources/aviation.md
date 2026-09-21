# Air traffic & aviation

<!-- Generated from catalog/sources.json; edit the catalog, then run python tools/catalog.py build. -->

[All categories](../LIBRARY.md) | [How to use this library](../docs/getting-started.md)

Original catalog text: Copyright (c) 2026 Joseph Dillard and contributors, [CC BY 4.0](../LICENSE-CONTENT). [Scope and attribution](../LICENSING.md). Provider material retains its own terms.

<a id="aviation-weather"></a>

## Aviation Weather Center Data API

**[Visit source](https://aviationweather.gov/)** | [Provider documentation](https://aviationweather.gov/data/api/)

- **Provider:** NOAA / Aviation Weather Center
- **Coverage:** Worldwide observations and forecasts; some products regional
- **Type / access:** `live-feed` / `open`
- **Formats:** JSON, GeoJSON, XML, CSV, Text
- **Updates:** Product dependent; latest observations and recent history.
- **Security use:** Weather disruption context at airports and along planned air travel.
- **License / terms:** Public API with query limits; use cache downloads for bulk data and follow provider guidance.
- **Limitations:** Aviation weather is not aircraft traffic; product coverage and observation ages differ.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://aviationweather.gov/api/data/metar?ids=KDFW&format=json). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://aviationweather.gov/data/api/)
- **Catalog ID:** `aviation-weather`

<a id="faa-nas"></a>

## FAA National Airspace System status

**[Visit source](https://nasstatus.faa.gov/)** | [Provider documentation](https://nasstatus.faa.gov/)

- **Provider:** Federal Aviation Administration
- **Coverage:** United States National Airspace System
- **Type / access:** `dashboard` / `open`
- **Formats:** Web dashboard
- **Updates:** Operational status updates; inspect published times.
- **Security use:** Airport and airspace disruption awareness for travel and logistics.
- **License / terms:** Public FAA status page; no reusable machine endpoint was validated for this entry.
- **Limitations:** Status page is not a complete aircraft position feed or flight-specific guarantee.
- **Review:** 2026-09-20 — `partial-review`
- **Evidence:** [Provider reference 1](https://nasstatus.faa.gov/)
- **Catalog ID:** `faa-nas`

<a id="opensky"></a>

## OpenSky aircraft state vectors

**[Visit source](https://opensky-network.org/)** | [Provider documentation](https://openskynetwork.github.io/opensky-api/rest.html)

- **Provider:** OpenSky Network
- **Coverage:** Global receiver network; coverage varies
- **Type / access:** `live-feed` / `approval`
- **Formats:** JSON
- **Updates:** Near real time where receivers report; API quotas apply.
- **Security use:** Airspace awareness and aviation exposure research where licensed.
- **License / terms:** OAuth2 client credentials. Written license required for commercial entities and operational REST API use; see current terms.
- **Limitations:** ADS-B coverage gaps and incomplete identity data; does not supply airline schedules or establish passenger identity.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://opensky-network.org/api/states/all). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://openskynetwork.github.io/opensky-api/rest.html) · [Provider reference 2](https://opensky-network.org/about/terms-of-use)
- **Catalog ID:** `opensky`
