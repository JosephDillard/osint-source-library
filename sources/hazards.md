# Natural hazards & disasters

<!-- Generated from catalog/sources.json; edit the catalog, then run python tools/catalog.py build. -->

[All categories](../LIBRARY.md) | [How to use this library](../docs/getting-started.md)

Original catalog text: Copyright (c) 2026 Joseph Dillard and contributors, [CC BY 4.0](../LICENSE-CONTENT). [Scope and attribution](../LICENSING.md). Provider material retains its own terms.

<a id="nasa-firms"></a>

## FIRMS active fire and thermal anomalies

**[Visit source](https://firms.modaps.eosdis.nasa.gov/)** | [Provider documentation](https://firms.modaps.eosdis.nasa.gov/api/area/)

- **Provider:** NASA / LANCE
- **Coverage:** Global for MODIS/VIIRS; some products restricted to US/Canada
- **Type / access:** `live-feed` / `registration`
- **Formats:** CSV, KML, WMS, WFS
- **Updates:** Satellite overpass and processing dependent; NRT, RT and URT availability varies.
- **Security use:** Wildfire awareness around sites, routes and utility corridors.
- **License / terms:** Free MAP_KEY for API use; follow NASA/FIRMS attribution and transaction limits.
- **Limitations:** Thermal detections can represent industrial heat; points are not fire perimeters or confirmed impact.
- **Review:** 2026-09-21 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://firms.modaps.eosdis.nasa.gov/api/area/) · [Provider reference 2](https://firms.modaps.eosdis.nasa.gov/api/)
- **Catalog ID:** `nasa-firms`

<a id="gdacs"></a>

## GDACS disaster alerts and geospatial services

**[Visit source](https://www.gdacs.org/)** | [Provider documentation](https://www.gdacs.org/gdacsapi/swagger/index.html)

- **Provider:** United Nations / European Commission partnership
- **Coverage:** Global
- **Type / access:** `live-feed` / `open`
- **Formats:** GeoJSON, RSS/XML, KML
- **Updates:** Published RSS feed reference specifies six-minute refreshes; inspect each event's timestamp and selected product schedule.
- **Security use:** International disaster awareness and regional exposure screening.
- **License / terms:** API quickstart describes free data access; check attribution and individual product terms.
- **Limitations:** Modelled alert levels are screening signals; local impacts require confirmation.
- **Review:** 2026-09-21 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://www.gdacs.org/gdacsapi/swagger/index.html) · [Provider reference 2](https://gdacs.org/Documents/2025/GDACS_API_quickstart_v1.pdf) · [Provider reference 3](https://gdacs.org/feed_reference.aspx)
- **Catalog ID:** `gdacs`

<a id="usgs-earthquakes"></a>

## USGS earthquake feeds

**[Visit source](https://earthquake.usgs.gov/)** | [Provider documentation](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php)

- **Provider:** US Geological Survey
- **Coverage:** Global, with uneven detection thresholds
- **Type / access:** `live-feed` / `open`
- **Formats:** GeoJSON, Atom, CSV, QuakeML
- **Updates:** Summary feeds refresh every minute; events can be revised.
- **Security use:** Seismic awareness and initial screening of potentially exposed facilities.
- **License / terms:** Public USGS data; retain source attribution and revision timestamps.
- **Limitations:** Magnitude and distance alone do not establish site damage; use appropriate shaking products.
- **Review:** 2026-09-21 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php)
- **Catalog ID:** `usgs-earthquakes`

<a id="vantor-open-data"></a>

## Vantor Open Data Program disaster imagery

**[Visit source](https://vantor.com/company/open-data-program/)** | [Provider documentation](https://vantor.com/company/open-data-program/)

- **Provider:** Vantor
- **Coverage:** Selected major disaster activations worldwide; event footprints and acquisition dates vary.
- **Type / access:** `catalog` / `open`
- **Formats:** Satellite imagery, GeoTIFF, Event downloads
- **Updates:** Event-triggered selected before/after image releases; not continuous global observation.
- **Security use:** Compare disaster-area imagery for situational awareness and humanitarian impact assessment within permitted use.
- **License / terms:** Provider identifies Creative Commons BY-NC 4.0 for Open Data Program imagery. Preserve attribution and noncommercial restrictions; confirm each activation and obtain separate permission for incompatible uses.
- **Limitations:** Clouds, acquisition timing and selective activation constrain coverage. The project bundles two dated Nepal-event image crops; those are not a live imagery feed. Visual change alone does not establish damage cause or severity.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://vantor.com/company/open-data-program/)
- **Catalog ID:** `vantor-open-data`
