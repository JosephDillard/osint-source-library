# Weather, flooding & air quality

<!-- Generated from catalog/sources.json; edit the catalog, then run python tools/catalog.py build. -->

[All categories](../LIBRARY.md) | [How to use this library](../docs/getting-started.md)

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
