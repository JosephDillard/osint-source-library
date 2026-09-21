#!/usr/bin/env python3
"""Offline validation, search, and Markdown generation for the source library."""
import argparse
from datetime import date, datetime, timezone
import json
from pathlib import Path
import re
import sys
from urllib.parse import parse_qsl, urlsplit

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "sources.json"
KINDS = {"live-feed", "periodic", "historical", "dashboard", "catalog", "reference", "mixed"}
ACCESS = {"open", "registration", "approval", "commercial", "mixed"}
REVIEWS = {"provider-documentation-reviewed", "provider-metadata-reviewed", "partial-review"}
TEXT_FIELDS = {
    "id", "name", "provider", "category", "coverage", "kind", "access", "url",
    "documentation_url", "update_frequency", "license_notes", "security_use",
    "limitations", "reviewed_on", "review_status",
}
FIELDS = TEXT_FIELDS | {"formats", "endpoint_url", "evidence_urls"}
SECRET_PARAMS = {"api_key", "apikey", "key", "map_key", "token", "access_token",
                 "client_secret", "password", "secret"}
GENERATED = "<!-- Generated from catalog/sources.json; edit the catalog, then run python tools/catalog.py build. -->"


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON property: {key}")
        result[key] = value
    return result


def load_catalog():
    return json.loads(CATALOG.read_text(encoding="utf-8"), object_pairs_hook=unique_keys)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def valid_date(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return False
    try:
        return date.fromisoformat(value) <= datetime.now(timezone.utc).date()
    except ValueError:
        return False


def valid_url(value):
    if not nonempty(value) or any(c.isspace() for c in value):
        return False
    try:
        parsed = urlsplit(value)
        return (
            parsed.scheme in {"http", "https"} and bool(parsed.hostname)
            and parsed.username is None and parsed.password is None
            and not any(k.lower() in SECRET_PARAMS for k, _ in parse_qsl(parsed.query))
        )
    except ValueError:
        return False


def validate(data):
    errors = []
    if not isinstance(data, dict):
        return ["Catalog must be an object."]
    if set(data) != {"catalog_version", "review_date", "categories", "sources"}:
        errors.append("Catalog has missing or unexpected fields.")
    if type(data.get("catalog_version")) is not int or data["catalog_version"] != 1:
        errors.append("catalog_version must be 1.")
    if not valid_date(data.get("review_date")):
        errors.append("review_date must be an ISO date no later than today.")
    categories = data.get("categories")
    if not isinstance(categories, dict) or not categories:
        return errors + ["categories must be a nonempty object."]
    for key, label in categories.items():
        if not re.fullmatch(r"[a-z][a-z0-9-]*", key) or not nonempty(label):
            errors.append(f"Invalid category: {key!r}")
    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        return errors + ["sources must be a nonempty list."]
    seen_ids, seen_urls = set(), set()
    for index, item in enumerate(sources):
        prefix = f"sources[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix}: must be an object.")
            continue
        prefix = str(item.get("id", prefix))
        if set(item) != FIELDS:
            errors.append(f"{prefix}: fields differ; missing={sorted(FIELDS-set(item))}, extra={sorted(set(item)-FIELDS)}")
        for field in TEXT_FIELDS:
            if not nonempty(item.get(field)):
                errors.append(f"{prefix}: {field} must be a nonempty string.")
        source_id = item.get("id")
        if isinstance(source_id, str):
            if not re.fullmatch(r"[a-z][a-z0-9-]*", source_id):
                errors.append(f"{prefix}: invalid id.")
            if source_id in seen_ids:
                errors.append(f"{prefix}: duplicate id.")
            seen_ids.add(source_id)
        for field, allowed in (("category", categories), ("kind", KINDS), ("access", ACCESS), ("review_status", REVIEWS)):
            if not isinstance(item.get(field), str) or item[field] not in allowed:
                errors.append(f"{prefix}: invalid {field}.")
        if not valid_date(item.get("reviewed_on")):
            errors.append(f"{prefix}: reviewed_on must be an ISO date no later than today.")
        elif valid_date(data.get("review_date")) and item["reviewed_on"] > data["review_date"]:
            errors.append(f"{prefix}: reviewed_on is later than the catalog review_date.")
        for field in ("formats", "evidence_urls"):
            values = item.get(field)
            if not isinstance(values, list) or not values or not all(nonempty(v) for v in values):
                errors.append(f"{prefix}: {field} must contain nonempty strings.")
            elif len(set(values)) != len(values):
                errors.append(f"{prefix}: duplicate {field} values.")
        for field in ("url", "documentation_url", "endpoint_url"):
            value = item.get(field)
            if field == "endpoint_url" and value is None:
                continue
            if not valid_url(value):
                errors.append(f"{prefix}: invalid or credential-bearing {field}.")
        evidence = item.get("evidence_urls")
        if isinstance(evidence, list):
            for value in evidence:
                if not valid_url(value):
                    errors.append(f"{prefix}: invalid or credential-bearing evidence URL.")
        url = item.get("url")
        if isinstance(url, str):
            canonical = url.rstrip("/").casefold()
            if canonical in seen_urls:
                errors.append(f"{prefix}: duplicate landing URL.")
            seen_urls.add(canonical)
    return errors


def escape(text):
    return str(text).replace("\\", "\\\\").replace("|", "\\|").replace("[", "\\[").replace("]", "\\]").replace("\n", " ")


