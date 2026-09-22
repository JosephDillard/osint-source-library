# God's Eye View source audit

Reviewed **2026-09-22 UTC** against [God's Eye View commit `0dbde1e`](https://github.com/bilawalsidhu/gods-eye-view/tree/0dbde1e36c0177b7664b47702d77ba50f11ddadc).

Added **41 source records**, bringing the catalog from 47 to **88 sources across 16 categories**. Updated OpenSky access/freshness notes and the existing OpenStreetMap record with Overpass discovery. Existing GDELT, USGS earthquake and NASA FIRMS records were reused without changing their review dates.

The project is a discovery lead, not the authority for a provider license or feed guarantee. Source cards contain primary documentation and explicit review limits. Catalog dates use UTC; this work began on September 21 in U.S. Central time.

## Source-to-catalog mapping

Different products from the same agency can deserve separate records: Caltrans CWWP2 camera files are distinct from QuickMap; TxDOT camera views are distinct from DriveTexas condition reports. GBFS operators are grouped under a feed-discovery entry with the configured systems preserved below.

| Catalog source | Action | Project evidence |
| --- | --- | --- |
| [OpenSky aircraft state vectors](../sources/aviation.md#opensky) | Updated existing | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/server/providers/aircraft/opensky.js) |
| [adsb.lol aircraft positions and traces](../sources/aviation.md#adsb-lol) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/server/providers/aircraft/adsb-lol.js) |
| [adsbdb aircraft and callsign metadata](../sources/aviation.md#adsbdb) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/server/providers/aircraft/enrichment.js) |
| [AISStream vessel message stream](../sources/maritime.md#aisstream) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/DATA_SOURCES.md) |
| [USGS earthquake feeds](../sources/hazards.md#usgs-earthquakes) | Already cataloged | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/DATA_SOURCES.md) |
| [FIRMS active fire and thermal anomalies](../sources/hazards.md#nasa-firms) | Already cataloged | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/DATA_SOURCES.md) |
| [GDELT event and news data](../sources/events.md#gdelt) | Already cataloged | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/DATA_SOURCES.md) |
| [Google Maps imagery, 3D tiles and place context](../sources/context.md#google-maps-platform) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/DATA_SOURCES.md) |
| [Esri World Imagery basemap](../sources/context.md#esri-world-imagery) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/DATA_SOURCES.md) |
| [Cesium ion global terrain and hosted content](../sources/context.md#cesium-ion-terrain) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/DATA_SOURCES.md) |
| [Open-Meteo weather models and current conditions](../sources/weather.md#open-meteo) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/DATA_SOURCES.md) |
| [TomTom traffic flow and incidents](../sources/roads.md#tomtom-traffic) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/DATA_SOURCES.md) |
| [Photon OpenStreetMap geocoding](../sources/context.md#photon-geocoding) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/DATA_SOURCES.md) |
| [Nominatim OpenStreetMap geocoding](../sources/context.md#nominatim-geocoding) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/DATA_SOURCES.md) |
| [Radio Browser station directory](../sources/government.md#radio-browser) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/DATA_SOURCES.md) |
| [Google News locality and topic RSS discovery](../sources/events.md#google-news-rss) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/DATA_SOURCES.md) |
| [FOSSGIS OpenStreetMap routing service](../sources/roads.md#fossgis-osrm) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/DATA_SOURCES.md) |
| [CelesTrak general perturbations orbital elements](../sources/space.md#celestrak) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/server/providers/space/celestrak.js) |
| [Launch Library 2 spaceflight events](../sources/space.md#launch-library-2) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/server/providers/space/launch-library.js) |
| [Austin traffic camera inventory and public views](../sources/roads.md#austin-traffic-cameras) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/server/providers/cctv/constants.js) |
| [Caltrans CWWP2 traffic-camera data](../sources/roads.md#caltrans-cctv) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/server/providers/cctv/constants.js) |
| [TxDOT public traffic cameras](../sources/roads.md#txdot-traffic-cameras) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/server/providers/cctv/constants.js) |
| [TfL Unified API and JamCam traffic cameras](../sources/roads.md#tfl-jamcams) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/server/providers/cctv/constants.js) |
| [Ontario 511 cameras and traveler-information API](../sources/roads.md#ontario-511) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/server/providers/cctv/constants.js) |
| [Fintraffic Digitraffic road-weather cameras and data](../sources/roads.md#fintraffic-digitraffic) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/server/providers/cctv/constants.js) |
| [DriveBC highway webcams](../sources/roads.md#drivebc-webcams) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/server/providers/cctv/constants.js) |
| [Calgary traffic camera inventory and images](../sources/roads.md#calgary-traffic-cameras) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/server/providers/cctv/constants.js) |
| [Live Traffic NSW cameras](../sources/roads.md#nsw-traffic-cameras) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/server/providers/cctv/constants.js) |
| [Tallinn public intersection cameras](../sources/roads.md#tallinn-traffic-cameras) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/server/providers/cctv/constants.js) |
| [Tark Tee road cameras and travel conditions](../sources/roads.md#tarktee-road-cameras) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/server/providers/cctv/constants.js) |
| [Warendorf municipal market-square webcam](../sources/roads.md#warendorf-webcam) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/config/cctv_sources.warendorf.json) |
| [MBTA real-time transit feeds](../sources/roads.md#mbta-realtime) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/src/data/transitFeeds.js) |
| [CapMetro real-time transit feeds](../sources/roads.md#capmetro-realtime) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/src/data/transitFeeds.js) |
| [Metro Transit Twin Cities real-time feeds](../sources/roads.md#metro-transit-realtime) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/src/data/transitFeeds.js) |
| [HSL Helsinki real-time transit feeds](../sources/roads.md#hsl-realtime) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/src/data/transitFeeds.js) |
| [OVapi Netherlands real-time transit feeds](../sources/roads.md#ovapi-realtime) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/src/data/transitFeeds.js) |
| [Entur Norway real-time transit feeds](../sources/roads.md#entur-realtime) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/src/data/transitFeeds.js) |
| [Translink South East Queensland real-time transit](../sources/roads.md#translink-seq-realtime) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/src/data/transitFeeds.js) |
| [GBFS shared-mobility feed directory and station availability](../sources/roads.md#gbfs-bikeshare) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/src/layers/bikeshare/registry.js) |
| [Re:Earth Terrain elevation and mesh service](../sources/context.md#reearth-terrain) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/server/providers/terrain.js) |
| [TeleGeography Submarine Cable Map](../sources/connectivity.md#telegeography-cables) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/src/data/local_data/telegeography_submarine_cables/README.md) |
| [Natural Earth physical and cultural map data](../sources/context.md#natural-earth) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/src/data/local_data/natural_earth/README.md) |
| [DataSF Analysis Neighborhoods](../sources/context.md#datasf-analysis-neighborhoods) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/src/data/local_data/neighborhoods/SOURCE.md) |
| [Open Infrastructure Map](../sources/context.md#open-infrastructure-map) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/src/data/local_data/dams/README.md) |
| [Vantor Open Data Program disaster imagery](../sources/hazards.md#vantor-open-data) | Added | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/public/events/bhote-koshi-2026/README.md) |
| [OpenStreetMap](../sources/context.md#openstreetmap) | Updated existing | [Source](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/DATA_SOURCES.md#alpr-camera-mapping) |

## Observation and access distinctions

- Aircraft reports come from OpenSky and adsb.lol; adsbdb supplies metadata. The project delays and interpolates display positions and may reuse cached data. Trace backfills have separate availability limits.
- AISStream is an authenticated WebSocket service. It is listed as a live feed, but its WSS address is described in the card rather than forcing it into the HTTP(S)-only endpoint field.
- Satellite positions are propagated from orbital elements. Launch Library provides mission/event metadata; reconstructed rocket trajectories are not measured telemetry.
- Road-car animation, thermal/night-vision shaders, detection overlays and synthetic weather effects are not additional data feeds. TomTom supplies aggregate flow, and Open-Meteo current conditions are based on weather models.
- Public camera catalogs, image capture times, stream health and estimated camera poses are separate facts. Public visibility does not establish a right to archive, redistribute or analyze every image.
- Basemaps, terrain, cables, neighborhood polygons and infrastructure extracts are reference data. Data downloaded at runtime is not necessarily freshly observed.
- The project's API-key and demo configuration is not a substitute for provider licensing, quotas or supported interfaces. No credentials or third-party imagery were added to this library.

## GBFS systems configured in the audited revision

These station-status URLs are transcribed from the pinned project registry to preserve discovery provenance. They are **not individually verified integrations or reuse approvals**. Confirm each system through the [MobilityData directory](https://github.com/MobilityData/gbfs/blob/master/systems.csv), operator documentation, feed timestamps and license fields. Station availability does not reveal individual rider trips.

| Project system ID | City | Configured station-status resource |
| --- | --- | --- |
| `nyc-citibike` | New York, NY | [Configured JSON](https://gbfs.lyft.com/gbfs/2.3/bkn/en/station_status.json) |
| `chicago-divvy` | Chicago, IL | [Configured JSON](https://gbfs.lyft.com/gbfs/2.3/chi/en/station_status.json) |
| `dc-capital-bikeshare` | Washington, DC | [Configured JSON](https://gbfs.lyft.com/gbfs/2.3/dca-cabi/en/station_status.json) |
| `sf-bay-wheels` | San Francisco, CA | [Configured JSON](https://gbfs.lyft.com/gbfs/2.3/bay/en/station_status.json) |
| `boston-bluebikes` | Boston, MA | [Configured JSON](https://gbfs.bluebikes.com/gbfs/en/station_status.json) |
| `philadelphia-indego` | Philadelphia, PA | [Configured JSON](https://gbfs.bcycle.com/bcycle_indego/station_status.json) |
| `portland-biketown` | Portland, OR | [Configured JSON](https://gbfs.biketownpdx.com/gbfs/2.3/en/station_status.json) |
| `la-metro-bike` | Los Angeles, CA | [Configured JSON](https://gbfs.bcycle.com/bcycle_lametro/station_status.json) |
| `austin-capmetro` | Austin, TX | [Configured JSON](https://austin.publicbikesystem.net/customer/gbfs/v2/en/station_status.json) |
| `honolulu-biki` | Honolulu, HI | [Configured JSON](https://hon.publicbikesystem.net/customer/gbfs/v2/en/station_status.json) |
| `columbus-cogo` | Columbus, OH | [Configured JSON](https://gbfs.cogobikeshare.com/gbfs/2.3/en/station_status.json) |
| `chattanooga-bikechatt` | Chattanooga, TN | [Configured JSON](https://chat.publicbikesystem.net/customer/gbfs/v2/en/station_status.json) |
| `boulder-bcycle` | Boulder, CO | [Configured JSON](https://gbfs.bcycle.com/bcycle_boulder/station_status.json) |
| `milwaukee-bublr` | Milwaukee, WI | [Configured JSON](https://gbfs.bcycle.com/bcycle_bublr/station_status.json) |
| `madison-bcycle` | Madison, WI | [Configured JSON](https://gbfs.bcycle.com/bcycle_madison/station_status.json) |
| `nashville-bcycle` | Nashville, TN | [Configured JSON](https://gbfs.bcycle.com/bcycle_nashville/station_status.json) |
| `salt-lake-greenbike` | Salt Lake City, UT | [Configured JSON](https://gbfs.bcycle.com/bcycle_greenbikeslc/station_status.json) |
| `san-antonio-bcycle` | San Antonio, TX | [Configured JSON](https://gbfs.bcycle.com/bcycle_sanantonio/station_status.json) |
| `cincinnati-red-bike` | Cincinnati, OH | [Configured JSON](https://gbfs.bcycle.com/bcycle_cincyredbike/station_status.json) |
| `el-paso-bcycle` | El Paso, TX | [Configured JSON](https://gbfs.bcycle.com/bcycle_elpaso/station_status.json) |
| `indianapolis-pacers` | Indianapolis, IN | [Configured JSON](https://gbfs.bcycle.com/bcycle_pacersbikeshare/station_status.json) |
| `fort-lauderdale-broward` | Fort Lauderdale, FL | [Configured JSON](https://gbfs.bcycle.com/bcycle_broward/station_status.json) |
| `memphis-bcycle` | Memphis, TN | [Configured JSON](https://gbfs.bcycle.com/bcycle_memphis/station_status.json) |
| `des-moines-bcycle` | Des Moines, IA | [Configured JSON](https://gbfs.bcycle.com/bcycle_desmoines/station_status.json) |
| `tucson-tugo` | Tucson, AZ | [Configured JSON](https://gbfs.bcycle.com/bcycle_tugo/station_status.json) |
| `fort-worth-trinity` | Fort Worth, TX | [Configured JSON](https://gbfs.bcycle.com/bcycle_fortworth/station_status.json) |
| `omaha-heartland` | Omaha, NE | [Configured JSON](https://gbfs.bcycle.com/bcycle_heartland/station_status.json) |
| `lincoln-bikelnk` | Lincoln, NE | [Configured JSON](https://gbfs.bcycle.com/bcycle_bikelnk/station_status.json) |
| `greenville-sc-bcycle` | Greenville, SC | [Configured JSON](https://gbfs.bcycle.com/bcycle_greenville/station_status.json) |
| `buffalo-reddy` | Buffalo, NY | [Configured JSON](https://gbfs.bcycle.com/bcycle_reddy/station_status.json) |
| `las-vegas-rtc-bike-share` | Las Vegas, NV | [Configured JSON](https://gbfs.bcycle.com/bcycle_rtcbikeshare/station_status.json) |
| `santa-barbara-bcycle` | Santa Barbara, CA | [Configured JSON](https://gbfs.bcycle.com/bcycle_santabarbara/station_status.json) |

## Reviewed but not added as operational feeds

- [Shinjuku pilot camera pack](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/config/cctv_sources.shinjuku.json): explicitly uses sample MP4 videos for projection testing. It is not evidence of Tokyo camera access; this review does not claim that the optional pack is enabled by default.
- [Bhote Koshi event pack](https://github.com/bilawalsidhu/gods-eye-view/blob/0dbde1e36c0177b7664b47702d77ba50f11ddadc/public/events/bhote-koshi-2026/README.md): Vantor's reusable imagery program is cataloged, while the [GeoPera reconstruction](https://github.com/geo-pera/bhotekoshi-2026-reconstruction) and linked witness posts remain case-specific historical evidence. The derived centerline and imagery have noncommercial restrictions; linked social posts are not a verified recurring feed.
- Bundled model assets, precomputed camera ground heights, shader effects and the OpenAI voice interface are rendering/software dependencies, not independent observations to catalog.
- OSM-derived datacenters, dams, installation tags and ALPR camera locations reuse the OSM/Open Infrastructure Map records. No duplicate live-feed entries were created for static extracts or alternate tags.

## Review limits

**13 of the new records remain `partial-review`:** [adsbdb aircraft and callsign metadata](../sources/aviation.md#adsbdb), [CelesTrak general perturbations orbital elements](../sources/space.md#celestrak), [TxDOT public traffic cameras](../sources/roads.md#txdot-traffic-cameras), [DriveBC highway webcams](../sources/roads.md#drivebc-webcams), [Tallinn public intersection cameras](../sources/roads.md#tallinn-traffic-cameras), [Tark Tee road cameras and travel conditions](../sources/roads.md#tarktee-road-cameras), [Warendorf municipal market-square webcam](../sources/roads.md#warendorf-webcam), [MBTA real-time transit feeds](../sources/roads.md#mbta-realtime), [Metro Transit Twin Cities real-time feeds](../sources/roads.md#metro-transit-realtime), [GBFS shared-mobility feed directory and station availability](../sources/roads.md#gbfs-bikeshare), [Google News locality and topic RSS discovery](../sources/events.md#google-news-rss), [TeleGeography Submarine Cable Map](../sources/connectivity.md#telegeography-cables), [DataSF Analysis Neighborhoods](../sources/context.md#datasf-analysis-neighborhoods).

Partial status preserves specific unresolved items: incomplete provider-page retrieval, unclear reuse terms, unconfirmed service contracts, or per-operator review still needed. An accessible endpoint is not a license and an HTTP error is not proof a source is dead. TLS verification was retained when DataSF retrieval failed.

Primary material was reviewed through publisher documentation and selected structured metadata. Paid or authenticated feeds were not exercised. The earlier direct OpenSky and adsb.lol checks were one-time samples, not uptime or coverage tests. No collector, recurring monitor, camera archive or city-profile change was added. Historical HTTP snapshots were not relabeled as a new comprehensive link check.
