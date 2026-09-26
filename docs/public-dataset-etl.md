# Public datasets for GIS and OSINT enrichment

Reviewed **2026-09-26 UTC**. This selection adds nine source records, bringing the national/global catalog to **97 sources across 16 categories**. It prioritizes U.S. preparedness, infrastructure exposure and location context, with global population and place-name options.

[Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets/blob/b5fa1f099d223e3935de1f56b72818e59cbf9e4c/README.rst) supplied discovery leads. The linked publishers support the source cards; the discovery repository's license does not grant rights to upstream datasets. EIA-860 is a companion to the listed EIA-923 source, and public forecast zones are a specific product under the listed NWS GIS portal.

These are proposed ETL paths. This repository stores descriptions, links and integration guidance; it does not download datasets, run collectors or schedule refreshes. Provider-documentation review does not establish a tested import. OpenAddresses remains a partial review because current batch-download access and exports were not verified.

## Selected sources and ingestion paths

Priority is a recommendation based on the current project scope, not measured integration performance. Source cards contain the provider evidence, access requirements and terms.

| Catalog record | Proposed extraction and transformation | Output and refresh approach |
| --- | --- | --- |
| [NWS forecast zones](../sources/weather.md#nws-forecast-zones) | Select dated polygon files; match supported forecast-zone identifiers to alerts lacking geometry. Validate the identifier namespace and effective date. | Versioned zone layer and a derived alert-area reference. Refresh on zone releases; keep original alert geometry when supplied. First pilot. |
| [Geofabrik extracts](../sources/context.md#geofabrik-extracts) | Discover a regional file through the documented download index, pin the snapshot and filter relevant OSM tags. Preserve object type and ID together. | Regional roads, buildings and mapped facilities in a spatial file or database. Start with full snapshots; consider replication only after reconciliation works. First pilot. |
| [Census TIGER/Line](../sources/context.md#census-tiger-line) | Download the chosen geography/vintage, validate the supplied CRS and retain GEOIDs as strings with leading zeros. | Versioned state, county, place or tract boundaries for joins and area summaries. Refresh by release. First pilot. |
| [Census ACS](../sources/government.md#census-acs) | Select tables, variables, geographic level and five-year period; use a registered API key or an appropriate public download. Retain estimates, margins of error and annotations. | Statistical tables joined to compatible TIGER geography; annual release snapshots. First pilot after credentials or download route are established. |
| [GeoNames](../sources/context.md#geonames) | Read country UTF-8 tab-delimited extracts and alternate names; use geonameid plus administrative and feature codes. | Local place-name lookup with explicit ambiguity. Full rebuild initially; process modifications and deletions together if incremental updates are adopted. Next enrichment. |
| [EIA-860](../sources/power.md#eia-860) | Read release-specific workbook layouts; relate plant and generator tables without merging proposed, operable and retired statuses. Validate location fields before mapping. | Dated power-plant reference layer and separate generator table; annual inventory refresh. Next infrastructure pilot. |
| [EIA-923](../sources/power.md#eia-923) | Read the selected survey schedule, preserve units and reporting period, and aggregate at its documented grain before joining compatible inventory records. | Generation/fuel time series with preliminary/final and revision metadata. Refresh on applicable monthly or annual releases. Pair with EIA-860. |
| [WorldPop](../sources/context.md#worldpop) | Select country, year, model and release; preserve raster CRS, resolution, NoData and units. Distinguish people per pixel from people per area. | Population summaries for nonoverlapping hazard areas. Refresh by product release; validate the chosen alpha or final product. Global extension. |
| [OpenAddresses](../sources/context.md#openaddresses) | Select jurisdiction source definitions and review their licenses, processing results and available downloads before implementing a reader. | Candidate address lookup with source-level attribution and match quality. Determine output freshness and access first. Conditional extension. |

Geofabrik distributes [OpenStreetMap](../sources/context.md#openstreetmap) data; it is a separate delivery choice, not a second independent account of a feature. Existing [Natural Earth](../sources/context.md#natural-earth), [Overture](../sources/context.md#overture) and [HDX](../sources/context.md#hdx) entries remain available for other scale, coverage and licensing needs.

## First pilot and acceptance criteria

Use one operating area within the existing Southwest U.S. GEOINT Watch pilot. Start with NWS public zones, a regional OSM extract, and matching Census boundaries/statistics. The intended question is: **Which mapped facilities and communities may fall within an active warning area?**

1. Preserve a supplied alert polygon. For a missing polygon, inspect the alert's affected-zone references and resolve only supported forecast zones with a known effective version. Store the original reference, resolution method and derived-geometry source. A public-zone number must not be substituted for a county, fire-weather or marine identifier. Keep unmatched references visible as gaps.
2. Extract a bounded set of mapped facilities and roads. Retain OSM object type/ID and tags; count missing classifications and questionable geometry. Keep any real authorized site inventory outside the public repository and separate from fictional demo fixtures.
3. Join ACS tables to the matching Census geography. Record unmatched IDs, boundary changes, missing-value annotations and margins of error. Do not silently join whichever two releases happen to be newest.
4. Report facility intersections as **potential exposure**. If a warning intersects only part of a tract, the tract's full population is not an affected-population count. Label intersecting-tract totals as broad context, or document and validate a separate population-allocation method.
5. Check empty inputs, duplicate identifiers, invalid geometries, failed downloads, changed schemas, stale snapshots, unavailable zones and boundary-edge intersections before accepting an import. Compare counts and geographic extents with the original source and inspect a small set on a map.
6. Rerunning the same snapshot must not duplicate records. Retain the last accepted snapshot with a stale label on failure. A dropped reference feature is not proof of a physical closure, and a missing alert is not an all-clear.

Acceptance means reproducible import results with documented gaps, correct joins and traceable exposure findings. Neither a successful download nor passing catalog tests establishes those outcomes.

## Keep reference layers and observations distinct

Boundaries, inventories, gazetteers and population estimates have reference periods or effective dates; they are not incident reports. Store them separately from time-stamped alerts and news observations. Preserve these fields in a future import manifest or database schema; they are recommendations, not additions to the catalog's current schema:

| Information | Suggested fields |
| --- | --- |
| Identity | Catalog `source_id`, provider record ID, record type and source-specific join keys |
| Provenance | Original URL, retrieval time in UTC, raw-download SHA-256 and processing version |
| Time | Publication time, release/version and reference period; effective dates for boundaries; event time only where meaningful |
| Spatial meaning | Original CRS, output CRS, geometry source, precision and any resolution or geocoding method |
| Quality | Input/accepted/rejected counts, geometry errors, missing fields, unmatched joins and uncertainty |
| Rights | Source license URL, required attribution, applicable retention and redistribution conditions |

Raw-file hashes identify retrieved bytes; separately label hashes of normalized content. Do not replace a publication or reference date with the retrieval date. Preserve original coordinates and record any transformation. Validate a complete import in staging before replacing the accepted snapshot.

GeoPackage is a reasonable portable output for reference vectors; GeoJSON can serve a small web view. Retain population rasters with their metadata and export derived summaries separately. A consumer can load larger inventories into PostGIS when needed. These are proposed output choices, not installed components.

## Existing event sources

[GDELT](../sources/events.md#gdelt) is already cataloged. A later pilot can filter its structured records or documented APIs by topic, time and geography, deduplicate reports and preserve original links. Separate a place mentioned in an article from a confirmed event location. Repeated or syndicated coverage is not independent corroboration; article text retains publisher rights. Use it for discovery and analyst review, not automatic confirmation of disruption. See the [provider's data guide](https://www.gdeltproject.org/data.html).

The existing [NWS alerts](../sources/weather.md#nws-alerts) entry supplies observations; the new zone entry supplies reference geometry. This catalog change does not resolve missing geometry in Open GEOINT Watch itself. [NASA FIRMS](../sources/hazards.md#nasa-firms) and [USGS earthquakes](../sources/hazards.md#usgs-earthquakes) also remain separate event sources with their own spatial meaning.

## Sources deferred from this selection

| Discovery lead | Reason and handling |
| --- | --- |
| HIFLD Open | DHS's [FY2025 report](https://www.fgdc.gov/gda/gda-ca-reports/FY25CoveredAgencyReports/FY25DHSGDAReport) describes movement into secure DHS GII access with government sponsorship and a data-use agreement. The old public portal is not an established open collection path. Evaluate original publishers individually; any archive needs explicit vintage and provenance. |
| GADM | The [provider license](https://gadm.org/license.html) requires permission for redistribution or commercial use. Prefer an appropriately licensed boundary source for a reusable public pilot. |
| OpenFlights routes | The [provider notice](https://openflights.org/data.php) says route updates stopped in June 2014. Historical route analysis is possible; current flight availability is not established. |

## Repository placement and review limits

Maintain source records and this guidance in OSINT Source Library. Implement and test any chosen collectors in a consumer such as [Open GEOINT Watch](https://github.com/JosephDillard/open-geoint-watch) or [Geospatial Data Gateway](https://github.com/JosephDillard/geospatial-data-gateway), preserving the catalog IDs without introducing a dependency on a sibling checkout.

No bulk data, credentials, private facilities, authenticated queries, spatial joins or scheduled jobs were added in this review. Eight new entries have provider documentation reviewed; OpenAddresses is partial. Existing source review dates and city profiles remain unchanged. The [review log](review-notes.md) records this expansion separately from older reviews and HTTP snapshots.
