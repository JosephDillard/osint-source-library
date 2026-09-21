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
| Detect significant incidents near people and assets | Factal, Samdesk, Dataminr; Seerist for context | Original evidence, event time, location precision, revisions, unique coverage and feed rights |
| Assess travel and executive-protection needs | Riskline, Crisis24 Horizon, Base Operations, Ontic | Destination coverage, incident versus baseline data, assistance scope and workflow fit |

The [expanded service shortlist](service-shortlist.md) compares these options and existing public sources. Its evaluation priorities are recommendations, not measured vendor rankings.

## A manageable first integration

Start with a small set for one operating area:

1. NWS weather alerts and USGS earthquakes.
2. One official road-condition source for the area.
3. The serving electric and water utilities' public notices.
4. Municipal public-event permits and a local reported-crime dataset.
5. A baseline map appropriate to the required licensing.

The utilities and road sources may initially require manual review. Once access and terms are established, consider documented APIs. Existing dashboard network calls are not automatically supported or authorized public APIs.

## API and ETL access

A native GIS connector is optional. A supported API, RSS/CAP/GeoJSON feed, or licensed CSV/JSON export can be collected and transformed into the same observation model. Scheduled file delivery is also suitable when offered under the provider agreement. Treat platform-only access as manual review until a usable outbound interface is confirmed.

For an integration pilot:

1. Confirm credentials, rate limits, outbound delivery, field availability and permitted uses with the provider.
2. Preserve the provider's IDs and provenance, distinguish event time from publication and retrieval times, and store raw payloads only within permitted retention.
3. Normalize times to UTC and transform geometry with an explicit coordinate reference system and precision. Leave unresolved locations unresolved.
4. Upsert revisions using provider IDs, retain cancellations, and group reports of the same event without losing their separate evidence. Syndicated reports are not independent corroboration.
5. Apply geographic relevance and event significance before sending an alert. Treat missing coverage or collection errors separately from an absence of incidents.
6. Publish permitted fields to a database or GIS layer, preserving original source links and required attribution. Keep credentials outside the catalog and generated pages.

Poll at documented rates and use supported incremental retrieval. Evaluate corrections, late reports, duplicate alerts and service failures as well as the first report. No collector or scheduled ETL job is installed by this repository.

## Major cybersecurity events

Include a cybersecurity event when credible reporting establishes substantial consequences, such as:

- A large, consequential breach at a major organization, including exposure of customer, employee, communications or operational data.
- Significant disruption to telecommunications, utilities, healthcare, transportation or another critical business provider.
- A major ransomware or destructive incident that interrupts operations, affects safety or requires a business-continuity response.

Seek affected-organization, authority or well-supported reporting, and label unconfirmed reports explicitly. Record what is known about impact and scope; do not infer attack attribution or cause from an outage signal. A confirmed major breach can qualify without an ongoing outage.

Routine vulnerability disclosures, scan results, leaked-account checks, malware indicators and minor isolated incidents do not qualify on their own. A vulnerability may become relevant when associated with a major consequential incident. This is an event-selection rule, not a replacement for a separate technical security program.

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
