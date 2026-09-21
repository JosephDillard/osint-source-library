# City selection and source review

The [city library](../CITIES.md) covers **three places in each of the 50 states**, with emergency-management/alert, police/public-safety, water and electric-utility references. The editable catalog is [catalog/cities.json](../catalog/cities.json).

## What “top three” means

For 49 states, rank Census **incorporated places** by the July 1, 2025 population estimate in **Vintage 2025**. This is population within the Census place geography, not metropolitan-area population, an assessment of risk, or a ranking of commercial importance.

The source is the Census Bureau's [SUB-EST2025 national file](https://www2.census.gov/programs-surveys/popest/datasets/2020-2025/cities/totals/sub-est2025.csv), available through its [city and town population estimates](https://www.census.gov/data/tables/time-series/demo/popest/2020s-total-cities-and-towns.html). The [file layout](https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2025/SUB-EST2025.pdf) defines the fields.

Selection procedure:

1. Read the CSV using its Windows-1252 encoding, keeping state and place FIPS as zero-padded strings.
2. Retain `SUMLEV == 162` (incorporated places). Exclude DC, Hawaii and Puerto Rico from this pass.
3. Within each state, sort `POPESTIMATE2025` descending and retain ranks 1–3.
4. Preserve the original `NAME`, population, population date and state/place FIPS. Short display names do not change the underlying geography.
5. Add Hawaii using the separate rule below.

`SUMLEV 170` consolidated-city totals are excluded to avoid mixing them with incorporated-place records. For consolidated governments with a Census “balance,” the selected balance excludes separately incorporated places. State pages flag these cases.

The catalog stores the SHA-256 of the actual Census CSV used. To reproduce the 147 annual-estimate records from a downloaded copy:

```powershell
python tools/rank_cities.py path/to/sub-est2025.csv --check
```

The command checks both the input hash and the selected FIPS IDs, names, populations and ranks. The large source CSV is not committed; generated rankings and source provenance are committed. A future Census vintage requires an intentional catalog and validation update.

## Hawaii exception

Hawaii does not have a comparable set of incorporated cities in this file. Its annual subcounty estimate program covers Urban Honolulu, while a consistent statewide comparison of CDPs needs a different source. See [Hawaii DBEDT population estimates](https://census.hawaii.gov/population-estimate/).

Use **April 1, 2020 Census counts for all three Hawaii CDPs**, from the Census Bureau's [Hawaii CDP table with 2020 population](https://tigerweb.geo.census.gov/tigerwebmain/Files/acs25/tigerweb_acs25_cdp_2020_tab20_hi.html):

| Rank | Census-designated place | Population | State–place FIPS |
| --- | --- | ---: | --- |
| 1 | Urban Honolulu | 350,964 | 15-71550 |
| 2 | East Honolulu | 50,922 | 15-06290 |
| 3 | Pearl City | 45,295 | 15-62600 |

These are CDPs rather than separate city governments. All three are on Oahu and share City and County of Honolulu agency references. The older date is displayed on every Hawaii profile; it is not presented as a 2025 estimate.

DC and territories are outside the requested 50-state scope. Other unincorporated places, metropolitan areas, and New England towns that Census treats as minor civil divisions rather than incorporated places are outside this selection definition.

## What a source entry establishes

Each city has references in all four categories. The initial review identified official municipal, county, state and utility pages through publisher navigation, search evidence and selected page inspection. A department directory, water quality page or subscription form can be a useful starting point without offering a live incident feed.

| Resource type | Meaning |
| --- | --- |
| `web-reference` | Agency or service reference; may be a department page, contact page, directory or water quality information. |
| `alert-page` | Publisher alert-center page; an empty page does not establish that no incidents exist. |
| `registration-portal` | Entry point for enrollment; no subscription was created or tested. |
| `outage-reference` | Utility outage map, reporting page, outage help or alert guidance; a working map or API is not implied. |
| `provider-portal` | Provider home or utility page; navigate to the relevant region and outage resources. |

| Review method | Evidence recorded |
| --- | --- |
| `official-directory-link` | A link was found in an official publisher's navigation or directory. |
| `publisher-search-evidence` | Official publisher search results were inspected; substantive page access may be incomplete. |
| `publisher-reference` | A publisher reference was selected or corrected using official material; see its evidence link and notes. |

The source's `reviewed_on` is a reference review date. It is not a certification of data accuracy, service coverage, freshness or feed functionality. Full content, subscriptions, authenticated services, licenses and operational access were not tested for every entry.

## Geography and utility coverage

Municipal limits, police jurisdiction, county emergency-management coverage, water districts and electric territories are different geographies. County and regional agencies are included where useful. A state directory is explicitly labeled when a stronger local link could not be established.

Electric utility assignments are starting references based on the city and known regional providers. They are **not a verified address-to-provider crosswalk or an exhaustive list**. Water references may cover only a portion of a city. Every city has `address_coverage_verified: false`.

For a specific facility, use the utility's service-area information or an authorized account record to confirm the provider. Some large providers require a state or operating-company choice. In particular, CenterPoint has Indiana and Texas regions; National Grid has different state regions; FirstEnergy combines several operating companies. Hawaii entries link to the Oahu outage resource.

Known limitations are called out in profiles, including split water coverage in San Jose and West Valley City, electric alternatives in New York City and municipal electric systems in Ohio. Other cities can also have split territories.

## HTTP snapshot and maintenance

[catalog/city-link-check.json](../catalog/city-link-check.json) records one retrieval per distinct source URL, with a timestamp, HTTP result, and where available a final URL and page title. Requests use normal TLS validation, a timeout, limited response reads and no authenticated sessions. Certificate failures and HTTP blocks are retained; no access protections are bypassed.

A 200 response is only evidence that a response was returned. It can be a shell, access page or unrelated redirect. A 403 response can mean automated access was blocked. Neither is a complete content review. The review corrected detected dead links and obvious jurisdiction mismatches; remaining incomplete checks are visible in the source details and snapshot.

Manual refresh commands:

```powershell
python tools/cities.py check-links
python tools/cities.py build
python tools/cities.py validate
python tools/cities.py build --check
```

`check-links --missing-only` fetches only newly added source URLs and preserves existing timestamps. Read error results and inspect suspicious titles/redirects before changing review notes. Neither command starts monitoring, creates accounts, enrolls in alerts or collects operational data.

The national/global catalog and city catalog are separate: the former records richer dataset/API access metadata, while this expansion is a directory of local references. Promote a city source to a documented integration only after establishing its format, cadence, geography, access and reuse conditions.
