# Sea traffic & maritime safety

<!-- Generated from catalog/sources.json; edit the catalog, then run python tools/catalog.py build. -->

[All categories](../LIBRARY.md) | [How to use this library](../docs/getting-started.md)

Original catalog text: Copyright (c) 2026 Joseph Dillard and contributors, [CC BY 4.0](../LICENSE-CONTENT). [Scope and attribution](../LICENSING.md). Provider material retains its own terms.

<a id="noaa-ais"></a>

## Marine Cadastre vessel traffic / AIS

**[Visit source](https://marinecadastre.gov/ais/)** | [Provider documentation](https://coast.noaa.gov/digitalcoast/data/vesseltraffic.html)

- **Provider:** BOEM / NOAA / US Coast Guard
- **Coverage:** US coastal waters and supported vessel-traffic products
- **Type / access:** `historical` / `open`
- **Formats:** CSV, GeoPackage, GeoTIFF, Esri web services
- **Updates:** Published archives and derived products; inspect each release.
- **Security use:** Historical shipping patterns, port approaches and maritime exposure planning.
- **License / terms:** Publicly distributed products; retain dataset metadata and check release-specific use constraints.
- **Limitations:** Not a live AIS feed. AccessAIS ordering was unavailable when reviewed; its page points to bulk downloads.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://coast.noaa.gov/digitalcoast/data/vesseltraffic.html) · [Provider reference 2](https://marinecadastre.gov/accessais/)
- **Catalog ID:** `noaa-ais`

<a id="marinetraffic"></a>

## MarineTraffic / Kpler AIS Data API

**[Visit source](https://www.marinetraffic.com/)** | [Provider documentation](https://servicedocs.marinetraffic.com/)

- **Provider:** Kpler / MarineTraffic
- **Coverage:** Global, subject to receiver coverage and subscription
- **Type / access:** `live-feed` / `commercial`
- **Formats:** API
- **Updates:** Service- and subscription-dependent live and historical access.
- **Security use:** Vessel-position and maritime logistics awareness where contracted.
- **License / terms:** Proprietary API; API key and applicable paid agreement required. Included as a licensed option.
- **Limitations:** Public map access does not grant bulk API or redistribution rights; AIS can be delayed or incomplete.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://servicedocs.marinetraffic.com/)
- **Catalog ID:** `marinetraffic`

<a id="nga-maritime"></a>

## NGA maritime navigational warnings

**[Visit source](https://msi.nga.mil/)** | [Provider documentation](https://msi.nga.mil/NavWarnings)

- **Provider:** National Geospatial-Intelligence Agency
- **Coverage:** Maritime warning areas and US shipping interests; coverage varies
- **Type / access:** `dashboard` / `open`
- **Formats:** Web notices, Text
- **Updates:** Warnings issued and cancelled as conditions change.
- **Security use:** Maritime route awareness, navigation hazards and regional shipping disruption.
- **License / terms:** Public maritime safety information; follow product usage notices.
- **Limitations:** Not a live vessel feed and not a replacement for required official onboard warning services.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://msi.nga.mil/NavWarnings)
- **Catalog ID:** `nga-maritime`
