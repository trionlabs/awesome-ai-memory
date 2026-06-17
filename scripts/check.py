#!/usr/bin/env python3
"""Validate the YAML data files.

Usage:
  python3 scripts/check.py           # schema, duplicates, ASCII, cross-references
  python3 scripts/check.py --links   # also check that every URL responds
"""

import concurrent.futures
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

PAPER_CATS = {"surveys", "foundations", "memory-systems", "graph-temporal",
              "parametric", "retrieval", "consolidation", "rl-memory",
              "multi-agent", "multimodal", "personalization", "security"}
PROJECT_CATS = {"engine", "mcp-server", "coding-agent", "framework-module",
                "platform", "research-code", "storage"}
BACKENDS = {"vector", "graph", "kv", "sql", "files", "parametric"}
LICENSES = {"Apache-2.0", "MIT", "BSD-2-Clause", "BSD-3-Clause", "GPL-2.0",
            "GPL-3.0", "AGPL-3.0", "LGPL-3.0", "MPL-2.0", "CC-BY-4.0",
            "CC0-1.0", "Unlicense", "other"}
BENCH_TYPES = {"dialogue", "long-context", "personalization", "agentic",
               "episodic", "safety"}
RESOURCE_TYPES = {"blog", "talk", "course", "podcast", "community", "list"}

ARXIV_RE = re.compile(r"^\d{4}\.\d{4,5}(v\d+)?$")
DATE_RE = re.compile(r"^\d{4}-\d{2}$")
SLUG_RE = re.compile(r"^[\w.-]+/[\w.-]+$")

errors = []


def err(msg):
    errors.append(msg)


def require(item, fields, where):
    for f in fields:
        if item.get(f) in (None, ""):
            err(f"{where}: missing field '{f}'")


def check_ascii(item, where):
    for k, v in item.items():
        if isinstance(v, str) and not v.isascii():
            bad = "".join(c for c in v if not c.isascii())
            err(f"{where}: non-ASCII in '{k}': {bad!r}")


def check_desc(item, where, field="desc"):
    d = item.get(field, "")
    if d and len(d) > 160:
        err(f"{where}: {field} too long ({len(d)} chars)")
    if d and d.endswith("."):
        err(f"{where}: {field} should not end with a period")


def load(name):
    path = DATA / name
    if not path.exists():
        err(f"{name}: file missing")
        return []
    with open(path) as f:
        data = yaml.safe_load(f)
    if not isinstance(data, list):
        err(f"{name}: top level must be a list")
        return []
    return data


