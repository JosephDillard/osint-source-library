# Internet & communications disruptions

<!-- Generated from catalog/sources.json; edit the catalog, then run python tools/catalog.py build. -->

[All categories](../LIBRARY.md) | [How to use this library](../docs/getting-started.md)

<a id="cloudflare-radar"></a>

## Cloudflare Radar outages and traffic anomalies

**[Visit source](https://radar.cloudflare.com/)** | [Provider documentation](https://developers.cloudflare.com/radar/investigate/outages/)

- **Provider:** Cloudflare
- **Coverage:** Global; country, region and network coverage varies
- **Type / access:** `live-feed` / `registration`
- **Formats:** JSON, Dashboard
- **Updates:** Outage annotations and anomaly updates; inspect reported times.
- **Security use:** Corroborate regional internet disruptions affecting offices and services.
- **License / terms:** API token with Radar read permission; follow Cloudflare terms and attribution requirements.
- **Limitations:** Cloudflare observations are not a complete view of every network or individual connection.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://developers.cloudflare.com/radar/investigate/outages/) · [Provider reference 2](https://developers.cloudflare.com/radar/get-started/first-request/)
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
