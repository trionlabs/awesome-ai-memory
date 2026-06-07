# Contributing

The README is generated. Do not edit it directly - edit the YAML files under
`data/` and regenerate.

## How to add an entry

1. Add one entry to the right file:
   - `data/projects.yaml` - tools, engines, MCP servers, framework modules
   - `data/papers.yaml` - research papers
   - `data/benchmarks.yaml` - benchmarks and evaluation datasets
   - `data/resources.yaml` - blog posts, talks, courses, communities, lists
2. Run the checks and regenerate:

   ```sh
   pip install pyyaml
   python3 scripts/check.py
   python3 scripts/generate.py
   ```

3. Commit both your YAML change and the regenerated `README.md`, open a PR.

## Inclusion criteria

An entry needs at least one of:

- a published paper (peer-reviewed venue, or arXiv with meaningful adoption),
- an active repository with real users (roughly 100+ stars, commits within the
  last six months), or
- a shipped product with public documentation.

Plus, always:

- a factual one-line description (no marketing language, max 160 chars,
  ASCII only, no trailing period - the generator adds punctuation),
- working links.

Self-promotion is fine when the criteria are met; they are the same for
everyone. Borderline entries should make the case in the PR description.

## Removal

Entries are removed when archived, dead-linked, or inactive for over a year
with a better-maintained alternative listed. The weekly refresh marks archived
repos automatically.

## Schemas

### papers.yaml

```yaml
- title: "MemGPT: Towards LLMs as Operating Systems"
  arxiv: "2310.08560"        # arXiv ID, or null with url set instead
  code: "https://github.com/letta-ai/letta"   # optional
  date: "2023-10"            # YYYY-MM of first publication
  venue: null                # e.g. "ICLR 2025" when accepted somewhere
  category: memory-systems
  desc: "OS-style virtual context management with paging between memory tiers"
```

Categories: `surveys`, `foundations`, `memory-systems`, `graph-temporal`,
`parametric`, `retrieval`, `consolidation`, `rl-memory`, `multi-agent`,
`multimodal`, `personalization`, `security`.

### projects.yaml

```yaml
- name: Mem0
  repo: mem0ai/mem0          # GitHub slug, or null for closed source
  site: "https://mem0.ai"    # optional
  category: engine
  oss: true
  backend: [vector, graph]   # vector, graph, kv, sql, files, parametric
  mcp: true                  # maintained MCP server or integration
  hosted: true               # managed offering exists
  paper: "2504.19413"        # optional arXiv ID
  desc: "Memory layer that extracts, consolidates and retrieves memories"
```

Categories: `engine`, `mcp-server`, `coding-agent`, `framework-module`,
`platform`, `research-code`, `storage`. Stars, last-commit and license columns
are filled by the generator - do not add them.

### benchmarks.yaml

```yaml
- name: LoCoMo
  url: "https://github.com/snap-research/locomo"
  paper: "2402.17753"        # optional
  type: dialogue             # dialogue, long-context, personalization,
                             # agentic, episodic, safety
  measures: "Very long-term multi-session conversational memory QA"
```

### resources.yaml

```yaml
- title: "Effective context engineering for AI agents"
  url: "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"
  source: Anthropic
  year: 2025
  type: blog                 # blog, talk, course, podcast, community, list
  desc: "Compaction and structured notes as memory primitives"
```

## Style

ASCII only, no emoji, no smart quotes. Descriptions state what the thing does,
not how great it is.