def main():
    papers = load("papers.yaml")
    projects = load("projects.yaml")
    benchmarks = load("benchmarks.yaml")
    resources = load("resources.yaml")

    seen_titles = set()
    seen_arxiv = set()
    for i, p in enumerate(papers):
        where = f"papers[{i}] {p.get('title', '?')[:40]}"
        require(p, ["title", "date", "category", "desc"], where)
        check_ascii(p, where)
        check_desc(p, where)
        if p.get("category") not in PAPER_CATS:
            err(f"{where}: bad category {p.get('category')!r}")
        if p.get("date") and not DATE_RE.match(str(p["date"])):
            err(f"{where}: date must be YYYY-MM")
        if p.get("arxiv"):
            if not ARXIV_RE.match(str(p["arxiv"])):
                err(f"{where}: bad arxiv id {p['arxiv']!r}")
            if p["arxiv"] in seen_arxiv:
                err(f"{where}: duplicate arxiv id {p['arxiv']}")
            seen_arxiv.add(p["arxiv"])
        elif not p.get("url"):
            err(f"{where}: needs arxiv or url")
        t = p.get("title", "").lower()
        if t in seen_titles:
            err(f"{where}: duplicate title")
        seen_titles.add(t)

    seen_slugs = set()
    seen_names = set()
    for i, p in enumerate(projects):
        where = f"projects[{i}] {p.get('name', '?')}"
        require(p, ["name", "category", "desc"], where)
        check_ascii(p, where)
        check_desc(p, where)
        if p.get("category") not in PROJECT_CATS:
            err(f"{where}: bad category {p.get('category')!r}")
        if p.get("repo"):
            if not SLUG_RE.match(p["repo"]):
                err(f"{where}: repo must be a owner/name slug")
            if p["repo"].lower() in seen_slugs:
                err(f"{where}: duplicate repo {p['repo']}")
            seen_slugs.add(p["repo"].lower())
        elif not p.get("site"):
            err(f"{where}: needs repo or site")
        for b in p.get("backend", []):
            if b not in BACKENDS:
                err(f"{where}: bad backend {b!r}")
        lic = p.get("license")
        if lic is not None and lic not in LICENSES:
            err(f"{where}: unknown license {lic!r} (use an SPDX id or 'other')")
        if lic and not p.get("oss"):
            err(f"{where}: license set on non-oss entry")
        n = p.get("name", "").lower()
        if n in seen_names:
            err(f"{where}: duplicate name")
        seen_names.add(n)

    seen_bench = set()
    for i, b in enumerate(benchmarks):
        where = f"benchmarks[{i}] {b.get('name', '?')}"
        require(b, ["name", "url", "type", "measures"], where)
        check_ascii(b, where)
        check_desc(b, where, "measures")
        if b.get("type") not in BENCH_TYPES:
            err(f"{where}: bad type {b.get('type')!r}")
        if b.get("paper") and not ARXIV_RE.match(str(b["paper"])):
            err(f"{where}: bad arxiv id {b['paper']!r}")
        n = b.get("name", "").lower()
        if n in seen_bench:
            err(f"{where}: duplicate name")
        seen_bench.add(n)

    seen_urls = set()
    for i, r in enumerate(resources):
        where = f"resources[{i}] {r.get('title', '?')[:40]}"
        require(r, ["title", "url", "source", "type", "desc"], where)
        check_ascii(r, where)
        check_desc(r, where)
        if r.get("type") not in RESOURCE_TYPES:
            err(f"{where}: bad type {r.get('type')!r}")
        u = r.get("url", "")
        if u in seen_urls:
            err(f"{where}: duplicate url")
        seen_urls.add(u)

    if "--links" in sys.argv:
        urls = set()
        for p in papers:
            urls.add(f"https://arxiv.org/abs/{p['arxiv']}" if p.get("arxiv") else p.get("url"))
            if p.get("code"):
                urls.add(p["code"])
        for p in projects:
            if p.get("repo"):
                urls.add(f"https://github.com/{p['repo']}")
            if p.get("site"):
                urls.add(p["site"])
        for b in benchmarks:
            urls.add(b["url"])
        for r in resources:
            urls.add(r["url"])
        urls.discard(None)
        print(f"checking {len(urls)} urls")
        dead = check_links(sorted(urls))
        for u, why in dead:
            err(f"dead link: {u} ({why})")

    if errors:
        for e in errors:
            print(f"ERROR {e}")
        print(f"\n{len(errors)} errors")
        sys.exit(1)
    print(f"ok: {len(papers)} papers, {len(projects)} projects, "
          f"{len(benchmarks)} benchmarks, {len(resources)} resources")


def probe(url):
    req = urllib.request.Request(url, method="HEAD",
                                 headers={"User-Agent": "awesome-ai-memory-linkcheck"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return url, resp.status
    except urllib.error.HTTPError as e:
        if e.code in (403, 405, 429):
            try:
                get = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(get, timeout=20) as resp:
                    return url, resp.status
            except Exception as e2:
                return url, f"{e.code} then {e2}"
        return url, e.code
    except Exception as e:
        return url, str(e)


def check_links(urls):
    dead = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        for url, status in ex.map(probe, urls):
            if not isinstance(status, int) or status >= 400:
                dead.append((url, status))
    return dead


if __name__ == "__main__":
    main()
