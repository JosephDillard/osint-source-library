# OSINT Source Library

A curated **open-source intelligence (OSINT)** library of public data, feeds and geospatial sources for **physical security, protective services, business continuity and government situational awareness**. U.S. first, with global sources.

Start with the **[source library](LIBRARY.md)**. It covers crime, public events and protests, weather, natural hazards, air traffic, sea traffic, roads, government information, power outages, water systems, internet disruptions, geographic context, commercial event intelligence, travel risk and protective intelligence.

Cybersecurity coverage is limited to major events: consequential breaches and incidents affecting people, business operations, essential services or critical providers. Routine vulnerability, malware and scanning feeds are outside this collection's scope. See the [major-event criteria](docs/getting-started.md#major-cybersecurity-events).

The collection prioritizes the United States and includes global sources. The **[city library](CITIES.md)** adds the three largest places in every state: 150 profiles with emergency-management, public-safety, water and electric-utility references.

## Browse the library

- **[Source directory](LIBRARY.md)** — categories, source links, access conditions and detailed source cards.
- **[Cities in all 50 states](CITIES.md)** — three ranked places per state, with local agency and utility references.
- **[Machine-readable catalog](catalog/sources.json)** — the editable source of truth.
- **[Machine-readable city catalog](catalog/cities.json)** — city populations, Census FIPS IDs, source records and provider links.
- **[Getting started](docs/getting-started.md)** — a practical source selection workflow.
- **[Expanded service shortlist](docs/service-shortlist.md)** — 18 candidates, evaluation priorities, API/ETL access and integration questions.
- **[Coverage and gaps](docs/coverage.md)** — what the collection covers and where local research is needed.
- **[Data model](docs/data-model.md)** — field definitions and review status.
- **[Roadmap](ROADMAP.md)** — a path from a links library to a useful intelligence capability.

Each national/global record includes the provider, geography, type of data, access requirements, formats, update timing, licensing notes, security uses, limitations, evidence links and review date.

The city directory uses a lighter reference schema. Its rankings use Census Vintage 2025 incorporated-place populations; Hawaii uses 2020 Census CDPs. Utility territories still need confirmation by address, and many agency links are reference pages rather than live feeds. See the [city methodology](docs/city-methodology.md).

## Access labels

| Label | Meaning |
| --- | --- |
| `open` | Public viewing or downloads without a required account for the cataloged entry; reuse terms still apply. |
| `registration` | An account, API key or developer enrollment is needed. |
| `approval` | Provider approval or an applicable written agreement is needed. |
| `commercial` | Licensed commercial integration option; public viewing may also exist. |
| `mixed` | Access depends on the dataset, product or endpoint. |

**Publicly accessible does not mean openly licensed.** Licensed and approval-based sources are explicitly labeled so the directory remains useful for commercial and government users. This repository stores links and original source descriptions; third-party data keeps its own terms.

A `live-feed` label describes the provider's offering. It does not mean this repository collects, monitors or validates that feed continuously. Historical datasets and dashboards are labeled separately.

## Search and maintain locally

The Markdown library works without installing anything. The optional catalog helper uses Python 3.10+ and its standard library.

```powershell
python tools/catalog.py search outage
python tools/catalog.py search --category aviation
python tools/catalog.py search --access open --kind live-feed
python tools/catalog.py validate
python tools/catalog.py build
python tools/catalog.py build --check
python tools/cities.py search --state TX
python tools/cities.py search "Kansas City" --category public-safety
python tools/cities.py validate
python tools/cities.py build
python tools/cities.py build --check
```

Edit `catalog/sources.json` for national/global sources or `catalog/cities.json` for city references, then rebuild the corresponding Markdown library. See [CONTRIBUTING.md](CONTRIBUTING.md). Validation checks catalog structure and generated files; it does not certify remote availability or licensing.

Repository instructions for coding agents are in [AGENTS.md](AGENTS.md).

## Initial scope

This first version is a research and source-discovery library. Use it to identify relevant sources for authorized facilities, routes and operating areas, then verify freshness and geographic precision before relying on an observation.

The [review notes](docs/review-notes.md) describe the September 20, 2026 initial review and September 21 service expansion, including their limits. Some provider sites require registration, block automated retrieval or expose only public dashboards.

## Relationship to other projects

This standalone catalog can inform **Open GEOINT Watch**, **Geospatial Data Gateway** or a future security dashboard. It has no runtime dependency on those projects. A future integration should preserve the source ID, provider terms, event time, retrieval time, location precision and confidence.

## License

Original code, tests, software configuration and code examples use [MIT](LICENSE). Original catalog descriptions and prose documentation use [CC BY 4.0](LICENSE-CONTENT). See [licensing and attribution](LICENSING.md) for the exact scope, attribution guidance and earlier MIT revisions.

Third-party datasets, articles, maps, software and API services retain their own terms. These repository licenses do not grant additional rights to that material.

## Repository guidance and copyright

Repository-specific coding and validation instructions are in [AGENTS.md](AGENTS.md). See [COPYRIGHT.md](COPYRIGHT.md) for ownership, licensing scope, and third-party notices. The [licensing guide](LICENSING.md) explains the MIT software / CC BY 4.0 content split.
