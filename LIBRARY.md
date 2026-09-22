# Source library

<!-- Generated from catalog/sources.json; edit the catalog, then run python tools/catalog.py build. -->

Original catalog text: Copyright (c) 2026 Joseph Dillard and contributors, [CC BY 4.0](LICENSE-CONTENT). [Scope and attribution](LICENSING.md). Provider material retains its own terms.

**88 sources across 16 categories.** Catalog review: 2026-09-22.

Browse a category for source cards with documentation, access, limitations and evidence.
For local agencies and utilities, browse the [three largest places in every state](CITIES.md).
Access labels describe how to reach the source; they do not grant reuse rights. See the [access guide](README.md#access-labels).
Review status describes evidence inspected, not a successful integration test.

| Category | Sources |
| --- | ---: |
| [Weather, flooding & air quality](sources/weather.md) | 5 |
| [Natural hazards & disasters](sources/hazards.md) | 4 |
| [Crime & public safety](sources/crime.md) | 4 |
| [Public events, protests & conflict](sources/events.md) | 4 |
| [Air traffic & aviation](sources/aviation.md) | 5 |
| [Sea traffic & maritime safety](sources/maritime.md) | 4 |
| [Road traffic & transport](sources/roads.md) | 25 |
| [Government & humanitarian information](sources/government.md) | 5 |
| [Power outages & grid resilience](sources/power.md) | 3 |
| [Water outages & water systems](sources/water.md) | 3 |
| [Internet & communications disruptions](sources/connectivity.md) | 3 |
| [Maps, infrastructure & geographic context](sources/context.md) | 12 |
| [Critical events & risk intelligence](sources/risk-intelligence.md) | 6 |
| [Travel risk & assistance](sources/travel-risk.md) | 2 |
| [Protective intelligence & investigations](sources/protective-intelligence.md) | 1 |
| [Satellite orbits & space activity](sources/space.md) | 2 |

## All sources

| Source | Category | Type | Access |
| --- | --- | --- | --- |
| [AirNow air quality observations and forecasts](sources/weather.md#airnow) | Weather, flooding & air quality | live-feed | registration |
| [National Hurricane Center GIS products](sources/weather.md#nhc-gis) | Weather, flooding & air quality | mixed | open |
| [National Water Prediction Service](sources/weather.md#nwps) | Weather, flooding & air quality | live-feed | open |
| [NWS forecasts, observations and alerts](sources/weather.md#nws-alerts) | Weather, flooding & air quality | live-feed | open |
| [Open-Meteo weather models and current conditions](sources/weather.md#open-meteo) | Weather, flooding & air quality | periodic | mixed |
| [FIRMS active fire and thermal anomalies](sources/hazards.md#nasa-firms) | Natural hazards & disasters | live-feed | registration |
| [GDACS disaster alerts and geospatial services](sources/hazards.md#gdacs) | Natural hazards & disasters | live-feed | open |
| [USGS earthquake feeds](sources/hazards.md#usgs-earthquakes) | Natural hazards & disasters | live-feed | open |
| [Vantor Open Data Program disaster imagery](sources/hazards.md#vantor-open-data) | Natural hazards & disasters | catalog | open |
| [Base Operations local crime and unrest intelligence](sources/crime.md#base-operations) | Crime & public safety | periodic | commercial |
| [Chicago reported crimes](sources/crime.md#chicago-crime) | Crime & public safety | periodic | open |
| [FBI Crime Data Explorer](sources/crime.md#fbi-cde) | Crime & public safety | historical | open |
| [NYPD complaint data, current year to date](sources/crime.md#nyc-complaints) | Crime & public safety | periodic | open |
| [ACLED political violence and protest data](sources/events.md#acled) | Public events, protests & conflict | periodic | approval |
| [GDELT event and news data](sources/events.md#gdelt) | Public events, protests & conflict | live-feed | open |
| [Google News locality and topic RSS discovery](sources/events.md#google-news-rss) | Public events, protests & conflict | mixed | open |
| [NYC permitted event information](sources/events.md#nyc-permitted-events) | Public events, protests & conflict | periodic | open |
| [adsb.lol aircraft positions and traces](sources/aviation.md#adsb-lol) | Air traffic & aviation | mixed | open |
| [adsbdb aircraft and callsign metadata](sources/aviation.md#adsbdb) | Air traffic & aviation | reference | open |
| [Aviation Weather Center Data API](sources/aviation.md#aviation-weather) | Air traffic & aviation | live-feed | open |
| [FAA National Airspace System status](sources/aviation.md#faa-nas) | Air traffic & aviation | dashboard | open |
| [OpenSky aircraft state vectors](sources/aviation.md#opensky) | Air traffic & aviation | live-feed | mixed |
| [AISStream vessel message stream](sources/maritime.md#aisstream) | Sea traffic & maritime safety | live-feed | registration |
| [Marine Cadastre vessel traffic / AIS](sources/maritime.md#noaa-ais) | Sea traffic & maritime safety | historical | open |
| [MarineTraffic / Kpler AIS Data API](sources/maritime.md#marinetraffic) | Sea traffic & maritime safety | live-feed | commercial |
| [NGA maritime navigational warnings](sources/maritime.md#nga-maritime) | Sea traffic & maritime safety | dashboard | open |
| [511NY traffic API](sources/roads.md#ny-511) | Road traffic & transport | live-feed | registration |
| [Austin traffic camera inventory and public views](sources/roads.md#austin-traffic-cameras) | Road traffic & transport | mixed | open |
| [Calgary traffic camera inventory and images](sources/roads.md#calgary-traffic-cameras) | Road traffic & transport | mixed | open |
| [Caltrans CWWP2 traffic-camera data](sources/roads.md#caltrans-cctv) | Road traffic & transport | mixed | open |
| [Caltrans QuickMap](sources/roads.md#caltrans-quickmap) | Road traffic & transport | dashboard | open |
| [CapMetro real-time transit feeds](sources/roads.md#capmetro-realtime) | Road traffic & transport | live-feed | open |
| [DriveBC highway webcams](sources/roads.md#drivebc-webcams) | Road traffic & transport | mixed | open |
| [DriveTexas highway conditions](sources/roads.md#drivetexas) | Road traffic & transport | dashboard | open |
| [Entur Norway real-time transit feeds](sources/roads.md#entur-realtime) | Road traffic & transport | live-feed | open |
| [Fintraffic Digitraffic road-weather cameras and data](sources/roads.md#fintraffic-digitraffic) | Road traffic & transport | mixed | open |
| [FOSSGIS OpenStreetMap routing service](sources/roads.md#fossgis-osrm) | Road traffic & transport | reference | open |
| [GBFS shared-mobility feed directory and station availability](sources/roads.md#gbfs-bikeshare) | Road traffic & transport | catalog | open |
| [HSL Helsinki real-time transit feeds](sources/roads.md#hsl-realtime) | Road traffic & transport | live-feed | open |
| [Live Traffic NSW cameras](sources/roads.md#nsw-traffic-cameras) | Road traffic & transport | mixed | mixed |
| [MBTA real-time transit feeds](sources/roads.md#mbta-realtime) | Road traffic & transport | live-feed | open |
| [Metro Transit Twin Cities real-time feeds](sources/roads.md#metro-transit-realtime) | Road traffic & transport | live-feed | open |
| [Ontario 511 cameras and traveler-information API](sources/roads.md#ontario-511) | Road traffic & transport | mixed | mixed |
| [OVapi Netherlands real-time transit feeds](sources/roads.md#ovapi-realtime) | Road traffic & transport | live-feed | open |
| [Tallinn public intersection cameras](sources/roads.md#tallinn-traffic-cameras) | Road traffic & transport | dashboard | open |
| [Tark Tee road cameras and travel conditions](sources/roads.md#tarktee-road-cameras) | Road traffic & transport | mixed | open |
| [TfL Unified API and JamCam traffic cameras](sources/roads.md#tfl-jamcams) | Road traffic & transport | mixed | mixed |
| [TomTom traffic flow and incidents](sources/roads.md#tomtom-traffic) | Road traffic & transport | live-feed | commercial |
| [Translink South East Queensland real-time transit](sources/roads.md#translink-seq-realtime) | Road traffic & transport | live-feed | open |
| [TxDOT public traffic cameras](sources/roads.md#txdot-traffic-cameras) | Road traffic & transport | dashboard | open |
| [Warendorf municipal market-square webcam](sources/roads.md#warendorf-webcam) | Road traffic & transport | dashboard | open |
| [Data.gov catalog](sources/government.md#data-gov) | Government & humanitarian information | catalog | mixed |
| [Federal Register API](sources/government.md#federal-register) | Government & humanitarian information | periodic | open |
| [OpenFEMA disaster declarations and program data](sources/government.md#openfema) | Government & humanitarian information | periodic | open |
| [Radio Browser station directory](sources/government.md#radio-browser) | Government & humanitarian information | catalog | open |
| [ReliefWeb reports and disasters API](sources/government.md#reliefweb) | Government & humanitarian information | live-feed | approval |
| [Austin Energy outage map](sources/power.md#austin-energy) | Power outages & grid resilience | dashboard | open |
| [EAGLE-I historical power outage data, 2014-2022](sources/power.md#eaglei-history) | Power outages & grid resilience | historical | open |
| [PowerOutage.us](sources/power.md#poweroutage-us) | Power outages & grid resilience | mixed | commercial |
| [DC Water service alerts and outage map](sources/water.md#dc-water) | Water outages & water systems | dashboard | open |
| [EPA drinking-water systems and compliance data](sources/water.md#epa-sdwis) | Water outages & water systems | periodic | open |
| [USGS modern Water Data APIs](sources/water.md#usgs-water) | Water outages & water systems | live-feed | mixed |
| [Cloudflare Radar outages and traffic anomalies](sources/connectivity.md#cloudflare-radar) | Internet & communications disruptions | live-feed | registration |
| [IODA internet outage detection](sources/connectivity.md#ioda) | Internet & communications disruptions | live-feed | open |
| [TeleGeography Submarine Cable Map](sources/connectivity.md#telegeography-cables) | Internet & communications disruptions | reference | mixed |
| [Cesium ion global terrain and hosted content](sources/context.md#cesium-ion-terrain) | Maps, infrastructure & geographic context | reference | mixed |
| [DataSF Analysis Neighborhoods](sources/context.md#datasf-analysis-neighborhoods) | Maps, infrastructure & geographic context | reference | open |
| [Esri World Imagery basemap](sources/context.md#esri-world-imagery) | Maps, infrastructure & geographic context | reference | mixed |
| [Google Maps imagery, 3D tiles and place context](sources/context.md#google-maps-platform) | Maps, infrastructure & geographic context | reference | commercial |
| [Humanitarian Data Exchange](sources/context.md#hdx) | Maps, infrastructure & geographic context | catalog | mixed |
| [Natural Earth physical and cultural map data](sources/context.md#natural-earth) | Maps, infrastructure & geographic context | reference | open |
| [Nominatim OpenStreetMap geocoding](sources/context.md#nominatim-geocoding) | Maps, infrastructure & geographic context | reference | open |
| [Open Infrastructure Map](sources/context.md#open-infrastructure-map) | Maps, infrastructure & geographic context | reference | open |
| [OpenStreetMap](sources/context.md#openstreetmap) | Maps, infrastructure & geographic context | reference | open |
| [Overture Maps](sources/context.md#overture) | Maps, infrastructure & geographic context | reference | open |
| [Photon OpenStreetMap geocoding](sources/context.md#photon-geocoding) | Maps, infrastructure & geographic context | reference | open |
| [Re:Earth Terrain elevation and mesh service](sources/context.md#reearth-terrain) | Maps, infrastructure & geographic context | reference | open |
| [AlertMedia risk intelligence](sources/risk-intelligence.md#alertmedia) | Critical events & risk intelligence | mixed | commercial |
| [Dataminr for Corporate Security](sources/risk-intelligence.md#dataminr-corporate-security) | Critical events & risk intelligence | live-feed | commercial |
| [Everbridge Risk Intelligence](sources/risk-intelligence.md#everbridge-risk-intelligence) | Critical events & risk intelligence | mixed | commercial |
| [Factal verified event intelligence](sources/risk-intelligence.md#factal) | Critical events & risk intelligence | live-feed | commercial |
| [Samdesk incident detection and situational awareness](sources/risk-intelligence.md#samdesk) | Critical events & risk intelligence | live-feed | commercial |
| [Seerist event and risk intelligence](sources/risk-intelligence.md#seerist) | Critical events & risk intelligence | mixed | commercial |
| [Crisis24 Horizon](sources/travel-risk.md#crisis24-horizon) | Travel risk & assistance | mixed | commercial |
| [Riskline travel intelligence and alerts](sources/travel-risk.md#riskline) | Travel risk & assistance | mixed | commercial |
| [Ontic protective intelligence and investigations](sources/protective-intelligence.md#ontic) | Protective intelligence & investigations | mixed | commercial |
| [CelesTrak general perturbations orbital elements](sources/space.md#celestrak) | Satellite orbits & space activity | periodic | open |
| [Launch Library 2 spaceflight events](sources/space.md#launch-library-2) | Satellite orbits & space activity | mixed | mixed |

[Coverage gaps](docs/coverage.md) · [Review notes](docs/review-notes.md) · [Contribute a source](CONTRIBUTING.md)
