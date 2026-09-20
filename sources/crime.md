# Crime & public safety

<!-- Generated from catalog/sources.json; edit the catalog, then run python tools/catalog.py build. -->

[All categories](../LIBRARY.md) | [How to use this library](../docs/getting-started.md)

<a id="chicago-crime"></a>

## Chicago reported crimes

**[Visit source](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2)** | [Provider documentation](https://data.cityofchicago.org/api/views/ijzp-q8t2.json)

- **Provider:** Chicago Police Department / City of Chicago
- **Coverage:** Chicago, Illinois
- **Type / access:** `periodic` / `open`
- **Formats:** JSON, CSV, Socrata API
- **Updates:** Updated daily; excludes the most recent seven days.
- **Security use:** Local reported-incident context for site planning.
- **License / terms:** City terms apply; metadata prohibits deriving exact addresses from approximate locations.
- **Limitations:** Block-level locations and preliminary classifications. Provider cautions against comparisons over time; not current dispatch.
- **Review:** 2026-09-20 — `provider-metadata-reviewed`
- **API entrypoint / example:** [Open endpoint](https://data.cityofchicago.org/resource/ijzp-q8t2.json). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://data.cityofchicago.org/api/views/ijzp-q8t2.json)
- **Catalog ID:** `chicago-crime`

<a id="fbi-cde"></a>

## FBI Crime Data Explorer

**[Visit source](https://cde.ucr.cjis.gov/)** | [Provider documentation](https://www.fbi.gov/how-we-can-help-you/more-fbi-services-and-information/ucr)

- **Provider:** FBI Uniform Crime Reporting Program
- **Coverage:** United States, participating law-enforcement agencies
- **Type / access:** `historical` / `open`
- **Formats:** Dashboard, Downloads
- **Updates:** Release based; inspect reporting period and agency participation.
- **Security use:** Area-level security planning and understanding reported crime patterns.
- **License / terms:** Public statistical releases; consult dataset documentation and methodology.
- **Limitations:** Not a live incident or dispatch feed. Missing submissions and changing reporting practices affect comparisons.
- **Review:** 2026-09-20 — `provider-documentation-reviewed`
- **Evidence:** [Provider reference 1](https://www.fbi.gov/how-we-can-help-you/more-fbi-services-and-information/ucr)
- **Catalog ID:** `fbi-cde`

<a id="nyc-complaints"></a>

## NYPD complaint data, current year to date

**[Visit source](https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Current-Year-To-Date-/5uac-w243)** | [Provider documentation](https://data.cityofnewyork.us/api/views/5uac-w243.json)

- **Provider:** NYPD / NYC Open Data
- **Coverage:** New York City
- **Type / access:** `periodic` / `open`
- **Formats:** JSON, CSV, Socrata API
- **Updates:** Periodic release covering completed reporting periods; check current rows and metadata.
- **Security use:** Reported-incident context around facilities and routes.
- **License / terms:** NYC Open Data terms apply; license identifier not supplied in reviewed metadata.
- **Limitations:** The description contains a stale year reference; inspect record dates. Complaints are not convictions or live dispatch.
- **Review:** 2026-09-20 — `provider-metadata-reviewed`
- **API entrypoint / example:** [Open endpoint](https://data.cityofnewyork.us/resource/5uac-w243.json). Required parameters, credentials and pagination may still apply.
- **Evidence:** [Provider reference 1](https://data.cityofnewyork.us/api/views/5uac-w243.json)
- **Catalog ID:** `nyc-complaints`
