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

<a id="austin-traffic-cameras"></a>

## Austin traffic camera inventory and public views

**[Visit source](https://data.austintexas.gov/Transportation-and-Mobility/Traffic-Cameras/b4k4-adkb)** | [Provider documentation](https://data.austintexas.gov/api/views/b4k4-adkb.json)

- **Provider:** City of Austin Transportation and Public Works
- **Coverage:** Austin, Texas municipal traffic-camera locations.
- **Type / access:** `mixed` / `open`
- **Formats:** Socrata JSON, CSV, Web camera imagery
- **Updates:** Inventory metadata states daily updates; image freshness is separate and camera-dependent.
- **Security use:** Visually corroborate traffic conditions near Austin routes and sites.
- **License / terms:** Catalog metadata marks the inventory PUBLIC_DOMAIN. Do not assume that this metadata declaration independently licenses every image stream; confirm camera-service reuse.
- **Limitations:** Locations are approximate. The city states footage is not recorded or retained; inventory availability does not establish camera health or an archive.
- **Review:** 2026-09-22 — `provider-metadata-reviewed`
- **API entrypoint / example:** [Open endpoint](https://data.austintexas.gov/resource/b4k4-adkb.json). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://data.austintexas.gov/api/views/b4k4-adkb.json)
- **Catalog ID:** `austin-traffic-cameras`

<a id="calgary-traffic-cameras"></a>

## Calgary traffic camera inventory and images

**[Visit source](https://data.calgary.ca/Transportation-Transit/Traffic-Cameras/k7p9-kppz)** | [Provider documentation](https://data.calgary.ca/api/views/k7p9-kppz.json)

- **Provider:** City of Calgary
- **Coverage:** Major Calgary routes and selected intersections.
- **Type / access:** `mixed` / `open`
- **Formats:** Socrata JSON, CSV, Camera stills
- **Updates:** Inventory metadata states daily updates; images are described as up-to-the-minute, with per-camera availability limits.
- **Security use:** Corroborate traffic and access conditions around Calgary operating areas.
- **License / terms:** Dataset metadata points to City of Calgary Open Data Terms; follow the linked license and attribution requirements rather than assuming public domain.
- **Limitations:** Provider states footage is not recorded and cameras may be disabled for maintenance or to protect people involved in collisions. A missing image is not evidence of a clear road.
- **Review:** 2026-09-22 — `provider-metadata-reviewed`
- **API entrypoint / example:** [Open endpoint](https://data.calgary.ca/resource/k7p9-kppz.json). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://data.calgary.ca/api/views/k7p9-kppz.json) · [Provider reference 2](https://data.calgary.ca/d/Open-Data-Terms/u45n-7awa)
- **Catalog ID:** `calgary-traffic-cameras`

<a id="caltrans-cctv"></a>

## Caltrans CWWP2 traffic-camera data

**[Visit source](https://cwwp2.dot.ca.gov/)** | [Provider documentation](https://cwwp2.dot.ca.gov/documentation/cctv/cctv.htm)

- **Provider:** California Department of Transportation
- **Coverage:** California highway cameras, published by Caltrans district.
- **Type / access:** `mixed` / `open`
- **Formats:** JSON, CSV, XML, Camera stills and video
- **Updates:** District catalogs update as necessary; individual images/streams have separate refresh timing.
- **Security use:** Corroborate California road, visibility and disruption reports with camera imagery.
- **License / terms:** Caltrans documents no-charge integration access subject to its Conditions of Use; retain provider attribution and inspect imagery restrictions.
- **Limitations:** Endpoint is a District 7 example, not the statewide catalog. District completeness varies; Caltrans states imagery is not retained or archived. Distinct from the existing QuickMap dashboard entry.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://cwwp2.dot.ca.gov/data/d7/cctv/cctvStatusD07.json). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://cwwp2.dot.ca.gov/documentation/cctv/cctv.htm)
- **Catalog ID:** `caltrans-cctv`

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

<a id="capmetro-realtime"></a>

## CapMetro real-time transit feeds

**[Visit source](https://www.capmetro.org/developertools)** | [Provider documentation](https://www.capmetro.org/developertools)

- **Provider:** Capital Metropolitan Transportation Authority
- **Coverage:** Austin and the CapMetro service area, Texas.
- **Type / access:** `live-feed` / `open`
- **Formats:** GTFS-Realtime Protocol Buffers, GTFS schedules
- **Updates:** Operational vehicle, trip and service-alert updates; inspect message timestamps.
- **Security use:** Public-transit service continuity, route disruption and last-mile access planning.
- **License / terms:** CapMetro grants limited, revocable use, reproduction and redistribution subject to its terms. Agency trademarks cannot be used in association with the data.
- **Limitations:** Texas open-data download is the vehicle-position resource used by the project; other resources cover trip updates and alerts. Vehicle positions are reports with age and coverage gaps; interpolation is not an additional measurement. Join identifiers to the matching static GTFS version.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://data.texas.gov/download/eiei-9rpf/application%2Foctet-stream). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://www.capmetro.org/developertools) · [Provider reference 2](https://data.texas.gov/Transportation/CapMetro-VehiclePositions/eiei-9rpf)
- **Catalog ID:** `capmetro-realtime`

<a id="drivebc-webcams"></a>

## DriveBC highway webcams

**[Visit source](https://www.drivebc.ca/)** | [Provider documentation](https://www.drivebc.ca/api/webcams/)

- **Provider:** Government of British Columbia
- **Coverage:** British Columbia highway camera locations.
- **Type / access:** `mixed` / `open`
- **Formats:** Web camera stills, JSON catalog
- **Updates:** Camera-specific image refresh; inspect image timestamps independently of catalog retrieval.
- **Security use:** Visual road-weather and route-condition corroboration in British Columbia.
- **License / terms:** Confirm applicability of the Open Government Licence - British Columbia to the selected catalog and imagery; public retrieval alone does not settle reuse.
- **Limitations:** Public JSON camera metadata was retrieved. A supported API contract and image-reuse scope were not independently established; endpoint remains unset. Camera failures and delayed stills are possible.
- **Review:** 2026-09-22 — `partial-review`
- **Evidence:** [Provider reference 1](https://www.drivebc.ca/api/webcams/) · [Provider reference 2](https://www2.gov.bc.ca/gov/content/data/open-data/open-government-licence-bc)
- **Catalog ID:** `drivebc-webcams`

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

<a id="entur-realtime"></a>

## Entur Norway real-time transit feeds

**[Visit source](https://developer.entur.no/)** | [Provider documentation](https://developer.entur.org/pages-real-time-intro/)

- **Provider:** Entur AS / Norwegian transport operators
- **Coverage:** Included Norwegian public-transport operators.
- **Type / access:** `live-feed` / `open`
- **Formats:** GTFS-Realtime Protocol Buffers, GTFS schedules
- **Updates:** Reviewed documentation describes GTFS-Realtime dataset refresh every 15 seconds.
- **Security use:** Public-transit service continuity, route disruption and last-mile access planning.
- **License / terms:** Most open APIs use NLOD; identify the application with ET-Client-Name. Privileged APIs have separate authorization requirements.
- **Limitations:** Developer documentation is migrating to developer.entur.no; confirm the current feed and policy before integration. Vehicle positions are reports with age and coverage gaps; interpolation is not an additional measurement. Join identifiers to the matching static GTFS version.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://api.entur.io/realtime/v1/gtfs-rt/vehicle-positions). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://developer.entur.org/pages-real-time-intro/) · [Provider reference 2](https://developer.entur.org/pages-intro-authentication/)
- **Catalog ID:** `entur-realtime`

<a id="fintraffic-digitraffic"></a>

## Fintraffic Digitraffic road-weather cameras and data

**[Visit source](https://www.digitraffic.fi/en/)** | [Provider documentation](https://www.digitraffic.fi/en/road-traffic/)

- **Provider:** Fintraffic / Digitraffic
- **Coverage:** Finnish road monitoring stations and weather-camera presets.
- **Type / access:** `mixed` / `open`
- **Formats:** GeoJSON, JSON, JPEG, REST
- **Updates:** Camera and station-dependent periodic updates; inspect image capture times and station collection intervals.
- **Security use:** Road-weather and visibility context for travel and logistics in Finland.
- **License / terms:** CC BY 4.0 with Fintraffic attribution; follow API guidance, identification headers, caching and current rate restrictions.
- **Limitations:** Weather-camera images are periodic stills, not continuous video. Inactive presets and collection gaps must remain visible.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://tie.digitraffic.fi/api/weathercam/v1/stations). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://www.digitraffic.fi/en/road-traffic/) · [Provider reference 2](https://www.digitraffic.fi/en/terms-of-service/)
- **Catalog ID:** `fintraffic-digitraffic`

<a id="fossgis-osrm"></a>

## FOSSGIS OpenStreetMap routing service

**[Visit source](https://routing.openstreetmap.de/)** | [Provider documentation](https://routing.openstreetmap.de/about.html)

- **Provider:** FOSSGIS e.V. / OSRM / OpenStreetMap contributors
- **Coverage:** OSM-covered road, cycling and walking networks; profile and regional completeness vary.
- **Type / access:** `reference` / `open`
- **Formats:** JSON routes, GeoJSON, Encoded polyline
- **Updates:** Routes computed on request from processed map data; not a live road-closure service.
- **Security use:** Preliminary route alternatives for travel and site-access planning.
- **License / terms:** ODbL-derived data plus FOSSGIS hosted-service policy. Attribution, a fix-the-map link and identified clients are required; maximum one request/second, no scraping or heavy use, and commercial restrictions apply.
- **Limitations:** Routing does not prove current passability, legal access or emergency suitability. Use provider documentation for current car/bike/foot endpoints and arrange self-hosting or licensed capacity for sustained use.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://routing.openstreetmap.de/about.html) · [Provider reference 2](https://www.fossgis.de/arbeitsgruppen/osm-server/nutzungsbedingungen/)
- **Catalog ID:** `fossgis-osrm`

<a id="gbfs-bikeshare"></a>

## GBFS shared-mobility feed directory and station availability

**[Visit source](https://gbfs.org/)** | [Provider documentation](https://gbfs.org/documentation/)

- **Provider:** Individual mobility operators / MobilityData GBFS directory
- **Coverage:** Global directory; audited project configures 32 U.S. systems including Citi Bike, Divvy, Capital Bikeshare, Bay Wheels, BCycle and PBSC-hosted operators.
- **Type / access:** `catalog` / `open`
- **Formats:** GBFS JSON, CSV system directory
- **Updates:** Operator-specific station_status reports with last_updated and TTL; directory changes are separate.
- **Security use:** Discover public station availability for alternative transport and last-mile continuity.
- **License / terms:** GBFS is a specification, not a common license for every operator. Read each feed system_information license URL or license identifier and terms; commercial reuse is not presumed.
- **Limitations:** Directory entry and schema compatibility do not establish active service, feed health or individual rider movement. All 32 configured systems were inventoried, not individually integration-tested; see the project-source audit.
- **Review:** 2026-09-22 — `partial-review`
- **Evidence:** [Provider reference 1](https://gbfs.org/documentation/) · [Provider reference 2](https://github.com/MobilityData/gbfs/blob/master/systems.csv)
- **Catalog ID:** `gbfs-bikeshare`

<a id="hsl-realtime"></a>

## HSL Helsinki real-time transit feeds

**[Visit source](https://www.hsl.fi/en/hsl/open-data)** | [Provider documentation](https://hsldevcom.github.io/gtfs_rt/)

- **Provider:** Helsinki Region Transport
- **Coverage:** Helsinki region, Finland.
- **Type / access:** `live-feed` / `open`
- **Formats:** GTFS-Realtime Protocol Buffers, GTFS schedules
- **Updates:** Feed-specific real-time updates; use the documented update table and message timestamps.
- **Security use:** Public-transit service continuity, route disruption and last-mile access planning.
- **License / terms:** HSL transit data is CC BY 4.0; credit HSL and delivery time. OSM-derived geometry uses separate ODbL terms.
- **Limitations:** Vehicle positions, trip updates and alerts have separate endpoints. Other Digitransit services can have different access requirements. Vehicle positions are reports with age and coverage gaps; interpolation is not an additional measurement. Join identifiers to the matching static GTFS version.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://realtime.hsl.fi/realtime/vehicle-positions/v2/hsl). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://hsldevcom.github.io/gtfs_rt/) · [Provider reference 2](https://www.hsl.fi/en/hsl/open-data)
- **Catalog ID:** `hsl-realtime`

<a id="nsw-traffic-cameras"></a>

## Live Traffic NSW cameras

**[Visit source](https://opendata.transport.nsw.gov.au/dataset/live-traffic-cameras)** | [Provider documentation](https://opendata.transport.nsw.gov.au/dataset/live-traffic-cameras)

- **Provider:** Transport for NSW
- **Coverage:** New South Wales published traffic-camera sites.
- **Type / access:** `mixed` / `mixed`
- **Formats:** GeoJSON, Camera images
- **Updates:** Periodic camera images and catalog updates; inspect per-image timestamps.
- **Security use:** Road-condition corroboration and travel planning in New South Wales.
- **License / terms:** Official catalog lists Creative Commons Attribution. Preserve the feed rights object and verify current portal/login and image-specific conditions.
- **Limitations:** Camera URLs, locations and view descriptions are supplied. Catalog access does not establish continuous video, accurate pose or incident detection; portal resources may require login.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://data.livetraffic.com/cameras/traffic-cam.json). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://opendata.transport.nsw.gov.au/dataset/live-traffic-cameras) · [Provider reference 2](https://opendata.transport.nsw.gov.au/sites/default/files/2023-08/Live_Traffic_Data_Developer_Guide.pdf)
- **Catalog ID:** `nsw-traffic-cameras`

<a id="mbta-realtime"></a>

## MBTA real-time transit feeds

**[Visit source](https://www.mbta.com/developers)** | [Provider documentation](https://www.mbta.com/developers)

- **Provider:** MBTA / MassDOT
- **Coverage:** Greater Boston, Massachusetts, by supported mode.
- **Type / access:** `live-feed` / `open`
- **Formats:** GTFS-Realtime Protocol Buffers, GTFS schedules
- **Updates:** Operational real-time reports; exact per-feed cadence not independently verified.
- **Security use:** Public-transit service continuity, route disruption and last-mile access planning.
- **License / terms:** MassDOT developer license governs use and attribution. Full agreement retrieval was blocked; confirm current redistribution and trademark conditions.
- **Limitations:** The project uses the public VehiclePositions feed. Documentation and license retrieval were incomplete; API availability is not certified. Vehicle positions are reports with age and coverage gaps; interpolation is not an additional measurement. Join identifiers to the matching static GTFS version.
- **Review:** 2026-09-22 — `partial-review`
- **API entrypoint / example:** [Open endpoint](https://cdn.mbta.com/realtime/VehiclePositions.pb). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://www.mbta.com/developers) · [Provider reference 2](https://cdn.mbta.com/sites/default/files/2023-08/mbta-massdot-develop-license-agreement.pdf)
- **Catalog ID:** `mbta-realtime`

<a id="metro-transit-realtime"></a>

## Metro Transit Twin Cities real-time feeds

**[Visit source](https://svc.metrotransit.org/)** | [Provider documentation](https://svc.metrotransit.org/)

- **Provider:** Metro Transit / Metropolitan Council
- **Coverage:** Minneapolis-Saint Paul service area, Minnesota.
- **Type / access:** `live-feed` / `open`
- **Formats:** GTFS-Realtime Protocol Buffers, GTFS schedules
- **Updates:** Provider documents GTFS-Realtime refresh every five seconds; individual observations can be older.
- **Security use:** Public-transit service continuity, route disruption and last-mile access planning.
- **License / terms:** Public developer feeds are documented, but a complete reuse license for the real-time feed was not established. Do not transfer the companion static schedule dataset license automatically.
- **Limitations:** Includes documented vehicle, trip-update and service-alert feeds. Redistribution terms need confirmation. Vehicle positions are reports with age and coverage gaps; interpolation is not an additional measurement. Join identifiers to the matching static GTFS version.
- **Review:** 2026-09-22 — `partial-review`
- **API entrypoint / example:** [Open endpoint](https://svc.metrotransit.org/mtgtfs/vehiclepositions.pb). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://svc.metrotransit.org/)
- **Catalog ID:** `metro-transit-realtime`

<a id="ontario-511"></a>

## Ontario 511 cameras and traveler-information API

**[Visit source](https://511on.ca/)** | [Provider documentation](https://511on.ca/developers/doc)

- **Provider:** Ontario Ministry of Transportation
- **Coverage:** Ontario provincial road network and listed transport facilities.
- **Type / access:** `mixed` / `mixed`
- **Formats:** JSON, XML, Camera imagery
- **Updates:** Resource-dependent operational updates; documentation limits calls to ten per 60 seconds.
- **Security use:** Highway closures, road conditions and camera corroboration for Ontario operations.
- **License / terms:** Review Ontario open-government licensing, imagery conditions and developer access requirements before reuse; no authenticated integration performed.
- **Limitations:** Catalog positions do not establish camera field of view or current image availability. Honor throttling and inspect each resource timestamp.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://511on.ca/api/v2/get/cameras?format=json&lang=en). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://511on.ca/developers/doc) · [Provider reference 2](https://www.ontario.ca/page/open-government-licence-ontario)
- **Catalog ID:** `ontario-511`

<a id="ovapi-realtime"></a>

## OVapi Netherlands real-time transit feeds

**[Visit source](https://gtfs.ovapi.nl/)** | [Provider documentation](https://gtfs.ovapi.nl/README)

- **Provider:** Stichting OpenGeo / OVapi and contributing operators
- **Coverage:** Netherlands; completeness varies by operator and mode.
- **Type / access:** `live-feed` / `open`
- **Formats:** GTFS-Realtime Protocol Buffers, GTFS schedules
- **Updates:** Real-time operator reports; use conditional requests when polling faster than once per minute.
- **Security use:** Public-transit service continuity, route disruption and last-mile access planning.
- **License / terms:** Provider README permits use with no SLA and prohibits representing or impersonating transit agencies. Identify clients and follow compression/caching guidance.
- **Limitations:** Integrated feeds inherit upstream coverage gaps and matching issues. Vehicle positions are reports with age and coverage gaps; interpolation is not an additional measurement. Join identifiers to the matching static GTFS version.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://gtfs.ovapi.nl/nl/vehiclePositions.pb). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://gtfs.ovapi.nl/README)
- **Catalog ID:** `ovapi-realtime`

<a id="tallinn-traffic-cameras"></a>

## Tallinn public intersection cameras

**[Visit source](https://ristmikud.tallinn.ee/)** | [Provider documentation](https://ristmikud.tallinn.ee/)

- **Provider:** City of Tallinn
- **Coverage:** Selected Tallinn intersections and corridors, Estonia.
- **Type / access:** `dashboard` / `open`
- **Formats:** Web camera views
- **Updates:** Camera-dependent public views; refresh cadence not established.
- **Security use:** Corroborate visible road conditions at selected Tallinn intersections.
- **License / terms:** Public municipal viewing does not establish an open-data license, bulk collection or redistribution permission; confirm with the city.
- **Limitations:** Public site and camera categories reviewed; supported API, capture timing and reuse terms remain unresolved. The project uses curated camera locations and estimated poses.
- **Review:** 2026-09-22 — `partial-review`
- **Evidence:** [Provider reference 1](https://ristmikud.tallinn.ee/)
- **Catalog ID:** `tallinn-traffic-cameras`

<a id="tarktee-road-cameras"></a>

## Tark Tee road cameras and travel conditions

**[Visit source](https://tarktee.transpordiamet.ee/)** | [Provider documentation](https://tarktee.transpordiamet.ee/tarktee/rest/services/road_cameras/MapServer)

- **Provider:** Estonian Transport Administration / Transpordiamet
- **Coverage:** Estonian road network and published road-weather camera locations.
- **Type / access:** `mixed` / `open`
- **Formats:** Web map, ArcGIS REST, JSON, GeoJSON
- **Updates:** Resource-specific updates; verify camera capture and road-event times.
- **Security use:** Road-weather, visibility and disruption context for travel in Estonia.
- **License / terms:** Public service metadata is available, but full image and data-reuse terms were not established. Confirm current conditions through Transpordiamet or its national access point.
- **Limitations:** The cataloged ArcGIS service exposes queryable camera geography. The project uses separate DATEX backend routes; their support contract and image access were not independently validated.
- **Review:** 2026-09-22 — `partial-review`
- **API entrypoint / example:** [Open endpoint](https://tarktee.transpordiamet.ee/tarktee/rest/services/road_cameras/MapServer). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://tarktee.transpordiamet.ee/tarktee/rest/services/road_cameras/MapServer) · [Provider reference 2](https://transpordiamet.ee/liiklusjuhtimiskeskus)
- **Catalog ID:** `tarktee-road-cameras`

<a id="tfl-jamcams"></a>

## TfL Unified API and JamCam traffic cameras

**[Visit source](https://tfl.gov.uk/info-for/open-data-users/)** | [Provider documentation](https://tfl.gov.uk/info-for/open-data-users/api-documentation)

- **Provider:** Transport for London
- **Coverage:** Greater London roads and TfL transport network.
- **Type / access:** `mixed` / `mixed`
- **Formats:** JSON, Camera imagery, REST
- **Updates:** Resource-dependent updates; camera image timestamps can differ from catalog retrieval.
- **Security use:** London road-condition corroboration and transport-disruption context.
- **License / terms:** TfL open-data terms and attribution apply, with third-party mapping exclusions. Register for appropriate API access and check request limits.
- **Limitations:** Camera coverage is selective and imagery can be unavailable or old. API access is distinct from rights to every returned image or third-party asset.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://api.tfl.gov.uk/Place/Type/JamCam). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://tfl.gov.uk/info-for/open-data-users/api-documentation) · [Provider reference 2](https://api.tfl.gov.uk/)
- **Catalog ID:** `tfl-jamcams`

<a id="tomtom-traffic"></a>

## TomTom traffic flow and incidents

**[Visit source](https://developer.tomtom.com/traffic-api)** | [Provider documentation](https://docs.tomtom.com/traffic-api/documentation/tomtom-maps/v1/traffic-flow/vector-flow-tiles)

- **Provider:** TomTom
- **Coverage:** Supported road networks worldwide; product coverage differs by country and road class.
- **Type / access:** `live-feed` / `commercial`
- **Formats:** Vector tiles, JSON, XML, REST
- **Updates:** Frequently refreshed traffic estimates; check product timestamps and cache instructions.
- **Security use:** Road congestion and travel-delay context for logistics and facility access.
- **License / terms:** Proprietary API with key, account terms and metered allowances; verify current pricing and permitted display, storage and redistribution.
- **Limitations:** Traffic flow is aggregate speed/congestion information. It does not locate individual vehicles; cars animated from these values remain simulated.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://docs.tomtom.com/traffic-api/documentation/tomtom-maps/v1/traffic-flow/vector-flow-tiles) · [Provider reference 2](https://docs.tomtom.com/pricing/)
- **Catalog ID:** `tomtom-traffic`

<a id="translink-seq-realtime"></a>

## Translink South East Queensland real-time transit

**[Visit source](https://translink.com.au/about-translink/open-data)** | [Provider documentation](https://translink.com.au/about-translink/open-data)

- **Provider:** Translink / Queensland Government
- **Coverage:** South East Queensland, Australia.
- **Type / access:** `live-feed` / `open`
- **Formats:** GTFS-Realtime Protocol Buffers, GTFS schedules
- **Updates:** Operational GTFS-Realtime updates; timestamps and reporting vary by mode.
- **Security use:** Public-transit service continuity, route disruption and last-mile access planning.
- **License / terms:** CC BY 4.0; provider states authentication is not required for these feeds.
- **Limitations:** SEQ vehicle positions, trip updates and alerts are separate resources. Do not infer coverage of all Queensland services. Vehicle positions are reports with age and coverage gaps; interpolation is not an additional measurement. Join identifiers to the matching static GTFS version.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://gtfsrt.api.translink.com.au/api/realtime/seq/VehiclePositions). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://translink.com.au/about-translink/open-data)
- **Catalog ID:** `translink-seq-realtime`

<a id="txdot-traffic-cameras"></a>

## TxDOT public traffic cameras

**[Visit source](https://www.txdot.gov/discover/live-traffic-cameras.html)** | [Provider documentation](https://www.txdot.gov/discover/live-traffic-cameras.html)

- **Provider:** Texas Department of Transportation
- **Coverage:** Texas highway cameras organized by TxDOT district.
- **Type / access:** `dashboard` / `open`
- **Formats:** Web camera views
- **Updates:** Camera-specific current views; verify timestamp and availability at each location.
- **Security use:** Check visible highway conditions around Texas facilities and travel corridors.
- **License / terms:** Public viewing is documented; supported third-party API access, archiving and redistribution rights were not established.
- **Limitations:** TxDOT says footage is not recorded. The audited project uses ITS backend routes; these are not promoted here as a documented public integration contract. Distinct from DriveTexas road-condition reports.
- **Review:** 2026-09-22 — `partial-review`
- **Evidence:** [Provider reference 1](https://www.txdot.gov/discover/live-traffic-cameras.html) · [Provider reference 2](https://its.txdot.gov/)
- **Catalog ID:** `txdot-traffic-cameras`

<a id="warendorf-webcam"></a>

## Warendorf municipal market-square webcam

**[Visit source](http://webcam.warendorf.de/)** | [Provider documentation](https://www.warendorf.de/de/)

- **Provider:** Stadt Warendorf
- **Coverage:** A single market-square view in Warendorf, Germany.
- **Type / access:** `dashboard` / `open`
- **Formats:** Webcam still image
- **Updates:** Refresh timing not established in this review.
- **Security use:** Limited visual context for the market square, subject to current provider access.
- **License / terms:** The municipal website links the webcam; independent image reuse and redistribution permission remain unverified.
- **Limitations:** Municipal webcam link verified, but camera health, timing, API support and image-reuse terms remain unresolved. The project uses an HTTP JPEG endpoint and an estimated pose.
- **Review:** 2026-09-22 — `partial-review`
- **Evidence:** [Provider reference 1](https://www.warendorf.de/de/) · [Provider reference 2](http://webcam.warendorf.de/)
- **Catalog ID:** `warendorf-webcam`
