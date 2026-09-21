# Coverage and gaps

The collection is US-focused with global hazard, event, aviation, maritime, connectivity and mapping sources. The [city library](../CITIES.md) covers three places in each of the 50 states, with emergency-management, police/public-safety, water and electric references. It is not a comprehensive inventory of every jurisdiction or utility.

| Domain | Included | Gap to close for an operating area |
| --- | --- | --- |
| Crime | National statistics, Chicago and NYC reports; police/public-safety references for 150 places | Dedicated local open data, reporting lag and permitted call-for-service feeds |
| Public events and protests | GDELT, ACLED, NYC permits | City permits, official closures and local corroboration; no exhaustive protest feed is assumed |
| Weather and hazards | Weather alerts, hurricanes, flooding, fires, earthquakes, air quality; emergency/alert references for 150 places | Confirm local alert enrollment and evacuation-notice coverage |
| Air traffic | OpenSky, FAA status and aviation weather | Applicable operational licenses, flight-specific status and local airport notices |
| Sea traffic | Historical AIS, navigational warnings and a commercial live AIS option | Live data agreement and port-specific notices |
| Roads | New York API, California and Texas dashboards | Relevant state/province 511 services, local roads and transit operators |
| Government | OpenFEMA, Federal Register, Data.gov, ReliefWeb | Local government bulletins, international travel and public-health advisories |
| Power | Historical outage data, aggregate option and electric-provider references across 150 places | Verify serving utility by facility address, regional selections and usable restoration notices |
| Water | DC Water outage example, USGS/EPA context and water-service references across 150 places | Replace general department/quality pages with direct outage and boil-water notices where available |
| Connectivity | IODA and Cloudflare Radar | Serving-carrier status and direct, authorized service-health checks |
| Geographic context | OSM, Overture and HDX | Authoritative local boundaries, licensed asset inventories and verified facility locations |

## Local coverage and remaining gaps

The state pages use Census Vintage 2025 incorporated-place rankings, with 2020 Census CDPs for Hawaii. See the [selection method and review limits](city-methodology.md). All four source categories are present for every profile, but dedicated live feeds, complete utility territories and authenticated access are not established.

For deeper coverage in each operating area, look for:

- Emergency management alerts and official evacuation notices.
- Police incident/open-data portals and fire/EMS public notices.
- Permit calendars, major-event schedules and announced road closures.
- Electric utility outages and restoration notices.
- Water utility service disruptions and drinking-water advisories.
- Public transit service alerts, airport notices and port authority advisories.
- Public-health notices and hazardous-material incident information.

Use a provider documentation link and record registration requirements. If a source has no supported API, label it as a dashboard or notice page.

## Sources that need special access review

OpenSky, ACLED, MarineTraffic and PowerOutage.us have licensing or approval considerations relevant to operational use. ReliefWeb requires a pre-approved application name. NASA FIRMS, AirNow, 511NY and Cloudflare APIs require credentials or enrollment.

These notes aid source selection; current publisher terms remain authoritative. Pricing and account entitlements have not been negotiated or tested.
