#!/usr/bin/env python3
"""Generate README.md from the YAML files in data/.

Usage:
  python3 scripts/generate.py            # render README.md from data + cached metadata
  python3 scripts/generate.py --fetch    # refresh data/github-meta.json first (uses GITHUB_TOKEN)
"""

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
FRAGMENTS = DATA / "fragments"
META_PATH = DATA / "github-meta.json"

PAPER_SECTIONS = [
    ("surveys", "Surveys and Taxonomies"),
    ("foundations", "Foundations"),
    ("memory-systems", "Memory Systems"),
    ("graph-temporal", "Graph and Temporal Memory"),
    ("parametric", "Parametric Memory"),
    ("retrieval", "Retrieval-Centric Memory"),
    ("consolidation", "Consolidation, Reflection and Forgetting"),
    ("rl-memory", "Learned and RL-Trained Memory"),
    ("multi-agent", "Multi-Agent Memory"),
    ("multimodal", "Multimodal Memory"),
    ("personalization", "Personalization and User Modeling"),
    ("security", "Memory Security and Privacy"),
]

PROJECT_SECTIONS = [
    ("engine", "Memory Engines and Layers"),
    ("mcp-server", "MCP Memory Servers"),
    ("coding-agent", "Memory for Coding Agents"),
    ("platform", "Platform and Consumer Memory"),
    ("framework-module", "Framework Memory Modules"),
    ("research-code", "Research Systems with Code"),
    ("storage", "Storage Substrates"),
]

BENCH_TYPES = [
    ("dialogue", "Conversational and Multi-Session"),
    ("long-context", "Long-Context"),
    ("personalization", "Personalization"),
    ("agentic", "Agentic"),
    ("episodic", "Episodic"),
    ("safety", "Safety and Hallucination"),
]

RESOURCE_TYPES = [
    ("blog", "Engineering Posts"),
    ("talk", "Talks"),
    ("course", "Courses"),
    ("podcast", "Podcasts"),
    ("community", "Communities"),
    ("list", "Related Lists"),
]


def load(name):
    with open(DATA / name) as f:
        return yaml.safe_load(f) or []


def load_meta():
    if META_PATH.exists():
        with open(META_PATH) as f:
            return json.load(f)
    return {"fetched_at": None, "repos": {}}


