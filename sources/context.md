# Maps, infrastructure & geographic context

<!-- Generated from catalog/sources.json; edit the catalog, then run python tools/catalog.py build. -->

[All categories](../LIBRARY.md) | [How to use this library](../docs/getting-started.md)

Original catalog text: Copyright (c) 2026 Joseph Dillard and contributors, [CC BY 4.0](../LICENSE-CONTENT). [Scope and attribution](../LICENSING.md). Provider material retains its own terms.

<a id="cesium-ion-terrain"></a>

## Cesium ion global terrain and hosted content

**[Visit source](https://cesium.com/platform/cesium-ion/content/cesium-world-terrain/)** | [Provider documentation](https://cesium.com/platform/cesium-ion/content/cesium-world-terrain/)

- **Provider:** Cesium / credited source providers
- **Coverage:** Global terrain with source-dependent detail; hosted imagery and 3D assets have separate coverage.
- **Type / access:** `reference` / `mixed`
- **Formats:** Quantized-mesh terrain, 3D Tiles
- **Updates:** Provider-curated terrain releases; not a live terrain-change feed.
- **Security use:** Terrain context, elevation-aware display and preliminary line-of-sight exploration.
- **License / terms:** ion account/token and plan terms govern access; source credits and third-party asset terms apply. Verify commercial eligibility and quotas independently.
- **Limitations:** Terrain meshes are generalized representations, not a survey or guaranteed clearance model. ion hosting does not transfer rights to Google or other third-party content.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://cesium.com/platform/cesium-ion/content/cesium-world-terrain/)
- **Catalog ID:** `cesium-ion-terrain`

<a id="datasf-analysis-neighborhoods"></a>

## DataSF Analysis Neighborhoods

**[Visit source](https://data.sf.gov/Geographic-Locations-and-Boundaries/Analysis-Neighborhoods/j2bu-swwd)** | [Provider documentation](https://data.sf.gov/api/views/j2bu-swwd.json)

- **Provider:** City and County of San Francisco / DataSF
- **Coverage:** San Francisco analysis-neighborhood polygons.
- **Type / access:** `reference` / `open`
- **Formats:** Socrata, GeoJSON, GIS download
- **Updates:** Administrative dataset revisions; no live update cadence established.
- **Security use:** Consistent neighborhood aggregation and locality labels for San Francisco reporting.
- **License / terms:** The upstream project records PDDL 1.0 for its source snapshot; current provider metadata could not be independently retrieved due to TLS/retrieval errors. Confirm before redistribution.
- **Limitations:** Analysis areas are not proof of colloquial, legal or operational boundaries. Preserve source version; project polygons were simplified. Endpoint is not promoted until current documentation is verified.
- **Review:** 2026-09-22 — `partial-review`
- **Evidence:** [Provider reference 1](https://data.sf.gov/api/views/j2bu-swwd.json)
- **Catalog ID:** `datasf-analysis-neighborhoods`

<a id="esri-world-imagery"></a>

## Esri World Imagery basemap

**[Visit source](https://www.arcgis.com/home/item.html?id=10df2279f9684e4a9f6a7f08febac2a9)** | [Provider documentation](https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer)

- **Provider:** Esri and credited imagery contributors
- **Coverage:** Worldwide imagery mosaic; resolution and acquisition age vary.
- **Type / access:** `reference` / `mixed`
- **Formats:** ArcGIS REST MapServer, Raster tiles
- **Updates:** Mosaic updates by region; imagery acquisition date is not the tile request time.
- **Security use:** Imagery context for facilities, routes and geographic interpretation.
- **License / terms:** Esri and contributor terms apply with required source credit. Public access to the classic service does not grant unlimited commercial usage, bulk downloads or redistribution rights.
- **Limitations:** Static aerial/satellite imagery may be old and has mixed spatial resolution. Service metadata was inspected; plan entitlements and offline-use rights were not validated.
- **Review:** 2026-09-22 — `provider-metadata-reviewed`
- **API entrypoint / example:** [Open endpoint](https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer) · [Provider reference 2](https://www.esri.com/en-us/legal/terms/full-master-agreement)
- **Catalog ID:** `esri-world-imagery`

<a id="google-maps-platform"></a>

## Google Maps imagery, 3D tiles and place context

**[Visit source](https://developers.google.com/maps)** | [Provider documentation](https://developers.google.com/maps/documentation/tile/3d-tiles)

- **Provider:** Google Maps Platform
- **Coverage:** Global mapping with product-dependent 3D, imagery and Places coverage.
- **Type / access:** `reference` / `commercial`
- **Formats:** 3D Tiles, Raster imagery, JSON APIs
- **Updates:** Provider-managed imagery and map updates; capture dates vary by location and product.
- **Security use:** Visual geographic context, geocoding and place discovery around authorized operating areas.
- **License / terms:** API key, billing and product-specific terms apply. Preserve attribution and review storage, caching, redistribution and derived-data restrictions; documentation license does not license map content.
- **Limitations:** Photorealistic 3D is a textured mesh, not live satellite video. Geocoding, Places and Street View are separate products; appearance or a place-search match does not verify present activity.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://tile.googleapis.com/v1/3dtiles/root.json). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://developers.google.com/maps/documentation/tile/3d-tiles) · [Provider reference 2](https://developers.google.com/maps/documentation/geocoding/overview) · [Provider reference 3](https://cloud.google.com/maps-platform/terms)
- **Catalog ID:** `google-maps-platform`

<a id="hdx"></a>

## Humanitarian Data Exchange

**[Visit source](https://data.humdata.org/)** | [Provider documentation](https://centre.humdata.org/ufaqs/about-the-humanitarian-data-exchange-api/)

- **Provider:** UN OCHA Centre for Humanitarian Data / contributing organizations
- **Coverage:** Global, with humanitarian-response focus
- **Type / access:** `catalog` / `mixed`
- **Formats:** CKAN API, Dataset downloads, Tabular Data Endpoints
- **Updates:** Dataset-specific; inspect source and last update.
- **Security use:** Find administrative boundaries, infrastructure and humanitarian baseline data.
- **License / terms:** Dataset-specific licenses and access conditions; tabular endpoints require an HDX API token.
- **Limitations:** Some datasets require access approval; country and dataset coverage varies. Portal fetch returned 403 in this review.
- **Review:** 2026-09-20 — `partial-review`
- **Evidence:** [Provider reference 1](https://centre.humdata.org/ufaqs/about-the-humanitarian-data-exchange-api/) · [Provider reference 2](https://centre.humdata.org/ufaqs/data-licenses/) · [Provider reference 3](https://centre.humdata.org/new-api-access-on-hdx-tabular-data-endpoints/)
- **Catalog ID:** `hdx`

<a id="natural-earth"></a>

## Natural Earth physical and cultural map data

**[Visit source](https://www.naturalearthdata.com/)** | [Provider documentation](https://www.naturalearthdata.com/about/terms-of-use/)

- **Provider:** Natural Earth contributors
- **Coverage:** Global small-scale cartography at 1:10m, 1:50m and 1:110m.
- **Type / access:** `reference` / `open`
- **Formats:** Shapefile, GeoPackage, Raster
- **Updates:** Versioned releases; review the source release and processing date.
- **Security use:** Regional names, land/marine boundaries and general geographic context.
- **License / terms:** Provider places raster and vector data in the public domain; attribution is appreciated but not required.
- **Limitations:** Cartographic generalization is unsuitable for parcel, legal boundary or facility-scale decisions. Project copies are simplified snapshots, not live boundary observations.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://www.naturalearthdata.com/about/terms-of-use/) · [Provider reference 2](https://www.naturalearthdata.com/downloads/)
- **Catalog ID:** `natural-earth`

<a id="nominatim-geocoding"></a>

## Nominatim OpenStreetMap geocoding

**[Visit source](https://nominatim.org/)** | [Provider documentation](https://operations.osmfoundation.org/policies/nominatim/)

- **Provider:** OpenStreetMap Foundation / Nominatim
- **Coverage:** Global OSM-derived addresses and named places; completeness varies.
- **Type / access:** `reference` / `open`
- **Formats:** JSON, GeoJSON, XML
- **Updates:** OSM-derived index updates; inspect returned geometry and place identity.
- **Security use:** Occasional place resolution and reverse-geocoded location context within permitted use.
- **License / terms:** ODbL data attribution and applicable share-alike terms. Public service policy requires identified clients, caching and at most one request/second across the application; bulk/systematic queries and autocomplete are restricted.
- **Limitations:** Read the linked usage policy before choosing the hosted endpoint. Public capacity is limited; this is not a default backend for generic no-code geocoding or recurring bulk enrichment. Self-hosted or contracted services have separate policies.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://nominatim.openstreetmap.org/search). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://operations.osmfoundation.org/policies/nominatim/)
- **Catalog ID:** `nominatim-geocoding`

<a id="open-infrastructure-map"></a>

## Open Infrastructure Map

**[Visit source](https://openinframap.org/)** | [Provider documentation](https://openinframap.org/about)

- **Provider:** Open Infrastructure Map / OpenStreetMap contributors
- **Coverage:** Global community-mapped infrastructure; completeness varies substantially.
- **Type / access:** `reference` / `open`
- **Formats:** Web map, OSM extracts, GeoJSON via Overpass
- **Updates:** Map processing of community edits; inspect extract age and underlying OSM features.
- **Security use:** Discover mapped power, communications and other infrastructure for further verification.
- **License / terms:** Underlying OSM data is ODbL; additional analysis and regional layers have their own credits. Commercial GIS exports are offered separately by Infrageomatics.
- **Limitations:** No guaranteed facility completeness, operational status, capacity or outage detection. Provider recommends Overpass for small extracts and raw OSM processing for large ones.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://openinframap.org/about)
- **Catalog ID:** `open-infrastructure-map`

<a id="openstreetmap"></a>

## OpenStreetMap

**[Visit source](https://www.openstreetmap.org/)** | [Provider documentation](https://www.openstreetmap.org/copyright)

- **Provider:** OpenStreetMap contributors / OpenStreetMap Foundation
- **Coverage:** Global community mapping; completeness varies
- **Type / access:** `reference` / `open`
- **Formats:** OSM PBF, OSM XML, JSON via Overpass, Map data
- **Updates:** Continuously edited; extracts have their own snapshot dates.
- **Security use:** Road, building, place and mapped infrastructure context; bounded Overpass queries for relevant tags.
- **License / terms:** ODbL database license; attribution and applicable share-alike terms. Tile-server policies are separate.
- **Limitations:** Community tags are not live observations or a verified infrastructure inventory. ALPR/camera tags describe mapped locations, not plate records, camera footage or present operating status. Public Overpass services have separate capacity and commercial-use policies.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://overpass-api.de/api/interpreter). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://www.openstreetmap.org/copyright) · [Provider reference 2](https://wiki.openstreetmap.org/wiki/Overpass_API)
- **Catalog ID:** `openstreetmap`

<a id="overture"></a>

## Overture Maps

**[Visit source](https://overturemaps.org/)** | [Provider documentation](https://docs.overturemaps.org/getting-data/)

- **Provider:** Overture Maps Foundation and contributors
- **Coverage:** Global, theme-dependent coverage
- **Type / access:** `reference` / `open`
- **Formats:** GeoParquet, GeoJSON
- **Updates:** Versioned releases; pin the release used.
- **Security use:** Buildings, transport and place context for facility exposure analysis.
- **License / terms:** Licensing and attribution vary by theme and source; inspect current attribution documentation.
- **Limitations:** Feature presence, geometry and business attributes can be incomplete or outdated.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://docs.overturemaps.org/getting-data/) · [Provider reference 2](https://docs.overturemaps.org/attribution/)
- **Catalog ID:** `overture`

<a id="photon-geocoding"></a>

## Photon OpenStreetMap geocoding

**[Visit source](https://photon.komoot.io/)** | [Provider documentation](https://photon.komoot.io/)

- **Provider:** komoot / Photon / OpenStreetMap contributors
- **Coverage:** Global OSM-derived place search and reverse geocoding.
- **Type / access:** `reference` / `open`
- **Formats:** GeoJSON, REST
- **Updates:** OSM-derived index updates; search results are geographic context rather than events.
- **Security use:** Resolve place mentions and label operating-area coordinates.
- **License / terms:** Underlying OSM data is ODbL. Public instance is fair-use, can throttle extensive use, and offers no availability guarantee; self-host or arrange capacity for sustained workloads.
- **Limitations:** Ambiguous names and incomplete OSM addresses require disambiguation. Public search access is not an unrestricted bulk-geocoding entitlement.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://photon.komoot.io/api/). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://photon.komoot.io/)
- **Catalog ID:** `photon-geocoding`

<a id="reearth-terrain"></a>

## Re:Earth Terrain elevation and mesh service

**[Visit source](https://terrain.reearth.land/)** | [Provider documentation](https://terrain.reearth.land/)

- **Provider:** Eukarya / Re:Earth / Mapterhorn and credited elevation providers
- **Coverage:** Global terrain product with heterogeneous source resolution.
- **Type / access:** `reference` / `open`
- **Formats:** Quantized-mesh terrain, Terrain-RGB, Terrarium
- **Updates:** Source/product release dependent; no live elevation-update promise established.
- **Security use:** Elevation context and terrain placement in situational-awareness maps.
- **License / terms:** Mapterhorn DEM: CC BY 4.0; EGM2008 geoid: public domain; optional Protomaps/OSM water mask: ODbL. Retain required credits. Hosted service is keyless and best-effort, with possible rate limits and no SLA.
- **Limitations:** The documented endpoint supplies ellipsoidal heights; sea-level and geoid products differ. Terrain is generalized, not a survey or clearance guarantee. The project also calls /heights.json, whose separate API contract was not established here.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://terrain.reearth.land/cesium-mesh/ellipsoid). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://terrain.reearth.land/)
- **Catalog ID:** `reearth-terrain`
