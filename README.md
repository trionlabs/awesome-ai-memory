# Awesome AI Memory

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Papers](https://img.shields.io/badge/papers-213-blue)
![Projects](https://img.shields.io/badge/projects-80-blue)
![Benchmarks](https://img.shields.io/badge/benchmarks-65-blue)
![Updated](https://img.shields.io/badge/metadata-2026-06-17-green)

Memory for LLMs and AI agents: the systems that let models remember across turns,
sessions and lifetimes. This list covers the full stack - research papers, memory
engines, MCP servers, framework modules, benchmarks and engineering guides.

Why this list:

- **Data-driven.** Every entry lives in a YAML file under `data/`. The README,
  star counts, last-commit dates and license columns are generated and refreshed
  weekly by CI. No stale tables.
- **Neutral.** No vendor owns this list. Inclusion criteria are written down in
  [CONTRIBUTING.md](CONTRIBUTING.md) and apply to everyone equally.
- **Curated.** Papers are selected, not scraped. Every entry has a one-line
  description and, where it exists, a code link.
- **Practitioner-first.** Comparison tables answer "which memory system should I
  use" before "what has been published".

## Contents

- [Start Here](#start-here)
- [Concepts](#concepts)
- [Memory Engines and Layers](#memory-engines-and-layers)
- [MCP Memory Servers](#mcp-memory-servers)
- [Memory for Coding Agents](#memory-for-coding-agents)
- [Platform and Consumer Memory](#platform-and-consumer-memory)
- [Framework Memory Modules](#framework-memory-modules)
- [Research Systems with Code](#research-systems-with-code)
- [Storage Substrates](#storage-substrates)
- [Research Papers](#research-papers)
  - [Surveys and Taxonomies](#surveys-and-taxonomies)
  - [Foundations](#foundations)
  - [Memory Systems](#memory-systems)
  - [Graph and Temporal Memory](#graph-and-temporal-memory)
  - [Parametric Memory](#parametric-memory)
  - [Retrieval-Centric Memory](#retrievalcentric-memory)
  - [Consolidation, Reflection and Forgetting](#consolidation-reflection-and-forgetting)
  - [Learned and RL-Trained Memory](#learned-and-rltrained-memory)
  - [Multi-Agent Memory](#multiagent-memory)
  - [Multimodal Memory](#multimodal-memory)
  - [Personalization and User Modeling](#personalization-and-user-modeling)
  - [Memory Security and Privacy](#memory-security-and-privacy)
- [Benchmarks and Evaluation](#benchmarks-and-evaluation)
- [Guides, Talks and Courses](#guides-talks-and-courses)
- [Contributing](#contributing)

## Start Here

New to AI memory? Read these five in order:

1. [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) (Lilian Weng, 2023) - the canonical mental model: memory as one of the three agent pillars.
2. [Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427) (CoALA, 2023) - working, episodic, semantic and procedural memory as a design framework.
3. [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) (2023) - the paper that started the memory-as-OS line; became Letta.
4. [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (Anthropic, 2025) - how memory and context management meet in production.
5. [Memory in the Age of AI Agents: A Survey](https://arxiv.org/abs/2512.13564) (2025) - the current map of the field: forms, functions and dynamics.

Then pick a memory engine from the [comparison table](#memory-engines-and-layers) and build something.

## Concepts

A 60-second taxonomy, distilled from the surveys below:

- **By substrate.** *Parametric* memory lives in model weights (fine-tuning, model
  editing, memory layers). *Contextual* (token-level) memory lives outside the
  model and is fed through the context window (RAG stores, memory engines,
  scratchpads). *Latent* memory lives in hidden states and KV caches.
- **By function.** *Working* memory is the active context of the current task.
  *Episodic* memory records what happened (events, sessions, trajectories).
  *Semantic* memory stores facts and knowledge. *Procedural* memory captures
  skills and how-to knowledge (prompts, code, workflows).
- **By lifecycle.** Memory systems differ in how they *write* (extraction,
  summarization), *index* (vectors, graphs, profiles), *retrieve* (semantic,
  temporal, multi-hop), *update* (conflict resolution, versioning) and *forget*
  (decay, eviction, consolidation).

Most production systems today are contextual episodic-plus-semantic stores with
vector or graph indexes; most open research problems sit in lifecycle operations
(consolidation, forgetting, self-organization) and in pushing memory back into
parameters and latents.

## Memory Engines and Layers

Dedicated memory layers you add to an agent or app. The table is sorted by stars
and refreshed weekly; "Backend" is the primary storage model, "MCP" means a
maintained MCP server or integration exists, "Hosted" means a managed offering.

| Project | Stars | Updated | License | Backend | MCP | Hosted | What it is |
|---|---|---|---|---|---|---|---|
| [Mem0](https://github.com/mem0ai/mem0) | 58.7k | 2026-06-17 | Apache-2.0 | vector, graph | yes | yes | Memory layer that extracts, consolidates and retrieves user/session/agent memories; ships OpenMemory MCP ([site](https://mem0.ai)) ([paper](https://arxiv.org/abs/2504.19413)) |
| [Khoj](https://github.com/khoj-ai/khoj) | 35.2k | 2026-03-26 | AGPL-3.0 | vector, files | no | yes | Personal AI brain over your notes and documents with semantic search and recall |
| [Graphiti](https://github.com/getzep/graphiti) | 27.5k | 2026-06-17 | Apache-2.0 | graph, vector | yes | yes | Temporal knowledge graph engine behind Zep: bi-temporal edges, episodes and hybrid retrieval ([paper](https://arxiv.org/abs/2501.13956)) |
| [Supermemory](https://github.com/supermemoryai/supermemory) | 27.1k | 2026-06-17 | MIT | vector | yes | yes | Universal memory API for ingesting documents, chats and web content with sub-second retrieval ([site](https://supermemory.ai)) |
| [Letta](https://github.com/letta-ai/letta) | 23.4k | 2026-05-14 | Apache-2.0 | sql, vector | yes | yes | Agent server with OS-style memory management; successor to MemGPT with self-editing core and archival memory ([site](https://www.letta.com)) ([paper](https://arxiv.org/abs/2310.08560)) |
| [cognee](https://github.com/topoteretes/cognee) | 17.9k | 2026-06-16 | Apache-2.0 | graph, vector | yes | yes | Memory engine that builds knowledge graphs plus embeddings from documents via ECL (extract, cognify, load) pipelines ([site](https://www.cognee.ai)) |
| [Hindsight](https://github.com/vectorize-io/hindsight) | 16.5k | 2026-06-17 | MIT | vector | no | yes | Open-source agent memory by Vectorize with retain/recall/reflect operations over typed memory banks ([site](https://hindsight.vectorize.io)) |
| [Second Me](https://github.com/mindverse/Second-Me) | 15.6k | 2025-09-30 | Apache-2.0 | parametric, vector | no | no | Trains a personal model as AI-native memory of you, served locally ([paper](https://arxiv.org/abs/2503.08102)) |
| [Memori](https://github.com/MemoriLabs/Memori) | 15.3k | 2026-06-15 | NOASSERTION | sql | no | no | SQL-first open-source memory engine storing agent memories in standard relational databases ([site](https://memorilabs.ai)) |
| [MemU](https://github.com/NevaMind-AI/memU) | 13.9k | 2026-06-14 | NOASSERTION | files, vector | yes | yes | Agent memory framework that organizes memories as an interlinked folder/file system curated by a memory agent ([site](https://memu.pro)) |
| [MemOS](https://github.com/MemTensor/MemOS) | 9.9k | 2026-06-17 | Apache-2.0 | vector, graph, kv | no | yes | Memory operating system organizing plaintext, activation (KV-cache) and parametric memory as MemCubes ([site](https://memos.openmem.net)) ([paper](https://arxiv.org/abs/2507.03724)) |
| [EverMemOS](https://github.com/EverMind-AI/EverMemOS) | 7.6k | 2026-06-17 | Apache-2.0 | vector | no | yes | Memory operating system by EverMind with engram-style consolidation, targeting long-horizon conversational recall ([site](https://evermind.ai)) |
| [MineContext](https://github.com/volcengine/MineContext) | 5.4k | 2026-05-07 | Apache-2.0 | vector, files | no | no | Proactive context engine from ByteDance Volcengine that captures screen activity into retrievable context |
| [Honcho](https://github.com/plastic-labs/honcho) | 5.2k | 2026-06-15 | AGPL-3.0 | vector, sql | yes | yes | User-modeling memory layer with theory-of-mind representations for personalized agents |
| [Zep](https://github.com/getzep/zep) | 4.7k | 2026-06-17 | Apache-2.0 | graph, vector | yes | yes | Agent memory service built on the Graphiti temporal knowledge graph; tracks facts with validity intervals ([site](https://www.getzep.com)) ([paper](https://arxiv.org/abs/2501.13956)) |
| [MIRIX](https://github.com/Mirix-AI/MIRIX) | 3.6k | 2026-06-06 | Apache-2.0 | sql, vector | no | no | Multi-agent memory system with six memory types (core, episodic, semantic, procedural, resource, vault) ([site](https://mirix.io)) ([paper](https://arxiv.org/abs/2507.07957)) |
| [MemMachine](https://github.com/MemMachine/MemMachine) | 3.1k | 2026-06-17 | Apache-2.0 | vector, sql | yes | no | Universal memory layer with episodic and profile memory for agents |
| [ReMe](https://github.com/agentscope-ai/ReMe) | 3.1k | 2026-06-10 | Apache-2.0 | vector | no | no | Memory and experience reuse framework for agents from the AgentScope team |
| [Memobase](https://github.com/memodb-io/memobase) | 2.8k | 2026-01-11 | Apache-2.0 | sql | no | yes | Profile-based long-term user memory: maintains structured user profiles and event timelines over Postgres ([site](https://www.memobase.io)) |
| [Memary](https://github.com/kingjulio8238/Memary) | 2.6k | 2024-10-22 | MIT | graph | no | no | Knowledge-graph long-term memory for agents using Neo4j or FalkorDB with entity and timeline modules |
| [Nemori](https://github.com/nemori-ai/nemori) | 203 | 2026-04-16 | MIT | vector | no | no | Self-organizing episodic memory that segments conversations into human-scale episodes for retrieval |
| [Mengram](https://github.com/alibaizhanov/mengram) | 178 | 2026-06-15 | Apache-2.0 | graph, vector | no | yes | Open-source memory layer combining knowledge graph and vector retrieval for LLM applications ([site](https://mengram.io)) |
| [MemClaw (Caura)](https://github.com/caura-ai/caura-memclaw) | 122 | 2026-06-16 | Apache-2.0 | graph, vector | no | yes | Graph and vector memory tool by Caura AI for persistent agent memory ([site](https://memclaw.net)) |
| [memonto](https://github.com/shihanwan/memonto) | 98 | 2024-10-16 | Apache-2.0 | graph | no | no | Ontology-driven graph memory library that stores agent knowledge as RDF triples |
| [MemClaw (Felo)](https://github.com/Felo-Inc/memclaw) | 32 | 2026-04-23 | MIT | vector | no | no | Vector-based agent memory tool by Felo for persisting and recalling agent context ([site](https://memclaw.me)) |
| [llongterm](https://www.llongterm.com) | - | - | closed | graph | no | yes | Closed-source API offering persistent per-user minds as a long-term memory layer for LLM apps |
| [WhyHow](https://www.whyhow.ai) | - | - | closed | graph | no | yes | Commercial knowledge-graph platform for building schema-controlled graphs as structured memory for RAG |
| [Hyperspell](https://hyperspell.com) | - | - | closed | vector | no | yes | Managed memory and context API that connects user data sources for AI apps |

## MCP Memory Servers

Memory exposed over the Model Context Protocol, usable from Claude, Cursor and
any MCP client.

| Project | Stars | Updated | License | Backend | MCP | Hosted | What it is |
|---|---|---|---|---|---|---|---|
| [MCP Memory Server (official)](https://github.com/modelcontextprotocol/servers) | 87.3k | 2026-06-17 | NOASSERTION | graph, files | yes | no | Reference knowledge-graph memory server from the MCP project: entities, relations, observations |
| [Basic Memory](https://github.com/basicmachines-co/basic-memory) | 3.2k | 2026-06-14 | AGPL-3.0 | files | yes | no | Local-first Markdown knowledge base over MCP, Obsidian-compatible notes as agent memory |
| [Redis Agent Memory Server](https://github.com/redis/agent-memory-server) | 280 | 2026-06-16 | NOASSERTION | vector, kv | yes | no | Redis-backed working and long-term memory service with MCP and REST interfaces |

## Memory for Coding Agents

Persistent memory for coding assistants: project conventions, decisions and
session context that survive the context window.

| Project | Stars | Updated | License | Backend | MCP | Hosted | What it is |
|---|---|---|---|---|---|---|---|
| [claude-mem](https://github.com/thedotmack/claude-mem) | 82.8k | 2026-06-16 | Apache-2.0 | vector, sql | yes | no | Claude Code plugin that compresses session transcripts into searchable persistent memory |
| [Agentmemory](https://github.com/rohitg00/agentmemory) | 23.2k | 2026-06-15 | Apache-2.0 | vector, sql | yes | no | Persistent memory toolkit for AI coding agents, tuned and ranked on real-world memory benchmarks |
| [ByteRover (formerly Cipher)](https://github.com/campfirein/byterover-cli) | 4.9k | 2026-06-17 | NOASSERTION | vector | yes | no | Shared memory layer for coding agents via MCP; works with Claude Code, Cursor, Windsurf and Copilot |
| [MCP Memory Keeper](https://github.com/mkreyman/mcp-memory-keeper) | 127 | 2026-06-06 | MIT | sql | yes | no | SQLite-backed MCP server preserving coding session context, decisions and progress across compactions |
| [Claude Code memory](https://docs.claude.com/en/docs/claude-code/memory) | - | - | closed | files | no | yes | CLAUDE.md project instructions plus auto-memory directories persisting context across sessions |
| [Cursor Memories](https://docs.cursor.com/context/memories) | - | - | closed | files | no | yes | Auto-generated rules from past conversations, scoped per project |
| [Windsurf Memories](https://docs.windsurf.com/windsurf/cascade/memories) | - | - | closed | files | no | yes | Cascade auto-memories and user rules persisting context between sessions |

## Platform and Consumer Memory

Memory built into the major assistants and platforms. Mostly closed source;
listed because they define what users expect memory to do.

| Project | Stars | Updated | License | Backend | MCP | Hosted | What it is |
|---|---|---|---|---|---|---|---|
| [ChatGPT memory](https://help.openai.com/en/articles/8590148-memory-faq) | - | - | closed | kv | no | yes | Saved memories plus reference-chat-history personalization in ChatGPT |
| [Claude memory](https://www.anthropic.com/news/memory) | - | - | closed | files | no | yes | Project-scoped memory in Claude apps plus a developer memory tool with context editing in the API |
| [Gemini personalization](https://support.google.com/gemini/answer/15637730) | - | - | closed | kv | no | yes | Past-chat recall and personal context settings in Gemini |
| [Graphlit](https://graphlit.com) | - | - | closed | graph, vector | yes | yes | Managed API platform that ingests unstructured content into a knowledge graph plus vector index for agents |
| [SID](https://www.sid.ai) | - | - | closed | vector | no | yes | Closed-source retrieval API connecting user accounts (email, drive, chat) as personal context for LLM apps |
| [Glean](https://www.glean.com) | - | - | closed | vector, graph | no | yes | Enterprise work assistant with a knowledge graph and personal memory over company data |

## Framework Memory Modules

| Project | Stars | Updated | License | Backend | MCP | Hosted | What it is |
|---|---|---|---|---|---|---|---|
| [LangChain](https://github.com/langchain-ai/langchain) | 139.5k | 2026-06-17 | MIT | vector | no | no | General LLM framework whose chat history and memory abstractions are widely used for conversational recall ([site](https://www.langchain.com)) |
| [AutoGen Teachability](https://github.com/microsoft/autogen) | 59.0k | 2026-04-15 | CC-BY-4.0 | vector | no | no | Teachable agents that persist user teachings to a vector store across conversations |
| [CrewAI memory](https://github.com/crewAIInc/crewAI) | 53.7k | 2026-06-17 | MIT | vector, sql | no | yes | Built-in short-term, long-term and entity memory for crews of agents |
| [LlamaIndex memory](https://github.com/run-llama/llama_index) | 50.2k | 2026-06-17 | MIT | vector | no | no | Composable memory blocks: chat buffers, vector memory and fact extraction for LlamaIndex agents |
| [Agno memory](https://github.com/agno-agi/agno) | 40.7k | 2026-06-17 | Apache-2.0 | vector, sql | no | yes | Session storage plus user memories built into the Agno agent framework |
| [LangGraph persistence](https://github.com/langchain-ai/langgraph) | 35.0k | 2026-06-17 | MIT | kv, sql | no | yes | Checkpointers and cross-thread memory store underlying LangChain agent persistence |
| [Semantic Kernel memory](https://github.com/microsoft/semantic-kernel) | 28.1k | 2026-06-17 | MIT | vector | no | no | Memory connectors and vector stores for .NET, Python and Java agents |
| [Google ADK memory](https://github.com/google/adk-python) | 20.1k | 2026-06-17 | Apache-2.0 | vector | no | yes | MemoryService abstraction in the Agent Development Kit, backed by Vertex AI Memory Bank |
| [Julep](https://github.com/julep-ai/julep) | 6.6k | 2026-03-13 | - | vector, sql | no | yes | Stateful agent platform with built-in sessions and long-term document and user memory ([site](https://julep.ai)) |
| [LangMem](https://github.com/langchain-ai/langmem) | 1.5k | 2026-06-12 | MIT | vector | no | no | LangChain SDK for semantic, episodic and procedural memory with a background memory manager |
| [BaseAI (Langbase Memory)](https://github.com/LangbaseInc/baseai) | 1.3k | 2026-05-16 | NOASSERTION | vector | no | yes | Langbase web AI framework with serverless RAG memory primitives attached to pipes/agents ([site](https://langbase.com/docs/memory)) |
| [HybridAGI](https://github.com/SynaLinks/HybridAGI) | 900 | 2026-05-08 | Apache-2.0 | graph, vector | no | no | Neuro-symbolic agent framework storing programs, documents and facts in graph-based memory |
| [BondAI](https://github.com/krohling/bondai) | 221 | 2024-01-14 | MIT | vector | no | no | Python agent framework with a MemGPT-inspired core/archival memory system ([site](https://bondai.dev)) |

## Research Systems with Code

| Project | Stars | Updated | License | Backend | MCP | Hosted | What it is |
|---|---|---|---|---|---|---|---|
| [GraphRAG](https://github.com/microsoft/graphrag) | 33.8k | 2026-06-17 | MIT | graph, vector | no | no | Microsoft pipeline that builds entity knowledge graphs and community summaries for global query answering ([site](https://microsoft.github.io/graphrag/)) ([paper](https://arxiv.org/abs/2404.16130)) |
| [SimpleMem](https://github.com/aiming-lab/SimpleMem) | 3.5k | 2026-05-21 | MIT | vector | no | no | Lifelong memory via semantically lossless compression; text and multimodal |
| [MemoRAG](https://github.com/qhjqhj00/MemoRAG) | 2.2k | 2025-09-11 | Apache-2.0 | vector, parametric | no | no | Memory-inspired retrieval with a global-memory model that drafts clues to guide evidence retrieval ([paper](https://arxiv.org/abs/2409.05591)) |
| [SkillClaw](https://github.com/AMAP-ML/SkillClaw) | 1.9k | 2026-06-02 | MIT | files | no | no | Procedural skill memory from AMAP-ML that extracts and reuses skills across agent trajectories ([paper](https://arxiv.org/abs/2604.08377)) |
| [MemoryOS](https://github.com/BAI-LAB/MemoryOS) | 1.5k | 2026-04-28 | Apache-2.0 | files, vector | yes | no | OS-inspired hierarchical memory with short/mid/long-term stores, heat-based promotion and an MCP server ([paper](https://arxiv.org/abs/2506.06326)) |
| [A-Mem](https://github.com/agiresearch/A-mem) | 1.1k | 2025-12-12 | MIT | vector | no | no | Agentic memory with Zettelkasten-style note construction, dynamic linking and memory evolution ([paper](https://arxiv.org/abs/2502.12110)) |
| [MemEngine](https://github.com/nuster1128/MemEngine) | 111 | 2025-05-13 | - | vector | no | no | Unified modular library implementing many research memory models for LLM agents under one API ([paper](https://arxiv.org/abs/2505.02099)) |

## Storage Substrates

Databases memory systems are built on. Pointer-level coverage only - exhaustive
vector-DB and graph-DB lists exist elsewhere.

| Project | Stars | Updated | License | Backend | MCP | Hosted | What it is |
|---|---|---|---|---|---|---|---|
| [Milvus](https://github.com/milvus-io/milvus) | 44.8k | 2026-06-17 | Apache-2.0 | vector | yes | yes | Distributed open-source vector database built for billion-scale similarity search ([site](https://milvus.io)) |
| [Faiss](https://github.com/facebookresearch/faiss) | 40.3k | 2026-06-17 | MIT | vector | no | no | Meta library for efficient similarity search and clustering of dense vectors; embedded index, not a server ([site](https://faiss.ai)) |
| [Qdrant](https://github.com/qdrant/qdrant) | 32.4k | 2026-06-17 | Apache-2.0 | vector | yes | yes | Rust vector database with filtering and payload indexing; common backend for agent memory engines ([site](https://qdrant.tech)) |
| [Chroma](https://github.com/chroma-core/chroma) | 28.5k | 2026-06-16 | Apache-2.0 | vector | yes | yes | Open-source embedding database for AI applications; frequent default vector store for memory layers ([site](https://www.trychroma.com)) |
| [Neo4j](https://github.com/neo4j/neo4j) | 16.7k | 2026-06-08 | GPL-3.0 | graph | yes | yes | Property graph database commonly used as the graph backend for agent memory and GraphRAG systems ([site](https://neo4j.com)) |
| [Weaviate](https://github.com/weaviate/weaviate) | 16.3k | 2026-06-17 | BSD-3-Clause | vector | no | yes | Open-source vector database with hybrid search and modular vectorizers ([site](https://weaviate.io)) |
| [txtai](https://github.com/neuml/txtai) | 12.7k | 2026-06-16 | Apache-2.0 | vector | no | no | All-in-one open-source embeddings database combining vector indexes, SQL and graph for semantic search ([site](https://neuml.github.io/txtai/)) |
| [NebulaGraph](https://github.com/vesoft-inc/nebula) | 12.2k | 2026-05-18 | Apache-2.0 | graph | no | yes | Distributed open-source graph database for large-scale knowledge graph storage ([site](https://www.nebula-graph.io)) |
| [FalkorDB](https://github.com/FalkorDB/falkordb) | 4.6k | 2026-06-16 | NOASSERTION | graph | yes | yes | Low-latency graph database (RedisGraph successor) with sparse-matrix engine, used for GraphRAG memory ([site](https://www.falkordb.com)) |
| [AllegroGraph](https://allegrograph.com) | - | - | closed | graph | no | yes | Commercial RDF graph database with vector and neuro-symbolic extensions from Franz Inc |
| [Ontotext GraphDB](https://www.ontotext.com) | - | - | closed | graph | no | yes | Commercial RDF triplestore (GraphDB) for knowledge graphs and semantic retrieval |
| [Pinecone](https://www.pinecone.io) | - | - | closed | vector | yes | yes | Managed vector database widely used as the retrieval substrate for RAG and agent memory |
| [Prometheux](https://www.prometheux.co.uk) | - | - | closed | graph | no | yes | Commercial knowledge graph and reasoning platform based on Vadalog logic programming |
| [RDFox (Oxford Semantic)](https://www.oxfordsemantic.tech) | - | - | closed | graph | no | yes | In-memory RDF triplestore with high-performance rule reasoning from Oxford Semantic Technologies |
| [Stardog](https://www.stardog.com) | - | - | closed | graph | no | yes | Enterprise knowledge graph platform with reasoning, used as structured memory for enterprise agents |
| [Vectara](https://www.vectara.com) | - | - | closed | vector | no | yes | Managed RAG platform with hosted ingestion, embedding and retrieval |

## Research Papers

Curated, not exhaustive. Selection favors papers that are peer-reviewed, introduce a named system or benchmark, or shaped how the field thinks. Each entry links the paper and, where available, the code.

### Surveys and Taxonomies

- **[Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads](https://arxiv.org/abs/2606.06448)** (2026-06) - Characterizes agent memory as a stateful systems workload with a phase-aware profiler and taxonomy across ten representative systems.
- **[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://arxiv.org/abs/2601.02163)** (2026-06) - Self-organizing memory OS with episodic trace formation, semantic consolidation, and reconstructive recollection over MemCell units.
- **[An Agent-Oriented Pluggable Experience-RAG Skill for Experience-Driven Retrieval Strategy Orchestration](https://arxiv.org/abs/2605.03989)** (2026-05) - Pluggable Experience-RAG agent skill with six modules for retrieval strategy routing; rule-based routing beats learned routing.
- **[MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory](https://arxiv.org/abs/2605.15128)** (2026-05) - Visual-centric benchmark for multimodal agent memory with granularity-by-reasoning-depth matrix and gates against text shortcuts.
- **[Agentic Frameworks for Reasoning Tasks: An Empirical Study](https://arxiv.org/abs/2604.16646)** (2026-04) - Empirical study of 22 agentic frameworks finding orchestration quality, memory control, and context growth drive performance gaps.
- **[Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering](https://arxiv.org/abs/2604.08224)** (2026-04) - Reviews LLM agent externalization across memory, skills, protocols, and harness engineering, mapping trade-offs and open challenges.
- **[Human Cognition in Machines: A Unified Perspective of World Models](https://arxiv.org/abs/2604.16592)** (2026-04) - Unified cognitive survey of world models covering memory, perception, reasoning, and metacognition; introduces Epistemic World Models.
- **[Beyond the Context Window: A Cost-Performance Analysis of Fact-Based Memory vs. Long-Context LLMs for Persistent Agents](https://arxiv.org/abs/2603.04814)** (2026-03) - Cost-performance comparison of long-context LLMs vs fact-based memory; memory wins cost efficiency after about 10 turns at 100k context.
- **[Emerging Human-like Strategies for Semantic Memory Foraging in Large Language Models](https://arxiv.org/abs/2603.01822)** (2026-03) - Mechanistic interpretability study finding human-like strategic semantic memory search behavior across LLM layers.
- **[Modular Memory is the Key to Continual Learning Agents](https://arxiv.org/abs/2603.01761)** (2026-03) - Roadmap for modular memory combining in-context learning for fast adaptation with weight updates for consolidation in lifelong agents.
- **[Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions](https://arxiv.org/abs/2602.22680)** (2026-02) - Capability-oriented review of personalized LLM agents with taxonomy over user profiling, memory, planning, and action execution.
- **[Rethinking Memory Mechanisms of Foundation Agents in the Second Half: A Survey](https://arxiv.org/abs/2602.06052)** (2026-01) - Unified taxonomy of foundation agent memory by substrate, cognitive mechanism, and subject; reviews learning policies and benchmarks.
- **[Memory in the Age of AI Agents: A Survey](https://arxiv.org/abs/2512.13564)** (2025-12) - Surveys agent memory through forms, functions, and dynamics lenses, distinguishing it from LLM memory, RAG, and context engineering.
- **[A Survey of Machine Unlearning](https://dl.acm.org/doi/full/10.1145/3749987)** (2025-09) - Surveys machine unlearning methods to remove data influence without full retraining, covering effectiveness, fairness, and privacy.
- **[A Survey on the Memory Mechanism of Large Language Model based Agents](https://dl.acm.org/doi/pdf/10.1145/3748302)** (2025-09) - Systematic survey of memory module designs and evaluation methods for LLM agents, analyzing roles and limits across applications.
- **[A Survey of Machine Unlearning in Large Language Models: Methods, Challenges and Future Directions](https://arxiv.org/abs/2503.01854)** (2025-05) - Taxonomy of LLM unlearning to remove undesirable data influence without retraining; reviews methods, challenges, and future work.
- **[Rethinking Memory in AI: Taxonomy, Operations, Topics, and Future Directions](https://arxiv.org/abs/2505.00675)** (2025-05) - Categorizes AI memory representations and operations (integration, updating, indexing, forgetting, retrieval, compression) in four themes.
- **[Cognitive Memory in Large Language Models](https://arxiv.org/abs/2504.02441)** (2025-04) - Examines memory types and mechanisms in LLMs and their role in reducing hallucination and enabling self-evolution.
- **[Digital Forgetting in Large Language Models: A Survey of Unlearning Methods](https://arxiv.org/abs/2404.02062)** (2025-04) - Surveys digital forgetting and unlearning in LLMs, covering retraining, machine unlearning, prompting, and forgetting guarantees.
- **[From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs](https://arxiv.org/abs/2504.15965)** (2025-04) - Links human memory to LLM memory and proposes a 3D taxonomy by object, form, and time with open issues in personal and system memory.
- **[Human-inspired Perspectives: A Survey on AI Long-term Memory](https://arxiv.org/abs/2411.00489)** (2025-01) - Maps human long-term memory mechanisms to parametric and non-parametric AI memory and proposes the SALM cognitive architecture.

### Foundations

- **[JARVIS-1: Open-World Multi-task Agents with Memory-Augmented Multimodal Language Models](https://arxiv.org/abs/2311.05997)** (2023-11) - Minecraft agent with multimodal memory of past plans and experiences; self-improves over 200 tasks incl. diamond pickaxe.
- **[Think-in-Memory: Recalling and Post-thinking Enable LLMs with Long-Term Memory](https://arxiv.org/abs/2311.08719)** (2023-11) - Stores post-thinking thoughts instead of raw history and recalls them via locality-sensitive hashing in long-term dialogue.
- **[Character-LLM: A Trainable Agent for Role-Playing](https://arxiv.org/abs/2310.10158)** (2023-10, EMNLP 2023) - Trains role-playing agents on reconstructed character experiences, with protective experiences to limit era-inconsistent answers.
- **[MemoChat: Tuning LLMs to Use Memos for Consistent Long-Range Open-Domain Conversation](https://arxiv.org/abs/2308.08239)** (2023-08) - Instruction tuning for memorization-retrieval-response cycles where LLMs write and consult structured memos in long chats.
- **[Augmenting Language Models with Long-Term Memory](https://arxiv.org/abs/2306.07174)** (2023-06, NeurIPS 2023) - LongMem: frozen backbone plus residual side-network caching long-term context as retrievable key-value memory.
- **[ChatDB: Augmenting LLMs with Databases as Their Symbolic Memory](https://arxiv.org/abs/2306.03901)** (2023-06) - SQL database as symbolic memory manipulated via chain-of-memory operations for precise, multi-hop record keeping and reasoning. [[code](https://github.com/huchenxucs/ChatDB)]
- **[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250)** (2023-05, AAAI 2024) - Long-term memory with Ebbinghaus-inspired forgetting and evolving user portraits; basis of the SiliconFriend companion bot.
- **[Prompted LLMs as Chatbot Modules for Long Open-domain Conversation](https://aclanthology.org/2023.findings-acl.277.pdf)** (2023-05, ACL 2023 Findings) - Modular prompted chatbot (clarifier, memory processor, generator) achieving long-term persona consistency without fine-tuning.
- **[RET-LLM: Towards a General Read-Write Memory for Large Language Models](https://arxiv.org/abs/2305.14322)** (2023-05) - Dedicated read-write memory unit storing knowledge triplets, managed through a text-based API for explicit store and recall.
- **[RecurrentGPT: Interactive Generation of (Arbitrarily) Long Text](https://arxiv.org/abs/2305.13304)** (2023-05) - Language-based LSTM-style recurrence over prompts with editable natural-language short/long-term memory for arbitrarily long text.
- **[Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291)** (2023-05, TMLR 2024) - Lifelong Minecraft agent storing self-written, self-verified code skills in a growing skill library for compositional reuse. [[code](https://github.com/MineDojo/Voyager)]
- **[Enhancing Large Language Model with Self-Controlled Memory Framework](https://arxiv.org/abs/2304.13343)** (2023-04) - Memory controller managing long-term activation and short-term flash memory streams for unbounded input without fine-tuning.
- **[Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442)** (2023-04, UIST 2023) - Memory stream with recency/importance/relevance retrieval plus reflection and planning; 25 believable agents in the Smallville sim. [[code](https://github.com/joonspk-research/generative_agents)]
- **[Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)** (2023-03, NeurIPS 2023) - Verbal self-reflections on task feedback stored in an episodic memory buffer let agents improve across trials without weight updates. [[code](https://github.com/noahshinn/reflexion)]

### Memory Systems

- **[Exploring Cross-Scenario Generality of Agentic Memory Systems: Diagnostics and a Strong Baseline](https://arxiv.org/abs/2606.04315)** (2026-06) - Diagnoses cross-scenario generality of agent memory systems; AutoMEM baseline shows active agent-controlled storage is more robust.
- **[Beyond Similarity Search: Tenure and the Case for Structured Belief State in LLM Memory](https://arxiv.org/abs/2605.11325)** (2026-05) - Typed belief-state schema for cross-session memory; scoped BM25 beats dense vector retrieval; ships as local OpenAI-compatible proxy.
- **[MEMTIER: Tiered Memory Architecture and Retrieval Bottleneck Analysis for Long-Running Autonomous AI Agents](https://arxiv.org/abs/2605.03675)** (2026-05) - Tiered episodic/semantic memory with five-signal retrieval, async consolidation daemon, and PPO-based cognitive weight updates.
- **[What Happens Inside Agent Memory? Circuit Analysis from Emergence to Diagnosis](https://arxiv.org/abs/2605.03354)** (2026-05) - Traces write/manage/read circuits inside agent memory systems and uses feature-space separation to localize silent memory failures.
- **[Building an Internal Coding Agent at Zup: Lessons and Open Questions](https://arxiv.org/abs/2604.09805)** (2026-04) - Production lessons from Zup's internal coding agent: tool design, safety guardrails, state management, and progressive supervision.
- **[ByteRover: Agent-Native Memory Through LLM-Curated Hierarchical Context](https://arxiv.org/abs/2604.01599)** (2026-04) - LLM curates a hierarchical Context Tree with importance scoring, maturity tiers, recency decay and 5-tier progressive retrieval.
- **[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization](https://arxiv.org/abs/2604.17091)** (2026-04) - Self-evolving long-horizon agent maximizing context information density via hierarchical memory, compression, and reusable SOPs.
- **[M*: Every Task Deserves Its Own Memory Harness](https://arxiv.org/abs/2604.11811)** (2026-04) - Represents agent memory as evolvable executable Python programs, discovering task-specific memory designs via code evolution.
- **[MemReader: From Passive to Active Extraction for Long-Term Agent Memory](https://arxiv.org/abs/2604.07877)** (2026-04) - Model family trained with GRPO to decide write/defer/retrieve/discard for memory extraction; integrated into MemOS.
- **[Memanto: Typed Semantic Memory with Information-Theoretic Retrieval for Long-Horizon Agents](https://arxiv.org/abs/2604.22085)** (2026-04) - 13-class typed memory schema with index-free information-theoretic retrieval; 89.8 LongMemEval and 87.1 LoCoMo without graphs.
- **[Omakase: Proactive Assistance with Actionable Suggestions for Evolving Scientific Research Projects](https://arxiv.org/abs/2604.08898)** (2026-04) - Proactive research assistant that monitors project documents and distills deep-research reports into timely actionable suggestions.
- **[Skilldex: A Package Manager and Registry for Agent Skill Packages with Hierarchical Scope-Based Distribution](https://arxiv.org/abs/2604.16911)** (2026-04) - Package manager and registry for agent skill packages with skillset bundles, scope-based distribution, and an MCP server.
- **[MemFactory: Unified Inference and Training Framework for Agent Memory](https://arxiv.org/abs/2603.29493)** (2026-03) - Unifies training, evaluation and inference for memory agents with plug-and-play extractors/updaters/retrievers and GRPO tuning.
- **[Memory as Ontology: A Constitutional Memory Architecture for Persistent Digital Citizens](https://arxiv.org/abs/2603.04740)** (2026-03) - Constitutional memory architecture for persistent digital identity with four-layer governance and replaceable model substrate.
- **[SuperLocalMemory V3: Information-Geometric Foundations for Zero-LLM Enterprise Agent Memory](https://arxiv.org/abs/2603.14588)** (2026-03) - Information-geometric framework unifying retrieval, lifecycle, and consistency for zero-LLM enterprise memory; +12.7% on LoCoMo.
- **[Hippocampus: An Efficient and Scalable Memory Module for Agentic AI](https://arxiv.org/abs/2602.13594)** (2026-02) - Binary-signature memory with dynamic wavelet matrix index; up to 31x lower retrieval latency on LoCoMo and LongMemEval.
- **[MemoPhishAgent: Memory-Augmented Multi-Modal LLM Agent for Phishing URL Detection](https://arxiv.org/abs/2602.21394)** (2026-02) - Multimodal phishing-URL detection agent using episodic memory of past reasoning trajectories; +13.6% recall over baselines.
- **[Chain-of-Memory: Lightweight Memory Construction with Dynamic Evolution for LLM Agents](https://arxiv.org/abs/2601.14287)** (2026-01) - Lightweight construction with dynamic memory-chain evolution; 7.5-10.4 point gains on LoCoMo/LongMemEval at ~2.7% token cost.
- **[Continuum Memory Architectures for Long-Horizon LLM Agents](https://arxiv.org/abs/2601.09913)** (2026-01) - Continuum memory architecture coordinating working, episodic, and semantic stores for long-horizon agent stability and recall.
- **[LLM-as-RNN: A Recurrent Language Model for Memory Updates and Sequence Prediction](https://arxiv.org/abs/2601.13352)** (2026-01) - Inference-only framework turning frozen LLMs into recurrent predictors with a natural-language memory state rewritten each step.
- **[MemoBrain: Executive Memory as an Agentic Brain for Reasoning](https://arxiv.org/abs/2601.08079)** (2026-01) - Executive memory co-pilot with trajectory folding and selective flush; outperforms baselines on GAIA and BrowseComp-Plus.
- **[SimpleMem: Efficient Lifelong Memory for LLM Agents](https://arxiv.org/abs/2601.02553)** (2026-01) - Semantic compression, recursive consolidation and adaptive retrieval; +26.4% F1 on LoCoMo with up to 30x fewer tokens.
- **[Hindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects](https://arxiv.org/abs/2512.12818)** (2025-12) - Four memory networks (facts, experiences, entity summaries, beliefs) with temporal priming retrieval; beats full-context models.
- **[Memory Bear AI: A Breakthrough from Memory to Cognition](https://arxiv.org/abs/2512.20651)** (2025-12) - Cognitive-science memory architecture (ACT-R, Ebbinghaus) with semantic pruning and self-reflection; ~90% token cuts, beats Mem0.
- **[Episodic Memory in Agentic Frameworks: Suggesting Next Steps in Workflow Creation](https://arxiv.org/abs/2511.17775)** (2025-11) - Episodic store of workflow traces used to retrieve similar histories and suggest next steps during agentic workflow creation.
- **[A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110)** (2025-10) - Zettelkasten-inspired agentic memory with self-linking and self-evolving notes for dynamic long-term memory organization.
- **[CAM: A Constructivist View of Agentic Memory for LLM-Based Reading Comprehension](https://arxiv.org/abs/2510.05520)** (2025-10, NeurIPS 2025) - Piaget-inspired memory with incremental overlapping clustering and prune-and-grow retrieval for long-document comprehension.
- **[Improving Code Localization with Repository Memory](https://arxiv.org/abs/2510.01003)** (2025-10) - Repository memory from commit history and linked issues improving code localization for software engineering agents on SWE-bench.
- **[LightMem: Lightweight and Efficient Memory-Augmented Generation](https://arxiv.org/abs/2510.18866)** (2025-10) - Atkinson-Shiffrin-inspired pipeline with sensory filtering, topic-aware short-term memory, and sleep-time updates; 100x fewer tokens.
- **[ToolMem: Enhancing Multimodal Agents with Learnable Tool Capability Memory](https://arxiv.org/abs/2510.06664)** (2025-10) - Evolving structured memory of what each tool is good or bad at, used to predict tool quality and pick tools for new tasks.
- **[Multiple Memory Systems for Enhancing the Long-term Memory of Agent](https://arxiv.org/abs/2508.15294)** (2025-08) - Cognitive-psychology design building keyword, perspective, episodic and semantic units; beats MemoryBank and A-Mem on LoCoMo.
- **[Nemori: Self-Organizing Agent Memory Inspired by Cognitive Science](https://arxiv.org/abs/2508.03341)** (2025-08) - Self-organizing memory with autonomous episode segmentation and predict-calibrate knowledge distillation; 88% fewer tokens used.
- **[H-MEM: Hierarchical Memory for High-Efficiency Long-Term Reasoning in LLM Agents](https://arxiv.org/abs/2507.22925)** (2025-07) - Four-level hierarchical memory with positional index encoding for layer-by-layer retrieval and feedback-driven weight updates.
- **[MIRIX: Multi-Agent Memory System for LLM-Based Agents](https://arxiv.org/abs/2507.07957)** (2025-07) - Multi-agent memory with six specialized components, active retrieval, and a meta memory manager; +35% over RAG on ScreenshotVQA.
- **[MemTool: Optimizing Short-Term Memory Management for Dynamic Tool Calling in LLM Agent Multi-Turn Conversations](https://arxiv.org/abs/2507.21428)** (2025-07) - Short-term memory for dynamic MCP tool sets across turns; autonomous mode reaches 90-94% tool-removal efficiency over 13 LLMs.
- **[MemOS: A Memory OS for AI System](https://arxiv.org/abs/2507.03724)** (2025-05) - Memory operating system treating memory as a schedulable resource, unifying explicit, activation, and parameter-level memory.
- **[Memory OS of AI Agent](https://aclanthology.org/2025.emnlp-main.1318.pdf)** (2025-05, EMNLP 2025) - MemoryOS: OS-inspired segment-page hierarchical memory with storage, updating, retrieval, and generation modules; +49% F1 on LoCoMo.
- **[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413)** (2025-04) - Production memory layer extracting and consolidating conversation facts; Mem0g variant adds graph-structured relational memory.
- **[MemInsight: Autonomous Memory Augmentation for LLM Agents](https://arxiv.org/abs/2503.21760)** (2025-03) - Autonomous attribute mining structures and filters salient interaction history for QA, recommendation and summarization.
- **[On the Structural Memory of LLM Agents](https://arxiv.org/abs/2412.15266)** (2024-12) - Empirical study of memory structures and retrieval methods; mixed structures prove most robust across tasks and noise.
- **[Human-inspired Episodic Memory for Infinite Context LLMs](https://arxiv.org/abs/2407.09450)** (2024-07, ICLR 2025) - EM-LLM segments token streams into episodic events via surprise and graph refinement; two-stage recall handles 10M-token contexts. [[code](https://github.com/em-llm/EM-LLM-model)]
- **[Memoro: Using Large Language Models to Realize a Concise Interface for Real-Time Memory Augmentation](https://dl.acm.org/doi/10.1145/3613904.3642450)** (2024-05, CHI 2024) - Wearable audio memory assistant with queryless proactive retrieval that boosts recall confidence with minimal device interaction.
- **[MemLLM: Finetuning LLMs to Use An Explicit Read-Write Memory](https://arxiv.org/abs/2404.11672)** (2024-04) - Finetunes LLMs to call read/write API functions over an explicit structured triple memory, improving factuality and interpretability.

### Graph and Temporal Memory

- **[TokenMizer: Graph-Structured Session Memory for Long-Horizon LLM Context Management](https://arxiv.org/abs/2606.06337)** (2026-06) - Models LLM session history as a typed knowledge graph serialized into compact resume blocks, improving recall at lower token cost.
- **[eMEM: A Hybrid Spatio-Temporal Memory System For Embodied Agents](https://arxiv.org/abs/2606.03374)** (2026-06) - Hybrid spatio-temporal graph memory for embodied agents searchable by meaning, space, and time; adds eMEM-Bench evaluation.
- **[HyperMem: Hypergraph Memory for Long-Term Conversations](https://arxiv.org/abs/2604.08256)** (2026-04) - Hypergraph memory with topic/event/fact layers and coarse-to-fine retrieval over higher-order relations; best results on LoCoMo.
- **[HyperRAG: Reasoning N-ary Facts over Hypergraphs for Retrieval Augmented Generation](https://arxiv.org/abs/2602.14470)** (2026-02, WWW 2026) - Replaces binary KGs with n-ary hypergraphs plus HyperRetriever and HyperMemory modules for multi-hop QA.
- **[MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents](https://arxiv.org/abs/2601.03236)** (2026-01) - Orthogonal semantic, temporal, causal and entity graphs with intent-aware traversal; beats A-Mem-class systems on LoCoMo.
- **[Membox: Weaving Topic Continuity into Long-Range Memory for LLM Agents](https://arxiv.org/abs/2601.03785)** (2026-01) - Topic-continuity memory boxes linked into long-range event timelines; up to 68% F1 gain on LoCoMo temporal reasoning vs Mem0.
- **[SYNAPSE: Empowering LLM Agents with Episodic-Semantic Memory via Spreading Activation](https://arxiv.org/abs/2601.02744)** (2026-01) - Episodic-semantic graph with spreading activation, lateral inhibition and temporal decay; SOTA multi-hop reasoning on LoCoMo.
- **[TiMem: Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents](https://arxiv.org/abs/2601.02845)** (2026-01) - Temporal memory tree consolidating dialogue into persona abstractions; 75.3 LoCoMo, 76.9 LongMemEval-S with 52% less context.
- **[From Experience to Strategy: Empowering LLM Agents with Trainable Graph Memory](https://arxiv.org/abs/2511.07800)** (2025-11) - Trainable graph-structured experience memory learning to weight and route past experiences for agent strategy formation.
- **[D-SMART: Enhancing LLM Dialogue Consistency via Dynamic Structured Memory And Reasoning Tree](https://arxiv.org/abs/2510.13363)** (2025-10) - Incrementally built OWL knowledge graph coupled with a reasoning tree; over 48% consistency improvement on MT-Bench-101.
- **[SGMem: Sentence Graph Memory for Long-Term Conversational Agents](https://arxiv.org/abs/2509.21212)** (2025-09) - Sentence-level graphs linking turns, rounds and sessions with multi-hop retrieval; gains on LongMemEval and LoCoMo.
- **[G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems](https://arxiv.org/abs/2506.07398)** (2025-06) - Three-tier insight/query/interaction graph memory for multi-agent systems; up to 20.9% higher success without framework changes.
- **[Memory-augmented Query Reconstruction for LLM-based Knowledge Graph Reasoning](https://aclanthology.org/2025.findings-acl.1234.pdf)** (2025-03, ACL 2025 Findings) - MemQ decouples reasoning from SPARQL generation via a memory bank of explanation-fragment pairs; best Hits@1 on WebQSP and CWQ.
- **[From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://arxiv.org/abs/2502.14802)** (2025-02, ICML 2025) - HippoRAG 2: KG with passage nodes, triple filtering and Personalized PageRank; improves factual, multi-hop and narrative QA.
- **[TReMu: Towards Neuro-Symbolic Temporal Reasoning for LLM-Agents with Memory in Multi-Session Dialogues](https://arxiv.org/abs/2502.01630)** (2025-02) - Neuro-symbolic framework with timeline-aware memory representations for temporal reasoning over multi-session dialogues.
- **[Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956)** (2025-01) - Memory layer powered by Graphiti temporal knowledge graph fusing chat and business data; beats MemGPT on DMR and LongMemEval.
- **[Towards Lifelong Dialogue Agents via Timeline-based Memory Management](https://aclanthology.org/2025.naacl-long.435.pdf)** (2024-06, NAACL 2025) - THEANINE: relation-aware memory graph with timeline-augmented generation for lifelong dialogue; TeaFarm counterfactual evaluation.
- **[HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://arxiv.org/abs/2405.14831)** (2024-05, NeurIPS 2024) - Hippocampal-index-inspired retrieval: LLM-built KG plus Personalized PageRank enables single-step multi-hop retrieval, up to +20%. [[code](https://github.com/OSU-NLP-Group/HippoRAG)]
- **[From Local to Global: A GraphRAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130)** (2024-04) - Entity KG with hierarchical Leiden communities and map-reduce summaries answers global questions over whole corpora. [[code](https://github.com/microsoft/graphrag)]

### Parametric Memory

- **[Learning to Forget Attention: Memory Consolidation for Adaptive Compute Reduction](https://arxiv.org/abs/2602.12204)** (2026-02) - Consolidation-aware router distills frequent episodic attention retrievals into parametric memory; 37.8x attention compute cut.
- **[Memory Retrieval in Transformers: Insights from The Encoding Specificity Principle](https://arxiv.org/abs/2601.20282)** (2026-01) - Maps transformer attention to encoding specificity: Q as retrieval context, K as memory index, V as content; finds retrieval neurons.
- **[S3-Attention: Attention-Aligned Endogenous Retrieval for Memory-Bounded Long-Context Inference](https://arxiv.org/abs/2601.17702)** (2026-01) - O(1)-GPU-memory long-context inference using SAE features and a CPU inverted index instead of KV cache, near full-context quality.
- **[Nested Learning: The Illusion of Deep Learning Architecture](https://arxiv.org/abs/2512.24695)** (2025-12) - Unifies optimizers and test-time-training layers as nested memory; HOPE combines Titans attention with self-modifying FFNs.
- **[Pretraining with Hierarchical Memories: Separating Long-Tail and Common Knowledge](https://arxiv.org/abs/2510.02375)** (2025-10) - Small anchor model fetches context-dependent parameter blocks from a memory bank; 160M model matches a 2x larger standard model.
- **[MLP Memory: A Retriever-Pretrained Memory for Large Language Models](https://arxiv.org/abs/2508.01832)** (2025-08) - MLP pretrained to imitate a kNN retriever compresses the datastore into differentiable memory; +12.3% QA, 2.5x faster than RAG.
- **[OpenUnlearning: Accelerating LLM Unlearning via Unified Benchmarking of Methods and Metrics](https://arxiv.org/abs/2506.12618)** (2025-06) - Unified framework integrating LLM unlearning algorithms and evaluation metrics for comparable, robust forgetting research.
- **[Pre-training Limited Memory Language Models with Internal and External Knowledge](https://arxiv.org/abs/2505.15962)** (2025-05) - Pretrains models to look up facts in an external database instead of memorizing, enabling instant updates and easy unlearning.
- **[Echo: A Large Language Model with Temporal Episodic Memory](https://arxiv.org/abs/2502.16090)** (2025-02) - LLM design with explicit temporal episodic memory for time-indexed events, improving recall of sequences and time dependencies.
- **[LM2: Large Memory Models](https://arxiv.org/abs/2502.06049)** (2025-02) - Decoder transformer with auxiliary gated cross-attention memory module improving multi-step reasoning and long contexts.
- **[M+: Extending MemoryLLM with Scalable Long-Term Memory](https://arxiv.org/abs/2502.00592)** (2025-02, ICML 2025) - Adds retriever-coupled long-term latent memory to MemoryLLM, greatly extending knowledge retention at similar GPU cost.
- **[MeMo: Towards Language Models with Associative Memory Mechanisms](https://arxiv.org/abs/2502.12851)** (2025-02) - Layered correlation-matrix architecture that explicitly memorizes token sequences, enabling one-shot learning and exact forgetting.
- **[Towards Effective Evaluation and Comparisons for LLM Unlearning Methods](https://openreview.net/forum?id=aLLuYpn83y)** (2025-02, ICLR 2025) - Unlearning-with-calibration evaluation framework; recommends extraction strength as the primary unlearning metric.
- **[Alternate Preference Optimization for Unlearning Factual Knowledge in Large Language Models](https://aclanthology.org/2025.coling-main.252.pdf)** (2025-01, COLING 2025) - AltPO pairs negative feedback on the forget set with plausible alternative responses, improving forget quality and utility.
- **[Titans: Learning to Memorize at Test Time](https://arxiv.org/abs/2501.00663)** (2025-01) - Neural long-term memory module that learns to memorize at test time, combined with attention for very large effective contexts.
- **[Memory Layers at Scale](https://arxiv.org/abs/2412.09764)** (2024-12) - Scales trainable key-value memory layers as sparse lookup capacity without extra FLOPs, improving factual tasks vs dense and MoE.
- **[Self-Updatable Large Language Models by Integrating Context into Model Parameters](https://arxiv.org/abs/2410.00487)** (2024-10, ICLR 2025) - SELF-PARAM distills context into parameters by minimizing KL to a context-conditioned teacher; zero extra storage.
- **[Memory3: Language Modeling with Explicit Memory](https://doi.org/10.4208/jml.240708)** (2024-09, Journal of Machine Learning) - LLM with explicit memory and a memory circuit theory, cutting training and inference cost via compressed external knowledge.
- **[ELDER: Enhancing Lifelong Model Editing with Mixture-of-LoRA](https://arxiv.org/abs/2408.11869)** (2024-08, AAAI 2025) - Lifelong model editing with mixture-of-LoRA routing and a deferral mechanism that preserves general capabilities.
- **[WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://arxiv.org/abs/2405.14768)** (2024-05, NeurIPS 2024) - Dual parametric memory: side memory holds edits, a router bridges to main memory, with knowledge sharding and merging.
- **[Larimar: Large Language Models with Episodic Memory Control](https://arxiv.org/abs/2403.11901)** (2024-03, ICML 2024) - Brain-inspired distributed episodic memory controller enabling one-shot knowledge updates and selective forgetting without retraining. [[code](https://github.com/IBM/larimar)]
- **[Online Adaptation of Language Models with a Memory of Amortized Contexts](https://arxiv.org/abs/2403.04317)** (2024-03, NeurIPS 2024) - Meta-learned amortization compresses new documents into PEFT modulations stored in a memory bank for online adaptation.
- **[MemoryLLM: Towards Self-Updatable Large Language Models](https://arxiv.org/abs/2402.04624)** (2024-02, ICML 2024) - Fixed-size latent memory pool inside the transformer supports continual self-update with slow, graceful forgetting. [[code](https://github.com/wangyu-ustc/MemoryLLM)]
- **[Towards Safer Large Language Models through Machine Unlearning](https://aclanthology.org/2024.findings-acl.107.pdf)** (2024-02, ACL 2024 Findings) - SKU: harmful-knowledge acquisition then negation removes harmful outputs while preserving utility on benign prompts.
- **[Compressed Context Memory for Online Language Model Interaction](https://arxiv.org/abs/2312.03414)** (2023-12, ICLR 2024) - Online compression of accumulating context via conditional LoRA; up to 5x memory reduction with preserved quality.
- **[Large Language Model Unlearning](https://arxiv.org/abs/2310.10683)** (2023-10, NeurIPS 2024) - Gradient-ascent unlearning with random-output loss removes harmful behaviors; early systematic study of LLM unlearning.
- **[Unlearn What You Want to Forget: Efficient Unlearning for LLMs](https://aclanthology.org/anthology-files/pdf/emnlp/2023.emnlp-main.738.pdf)** (2023-10, EMNLP 2023) - EUL removes specific user data with lightweight unlearning layers and fusion, avoiding full retraining.

### Retrieval-Centric Memory

- **[MemReranker: Reasoning-Aware Reranking for Agent Memory Retrieval](https://arxiv.org/abs/2605.06132)** (2026-05) - 0.6B/4B rerankers distilled from LLMs with calibrated scoring; SOTA on LoCoMo and LongMemEval at low inference latency.
- **[Storage Is Not Memory: A Retrieval-Centered Architecture for Agent Recall](https://arxiv.org/abs/2605.04897)** (2026-05) - True Memory: six-layer retrieval-centered architecture over verbatim events with novelty/salience/prediction-error encoding gate.
- **[SelRoute: Query-Type-Aware Routing for Long-Term Conversational Memory Retrieval](https://arxiv.org/abs/2604.02431)** (2026-04) - Routes queries to specialized retrieval pipelines; SOTA on LongMemEval_M with CPU-only inference and no LLM at query time.
- **[Diagnosing Retrieval vs. Utilization Bottlenecks in LLM Agent Memory](https://arxiv.org/abs/2603.02473)** (2026-03) - Cross-ablation of write/retrieve/utilize stages shows retrieval dominates performance and raw chunk storage remains strong.
- **[MemR3: Memory Retrieval via Reflective Reasoning for LLM Agents](https://arxiv.org/abs/2512.20237)** (2025-12) - Closed-loop retrieve/reflect/respond controller with an evidence-gap state tracker; improves LoCoMo across memory backends.
- **[ComoRAG: A Cognitive-Inspired Memory-Organized RAG for Stateful Long Narrative Reasoning](https://ojs.aaai.org/index.php/AAAI/article/view/40644)** (2025-11, AAAI 2026) - Dynamic memory workspace with a metacognitive regulation loop for stateful reasoning; beats baselines on NarrativeQA.
- **[WebWeaver: Structuring Web-Scale Evidence with Dynamic Outlines for Open-Ended Deep Research](https://arxiv.org/abs/2509.13312)** (2025-09) - Planner/writer dual agents with an evidence memory bank and dynamic outlines; SOTA on DeepResearch Bench.
- **[Conflict-Aware Soft Prompting for Retrieval-Augmented Generation](https://arxiv.org/abs/2508.15253)** (2025-08, EMNLP 2025) - CARE adds a context assessor and adversarial soft prompts to resolve context-memory conflicts in RAG.
- **[SynapticRAG: Enhancing Temporal Memory Retrieval in Large Language Models through Synaptic Mechanisms](https://aclanthology.org/2025.findings-acl.1048.pdf)** (2025-07, ACL 2025 Findings) - Temporal association triggers with synaptic propagation improve cross-session memory retrieval by up to 14.7%.
- **[MemoRAG: Boosting Long Context Processing with Global Memory-Enhanced Retrieval Augmentation](https://arxiv.org/abs/2409.05591)** (2024-09, WWW 2025) - Lightweight global memory model generates clues that guide retrieval for long-document QA and summarization.
- **[MemLong: Memory-Augmented Retrieval for Long Text Modeling](https://arxiv.org/abs/2408.16967)** (2024-08) - External chunk memory with controllable retrieval attention extends the effective context of decoder-only LMs.
- **[RULER: What's the Real Context Size of Your Long-Context Language Models?](https://arxiv.org/abs/2404.06654)** (2024-04, COLM 2024) - Synthetic evaluation beyond needle-in-a-haystack (multi-hop tracing, aggregation) exposing true effective context length. [[code](https://github.com/NVIDIA/RULER)]
- **[A Human-Inspired Reading Agent with Gist Memory of Very Long Contexts](https://arxiv.org/abs/2402.09727)** (2024-02, ICML 2024) - ReadAgent paginates episodes into gist memories with interactive lookup, extending effective context up to 20x.

### Consolidation, Reflection and Forgetting

- **[Continual Knowledge Updating in LLM Systems: Learning Through Multi-Timescale Memory Dynamics](https://arxiv.org/abs/2605.05097)** (2026-05) - Memini: directed associative graph memory with fast/slow edge dynamics (Benna-Fusi) for consolidation and selective forgetting.
- **[LightThinker++: From Reasoning Compression to Memory Management](https://arxiv.org/abs/2604.03679)** (2026-04) - Explicit adaptive memory management (commit/expand/fold) over gist-token thought compression for long-horizon reasoning.
- **[MEMENTO: Teaching LLMs to Manage Their Own Context](https://arxiv.org/abs/2604.09852)** (2026-04) - Summarizes reasoning blocks into dense mementos and continues from them, cutting context and KV cache; OpenMementos dataset.
- **[FadeMem: Biologically-Inspired Forgetting for Efficient Agent Memory](https://arxiv.org/abs/2601.18642)** (2026-01) - Ebbinghaus-style adaptive decay over a dual-layer memory; better multi-hop reasoning on LoCoMo with 45% less storage.
- **[Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models](https://arxiv.org/abs/2510.04618)** (2025-10) - ACE treats contexts as evolving playbooks updated by generation, reflection and curation; +10.6% on agent tasks with lower cost.
- **[MOOM: Maintenance, Organization and Optimization of Memory in Ultra-Long Role-Playing Dialogues](https://arxiv.org/abs/2509.11860)** (2025-09) - Dual-branch plot/character memory with competition-inhibition forgetting; releases ZH-4O 600-turn role-play dataset.
- **[Pre-Storage Reasoning for Episodic Memory: Shifting Inference Burden to Memory for Personalized Dialogue](https://arxiv.org/abs/2509.10852)** (2025-09) - PREMem moves reasoning into memory construction with cross-session links; small models match larger baselines on LongMemEval.
- **[ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://arxiv.org/abs/2509.25140)** (2025-09) - Distills successes and failures into reusable reasoning memories plus memory-aware test-time scaling; gains on WebArena, SWE-Bench.
- **[Livia: An Emotion-Aware AR Companion Powered by Modular AI Agents and Progressive Memory Compression](https://arxiv.org/abs/2509.05298)** (2025-08) - Emotion-aware AR companion with progressive memory compression (TBC, DIMF) retaining emotionally significant long-term context.
- **[How Memory Management Impacts LLM Agents: An Empirical Study of Experience-Following Behavior](https://arxiv.org/abs/2505.16067)** (2025-05) - Identifies experience-following behavior; selective insertion and deletion strategies curb error propagation in agent memory.
- **[Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory](https://arxiv.org/abs/2504.07952)** (2025-04) - Generator plus curator maintain an evolving external memory of verified strategies and code; large gains on AIME and Game of 24. [[code](https://github.com/suzgunmirac/dynamic-cheatsheet)]
- **[SAGE: Self-evolving Agents with Reflective and Memory-augmented Abilities](https://www.sciencedirect.com/science/article/abs/pii/S0925231225011427)** (2025-04) - Iterative reflection with Ebbinghaus-curve MemorySyntax for memory decay; up to 2.26x gains on AgentBench-style tasks.
- **[Sleep-time Compute: Beyond Inference Scaling at Test-time](https://arxiv.org/abs/2504.13171)** (2025-04) - Precomputes inferences about persistent context while idle, cutting test-time compute about 5x at matched accuracy on GSM variants. [[code](https://github.com/letta-ai/sleep-time-compute)]
- **[In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents](https://arxiv.org/abs/2503.08026)** (2025-03, ACL 2025) - Prospective topic-based reorganization plus retrospective RL retrieval refinement; over 10% accuracy gain on MSC and LongMemEval.

### Learned and RL-Trained Memory

- **[MemPO: Self-Memory Policy Optimization for Long-Horizon Agents](https://arxiv.org/abs/2603.00680)** (2026-03) - Credit-assignment-improved policy optimization for proactive memory summarize-and-filter; higher F1 at lower token cost.
- **[Memex(RL): Scaling Long-Horizon LLM Agents via Indexed Experience Memory](https://arxiv.org/abs/2603.04257)** (2026-03) - Indexed experience memory with RL-optimized read-write archiving so agents decide when to archive and retrieve, compressing context.
- **[Learning to Remember: End-to-End Training of Memory Agents for Long-Context Reasoning](https://arxiv.org/abs/2602.18493)** (2026-02) - Unified memory agent trained end-to-end with RL for dynamic state tracking; accuracy rises from 61.4% to 76.5%.
- **[MIRA: Memory-Integrated Reinforcement Learning Agent with Limited LLM Guidance](https://arxiv.org/abs/2602.17930)** (2026-02, ICLR 2026) - Structured memory graph built from limited offline/online LLM guidance improves RL sample efficiency and convergence.
- **[Memory-Based Advantage Shaping for LLM-Guided Reinforcement Learning](https://arxiv.org/abs/2602.17931)** (2026-02, AAAI 2026) - Memory graph and utility function shape RL advantages from LLM guidance, improving sample efficiency under sparse reward.
- **[Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents](https://arxiv.org/abs/2601.01885)** (2026-01) - AgeMem integrates LTM and STM management as tool actions via three-stage stepwise GRPO; beats LangMem and Mem0.
- **[AtomMem: Learnable Dynamic Agentic Memory with Atomic Memory Operation](https://arxiv.org/abs/2601.08323)** (2026-01) - Reframes memory management as learnable sequential decisions over atomic CRUD operations trained with GRPO.
- **[Fine-Mem: Fine-Grained Feedback Alignment for Long-Horizon Memory Management](https://arxiv.org/abs/2601.08435)** (2026-01) - Chunk-level step rewards and evidence-anchored attribution align RL with memory ops; beats baselines on MemoryAgentBench.
- **[MemBuilder: Reinforcing LLMs for Long-Term Memory Construction via Attributed Dense Rewards](https://arxiv.org/abs/2601.05488)** (2026-01) - Attributed dense-reward RL for memory construction; 4B model beats closed-source models on LoCoMo and LongMemEval.
- **[MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory](https://arxiv.org/abs/2601.03192)** (2026-01) - Runtime RL over episodic memory with Q-value utility updates lets frozen agents self-evolve; beats Memp and RAG on ALFWorld.
- **[MemEvolve: Meta-Evolution of Agent Memory Systems](https://arxiv.org/abs/2512.18746)** (2025-12) - Two-level framework learning memory extraction and the extraction method itself; SOTA on GAIA with Flash-Searcher.
- **[Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution](https://arxiv.org/abs/2512.06653)** (2025-12) - ReMe maintains an experience pool with acquisition, reuse and refinement; dynamic pools beat static on BFCL-V3 and AppWorld.
- **[MemSearcher: Training LLMs to Reason, Search and Manage Memory via End-to-End Reinforcement Learning](https://arxiv.org/abs/2511.02805)** (2025-11) - Multi-context GRPO trains agents to reason, search and maintain compact memory; strong gains especially for small models.
- **[Memory as Action: Autonomous Context Curation for Long-Horizon Agentic Tasks](https://arxiv.org/abs/2510.12635)** (2025-10) - Treats context curation as policy actions; dynamic context policy optimization handles trajectory breaks from memory edits.
- **[Mem-alpha: Learning Memory Construction via Reinforcement Learning](https://arxiv.org/abs/2509.25911)** (2025-09) - RL over core/episodic/semantic memory construction; trained on 30k-token contexts, generalizes beyond 400k tokens.
- **[MemGen: Weaving Generative Latent Memory for Self-Evolving Agents](https://arxiv.org/abs/2509.24704)** (2025-09) - Memory trigger and weaver modules generate latent memory tokens interleaved with reasoning for self-evolving agents.
- **[Memento: Fine-tuning LLM Agents without Fine-tuning LLMs](https://arxiv.org/abs/2508.16153)** (2025-08) - Memory-based online learning adapts agent behavior from case experience while keeping the base LLM frozen. [[code](https://github.com/Agent-on-the-Fly/Memento)]
- **[Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning](https://arxiv.org/abs/2508.19828)** (2025-08) - RL memory manager (ADD/UPDATE/DELETE) plus answer agent; beats baselines on LoCoMo, MSC, LongMemEval with 152 samples.
- **[Memp: Exploring Agent Procedural Memory](https://arxiv.org/abs/2508.06433)** (2025-08) - Build-retrieve-update loop for procedural memory; beats ReAct on TravelPlanner and ALFWorld and transfers across models.
- **[MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent](https://arxiv.org/abs/2507.02259)** (2025-07) - RL-trained streaming agent rewrites a fixed-size memory over chunks, scaling to effectively unbounded inputs at linear cost. [[code](https://github.com/BytedTsinghua-SIA/MemAgent)]
- **[MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents](https://arxiv.org/abs/2506.15841)** (2025-06) - End-to-end RL agents keep a constant-size shared internal state across turns, cutting memory while improving long-horizon tasks.

### Multi-Agent Memory

- **[CoMIC: Collaborative Memory and Insights Circulation for Long-Horizon LLM Agents in Cloud-Edge Systems](https://arxiv.org/abs/2606.00756)** (2026-05) - Cloud-edge collaborative memory with decentralized execution and centralized reflection to circulate reusable insights across agents.
- **[Cost and Accuracy of Long-Term Memory in Distributed Multi-Agent Systems Based on Large Language Models](https://arxiv.org/abs/2601.07978)** (2026-05) - Independent evaluation of long-term memory backends in multi-agent systems measuring accuracy, latency, resource use, and total cost.
- **[Bolzano: Case Studies in LLM-Assisted Mathematical Research](https://arxiv.org/abs/2604.16989)** (2026-04) - Multi-agent LLM system for math research with persistent cross-turn knowledge base coordinating proving and verification agents.
- **[MEMO: Memory-Augmented Model Context Optimization for Robust Multi-Turn Multi-Agent LLM Games](https://arxiv.org/abs/2603.09022)** (2026-03) - Self-play memory bank with CRUD insights and TrueSkill prompt evolution; GPT-4o-mini win rate 25.1% to 49.5% in text games.
- **[AMA: Adaptive Memory via Multi-Agent Collaboration](https://arxiv.org/abs/2601.20352)** (2026-01) - Constructor, retriever, judge and refresher agents manage multi-granularity memory; beats baselines on LoCoMo, 80% fewer tokens.
- **[E-mem: Multi-agent based Episodic Context Reconstruction for LLM Agent Memory](https://arxiv.org/abs/2601.21714)** (2026-01) - Master-assistant agents keep uncompressed contexts as memory nodes; SOTA on LoCoMo and HotpotQA with 70% token reduction.
- **[Intrinsic Memory Agents: Heterogeneous Multi-Agent LLM Systems through Structured Contextual Memory](https://arxiv.org/abs/2508.08997)** (2025-08) - Role-aligned structured per-agent memories updated from own outputs; +38.6% on PDDL planning with high token efficiency.
- **[RCR-Router: Efficient Role-Aware Context Routing for Multi-Agent LLM Systems with Structured Memory](https://arxiv.org/abs/2508.04903)** (2025-08) - Role- and stage-aware routing of memory subsets under token budgets; 25-47% token reduction on multi-hop QA.
- **[Memory Sharing for Large Language Model based Agents](https://arxiv.org/abs/2404.09982)** (2024-04) - Real-time pool of prompt-answer pairs shared among agents with retriever training for collective in-context learning.

### Multimodal Memory

- **[Deco: Extending Personal Physical Objects into Pervasive AI Companion through a Dual-Embodiment Framework](https://arxiv.org/abs/2605.03882)** (2026-05) - Dual-embodiment AR framework turning personal objects into AI companions with reciprocal memory to sustain emotional bonds.
- **[EpiAgent: An Agent-Centric System for Ancient Inscription Restoration](https://arxiv.org/abs/2604.09367)** (2026-04) - Agent for ancient inscription restoration using an Observe-Conceive-Execute-Reevaluate loop with historical experience memory.
- **[Mosaic: Cross-Modal Clustering for Efficient Video Understanding](https://arxiv.org/abs/2604.10060)** (2026-04) - Cross-modal clustering over VLM KV caches as the unit of cache organization for long-video inference; up to 1.38x speedups.
- **[OMNI-SIMPLEMEM: Autoresearch-Guided Discovery of Lifelong Multimodal Agent Memory](https://arxiv.org/abs/2604.00131)** (2026-04) - Multimodal memory with selective ingestion and pyramid retrieval, discovered by an autonomous research pipeline; SOTA LoCoMo.
- **[M2A: Multimodal Memory Agent with Dual-Layer Hybrid Memory for Long-Term Personalized Interactions](https://arxiv.org/abs/2602.07624)** (2026-02) - Dual-layer hybrid multimodal memory linking raw logs to semantic observations via evidence IDs with tri-path retrieval.
- **[MMA: Multimodal Memory Agent](https://arxiv.org/abs/2602.16493)** (2026-02) - Multimodal memory agent assigning dynamic reliability scores to retrieved items; MMA-Bench reveals a visual reassurance effect.
- **[TeleMem: Building Long-Term and Multimodal Memory for Agentic AI](https://arxiv.org/abs/2601.06037)** (2026-01) - Narrative-grounded writing pipeline plus ReAct video reasoning; +19% accuracy over Mem0 with 43% fewer tokens on ZH-4O.
- **[MemVerse: Multimodal Memory for Lifelong Learning Agents](https://arxiv.org/abs/2512.03627)** (2025-12) - Pairs retrieval-based long-term store with parametric fast memory and periodic distillation for lifelong multimodal agents.
- **[Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory](https://arxiv.org/abs/2508.09736)** (2025-10) - M3-Agent builds entity-centric episodic and semantic memory from continuous video and audio, RL-trained; introduces M3-Bench.
- **[MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation](https://arxiv.org/abs/2508.19236)** (2025-08) - Perceptual-cognitive memory bank inspired by dual-memory systems raises success on long-horizon robot manipulation.
- **[Context as Memory: Scene-Consistent Interactive Long Video Generation with Memory Retrieval](https://arxiv.org/abs/2506.03141)** (2025-06) - Uses retrieved historical context frames as memory for scene-consistent interactive long video generation.
- **[Ella: Embodied Social Agents with Lifelong Memory](https://arxiv.org/abs/2506.24019)** (2025-06) - Embodied social agent with name-centric semantic and spatiotemporal episodic memory for lifelong learning in a 3D open world.
- **[Towards General Continuous Memory for Vision-Language Models](https://arxiv.org/abs/2505.17670)** (2025-05) - CoMEM encodes multimodal knowledge into compact continuous embeddings via the VLM plus a Q-Former; 1.2% trainable params.
- **[Embodied VideoAgent: Persistent Memory from Egocentric Videos and Embodied Sensors Enables Dynamic Scene Understanding](https://arxiv.org/abs/2501.00358)** (2025-01) - Builds persistent scene memory from egocentric video plus depth and pose with VLM-driven object state tracking; SOTA on OpenEQA.

### Personalization and User Modeling

- **[Hierarchical Long-Term Semantic Memory for LinkedIn's Hiring Agent](https://arxiv.org/abs/2604.26197)** (2026-05) - Production hierarchical semantic memory for LinkedIn's hiring agent extracting signals from behavioral data under privacy constraints.
- **[PSI: Shared State as the Missing Layer for Coherent AI-Generated Instruments in Personal AI Agents](https://arxiv.org/abs/2604.08529)** (2026-04) - Shared-state layer connecting generated personal AI modules via a personal context bus with writeback for cross-module reasoning.
- **[TSUBASA: Improving Long-Horizon Personalization via Evolving Memory and Self-Learning with Context Distillation](https://arxiv.org/abs/2604.07894)** (2026-04) - Dynamic memory evolution plus context-distilled self-learning; outperforms Mem0 on long-horizon personalization benchmarks.
- **[Structured Distillation for Personalized Agent Memory: 11x Token Reduction with Retrieval Preservation](https://arxiv.org/abs/2603.13017)** (2026-03) - Distills interactions into structured composites: 11x token compression keeps 96% retrieval MRR; BM25 degrades, vectors do not.
- **[O-Mem: Omni Memory System for Personalized, Long Horizon, Self-Evolving Agents](https://arxiv.org/abs/2511.13593)** (2025-12) - Active user-profiling memory with hierarchical retrieval of persona attributes and topics; SOTA on LoCoMo and PERSONAMEM.
- **[PRINCIPLES: Synthetic Strategy Memory for Proactive Dialogue Agents](https://aclanthology.org/2025.findings-emnlp.1164.pdf)** (2025-09, EMNLP 2025 Findings) - Strategy-principle memory mined from offline self-play guides proactive dialogue; better success in support and persuasion.
- **[On Memory Construction and Retrieval for Personalized Conversational Agents](https://arxiv.org/abs/2502.05589)** (2025-02, ICLR 2025) - SeCom builds segment-level memory with LLMLingua-2 compression denoising; beats turn and session granularity on LoCoMo.

### Memory Security and Privacy

- **[Honest Lying: Understanding Memory Confabulation in Reflexive Agents](https://arxiv.org/abs/2605.29463)** (2026-05) - Shows reflexive agents store false self-explanations as memory; trajectory-level failure extraction curbs confabulation.
- **[MAGE: Safeguarding LLM Agents against Long-Horizon Threats via Shadow Memory](https://arxiv.org/abs/2605.03228)** (2026-05) - Shadow-stack-inspired safety memory checks pending actions against distilled security context across long trajectories.
- **[ADAM: A Systematic Data Extraction Attack on Agent Memory via Adaptive Querying](https://arxiv.org/abs/2604.09747)** (2026-04) - Entropy-guided adaptive querying extracts agent memory contents with up to 100% attack success in some settings.
- **[On Safety Risks in Experience-Driven Self-Evolving Agents](https://arxiv.org/abs/2604.16968)** (2026-04) - Benign-task experience can erode refusal behavior in self-evolving agents, exposing a safety-utility trade-off in memory.
- **[Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents](https://arxiv.org/abs/2604.02623)** (2026-04) - eTAMP poisons web-agent memory via environmental observations; task frustration amplifies susceptibility up to 8x.
- **[Visual Inception: Compromising Long-term Planning in Agentic Recommenders via Multimodal Memory Poisoning](https://arxiv.org/abs/2604.16966)** (2026-04) - Image-embedded triggers poison long-term memory of agentic recommenders; CognitiveGuard dual-process defense reduces risk.
- **[ER-MIA: Black-Box Adversarial Memory Injection Attacks on Long-Term Memory-Augmented Large Language Models](https://arxiv.org/abs/2602.15344)** (2026-02) - Automated black-box memory injection via normal interactions corrupts reasoning of long-term-memory LLMs.
- **[MemPot: Defending Against Memory Extraction Attack with Optimized Honeypots](https://arxiv.org/abs/2602.07517)** (2026-02) - Optimized honeypot documents plus SPRT detection defend memory extraction with near-perfect accuracy and zero added latency.
- **[Position: Stateless Yet Not Forgetful: Implicit Memory as a Hidden Channel in LLMs](https://arxiv.org/abs/2602.08563)** (2026-02) - LLMs encode state in their own outputs as a hidden cross-session channel; demonstrates time-bomb temporal backdoors.
- **[Zombie Agents: Persistent Control of Self-Evolving LLM Agents via Self-Reinforcing Injections](https://arxiv.org/abs/2602.15654)** (2026-02) - Two-stage black-box self-reinforcing injections persistently control self-evolving agents; prompt filters are insufficient.
- **[Topology Matters: Measuring Memory Leakage in Multi-Agent LLMs](https://arxiv.org/abs/2512.04668)** (2025-12) - MAMA framework measures cross-agent PII leakage; denser topology, shorter paths and central targets raise leakage risk.

## Benchmarks and Evaluation

### Conversational and Multi-Session

| Benchmark | Paper | Measures |
|---|---|---|
| [AMemGym](https://arxiv.org/abs/2603.01966) | [2603.01966](https://arxiv.org/abs/2603.01966) | Interactive environment for online memory-policy evaluation with synthetic user profiles and state-evolution trajectories |
| [DialSim](https://arxiv.org/abs/2406.13144) | [2406.13144](https://arxiv.org/abs/2406.13144) | Real-time dialogue simulator over long multi-party TV-show conversations testing long-term conversational memory |
| [EvolMem](https://arxiv.org/abs/2601.03543) | [2601.03543](https://arxiv.org/abs/2601.03543) | Cognitive-driven multi-session dialogue memory covering declarative and non-declarative (habituation) memory types |
| [LOCCO](https://aclanthology.org/2025.findings-acl.1014.pdf) | - | Long-order chronological conversations quantifying how LLM memory of dialogue history degrades over time |
| [LoCoMo](https://github.com/snap-research/locomo) | [2402.17753](https://arxiv.org/abs/2402.17753) | Very long-term multi-session conversational memory: QA, event summarization, multimodal dialogue generation |
| [LoCoMo-Plus](https://arxiv.org/abs/2602.10715) | [2602.10715](https://arxiv.org/abs/2602.10715) | Cognitive memory beyond facts: applying latent user goals/values under cue-trigger semantic disconnect |
| [LongMemEval](https://github.com/xiaowu0162/LongMemEval) | [2410.10813](https://arxiv.org/abs/2410.10813) | Five core long-term memory abilities of chat assistants under a unified indexing-retrieval-reading framework |
| [MADial-Bench](https://arxiv.org/abs/2409.15240) | [2409.15240](https://arxiv.org/abs/2409.15240) | Memory-augmented dialogue generation with cognitive-science-based memory recall and recognition metrics |
| [Mem-Gallery](https://arxiv.org/abs/2601.03515) | [2601.03515](https://arxiv.org/abs/2601.03515) | Multimodal multi-session conversations; memory extraction/adaptation, reasoning, and knowledge management across 13 systems |
| [MemEmo](https://arxiv.org/abs/2602.23944) | [2602.23944](https://arxiv.org/abs/2602.23944) | Emotional memory in agents: emotion extraction, emotional memory updating, emotion-aware QA (HLME dataset) |
| [RealMem](https://arxiv.org/abs/2601.06966) | [2601.06966](https://arxiv.org/abs/2601.06966) | 2,000+ cross-session project-oriented dialogues in 11 scenarios with evolving goals, states, and temporal reasoning |
| [RefMem-Bench](https://arxiv.org/abs/2606.01223) | [2606.01223](https://arxiv.org/abs/2606.01223) | Reflective memory in long-horizon dialogue: annotated QA requiring synthesis of fragmented cues, not explicit recall |
| [RHELM](https://arxiv.org/abs/2605.31086) | [2605.31086](https://arxiv.org/abs/2605.31086) | One-year virtual life trajectories of 10 personas (500K-1M tokens) with heterogeneous sources; 7 question types |
| [StoryBench](https://arxiv.org/abs/2506.13356) | [2506.13356](https://arxiv.org/abs/2506.13356) | Long-term memory evaluation through multi-turn interactive story settings requiring sustained recall |
| [StratMem-Bench](https://arxiv.org/abs/2604.26243) | [2604.26243](https://arxiv.org/abs/2604.26243) | 657 virtual-character dialogues with mandatory/auxiliary/irrelevant memory pools; strategic memory-use metrics |

### Long-Context

| Benchmark | Paper | Measures |
|---|---|---|
| [AgentLongBench](https://arxiv.org/abs/2601.20730) | [2601.20730](https://arxiv.org/abs/2601.20730) | Controllable long-context agent eval via environment rollouts from 32K to 4M tokens using lateral thinking puzzles |
| [BABILong](https://github.com/booydar/babilong) | [2406.10149](https://arxiv.org/abs/2406.10149) | Needle-in-haystack reasoning: bAbI tasks embedded in distractor text scaling to millions of tokens |
| [HotpotQA](https://hotpotqa.github.io) | [1809.09600](https://arxiv.org/abs/1809.09600) | 113K Wikipedia multi-hop QA pairs with supporting-fact supervision; common substrate for memory retrieval evals |
| [LongBench](https://github.com/THUDM/LongBench) | [2308.14508](https://arxiv.org/abs/2308.14508) | Bilingual multitask suite: 21 datasets over single/multi-doc QA, summarization, few-shot, synthetic, code tasks |
| [LongBench v2](https://longbench2.github.io) | [2412.15204](https://arxiv.org/abs/2412.15204) | 503 multiple-choice questions requiring deep understanding and reasoning over realistic long-context multitasks |
| [LongGenBench](https://arxiv.org/abs/2409.02076) | [2409.02076](https://arxiv.org/abs/2409.02076) | Long-form generation following complex instructions (e.g. diary writing, menu design) in long-context LLMs |
| [Minerva](https://arxiv.org/abs/2502.03358) | [2502.03358](https://arxiv.org/abs/2502.03358) | Programmable memory test tasks quantifying retrieval, reasoning, and state tracking over model context |
| [RULER](https://github.com/NVIDIA/RULER) | [2404.06654](https://arxiv.org/abs/2404.06654) | Synthetic retrieval, multi-hop tracing, aggregation, and QA tasks probing models' effective context length |
| [SCBench](https://arxiv.org/abs/2412.10319) | [2412.10319](https://arxiv.org/abs/2412.10319) | KV-cache lifecycle (generation, compression, retrieval, loading) in shared-context multi-turn settings |

### Personalization

| Benchmark | Paper | Measures |
|---|---|---|
| [ATM-Bench](https://arxiv.org/abs/2603.01990) | [2603.01990](https://arxiv.org/abs/2603.01990) | Long-term personalized referential memory QA over four years of multimodal multi-source private data |
| [IMPLEXCONV](https://aclanthology.org/2025.emnlp-main.580.pdf) | - | 2,500 examples of implicit reasoning over subtle semantic relationships in multi-session personalized dialogue |
| [KnowMe-Bench](https://arxiv.org/abs/2601.04745) | [2601.04745](https://arxiv.org/abs/2601.04745) | Person understanding from 4.7M-token autobiographical narratives; 3-tier eval from facts to motivations |
| [KnowU-Bench](https://arxiv.org/abs/2604.08455) | [2604.08455](https://arxiv.org/abs/2604.08455) | Online Android benchmark for proactive personalized agents inferring hidden preferences from behavioral traces |
| [LaMP](https://lamp-benchmark.github.io) | [2304.11406](https://arxiv.org/abs/2304.11406) | Seven personalized text classification and generation subtasks using user history and retrieval augmentation |
| [MemDaily](https://arxiv.org/abs/2409.20163) | [2409.20163](https://arxiv.org/abs/2409.20163) | Daily-life QA trajectories from the MemSim Bayesian simulator for evaluating personal assistant memory |
| [MEMENTO](https://arxiv.org/abs/2505.16348) | [2505.16348](https://arxiv.org/abs/2505.16348) | Two-stage eval of embodied agents using memory of object semantics and user behavioral patterns |
| [PersonaBench](https://aclanthology.org/2025.findings-acl.49.pdf) | - | Understanding personal information by accessing synthetic private user data; RAG-focused evaluation |
| [PersonaFeedback](https://arxiv.org/abs/2506.12915) | [2506.12915](https://arxiv.org/abs/2506.12915) | Large-scale human-annotated benchmark for personalized response generation given user personas |
| [PersonaMem](https://arxiv.org/abs/2504.14225) | [2504.14225](https://arxiv.org/abs/2504.14225) | Dynamic user profiling and personalized response generation as user profiles evolve across sessions |
| [PersonaMem-v2](https://arxiv.org/abs/2512.06688) | [2512.06688](https://arxiv.org/abs/2512.06688) | 1,000 personas, 300+ scenarios, 20K+ implicit preferences in up to 128K-token interactions; frontier LLMs 37-48% |
| [PrefEval](https://github.com/amazon-science/PrefEval) | [2502.09597](https://arxiv.org/abs/2502.09597) | 3,000 preference-query pairs over 20 topics: inferring, remembering, and following user preferences in long dialogue |
| [RealPref](https://arxiv.org/abs/2603.04191) | [2603.04191](https://arxiv.org/abs/2603.04191) | 100 user profiles testing long-horizon preference following from explicit to implicit expressions |
| [RPEval](https://arxiv.org/abs/2601.16621) | [2601.16621](https://arxiv.org/abs/2601.16621) | Rational preference utilization: intent-reasoning dataset and multi-granularity protocol exposing filter bubbles |

### Agentic

| Benchmark | Paper | Measures |
|---|---|---|
| [LifelongAgentBench](https://arxiv.org/abs/2505.11942) | [2505.11942](https://arxiv.org/abs/2505.11942) | Lifelong learning of LLM agents accumulating experience across sequential tasks in interactive environments |
| [Mem2ActBench](https://arxiv.org/abs/2601.19935) | [2601.19935](https://arxiv.org/abs/2601.19935) | 400 memory-dependent tool-use tasks from 2,029 sessions; tests grounding tool parameters in long-term memory |
| [MemBench](https://aclanthology.org/2025.findings-acl.989.pdf) | - | Factual and reflective memory of LLM agents with accuracy, efficiency, and capacity metrics |
| [MemHome](https://arxiv.org/abs/2604.10110) | [2604.10110](https://arxiv.org/abs/2604.10110) | Memory-driven smart home control from real interaction logs: adding, updating, deleting, using memories |
| [MemoryAgentBench](https://arxiv.org/abs/2507.05257) | [2507.05257](https://arxiv.org/abs/2507.05257) | Four memory-agent capabilities: accurate retrieval, test-time learning, long-range understanding, conflict resolution |
| [MemoryArena](https://arxiv.org/abs/2602.16313) | [2602.16313](https://arxiv.org/abs/2602.16313) | Interdependent multi-session agentic tasks (web navigation, planning, search) jointly evaluating memory and action |
| [MemoryBench](https://arxiv.org/abs/2510.17281) | [2510.17281](https://arxiv.org/abs/2510.17281) | Continual learning from simulated service-time user feedback across domains, languages, and task types |
| [MemoryRewardBench](https://arxiv.org/abs/2601.11969) | [2601.11969](https://arxiv.org/abs/2601.11969) | Reward models judged on assessing long-term memory management: 10 settings, 8K-128K token contexts |
| [Momento](https://arxiv.org/abs/2606.00832) | [2606.00832](https://arxiv.org/abs/2606.00832) | Tool-mediated multi-session tasks with persistent memory, temporal dependencies, and changing user goals |
| [MT-Mind2Web](https://arxiv.org/abs/2402.15057) | [2402.15057](https://arxiv.org/abs/2402.15057) | Multi-turn conversational web navigation requiring retention of instructions across turns (Mind2Web extension) |
| [StreamBench](https://arxiv.org/abs/2406.08747) | [2406.08747](https://arxiv.org/abs/2406.08747) | Continuous improvement of language agents over streaming input-feedback sequences across downstream tasks |
| [WebArena](https://webarena.dev) | [2307.13854](https://arxiv.org/abs/2307.13854) | Self-hosted realistic web environments (e-commerce, forum, gitlab, CMS) for long-horizon autonomous agent tasks |
| [WebChoreArena](https://arxiv.org/abs/2506.01952) | [2506.01952](https://arxiv.org/abs/2506.01952) | Tedious memory-intensive web tasks extending WebArena, stressing cross-page information retention |
| [WorldMemArena](https://arxiv.org/abs/2605.29341) | [2605.29341](https://arxiv.org/abs/2605.29341) | Multimodal agent memory via action-world interaction loop: writing, maintenance, retrieval, and use |

### Episodic

| Benchmark | Paper | Measures |
|---|---|---|
| [CloneMem](https://arxiv.org/abs/2601.07023) | [2601.07023](https://arxiv.org/abs/2601.07023) | AI-clone memory over 1-3 years of non-conversational traces (diaries, social media, emails); state tracking |
| [EGOSTREAM](https://arxiv.org/abs/2605.31557) | [2605.31557](https://arxiv.org/abs/2605.31557) | Streaming episodic memory in egocentric vision; diagnostic questions across cognitive dimensions for MLLMs |
| [Episodic Memory Benchmark](https://arxiv.org/abs/2501.13121) | [2501.13121](https://arxiv.org/abs/2501.13121) | Episodic memory generation and evaluation tasks for LLMs with dedicated protocols for event recall |
| [LifeBench](https://arxiv.org/abs/2603.03781) | [2603.03781](https://arxiv.org/abs/2603.03781) | Long-horizon multi-source life events; integrative reasoning over fragmented digital traces (SOTA ~55%) |
| [PerLTQA](https://aclanthology.org/2024.sighan-1.18.pdf) | - | 8,593 questions over 30 personas combining semantic and episodic memory: classification, retrieval, synthesis |
| [STALE](https://arxiv.org/abs/2605.06527) | [2605.06527](https://arxiv.org/abs/2605.06527) | 400 expert-validated implicit conflict scenarios testing detection of invalidated memories without explicit negation |
| [SubtleMemory](https://arxiv.org/abs/2606.05761) | [2606.05761](https://arxiv.org/abs/2606.05761) | Fine-grained relational memory discrimination: complementary/divergent/contradictory variants in long agent histories |
| [SuperMemory-VQA](https://arxiv.org/abs/2606.00825) | [2606.00825](https://arxiv.org/abs/2606.00825) | Egocentric daily-activity VQA for long-horizon visual memory: object, location, intention, and scene recall |

### Safety and Hallucination

| Benchmark | Paper | Measures |
|---|---|---|
| [AgentLAB](https://arxiv.org/abs/2602.16901) | [2602.16901](https://arxiv.org/abs/2602.16901) | Long-horizon attacks incl. memory poisoning: 5 attack types, 28 agent environments, 644 security test cases |
| [HaluMem](https://arxiv.org/abs/2511.03506) | [2511.03506](https://arxiv.org/abs/2511.03506) | Memory hallucination evaluation across memory extraction, updating, and question-answering operations |
| [MPBench](https://arxiv.org/abs/2606.04329) | [2606.04329](https://arxiv.org/abs/2606.04329) | Memory poisoning attacks on LLM agents across write channels, structural vulnerabilities, and attack categories |
| [PersistBench](https://arxiv.org/abs/2602.01146) | [2602.01146](https://arxiv.org/abs/2602.01146) | Memory retention safety: cross-domain leakage and memory-induced sycophancy as memory-specific failure modes |
| [RBI-Eval](https://arxiv.org/abs/2606.06055) | [2606.06055](https://arxiv.org/abs/2606.06055) | Probes when sensitive memories should stay unused, comparing behavior with and without sensitive memory access |

## Guides, Talks and Courses

### Engineering Posts

- [State of AI Agent Memory 2026](https://mem0.ai/blog/state-of-ai-agent-memory-2026) - Mem0, 2026. Vendor view of benchmarks, architectures and production gaps; read with the usual salt.
- [Context Engineering for Agents](https://blog.langchain.com/context-engineering-for-agents/) - LangChain, 2025. Write, select, compress, isolate: a four-operation view of agent context and memory.
- [Context Engineering for AI Agents: Lessons from Building Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Manus) - Manus, 2025. KV-cache-aware design, file-system-as-memory and attention manipulation lessons from a production agent.
- [Context Rot: How Increasing Input Tokens Impacts LLM Performance](https://research.trychroma.com/context-rot) - Chroma, 2025. Empirical study showing degradation with input length, motivating retrieval and memory over context stuffing.
- [Don't Build Multi-Agents](https://cognition.ai/blog/dont-build-multi-agents) - Cognition, 2025. Context and memory sharing arguments against naive multi-agent architectures.
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) - Anthropic, 2025. Compaction, structured note-taking and sub-agent contexts as memory primitives in production agents.
- [How Long Contexts Fail](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html) - Drew Breunig, 2025. Context poisoning, distraction, confusion and clash: failure modes that motivate external memory.
- [How to Fix Your Context](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html) - Drew Breunig, 2025. RAG, tool loadout, quarantine, pruning, summarization and offloading as context repair tactics.
- [LangMem SDK launch](https://blog.langchain.dev/langmem-sdk-launch/) - LangChain, 2025. Design rationale for LangChain's long-term memory SDK.
- [Managing context on the Claude Developer Platform](https://www.anthropic.com/news/context-management) - Anthropic, 2025. Introduces the memory tool and context editing in the Claude API.
- [The New Skill in AI is Not Prompting, It's Context Engineering](https://www.philschmid.de/context-engineering) - Phil Schmid, 2025. Widely shared framing of context engineering with memory as a first-class component.
- [Memory for Agents](https://blog.langchain.dev/memory-for-agents/) - LangChain, 2024. Procedural, semantic and episodic memory framing for agent builders.
- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) - Lilian Weng, 2023. Canonical agent overview whose memory section defined the sensory, short-term and long-term mapping.

### Courses

- [Long-Term Agentic Memory with LangGraph](https://www.deeplearning.ai/short-courses/long-term-agentic-memory-with-langgraph/) - DeepLearning.AI, 2025. Hands-on course building semantic, episodic and procedural memory into a LangGraph agent.
- [LLMs as Operating Systems: Agent Memory](https://www.deeplearning.ai/short-courses/llms-as-operating-systems-agent-memory/) - DeepLearning.AI, 2024. Short course by the MemGPT authors on self-editing memory and the memory-as-OS pattern.

### Communities

- [r/AIMemory](https://www.reddit.com/r/AIMemory/) - Reddit, 2024. Subreddit dedicated to AI memory systems and persistence.

### Related Lists

- [Agent-Memory-Paper-List](https://github.com/Shichun-Liu/Agent-Memory-Paper-List) - GitHub, 2025. Companion paper list to the survey Memory in the Age of AI Agents.
- [Awesome-Context-Engineering](https://github.com/Meirtz/Awesome-Context-Engineering) - GitHub, 2025. Survey companion for context engineering, the discipline memory engineering sits inside.
- [DEEP-PolyU/Awesome-GraphMemory](https://github.com/DEEP-PolyU/Awesome-GraphMemory) - GitHub, 2025. Survey companion focused on graph-based agent memory.
- [IAAR-Shanghai/Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory) - GitHub, 2025. Large bilingual paper feed with per-paper summaries; strongest raw paper coverage.
- [Survey_Memory_in_AI](https://github.com/Elvin-Yiming-Du/Survey_Memory_in_AI) - GitHub, 2025. Companion list to Rethinking Memory in AI (arXiv 2505.00675), organized by memory operations.
- [TeleAI-UAGI/Awesome-Agent-Memory](https://github.com/TeleAI-UAGI/Awesome-Agent-Memory) - GitHub, 2025. Systems, benchmarks and papers on memory for LLMs and MLLMs.
- [TsinghuaC3I/Awesome-Memory-for-Agents](https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents) - GitHub, 2025. Paper collection split by short-term versus long-term persistence.
- [Awesome-LLM-Long-Context-Modeling](https://github.com/Xnhyacinth/Awesome-LLM-Long-Context-Modeling) - GitHub, 2024. KV cache, compression and length extrapolation: the architectural side of memory.
- [LLM_Agent_Memory_Survey](https://github.com/nuster1128/LLM_Agent_Memory_Survey) - GitHub, 2024. Companion list to the canonical agent-memory survey (arXiv 2404.13501).
- [topoteretes/awesome-ai-memory](https://github.com/topoteretes/awesome-ai-memory) - GitHub, 2024. Vendor-maintained product table from the cognee team.

## Contributing

Add one YAML entry under `data/`, run `python3 scripts/generate.py`, open a PR.
Inclusion criteria and schema live in [CONTRIBUTING.md](CONTRIBUTING.md).
Self-promotion is welcome when the project meets the criteria; the criteria are
the same for everyone.

## License

[CC0 1.0](LICENSE). Do whatever you want with this.
