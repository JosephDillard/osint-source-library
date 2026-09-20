# Geospatial Intelligence

A curated library of public data, feeds and reference sources for **physical security, protective services, business continuity and government situational awareness**.

Start with the **[source library](LIBRARY.md)**. It covers crime, public events and protests, weather, natural hazards, air traffic, sea traffic, roads, government information, power outages, water systems, internet disruptions and geographic context.

The initial collection prioritizes the United States and includes global sources. Local entries illustrate the utility, transport and public-safety sources to add for each operating area.

## Browse the library

- **[Source directory](LIBRARY.md)** — categories, source links, access conditions and detailed source cards.
- **[Machine-readable catalog](catalog/sources.json)** — the editable source of truth.
- **[Getting started](docs/getting-started.md)** — a practical source selection workflow.
- **[Coverage and gaps](docs/coverage.md)** — what the collection covers and where local research is needed.
- **[Data model](docs/data-model.md)** — field definitions and review status.
- **[Roadmap](ROADMAP.md)** — a path from a links library to a useful intelligence capability.

Each record includes the provider, geography, type of data, access requirements, formats, update timing, licensing notes, security uses, limitations, evidence links and review date.

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
```

Edit `catalog/sources.json`, then rebuild the Markdown library. See [CONTRIBUTING.md](CONTRIBUTING.md). Validation checks catalog structure and generated files; it does not certify remote availability or licensing.

## Initial scope

This first version is a research and source-discovery library. Use it to identify relevant sources for authorized facilities, routes and operating areas, then verify freshness and geographic precision before relying on an observation.

The [review notes](docs/review-notes.md) describe the September 20, 2026 review and its limits. Some provider sites require registration, block automated retrieval or expose only public dashboards.

## Relationship to other projects

This standalone catalog can inform **Open GEOINT Watch**, **Geospatial Data Gateway** or a future security dashboard. It has no runtime dependency on those projects. A future integration should preserve the source ID, provider terms, event time, retrieval time, location precision and confidence.

Original repository code and written content are MIT licensed; see [LICENSE](LICENSE). This does not grant rights to third-party datasets, articles, maps or API services.