def fetch_meta(projects):
    token = os.environ.get("GITHUB_TOKEN", "")
    meta = {"fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "repos": {}}
    slugs = sorted({p["repo"] for p in projects if p.get("repo")})
    for slug in slugs:
        req = urllib.request.Request(f"https://api.github.com/repos/{slug}")
        req.add_header("Accept", "application/vnd.github+json")
        if token:
            req.add_header("Authorization", f"Bearer {token}")
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                d = json.load(resp)
        except urllib.error.HTTPError as e:
            print(f"warn: {slug}: HTTP {e.code}", file=sys.stderr)
            continue
        except Exception as e:
            print(f"warn: {slug}: {e}", file=sys.stderr)
            continue
        meta["repos"][slug] = {
            "stars": d.get("stargazers_count", 0),
            "pushed_at": (d.get("pushed_at") or "")[:10],
            "license": (d.get("license") or {}).get("spdx_id") or "-",
            "archived": d.get("archived", False),
        }
        print(f"  {slug}: {meta['repos'][slug]['stars']} stars", file=sys.stderr)
    with open(META_PATH, "w") as f:
        json.dump(meta, f, indent=2, sort_keys=True)
        f.write("\n")
    return meta


def fmt_stars(n):
    if n >= 1000:
        return f"{n / 1000:.1f}k"
    return str(n)


def anchor(title):
    out = []
    for ch in title.lower():
        if ch.isalnum():
            out.append(ch)
        elif ch == " ":
            out.append("-")
    return "".join(out)


def arxiv_url(aid):
    return f"https://arxiv.org/abs/{aid}"


def paper_line(p):
    url = arxiv_url(p["arxiv"]) if p.get("arxiv") else p.get("url", "")
    bits = [f"- **[{p['title']}]({url})**"]
    when = p.get("date", "")
    venue = p.get("venue")
    if venue:
        bits.append(f"({when}, {venue})")
    elif when:
        bits.append(f"({when})")
    bits.append(f"- {p['desc']}.")
    if p.get("code"):
        bits.append(f"[[code]({p['code']})]")
    return " ".join(bits)


def project_row(p, meta):
    repo = p.get("repo")
    info = meta["repos"].get(repo, {}) if repo else {}
    if repo:
        name = f"[{p['name']}](https://github.com/{repo})"
    else:
        name = f"[{p['name']}]({p['site']})" if p.get("site") else p["name"]
    stars = fmt_stars(info["stars"]) if info else "-"
    pushed = info.get("pushed_at", "-") if info else "-"
    lic = info.get("license", "-") if info else ("-" if p.get("oss") else "closed")
    if info and info.get("archived"):
        pushed += " (archived)"
    backend = ", ".join(p.get("backend", [])) or "-"
    mcp = "yes" if p.get("mcp") else "no"
    hosted = "yes" if p.get("hosted") else "no"
    desc = p["desc"]
    if p.get("site") and repo:
        desc += f" ([site]({p['site']}))"
    if p.get("paper"):
        desc += f" ([paper]({arxiv_url(p['paper'])}))"
    return f"| {name} | {stars} | {pushed} | {lic} | {backend} | {mcp} | {hosted} | {desc} |"


def bench_row(b):
    name = f"[{b['name']}]({b['url']})"
    paper = f"[{b['paper']}]({arxiv_url(b['paper'])})" if b.get("paper") else "-"
    return f"| {name} | {paper} | {b['measures']} |"


def resource_line(r):
    line = f"- [{r['title']}]({r['url']}) - {r['source']}"
    if r.get("year"):
        line += f", {r['year']}"
    line += f". {r['desc']}."
    return line


def fragment(name):
    return (FRAGMENTS / name).read_text().rstrip()


def main():
    projects = load("projects.yaml")
    papers = load("papers.yaml")
    benchmarks = load("benchmarks.yaml")
    resources = load("resources.yaml")

    if "--fetch" in sys.argv:
        meta = fetch_meta(projects)
    else:
        meta = load_meta()

    out = []
    header = fragment("header.md")
    counts = {
        "PAPER_COUNT": str(len(papers)),
        "PROJECT_COUNT": str(len(projects)),
        "BENCH_COUNT": str(len(benchmarks)),
        "UPDATED": meta.get("fetched_at") or datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    }
    for k, v in counts.items():
        header = header.replace("{{" + k + "}}", v)
    out.append(header)
    out.append("")

    toc = ["## Contents", ""]
    toc.append("- [Start Here](#start-here)")
    toc.append("- [Concepts](#concepts)")
    for _, title in PROJECT_SECTIONS:
        toc.append(f"- [{title}](#{anchor(title)})")
    toc.append("- [Research Papers](#research-papers)")
    for _, title in PAPER_SECTIONS:
        toc.append(f"  - [{title}](#{anchor(title)})")
    toc.append("- [Benchmarks and Evaluation](#benchmarks-and-evaluation)")
    toc.append("- [Guides, Talks and Courses](#guides-talks-and-courses)")
    toc.append("- [Contributing](#contributing)")
    out.extend(toc)
    out.append("")

    out.append(fragment("start-here.md"))
    out.append("")
    out.append(fragment("concepts.md"))
    out.append("")

    table_header = (
        "| Project | Stars | Updated | License | Backend | MCP | Hosted | What it is |\n"
        "|---|---|---|---|---|---|---|---|"
    )
    for cat, title in PROJECT_SECTIONS:
        rows = [p for p in projects if p["category"] == cat]
        if not rows:
            continue
        rows.sort(key=lambda p: meta["repos"].get(p.get("repo") or "", {}).get("stars", -1), reverse=True)
        out.append(f"## {title}")
        out.append("")
        frag = FRAGMENTS / f"section-{cat}.md"
        if frag.exists():
            out.append(frag.read_text().rstrip())
            out.append("")
        out.append(table_header)
        for p in rows:
            out.append(project_row(p, meta))
        out.append("")

    out.append("## Research Papers")
    out.append("")
    out.append("Curated, not exhaustive. Selection favors papers that are peer-reviewed, "
               "introduce a named system or benchmark, or shaped how the field thinks. "
               "Each entry links the paper and, where available, the code.")
    out.append("")
    for cat, title in PAPER_SECTIONS:
        rows = [p for p in papers if p["category"] == cat]
        if not rows:
            continue
        rows.sort(key=lambda p: p.get("date", ""), reverse=True)
        out.append(f"### {title}")
        out.append("")
        for p in rows:
            out.append(paper_line(p))
        out.append("")

    out.append("## Benchmarks and Evaluation")
    out.append("")
    for btype, title in BENCH_TYPES:
        rows = [b for b in benchmarks if b["type"] == btype]
        if not rows:
            continue
        rows.sort(key=lambda b: b["name"].lower())
        out.append(f"### {title}")
        out.append("")
        out.append("| Benchmark | Paper | Measures |")
        out.append("|---|---|---|")
        for b in rows:
            out.append(bench_row(b))
        out.append("")

    out.append("## Guides, Talks and Courses")
    out.append("")
    for rtype, title in RESOURCE_TYPES:
        rows = [r for r in resources if r["type"] == rtype]
        if not rows:
            continue
        rows.sort(key=lambda r: (-(r.get("year") or 0), r["title"].lower()))
        out.append(f"### {title}")
        out.append("")
        for r in rows:
            out.append(resource_line(r))
        out.append("")

    out.append(fragment("footer.md"))
    out.append("")

    (ROOT / "README.md").write_text("\n".join(out))
    print(f"README.md written: {len(papers)} papers, {len(projects)} projects, "
          f"{len(benchmarks)} benchmarks, {len(resources)} resources")


if __name__ == "__main__":
    main()
