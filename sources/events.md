# Public events, protests & conflict

<!-- Generated from catalog/sources.json; edit the catalog, then run python tools/catalog.py build. -->

[All categories](../LIBRARY.md) | [How to use this library](../docs/getting-started.md)

<a id="acled"></a>

## ACLED political violence and protest data

**[Visit source](https://acleddata.com/)** | [Provider documentation](https://acleddata.com/acled-api-documentation)

- **Provider:** ACLED
- **Coverage:** Global; collection and release coverage vary
- **Type / access:** `periodic` / `approval`
- **Formats:** API, Downloads
- **Updates:** Curated releases and revisions; inspect product schedule.
- **Security use:** Regional context for event exposure and travel planning.
- **License / terms:** Account and applicable access agreement required. Commercial reuse and redistribution depend on ACLED's current EULA and written permissions.
- **Limitations:** Not an emergency feed; review event and geographic precision. A peaceful protest is not evidence of a threat.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://acleddata.com/acled-api-documentation) · [Provider reference 2](https://acleddata.com/eula) · [Provider reference 3](https://acleddata.com/contentusage)
- **Catalog ID:** `acled`

<a id="gdelt"></a>

## GDELT event and news data

**[Visit source](https://www.gdeltproject.org/)** | [Provider documentation](https://gdeltproject.org/data.html)

- **Provider:** The GDELT Project
- **Coverage:** Global news coverage; uneven by language and region
- **Type / access:** `live-feed` / `open`
- **Formats:** CSV, JSON, BigQuery
- **Updates:** Some GDELT 2.0 datasets update every 15 minutes; product windows vary.
- **Security use:** Discover reports of protests, disruption and other emerging events.
- **License / terms:** Provider describes database as free and open; underlying news articles retain publisher rights.
- **Limitations:** Machine-extracted events and place mentions need corroboration, deduplication and geolocation review.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://gdeltproject.org/data.html) · [Provider reference 2](https://blog.gdeltproject.org/gdelt-doc-2-0-api-debuts/)
- **Catalog ID:** `gdelt`

<a id="nyc-permitted-events"></a>

## NYC permitted event information

**[Visit source](https://data.cityofnewyork.us/City-Government/NYC-Permitted-Event-Information/tvpp-9vvx)** | [Provider documentation](https://data.cityofnewyork.us/api/views/tvpp-9vvx.json)

- **Provider:** NYC Office of Citywide Event Coordination and Management
- **Coverage:** New York City
- **Type / access:** `periodic` / `open`
- **Formats:** JSON, CSV, Socrata API
- **Updates:** Rolling list of approved events in the next month; inspect updates.
- **Security use:** Plan access, staffing and travel around permitted public events.
- **License / terms:** NYC Open Data terms apply; license identifier not supplied in reviewed metadata.
- **Limitations:** Does not include all gatherings. Film permits included only when street impacts meet the dataset's duration criterion.
- **Review:** 2026-09-20 — `provider-metadata-reviewed`
- **API entrypoint / example:** [Open endpoint](https://data.cityofnewyork.us/resource/tvpp-9vvx.json). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://data.cityofnewyork.us/api/views/tvpp-9vvx.json)
- **Catalog ID:** `nyc-permitted-events`
