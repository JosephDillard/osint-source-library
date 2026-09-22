# Satellite orbits & space activity

<!-- Generated from catalog/sources.json; edit the catalog, then run python tools/catalog.py build. -->

[All categories](../LIBRARY.md) | [How to use this library](../docs/getting-started.md)

Original catalog text: Copyright (c) 2026 Joseph Dillard and contributors, [CC BY 4.0](../LICENSE-CONTENT). [Scope and attribution](../LICENSING.md). Provider material retains its own terms.

<a id="celestrak"></a>

## CelesTrak general perturbations orbital elements

**[Visit source](https://celestrak.org/)** | [Provider documentation](https://celestrak.org/NORAD/documentation/gp-data-formats.php)

- **Provider:** CelesTrak
- **Coverage:** Cataloged Earth-orbiting objects; groups and public availability vary.
- **Type / access:** `periodic` / `open`
- **Formats:** TLE, OMM XML, JSON, CSV
- **Updates:** Orbital-element updates, not continuous measured positions. Inspect each element epoch and avoid excessive polling.
- **Security use:** Orbital context for satellite communications, observation planning and space-event research.
- **License / terms:** Follow CelesTrak usage policy, caching and backoff requirements and identify the data source. Public access does not imply unrestricted polling or an operational guarantee.
- **Limitations:** SGP4 positions are predictions from orbital elements; error grows with age and maneuvers. Legacy TLE numeric limits affect newer catalog identifiers. GP-format documentation retrieval failed; usage-policy material was accessible, so the record remains a partial review.
- **Review:** 2026-09-22 — `partial-review`
- **API entrypoint / example:** [Open endpoint](https://celestrak.org/NORAD/elements/gp.php). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://celestrak.org/NORAD/documentation/gp-data-formats.php) · [Provider reference 2](https://celestrak.org/usage-policy.php)
- **Catalog ID:** `celestrak`

<a id="launch-library-2"></a>

## Launch Library 2 spaceflight events

**[Visit source](https://thespacedevs.com/llapi)** | [Provider documentation](https://ll.thespacedevs.com/docs/)

- **Provider:** The Space Devs
- **Coverage:** Worldwide launch and space-event catalog; historical and scheduled missions.
- **Type / access:** `mixed` / `mixed`
- **Formats:** JSON, REST
- **Updates:** Curated updates as information changes; public allowance documented as 15 calls/hour, with token-based higher limits.
- **Security use:** Identify planned launches and recovery activity relevant to travel, ports and regional operations.
- **License / terms:** Provider FAQ permits use and sharing, discourages forwarding without added value, and encourages attribution. Cache results and check current tier limits.
- **Limitations:** Schedule and mission metadata are not flight telemetry, exclusion-zone authority or an observed launch trajectory. Development API data can be stale.
- **Review:** 2026-09-22 — `provider-documentation-reviewed`
- **API entrypoint / example:** [Open endpoint](https://ll.thespacedevs.com/2.3.0/launches/). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://ll.thespacedevs.com/docs/) · [Provider reference 2](https://github.com/TheSpaceDevs/Tutorials/blob/main/faqs/faq_TSD.md)
- **Catalog ID:** `launch-library-2`
