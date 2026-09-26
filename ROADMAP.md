# Roadmap

## Phase 1 — Source library

- [x] Categorized source records and browseable Markdown.
- [x] Public, registered, approved and commercial access labels.
- [x] Coverage, timing, limitations, evidence links and review dates.
- [x] Local search, validation and deterministic Markdown generation.
- [x] Contribution guidance and CI catalog checks.
- [x] Add source packs for three largest places in each of the 50 states, with the Hawaii CDP exception documented.
- [x] Catalog selected public GIS, population and power datasets with [proposed ETL paths](docs/public-dataset-etl.md).
- [ ] Extend city profiles with dedicated fire/EMS, public-health, transit, event-permit and closure sources.

## Phase 2 — Evaluate and prioritize

- Confirm licenses and access for the intended commercial or government use.
- Rank sources by relevance, geographic precision, freshness and maintenance effort.
- Define what constitutes actionable evidence for each decision.
- Record test queries, sample schemas and outage behavior without committing secrets.
- Confirm facility-level electric and water providers and replace general reference pages with documented notice feeds where available.
- Add dedicated transit, fire/EMS and public-health sources and expand to additional countries and operating areas.

## Phase 3 — Collect selected feeds

- Pilot versioned NWS forecast zones, regional OSM extracts and compatible Census geography/statistics using the [documented acceptance criteria](docs/public-dataset-etl.md#first-pilot-and-acceptance-criteria).
- Evaluate EIA inventory/generation joins next; keep periodic infrastructure context separate from outage observations.
- Implement small, documented connectors with timeouts, backoff and source attribution.
- Track source health and distinguish no events from collection failure.
- Retain event time, retrieval time, revisions and geolocation uncertainty.
- Normalize only after preserving provenance and source-specific meaning.

## Phase 4 — Situational awareness

- Map authorized areas, facilities and travel corridors.
- Show observations, possible exposure and confirmed impacts separately.
- Add analyst review and source-linked briefs.
- Introduce notifications only after thresholds, users and channels are explicitly configured.

Potential consumers include Open GEOINT Watch or Geospatial Data Gateway. These are future integration directions, not installed capabilities.
