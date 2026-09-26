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

<a id="eia-860"></a>

## EIA-860 electric power plant and generator inventory

**[Visit source](https://www.eia.gov/electricity/data/eia860/)** | [Provider documentation](https://www.eia.gov/electricity/data/eia860/)

- **Provider:** U.S. Energy Information Administration
- **Coverage:** U.S. surveyed electric power plants with at least 1 MW combined nameplate capacity; plant, utility and generator tables.
- **Type / access:** `periodic` / `open`
- **Formats:** Zipped Excel workbooks, Data layouts and code descriptions
- **Updates:** Annual inventory releases; the separate preliminary monthly generator inventory is a different product.
- **Security use:** Build a dated public power-plant inventory with generator, fuel and capacity context for hazard exposure screening.
- **License / terms:** EIA permits reuse and distribution of its government data and requests source acknowledgment with publication date. Third-party material and agency marks have separate restrictions.
- **Limitations:** Survey coverage excludes smaller installations. Proposed, operable and retired records must stay distinct; the annual retired tab is not a complete retirement history. Inventory status is not live availability, a service territory or evidence that a plant supplies a particular site. Validate coordinates and generator-to-plant joins before mapping.
- **Review:** 2026-09-26 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://www.eia.gov/electricity/data/eia860/) · [Provider reference 2](https://www.eia.gov/about/copyrights_reuse.php)
- **Catalog ID:** `eia-860`

<a id="eia-923"></a>

## EIA-923 power generation, fuel use and fuel stocks

**[Visit source](https://www.eia.gov/electricity/data/eia923/)** | [Provider documentation](https://www.eia.gov/electricity/data/eia923/)

- **Provider:** U.S. Energy Information Administration
- **Coverage:** U.S. surveyed power plants; the monthly reporting subset and annual population differ.
- **Type / access:** `periodic` / `open`
- **Formats:** Zipped Excel workbooks, Survey schedules and documentation
- **Updates:** Monthly and annual releases with reporting lag, preliminary values and later revisions; preserve reporting period and release date.
- **Security use:** Enrich a compatible EIA-860 inventory with generation and fuel context for continuity research and historical comparisons.
- **License / terms:** EIA government data can be reused and distributed with requested source/date acknowledgment; separately credited third-party material keeps its own terms.
- **Limitations:** Tables have different plant, prime-mover, generator or boiler grains. Document join keys and units; aggregate before joining to avoid multiplying values. Missing data is not zero, and generation changes alone do not establish an outage, cause or customer impact. Downloaded workbooks and joins were not tested in this review.
- **Review:** 2026-09-26 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://www.eia.gov/electricity/data/eia923/) · [Provider reference 2](https://www.eia.gov/about/copyrights_reuse.php)
- **Catalog ID:** `eia-923`

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
