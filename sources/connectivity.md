# Internet & communications disruptions

<!-- Generated from catalog/sources.json; edit the catalog, then run python tools/catalog.py build. -->

[All categories](../LIBRARY.md) | [How to use this library](../docs/getting-started.md)

Original catalog text: Copyright (c) 2026 Joseph Dillard and contributors, [CC BY 4.0](../LICENSE-CONTENT). [Scope and attribution](../LICENSING.md). Provider material retains its own terms.

<a id="cloudflare-radar"></a>

## Cloudflare Radar outages and traffic anomalies

**[Visit source](https://radar.cloudflare.com/)** | [Provider documentation](https://developers.cloudflare.com/radar/investigate/outages/)

- **Provider:** Cloudflare
- **Coverage:** Global; country, region and network coverage varies
- **Type / access:** `live-feed` / `registration`
- **Formats:** JSON, Dashboard
- **Updates:** Outage annotations and anomaly updates; inspect reported times.
- **Security use:** Corroborate regional internet disruptions affecting offices and services.
- **License / terms:** Radar API documentation states CC BY-NC 4.0. Confirm rights for corporate operational use before ingestion; a free API token alone does not resolve permitted use.
- **Limitations:** Regional/network observations do not establish individual-site impact or a cyberattack cause. Verify serving-provider status and business consequences.
- **Review:** 2026-09-21 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://developers.cloudflare.com/radar/investigate/outages/) · [Provider reference 2](https://developers.cloudflare.com/radar/get-started/first-request/) · [Provider reference 3](https://developers.cloudflare.com/radar/)
- **Catalog ID:** `cloudflare-radar`

<a id="ioda"></a>

## IODA internet outage detection

**[Visit source](https://ioda.inetintel.cc.gatech.edu/)** | [Provider documentation](https://api.ioda.inetintel.cc.gatech.edu/v2/)

- **Provider:** Georgia Tech Internet Intelligence Lab
- **Coverage:** Global country, region and autonomous-system observations
- **Type / access:** `live-feed` / `open`
- **Formats:** JSON, Dashboard
- **Updates:** Signal-dependent observation windows; check series timestamps.
- **Security use:** Regional communications disruption and business-continuity context.
- **License / terms:** Public research interface; verify current data-reuse terms before production redistribution.
- **Limitations:** Inferred internet anomalies do not prove a cause or establish connectivity at a specific site.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://api.ioda.inetintel.cc.gatech.edu/v2/) · [Provider reference 2](https://ioda.inetintel.cc.gatech.edu/resources?tab=glossary)
- **Catalog ID:** `ioda`

<a id="telegeography-cables"></a>

## TeleGeography Submarine Cable Map

**[Visit source](https://www.submarinecablemap.com/)** | [Provider documentation](https://www.submarinecablemap.com/)

- **Provider:** TeleGeography
- **Coverage:** Global mapped submarine cable systems and landing points.
- **Type / access:** `reference` / `mixed`
- **Formats:** Web map, Licensed GIS data
- **Updates:** Editorial updates; bundled project extracts are dated snapshots.
- **Security use:** Connectivity dependency and geographic cable-landing context.
- **License / terms:** The audited project labels its bundled extract CC BY-NC-SA 3.0. Current publisher licensing and commercial structured-data access must be confirmed independently; do not assume the code license covers cable data.
- **Limitations:** Map lines are schematic context, not precise engineering routes or cable-outage observations. Publisher site rendered insufficient text for a full license review.
- **Review:** 2026-09-22 — `partial-review`
- **Evidence:** [Provider reference 1](https://www.submarinecablemap.com/) · [Provider reference 2](https://www2.telegeography.com/submarine-cable-map)
- **Catalog ID:** `telegeography-cables`
