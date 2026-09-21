# Power outages & grid resilience

<!-- Generated from catalog/sources.json; edit the catalog, then run python tools/catalog.py build. -->

[All categories](../LIBRARY.md) | [How to use this library](../docs/getting-started.md)

Original catalog text: Copyright (c) 2026 Joseph Dillard and contributors, [CC BY 4.0](../LICENSE-CONTENT). [Scope and attribution](../LICENSING.md). Provider material retains its own terms.

<a id="austin-energy"></a>

## Austin Energy outage map

**[Visit source](https://www.austintexas.gov/services/view-and-report-power-outages)** | [Provider documentation](https://www.austintexas.gov/services/view-and-report-power-outages)

- **Provider:** Austin Energy / City of Austin
- **Coverage:** Austin Energy service territory, Texas
- **Type / access:** `dashboard` / `open`
- **Formats:** Web map
- **Updates:** Operational outage updates; inspect map timestamps.
- **Security use:** Local utility outage awareness and restoration context.
- **License / terms:** Public utility status map; integration and redistribution terms require provider review.
- **Limitations:** Service territory differs from city boundaries; map estimates do not establish building-level service.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://www.austintexas.gov/services/view-and-report-power-outages)
- **Catalog ID:** `austin-energy`

<a id="eaglei-history"></a>

## EAGLE-I historical power outage data, 2014-2022

**[Visit source](https://doi.ccs.ornl.gov/dataset/ccec86f0-e144-5de8-aee0-fb26028b26e1)** | [Provider documentation](https://doi.ccs.ornl.gov/dataset/ccec86f0-e144-5de8-aee0-fb26028b26e1)

- **Provider:** Oak Ridge National Laboratory
- **Coverage:** United States, reporting utility coverage varies
- **Type / access:** `historical` / `open`
- **Formats:** Dataset downloads
- **Updates:** Fixed historical release; this entry is specifically the 2014-2022 dataset.
- **Security use:** Historical outage exposure and resilience research.
- **License / terms:** Review repository license and citation instructions before reuse; current bulk-download availability not tested.
- **Limitations:** Does not provide current outages. Collection gaps and varying utility coverage affect comparisons.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://doi.ccs.ornl.gov/dataset/ccec86f0-e144-5de8-aee0-fb26028b26e1)
- **Catalog ID:** `eaglei-history`

<a id="poweroutage-us"></a>

## PowerOutage.us

**[Visit source](https://poweroutage.us/)** | [Provider documentation](https://poweroutage.us/use-our-data)

- **Provider:** Bluefire Studios / PowerOutage.us
- **Coverage:** Tracked utilities in the United States; other markets via provider products
- **Type / access:** `mixed` / `commercial`
- **Formats:** Dashboard, REST API
- **Updates:** Provider and utility dependent; inspect freshness.
- **Security use:** Area-level electricity disruption and business-continuity awareness.
- **License / terms:** Public viewing and licensed API products are distinct. API use and redistribution are governed by commercial terms.
- **Limitations:** Outage counts and estimated affected areas do not prove a particular building has lost power.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://poweroutage.us/use-our-data) · [Provider reference 2](https://poweroutage.us/legal/apitermsofuse) · [Provider reference 3](https://poweroutage.us/legal/termsofuse)
- **Catalog ID:** `poweroutage-us`