def render(data):
    sources = data["sources"]
    index = [
        "# Source library", "", GENERATED, "",
        "Original catalog text: Copyright (c) 2026 Joseph Dillard and contributors, [CC BY 4.0](LICENSE-CONTENT). [Scope and attribution](LICENSING.md). Provider material retains its own terms.", "",
        f"**{len(sources)} sources across {len(data['categories'])} categories.** Catalog review: {data['review_date']}.", "",
        "Browse a category for source cards with documentation, access, limitations and evidence.",
        "For local agencies and utilities, browse the [three largest places in every state](CITIES.md).",
        "Access labels describe how to reach the source; they do not grant reuse rights. See the [access guide](README.md#access-labels).",
        "Review status describes evidence inspected, not a successful integration test.", "",
        "| Category | Sources |", "| --- | ---: |",
    ]
    pages = {}
    for category, title in data["categories"].items():
        entries = sorted((s for s in sources if s["category"] == category), key=lambda s: s["name"].casefold())
        index.append(f"| [{escape(title)}](sources/{category}.md) | {len(entries)} |")
        page = [f"# {title}", "", GENERATED, "", "[All categories](../LIBRARY.md) | [How to use this library](../docs/getting-started.md)", "",
                "Original catalog text: Copyright (c) 2026 Joseph Dillard and contributors, [CC BY 4.0](../LICENSE-CONTENT). [Scope and attribution](../LICENSING.md). Provider material retains its own terms.", ""]
        for item in entries:
            page += [
                f'<a id="{item["id"]}"></a>', "",
                f"## {item['name']}", "",
                f"**[Visit source]({item['url']})** | [Provider documentation]({item['documentation_url']})", "",
                f"- **Provider:** {item['provider']}",
                f"- **Coverage:** {item['coverage']}",
                f"- **Type / access:** `{item['kind']}` / `{item['access']}`",
                f"- **Formats:** {', '.join(item['formats'])}",
                f"- **Updates:** {item['update_frequency']}",
                f"- **Security use:** {item['security_use']}",
                f"- **License / terms:** {item['license_notes']}",
                f"- **Limitations:** {item['limitations']}",
                f"- **Review:** {item['reviewed_on']} — `{item['review_status']}`",
            ]
            if item["endpoint_url"]:
                page.append(f"- **API entrypoint / example:** [Open endpoint]({item['endpoint_url']}). Required parameters, credentials and pagination may still apply.")
            refs = " · ".join(f"[Provider reference {n}]({url})" for n, url in enumerate(item["evidence_urls"], 1))
            page += [f"- **Evidence:** {refs}", f"- **Catalog ID:** `{item['id']}`", ""]
        pages[ROOT / "sources" / f"{category}.md"] = "\n".join(page).rstrip() + "\n"
    index += ["", "## All sources", "", "| Source | Category | Type | Access |", "| --- | --- | --- | --- |"]
    for item in sorted(sources, key=lambda s: (list(data["categories"]).index(s["category"]), s["name"].casefold())):
        index.append(f"| [{escape(item['name'])}](sources/{item['category']}.md#{item['id']}) | {escape(data['categories'][item['category']])} | {item['kind']} | {item['access']} |")
    index += ["", "[Coverage gaps](docs/coverage.md) · [Review notes](docs/review-notes.md) · [Contribute a source](CONTRIBUTING.md)", ""]
    pages[ROOT / "LIBRARY.md"] = "\n".join(index)
    return pages


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate", help="Validate catalog structure without network access")
    build = sub.add_parser("build", help="Generate browsable Markdown from the catalog")
    build.add_argument("--check", action="store_true", help="Fail if generated Markdown differs")
    search = sub.add_parser("search", help="Search source metadata locally")
    search.add_argument("query", nargs="?", default="")
    search.add_argument("--category", help="Category ID, e.g. water, crime, aviation")
    search.add_argument("--access", choices=sorted(ACCESS))
    search.add_argument("--kind", choices=sorted(KINDS))
    search.add_argument("--json", action="store_true", help="Print matching source records as JSON")
    args = parser.parse_args()
    try:
        data = load_catalog()
        errors = validate(data)
        if errors:
            for error in errors:
                print(f"ERROR: {error}", file=sys.stderr)
            return 1
        if args.command == "validate":
            print(f"Valid: {len(data['sources'])} sources in {len(data['categories'])} categories.")
        elif args.command == "search":
            if args.category and args.category not in data["categories"]:
                parser.error("Unknown category. Choose: " + ", ".join(data["categories"]))
            matches = [
                s for s in data["sources"]
                if (not args.category or s["category"] == args.category)
                and (not args.access or s["access"] == args.access)
                and (not args.kind or s["kind"] == args.kind)
                and args.query.casefold() in json.dumps(s, ensure_ascii=False).casefold()
            ]
            if args.json:
                print(json.dumps(matches, indent=2, ensure_ascii=False))
            else:
                for item in matches:
                    print(f"{item['id']} | {item['name']} | {item['kind']} | {item['access']}\n  {item['url']}")
                print(f"\n{len(matches)} source(s).")
        else:
            pages = render(data)
            obsolete = set((ROOT / "sources").glob("*.md")) - set(pages)
            if obsolete:
                for path in sorted(obsolete):
                    print(f"Obsolete category file: {path.relative_to(ROOT)}; review and remove it.", file=sys.stderr)
                return 1
            different = [path for path, body in pages.items() if not path.exists() or path.read_text(encoding="utf-8") != body]
            if args.check:
                for path in different:
                    print(f"Stale or missing: {path.relative_to(ROOT)}", file=sys.stderr)
                if different:
                    return 1
                print(f"Generated Markdown is current ({len(pages)} files).")
            else:
                for path, body in pages.items():
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text(body, encoding="utf-8", newline="\n")
                print(f"Built {len(pages)} Markdown files.")
        return 0
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
