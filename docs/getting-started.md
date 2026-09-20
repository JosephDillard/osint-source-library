# Getting started

## Define the operating area

Begin with a city, region or authorized site portfolio. Record the public jurisdiction, electric utility, water utility, road authority, port and airport that actually serve the area. City boundaries often differ from utility service territories.

Keep real protected-site inventories and nonpublic response procedures outside a public source library. This repository's ignored `local/` directory can hold private working notes, but ignore rules are not encryption or access control.

## Select sources by the decision

| Decision | Useful starting points | Evidence to confirm |
| --- | --- | --- |
| Prepare facilities for a hazard | NWS, NHC, USGS earthquakes, FIRMS, NWPS | Event time, geometry, forecast uncertainty and local authority notices |
| Plan site security | FBI and local reported-crime datasets | Reporting coverage, delay, location precision and incident definitions |
| Plan movement around public events | Municipal permits, road authorities, GDELT, appropriately licensed ACLED | Event location, schedule, actual road restrictions and corroborating reports |
| Assess travel disruption | FAA NAS, Aviation Weather Center, 511NY, DriveTexas, Caltrans | Affected airport or road, latest status and alternate access |
| Assess maritime disruption | NGA warnings, historical NOAA AIS, licensed live AIS | Warning area, vessel-data age and actual port or route status |
| Maintain essential services | Serving power and water utilities, licensed outage aggregators, IODA/Radar | Relevant service territory and direct confirmation of site impact |
| Build a reference map | OpenStreetMap, Overture, HDX, Data.gov | Dataset date, coverage, geometry quality and reuse terms |

## A manageable first integration

Start with a small set for one operating area:

1. NWS weather alerts and USGS earthquakes.
2. One official road-condition source for the area.
3. The serving electric and water utilities' public notices.
4. Municipal public-event permits and a local reported-crime dataset.
5. A baseline map appropriate to the required licensing.

The utilities and road sources may initially require manual review. Once access and terms are established, consider documented APIs. Existing dashboard network calls are not automatically supported or authorized public APIs.

## A useful observation record

A future collector should retain:

- Source ID, original record ID and original link.
- Event or observation time, publication/update time and retrieval time in UTC.
- Original geometry and coordinate reference system, plus any derived geometry.
- Location precision and geocoding method, including unresolved locations.
- Original severity and an explicitly separate analyst assessment.
- Confidence, corroborating sources and whether impact is observed or only possible.
- Source terms, required attribution, permitted retention and redistribution.
- Freshness threshold and collection errors.

No observation is produced by this library. These fields guide a later integration.

## Interpret carefully

A nearby hazard indicates possible exposure, not confirmed business disruption. No result can mean missing coverage, delayed reporting or collection failure. A protest report does not itself establish violent activity. Public crime statistics are a planning input, not a prediction about individuals.
