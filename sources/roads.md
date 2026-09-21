# Road traffic & transport

<!-- Generated from catalog/sources.json; edit the catalog, then run python tools/catalog.py build. -->

[All categories](../LIBRARY.md) | [How to use this library](../docs/getting-started.md)

Original catalog text: Copyright (c) 2026 Joseph Dillard and contributors, [CC BY 4.0](../LICENSE-CONTENT). [Scope and attribution](../LICENSING.md). Provider material retains its own terms.

<a id="ny-511"></a>

## 511NY traffic API

**[Visit source](https://511ny.org/)** | [Provider documentation](https://www.511ny.org/developers/help)

- **Provider:** New York State Department of Transportation
- **Coverage:** New York State and included neighboring observations
- **Type / access:** `live-feed` / `registration`
- **Formats:** JSON, XML
- **Updates:** Operational updates; inspect individual event times.
- **Security use:** Road incidents, closures, construction and travel disruption around routes.
- **License / terms:** Developer key and Developer Access Agreement required.
- **Limitations:** Coverage is not every street; camera availability does not confer unrestricted image reuse.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://511ny.org/api/v2/get/event). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://www.511ny.org/developers/help) · [Provider reference 2](https://www.511ny.org/developers/daa) · [Provider reference 3](https://511ny.org/help/endpoint/event)
- **Catalog ID:** `ny-511`

<a id="caltrans-quickmap"></a>

## Caltrans QuickMap

**[Visit source](https://quickmap.dot.ca.gov/)** | [Provider documentation](https://dot.ca.gov/travel)

- **Provider:** California Department of Transportation
- **Coverage:** California state highway network
- **Type / access:** `dashboard` / `open`
- **Formats:** Web map
- **Updates:** Operational traffic, closure and incident updates.
- **Security use:** California road closure and travel-condition awareness.
- **License / terms:** Public traveler information; check layer terms before integration. No supported API validated here.
- **Limitations:** Map layers have different providers and timestamps; QuickMap is not a navigation application.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://dot.ca.gov/travel) · [Provider reference 2](https://quickmap.dot.ca.gov/maps/traffic/mwebview.html)
- **Catalog ID:** `caltrans-quickmap`

<a id="drivetexas"></a>

## DriveTexas highway conditions

**[Visit source](https://drivetexas.org/)** | [Provider documentation](https://www.txdot.gov/about/newsroom/stories/be-your-own-traffic-reporter.html)

- **Provider:** Texas Department of Transportation
- **Coverage:** Texas state-maintained roads
- **Type / access:** `dashboard` / `open`
- **Formats:** Web map
- **Updates:** Updates from TxDOT operations; inspect event times.
- **Security use:** Texas road conditions, crashes, closures and logistics awareness.
- **License / terms:** Public traveler information; no supported public integration API validated here.
- **Limitations:** State roadway coverage does not establish the status of every local access road.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://www.txdot.gov/about/newsroom/stories/be-your-own-traffic-reporter.html)
- **Catalog ID:** `drivetexas`
