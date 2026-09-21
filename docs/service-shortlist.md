# Expanded event-intelligence service shortlist

Reviewed: **2026-09-21**. Scope: physical security, executive protection, travel, business continuity and major events. Cybersecurity is included only for [major consequential events](getting-started.md#major-cybersecurity-events).

This expansion covers 18 candidates: ten new commercial services and eight existing public or approval-based sources. The [machine-readable catalog](../catalog/sources.json) remains the source of truth for access labels, limitations and supporting evidence. This document adds evaluation priorities and an integration approach; it does not establish tested feeds or negotiated licenses.

## Commercial services

Priorities below are editorial recommendations based on documented capabilities and the intended use. Actual coverage, usefulness and latency require comparison in representative operating areas.

| Service | Best use to evaluate | Documented access and ETL position | Suggested priority |
| --- | --- | --- | --- |
| [Factal](https://www.factal.com/partners/) | Verified critical-event reports affecting facilities, travelers and providers | API and ArcGIS feature layer advertised; obtain supported schema and deployment requirements | First comparison |
| [Samdesk](https://www.samdesk.io/faq) | Early incident detection and situational awareness | API and ArcGIS integration advertised; verify alert fields, revisions and outbound rights | First comparison |
| [Dataminr for Corporate Security](https://www.dataminr.com/resources/developer-portal/) | Broad emerging-event awareness | Developer APIs and SDKs; confirm Corporate Security entitlement and sample payloads | First comparison |
| [Seerist](https://www.seerist.com/platform/api) | Live events plus historical and geographic risk context | REST/JSON and Server-Sent Events documented; authenticated access remains untested | Add for context and history |
| [Riskline](https://riskline.com/products/alerts/) | Travel disruptions and destination intelligence | API-delivered alerts can include coordinates and affected-area radii | Add for travel exposure |
| [Base Operations](https://www.baseoperations.com/product/api) | Local crime/unrest context around sites and destinations | REST API, JSON and CSV; monthly crime and biweekly unrest updates advertised; clarify exact schedule and incident-level access | Add for baseline assessment |
| [Crisis24 Horizon](https://www.crisis24.com/platforms/crisis24-horizon) | Travel/site risk with assistance and response services | Platform and alerts; supported outbound intelligence API or export not established in reviewed material | Evaluate when assistance is needed |
| [AlertMedia](https://www.alertmedia.com/products/threat-intelligence-and-warnings/) | Risk awareness linked to employee communications | API customization and incoming feeds advertised; confirm outbound incident access separately | Evaluate with communications needs |
| [Everbridge Risk Intelligence](https://www.everbridge.com/products/risk-intelligence/) | Critical-event management and continuity response | GIS integrations advertised; confirm outbound feed, payload and contract | Evaluate with response workflows |
| [Ontic](https://ontic.co/) | Protective-intelligence assessment and investigation workflows | Platform and integrations; outbound GIS/ETL access not established here | Evaluate with executive-protection workflows |

Use a limited comparison of Factal, Samdesk and Dataminr before selecting overlapping alert subscriptions. Measure unique, relevant events rather than raw alert volume. Factal's [partner directory](https://www.factal.com/partners/) illustrates that some platforms share upstream intelligence; the same underlying report should not count as independent corroboration.

## Existing sources to retain and strengthen

| Source | Role | Access / integration consideration |
| --- | --- | --- |
| [NWS alerts](https://www.weather.gov/documentation/services-web-api) | Official U.S. weather alerts | Public API and structured alerts; identify the client, handle revisions and resolve alert zones when geometry is absent |
| [USGS earthquakes](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php) | Official earthquake observations | Public GeoJSON feeds; retain revisions and distinguish magnitude from actual local impact |
| [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/api/) | Satellite fire and thermal detections | MAP_KEY registration for API access; transform documented formats; detections are not fire perimeters |
| [GDACS](https://www.gdacs.org/feed_reference.aspx) | Global disaster alerts and impact context | Public structured feeds including RSS/XML and GeoJSON; respect cadence and check event-level precision |
| [GDELT](https://www.gdeltproject.org/) | News discovery for unrest, disruptions and major corporate events | Public datasets and APIs; filter and corroborate machine-derived reports; underlying publisher content retains its rights |
| [ACLED](https://acleddata.com/) | Political violence, demonstrations and historical context | Approval and applicable agreement; confirm API/export entitlement, operational use and current publication schedule |
| [ReliefWeb](https://apidoc.reliefweb.int/parameters) | Humanitarian situation reports and disaster context | API requires a pre-approved appname; reports retain original publisher terms and are not a uniform real-time sensor feed |
| [Cloudflare Radar](https://developers.cloudflare.com/radar/) | Internet disruption indicators | API token; documented CC BY-NC 4.0 terms require corporate-use review; outage data does not establish a cyberattack |

These sources complement commercial reporting with original observations and context. They are not interchangeable in latency, geography or event meaning. Existing catalog evidence and source-specific review dates apply; ACLED was not reclassified or treated as newly approved during this expansion.

## How the OSINT tools article informs selection

The [Recorded Future OSINT tools overview](https://www.recordedfuture.com/threat-intelligence-101/tools-and-technologies/osint-tools) is a discovery aid. A tool belongs in this catalog when it supplies useful event-level evidence for people, sites, travel or continuity decisions. Reconnaissance, account lookup and exposed-service tools do not by themselves meet that requirement. Original provider documentation supports each service entry.

## Integration and pilot decisions

Accept a supported API, structured feed, native GIS service or licensed export suitable for ETL. A vendor portal or an inbound integration alone is insufficient evidence of an outbound feed. See the [ETL workflow](getting-started.md#api-and-etl-access) and [observation fields](getting-started.md#a-useful-observation-record).

Before selecting a service, establish:

- **Delivery:** supported endpoint or export, authentication, incremental updates, stable event IDs, cancellations, rate limits and latency commitments.
- **Geographic usefulness:** coverage in actual operating areas, precision, coordinate system, affected-area geometry and geocoding uncertainty.
- **Evidence quality:** source links, confidence meaning, analyst verification, corrections, duplicates and upstream-provider overlap.
- **Rights and cost:** API entitlement, internal GIS display, retention, sharing, attribution and any intended AI processing. Public access or a subscription does not establish every reuse right.
- **Operational value:** time to useful alert, relevant-event coverage, false positives, stale records, operator effort and incremental value over existing public feeds.

Cyber alerts should pass the major-event criteria before delivery. Preserve uncertainty and separate confirmed consequences from possible exposure. This change adds catalog entries and evaluation guidance; it does not activate subscriptions, monitoring, ETL jobs or vendor connections.
