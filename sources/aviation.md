# Air traffic & aviation

<!-- Generated from catalog/sources.json; edit the catalog, then run python tools/catalog.py build. -->

[All categories](../LIBRARY.md) | [How to use this library](../docs/getting-started.md)

Original catalog text: Copyright (c) 2026 Joseph Dillard and contributors, [CC BY 4.0](../LICENSE-CONTENT). [Scope and attribution](../LICENSING.md). Provider material retains its own terms.

<a id="adsb-lol"></a>

## adsb.lol aircraft positions and traces

**[Visit source](https://www.adsb.lol/)** | [Provider documentation](https://www.adsb.lol/docs/open-data/api/)

- **Provider:** adsb.lol contributor network
- **Coverage:** Global volunteer receiver network; reception and altitude determine actual coverage.
- **Type / access:** `mixed` / `open`
- **Formats:** JSON, ADS-B / MLAT positions
- **Updates:** Near-real-time reports where received; use position age and source timestamps rather than animation speed.
- **Security use:** Aircraft activity near airports and operating areas; compare civilian and military-classified contacts.
- **License / terms:** API data is published under ODbL 1.0; retain attribution and applicable database share-alike obligations. Public access does not provide an SLA.
- **Limitations:** The project also uses the regional /v2/lat/{lat}/lon/{lon}/dist/{radius} API. Its tar1090 trace-file path is an undocumented dependency, not a supported history API established here. Missing aircraft do not prove absence.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://api.adsb.lol/v2/mil). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://www.adsb.lol/docs/open-data/api/) · [Provider reference 2](https://api.adsb.lol/docs) · [Provider reference 3](https://www.adsb.lol/docs/overview/introduction/)
- **Catalog ID:** `adsb-lol`

<a id="adsbdb"></a>

## adsbdb aircraft and callsign metadata

**[Visit source](https://www.adsbdb.com/)** | [Provider documentation](https://www.adsbdb.com/)

- **Provider:** adsbdb / upstream aircraft and route contributors
- **Coverage:** International aircraft and callsign database; matching completeness varies.
- **Type / access:** `reference` / `open`
- **Formats:** JSON
- **Updates:** Lookup service; no reliable public refresh commitment established in this review.
- **Security use:** Enrich an observed aircraft identifier with type, registration and route context.
- **License / terms:** Underlying aircraft and route data have separate contributor rights. Full reuse and redistribution terms were not independently established; do not infer rights from public API access or software licensing.
- **Limitations:** Not a position feed or authoritative airline schedule. Website documentation rendered incompletely; project code identifies /aircraft/{identifier} and /callsign/{callsign}. Route matches may be stale or ambiguous. API routes are retained as discovery context only until current primary documentation can be fully reviewed.
- **Review:** 2026-09-22 — `partial-review`
- **Evidence:** [Provider reference 1](https://www.adsbdb.com/)
- **Catalog ID:** `adsbdb`

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
- **Type / access:** `live-feed` / `mixed`
- **Formats:** JSON
- **Updates:** Near-real-time state vectors where received. Anonymous access: 400 daily credits; standard authenticated access: 4,000. Global states query costs four credits; verify current tiers.
- **Security use:** Airspace awareness and aviation exposure research where licensed.
- **License / terms:** Anonymous position queries are technically available; OAuth2 client credentials enable authenticated tiers. Commercial entities and operational REST API use require a written license under current OpenSky terms.
- **Limitations:** Receiver coverage and position age vary. No airline schedules or passenger identity. Client polling, cache age and interpolated animation must remain distinct from the latest position timestamp.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://opensky-network.org/api/states/all). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://openskynetwork.github.io/opensky-api/rest.html) · [Provider reference 2](https://opensky-network.org/about/terms-of-use)
- **Catalog ID:** `opensky`
