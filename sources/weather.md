# Weather, flooding & air quality

<!-- Generated from catalog/sources.json; edit the catalog, then run python tools/catalog.py build. -->

[All categories](../LIBRARY.md) | [How to use this library](../docs/getting-started.md)

Original catalog text: Copyright (c) 2026 Joseph Dillard and contributors, [CC BY 4.0](../LICENSE-CONTENT). [Scope and attribution](../LICENSING.md). Provider material retains its own terms.

<a id="airnow"></a>

## AirNow air quality observations and forecasts

**[Visit source](https://www.airnow.gov/)** | [Provider documentation](https://docs.airnowapi.org/webservices)

- **Provider:** US EPA and AirNow partners
- **Coverage:** Supported reporting areas, principally United States
- **Type / access:** `live-feed` / `registration`
- **Formats:** JSON, CSV, XML, KML
- **Updates:** Observation and forecast schedules vary; see endpoint documentation.
- **Security use:** Smoke and air-quality awareness for outdoor staff and facility operations.
- **License / terms:** API key required; follow AirNow Data Use Guidelines and request limits.
- **Limitations:** Preliminary regional observations are not a measurement of indoor conditions.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://docs.airnowapi.org/webservices) · [Provider reference 2](https://docs.airnowapi.org/faq)
- **Catalog ID:** `airnow`

<a id="nhc-gis"></a>

## National Hurricane Center GIS products

**[Visit source](https://www.nhc.noaa.gov/)** | [Provider documentation](https://www.nhc.noaa.gov/gis)

- **Provider:** NOAA / National Hurricane Center
- **Coverage:** Atlantic and eastern North Pacific; product coverage varies
- **Type / access:** `mixed` / `open`
- **Formats:** Shapefile, KML, KMZ
- **Updates:** Advisory and product schedules; archives are also available.
- **Security use:** Hurricane planning, coastal facilities and port disruption awareness.
- **License / terms:** Public NOAA products; retain attribution and product-specific caveats.
- **Limitations:** The forecast cone describes track uncertainty, not the full area of hazards.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://www.nhc.noaa.gov/gis)
- **Catalog ID:** `nhc-gis`

<a id="nwps"></a>

## National Water Prediction Service

**[Visit source](https://water.noaa.gov/)** | [Provider documentation](https://api.water.noaa.gov/about/api)

- **Provider:** NOAA / National Weather Service
- **Coverage:** United States; coverage varies by gauge and model product
- **Type / access:** `live-feed` / `open`
- **Formats:** JSON, GIS web services
- **Updates:** Observation, forecast and model schedules vary.
- **Security use:** River flooding awareness near sites, access roads and supply routes.
- **License / terms:** Public NOAA service; check each GIS product's terms and operational status.
- **Limitations:** Flood forecasts and river gauges do not report drinking-water service outages.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://api.water.noaa.gov/about/api)
- **Catalog ID:** `nwps`

<a id="nws-alerts"></a>

## NWS forecasts, observations and alerts

**[Visit source](https://www.weather.gov/)** | [Provider documentation](https://www.weather.gov/documentation/services-web-api)

- **Provider:** NOAA / National Weather Service
- **Coverage:** United States and supported territories
- **Type / access:** `live-feed` / `open`
- **Formats:** GeoJSON, JSON-LD, CAP, Atom
- **Updates:** Event driven; observations can lag. Respect cache headers and rate limits.
- **Security use:** Weather alerts around facilities, outdoor operations and travel corridors.
- **License / terms:** Documentation permits free use for any purpose; identify the application with a User-Agent.
- **Limitations:** Some alerts use forecast zones without direct polygon geometry; an alert does not confirm damage.
- **Review:** 2026-09-21 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://api.weather.gov/alerts/active). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://www.weather.gov/documentation/services-web-api)
- **Catalog ID:** `nws-alerts`

<a id="nws-forecast-zones"></a>

## NWS public forecast-zone boundaries

**[Visit source](https://www.weather.gov/gis/PublicZones)** | [Provider documentation](https://www.weather.gov/gis/PublicZones)

- **Provider:** NOAA / National Weather Service
- **Coverage:** NWS public forecast zones in supported U.S. jurisdictions; this product does not cover every alert-zone type.
- **Type / access:** `periodic` / `open`
- **Formats:** Zipped polygon Shapefile, Metadata and change history
- **Updates:** Releases follow zone changes and carry effective dates; select the boundary version applicable to the alert time.
- **Security use:** Provide reference polygons for supported forecast-zone alerts without supplied geometry, enabling explicitly labeled area-level exposure screening.
- **License / terms:** NWS information is public domain unless otherwise noted. Preserve attribution and product metadata; identify transformed geometry and do not present it as an unmodified official product or imply endorsement.
- **Limitations:** Public forecast zones can be county subsets. Match the identifier namespace and effective date; fire, county and marine references require appropriate products. A resolved zone is an alert-area reference, not observed hazard extent or confirmed damage. Unmatched or ambiguous references must remain geometry gaps.
- **Review:** 2026-09-26 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://www.weather.gov/gis/PublicZones) · [Provider reference 2](https://www.weather.gov/documentation/services-web-api) · [Provider reference 3](https://www.weather.gov/disclaimer)
- **Catalog ID:** `nws-forecast-zones`

<a id="open-meteo"></a>

## Open-Meteo weather models and current conditions

**[Visit source](https://open-meteo.com/)** | [Provider documentation](https://open-meteo.com/en/docs)

- **Provider:** Open-Meteo / contributing weather agencies
- **Coverage:** Global model coverage; resolution and available variables differ by model and region.
- **Type / access:** `periodic` / `mixed`
- **Formats:** JSON, CSV, XLSX
- **Updates:** Model-dependent runs; current conditions are based on 15-minutely model data.
- **Security use:** Weather context and forecasts for outdoor operations, routes and facilities.
- **License / terms:** Data uses CC BY 4.0 with attribution. The hosted free API is restricted to noncommercial use and quotas; commercial service access requires an appropriate subscription.
- **Limitations:** Current conditions are modeled estimates, not necessarily a nearby station observation. Weather animation is a visualization, not measured cloud geometry; retain model/time information.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://api.open-meteo.com/v1/forecast). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://open-meteo.com/en/docs) · [Provider reference 2](https://open-meteo.com/en/terms) · [Provider reference 3](https://open-meteo.com/en/licence)
- **Catalog ID:** `open-meteo`
