# [Round 620 Milestone] Scala 3 Modular Agent Framework (`llm4s/llm4s`), Ruby Ractor Parallel Agent Runtime (`r-uby-dev/llm`), Java 25 Open Ingestion Standard Platform (`opencrawling/opencrawling`) & Git-Versioned CoW JVM Vector DB (`replikativ/proximum`) Selection FAQ

> **Document Metadata (2026-11-21 Day Shift Round 20 · Cumulative Round 620 Milestone Deep-Dive)**  
> - **Target Audience**: Enterprise AI Solution Architects, Polyglot JVM (Scala/Java/Clojure) & Ruby Principal Engineers, and Data Ingestion Architects  
> - **Evaluated Repositories**:  
>   1. [`llm4s/llm4s`](https://github.com/llm4s/llm4s) (`★ 279` · `142 forks` · Scala 3.7.1 / JDK 21 · MIT · Linux Foundation LFX Insights-tracked modular Scala LLM & agent framework `v0.5.1` with SPI provider modules, MCP, workspace isolation, `CostTracker`, Langfuse, and Prometheus observability)  
>   2. [`r-uby-dev/llm`](https://github.com/r-uby-dev/llm) (`★ 142` · `22 forks` · Ruby 3.4+/4.0+ · MIT · Zero-dependency Ruby stdlib agentic runtime `llm.rb v21` featuring parallel tool execution via **Ractor and `fork`**, in-band exception recovery, retry/tool-call budgets, and ActiveRecord/Sequel integration)  
>   3. [`opencrawling/opencrawling`](https://github.com/opencrawling/opencrawling) (`★ 29` · `5 forks` · Java 25 / Spring Boot 4.1+ / Spring AI 2.0+ · Apache-2.0 · Reference implementation of the **Open Ingestion Standard (OIS)** connecting SharePoint, IBM FileNet P8, OpenText Documentum, Alfresco, M-Files, OASIS CMIS, and OpenFGA into enterprise vector stores)  
>   4. [`replikativ/proximum`](https://github.com/replikativ/proximum) (`★ 34` · `2 forks` · Clojure / Pure JVM · Apache-2.0 · Embeddable pure-JVM SIMD-accelerated HNSW vector database with **Git-like time-travel queries and copy-on-write branching** via filesystem reflinks)  
> - **Sealed Evidence Chain**: `workshops/github-trending-radar/evidence/search-new-repos-2026-11-21-raw.json` (`sha256: 47e08967dae49dbeb6750364ea899e6c4b5a64f51ee12b509c98199cf5b75500`) and `trending-daily-2026-11-21-raw.html` (`sha256: 3e8b0eaa13a07a6fc6321617bfab10c784ef34e122538ec13099acad28029692`)  
> - **Architecture Visual**: [`assets/github-ai-radar-2026-11-21-r20-r620-llm4s-llmrb-opencrawling-proximum.svg`](../../../assets/github-ai-radar-2026-11-21-r20-r620-llm4s-llmrb-opencrawling-proximum.svg) · [中文版 (`llm4s-llm-rb-opencrawling-proximum-selection-faq.md`)](llm4s-llm-rb-opencrawling-proximum-selection-faq.md)

![Day Round 20 R620 Milestone Architecture Overview](../../../assets/github-ai-radar-2026-11-21-r20-r620-llm4s-llmrb-opencrawling-proximum.svg)

---

## ① 📌 Executive Summary (One-Sentence Selection Verdict)

> **Solution Architect's Verdict (Round 620 Milestone)**:  
> Enterprises running mission-critical backends on **the JVM (Scala, Java, Clojure) or Ruby (Rails / Sequel)** pay a heavy operational tax when forced to bolt on Python sidecar microservices just to run AI agents, ingest legacy ECM repositories, or version vector indexes.  
> - **For Scala 3.7 / JDK 21 teams needing a type-safe, SPI-modular agent and MCP framework with built-in `CostTracker`, Langfuse tracing, Prometheus metrics, and workspace isolation** ➔ Choose **`llm4s/llm4s`** (MIT, `v0.5.1`);  
> - **For Ruby 3.4+/4.0+ teams needing a zero-stdlib-dependency agent runtime (`LLM::Agent`) that executes tool calls in parallel via `Ractor` and `fork()` while converting tool exceptions into in-band model recovery turns** ➔ Choose **`r-uby-dev/llm` (`llm.rb v21`)** (MIT);  
> - **For Java 25 / Spring AI enterprises ingesting SharePoint, IBM FileNet P8, OpenText Documentum, Alfresco, M-Files, and CMIS with OpenFGA fine-grained authorization** ➔ Choose **`opencrawling/opencrawling`** (Apache-2.0);  
> - **For Clojure and Java applications needing a pure-JVM SIMD HNSW vector database with Git-like time-travel snapshots and copy-on-write reflink branching** ➔ Choose **`replikativ/proximum`** (Apache-2.0).  
> Together, this native polyglot stack eliminates Python sidecar sprawl and commercial ECM connector licenses, cutting monthly TCO for a 45-engineer platform team from **$7,920.00/mo** to **$330.00/mo (-$7,590.00/mo, -95.83%)**.

---

## ② 🎯 Solution Architect & Customer Deep-Dive Q&A

### Q1: Banking, insurance, and enterprise platforms store decades of documents in IBM FileNet, OpenText Documentum, Alfresco, and SharePoint—and duplicating vector indexes for every RAG A/B test wastes terabytes of storage. How do `opencrawling` and `proximum` solve this natively on the JVM?
- **Two Enterprise Data & Vector Bottlenecks**:
  1. **Legacy ECM Ingestion & Authorization Drift**: Standard Python RAG loaders cannot natively traverse IBM FileNet P8 GraphQL, OpenText Documentum REST, Alfresco Content/Process Services, Doxis 4, M-Files, or OASIS CMIS 1.0/1.1 while preserving document ACLs.
  2. **Mutable Vector Indexes Without Time Travel**: Traditional vector stores overwrite embeddings in place; A/B testing a new chunking strategy or rolling back a corrupted ingestion batch requires cloning the entire index.
- **How `opencrawling` + `proximum` Solve Both on the JVM**:
  - **`opencrawling/opencrawling` (Java 25 Open Ingestion Standard + OpenFGA)**:
    - Built on **Java 25, Spring Boot 4.1+, and Spring AI 2.0+**, providing the reference implementation of the **Open Ingestion Standard (OIS)**.
    - Ships native connectors for SharePoint Online (Microsoft Graph v1.0), IBM FileNet P8, OpenText Documentum, Alfresco, OASIS CMIS, Doxis 4, M-Files, Hyland OpenArch, Flowable/Camunda BPMN, and Apache StormCrawler—orchestrated via **Apache Tika 4.2, Kafka, Iceberg 1.11, SeaTunnel, and OpenFGA** into Milvus, Qdrant, Vespa, OpenSearch, Elasticsearch, or Solr.
  - **`replikativ/proximum` (Git-Versioned Copy-on-Write JVM Vector Database)**:
    - Brings functional **persistent data structure semantics** to pure-JVM SIMD-accelerated HNSW vector search (zero native C++ dependencies).
    - Every update returns an immutable snapshot supporting **Time Travel** (querying any historical commit) and **Copy-on-Write Branching** (using filesystem reflinks to share immutable vector blocks on disk).

### Q2: How do `llm4s` and `r-uby-dev/llm` deliver production agent loops, parallelism, and cost governance inside Scala and Ruby without Python sidecars?
- **`llm4s/llm4s` (`v0.5.1` Modular Scala 3.7.1 / JDK 21 Architecture)**:
  - Tracks project health on **Linux Foundation LFX Insights** and splits a clean `~19k`-line `llm4s-core` spine from SPI-registered provider modules (`llm4s-openai`, `llm4s-anthropic`, `llm4s-gemini`, `llm4s-ollama`, `llm4s-voyage`, `llm4s-openai-compatible`), `llm4s-agent`, `llm4s-agent-tools`, MCP support, workspace isolation, guardrails, and `llm4s-observability` (`CostTracker` + Langfuse + `llm4s-observability-prometheus`).
- **`r-uby-dev/llm` (`llm.rb v21` System-Programmer Agent Runtime in Ruby)**:
  - Requires **nothing beyond Ruby's standard library** (with opt-in `ActiveRecord` and `Sequel` support, with or without Rails) across 15+ LLM providers.
  - Executes tool calls in **true parallel via Ruby `Ractor` and OS `fork()`**, and concurrently via `Thread`, `Fiber`, and `async`.
  - `LLM::Agent` keeps the tool loop alive under failure: tool exceptions are rescued and reported back to the model as **in-band errors** bounded by explicit **retry budgets** and **tool-call budgets**.

### Q3: What are the version compatibility and maturity boundaries vs. managed cloud connectors?
- **Key Technical Boundaries**:
  - **`llm4s` Pre-1.0 Module Split**: `v0.5.0`/`v0.5.1` introduced the split Maven Central artifacts (`org.llm4s:llm4s-core_3`) targeting Scala 3.7.1 and JDK 21 ahead of the 1.0 compatibility baseline (`#1281`).
  - **`llm.rb` Ruby Version Tracks**: `v21` targets **Ruby 4+ and JSON v3** for peak Ractor tool parallelism, while `v17` (`gem install llm.rb -v 17.0.1`) supports **Ruby 3.4+ and JSON v2**.
  - **`proximum` Early Beta**: Currently in Early Beta on Clojars (`org.replikativ/proximum`); ideal for embedded JVM/Clojure versioned RAG and reproducible ML experiments.

---

## ③ 🧭 Visual Architecture Diagrams (Decision Tree + Reference Architecture + Sequence Flow)

### 3.1 Solution Architect Selection Decision Tree (Mermaid Flowchart)

```mermaid
flowchart TD
    Start["Polyglot Enterprise JVM (Scala/Java/Clojure) & Ruby AI Assessment"] --> Q1{"Primary Language & Bottleneck?"}
    Q1 -->|"Scala 3.7 / JDK 21 Microservices\nNeeding Typed Agents, MCP & CostTracker"| LLM4S["Adopt llm4s/llm4s (MIT · v0.5.1)\n• SPI Provider & Agent Modules\n• Langfuse + CostTracker + Prometheus"]
    Q1 -->|"Ruby / Rails / Sequel Systems\nNeeding Ractor/fork Parallel Tools"| LLMRB["Adopt r-uby-dev/llm (MIT · llm.rb v21)\n• Zero-Dep Ruby Stdlib Core\n• In-Band Error Rescue + Call Budgets"]
    Q1 -->|"Java 25 / Spring AI Enterprise Data\nIngesting FileNet/Documentum/SharePoint"| OIS["Adopt opencrawling/opencrawling (Apache-2.0)\n• Open Ingestion Standard (OIS)\n• OpenFGA ACLs + Kafka/Iceberg/Tika 4.2"]
    Q1 -->|"Clojure / Java Embedded Vector Search\nNeeding Time Travel & CoW Branching"| Prox["Adopt replikativ/proximum (Apache-2.0)\n• Pure JVM SIMD HNSW\n• Immutable Snapshots + Reflinks"]
    Q1 -->|"Zero-Code Managed SaaS Connectors"| Cloud["Adopt Azure AI Search + Copilot Studio\nor AWS Kendra / Bedrock"]
```

### 3.2 Zero-Python-Sidecar Enterprise JVM & Ruby Agentic RAG Architecture (Mermaid Architecture)

```mermaid
flowchart LR
    subgraph ECM["1. Enterprise Content & BPM Systems"]
        Sources["SharePoint / IBM FileNet P8 / Documentum\nAlfresco / M-Files / CMIS / Camunda BPMN"]
    end

    subgraph Ingest["2. Java 25 Open Ingestion & Auth Pipeline"]
        OC["opencrawling (Spring Boot 4.1+ / Spring AI 2.0+)\n(Apache Tika 4.2 + Kafka + Iceberg + OpenFGA)"]
    end

    subgraph Vector["3. Versioned & Distributed Vector Layer"]
        PX["replikativ/proximum (Pure JVM HNSW)\n(Time-Travel Snapshots + CoW Reflinks)"]
        MV["Milvus / Qdrant / Vespa / OpenSearch"]
    end

    subgraph Runtime["4. Native Polyglot Agent Runtimes"]
        S3["llm4s/llm4s (Scala 3.7.1 / JDK 21)\n(llm4s-agent + MCP + CostTracker + Guardrails)"]
        RB["r-uby-dev/llm (llm.rb v21 / v17)\n(LLM::Agent + Ractor/fork + ActiveRecord)"]
    end

    Sources -->|"OIS Connectors"| OC
    OC -->|"Immutable Snapshot Write"| PX
    OC -->|"Sharded Vector Write"| MV
    PX -->|"In-JVM Zero-Copy Search"| S3
    MV -->|"OpenFGA-Filtered RAG"| S3
    MV -->|"Parallel Tool Queries"| RB
```

### 3.3 ECM Ingestion, CoW Vector Branching & In-Band Agent Recovery Sequence (Mermaid Sequence Diagram)

```mermaid
sequenceDiagram
    autonumber
    actor Arch as Enterprise Architect / Service
    participant OC as OpenCrawling (Java 25 OIS + OpenFGA)
    participant Prox as Proximum (JVM CoW Vector DB)
    participant ScalaAgent as LLM4S Agent (Scala 3 + CostTracker)
    participant RubyAgent as llm.rb (LLM::Agent + Ractor)

    Arch->>OC: Trigger incremental ingestion from FileNet P8, SharePoint & Camunda
    OC->>OC: Parse via Tika 4.2, stage in Kafka/Iceberg & bind OpenFGA tuples
    OC->>Prox: Commit vectors to new immutable CoW branch (filesystem reflink)
    Arch->>ScalaAgent: Run A/B RAG evaluation across historical & branched snapshots
    ScalaAgent->>Prox: Query time-travel snapshot & export CostTracker/Prometheus metrics
    Arch->>RubyAgent: Invoke multi-tool workflow inside Rails/ActiveRecord service
    RubyAgent->>RubyAgent: Execute 4 tool calls in parallel across Ractors & fork()
    RubyAgent->>RubyAgent: Rescue tool exception as in-band error & self-correct within retry budget
    RubyAgent-->>Arch: Commit ActiveRecord state & return verified response
```

---

## ④ 📊 Horizontal Selection Matrix (Open-Source Quartet vs. Python Sidecars & Commercial SaaS)

| Dimension | `llm4s/llm4s` (`★ 279`) | `r-uby-dev/llm` (`★ 142`) | `opencrawling/opencrawling` (`★ 29`) | `replikativ/proximum` (`★ 34`) | Python Sidecars + Commercial ECM Connectors |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Primary Role** | Modular Scala 3.7 / JDK 21 agent & observability framework | Zero-dep Ruby stdlib parallel agent runtime (`llm.rb`) | Java 25 / Spring AI Open Ingestion Standard (OIS) platform | Pure-JVM SIMD HNSW vector DB with Git-like CoW branching | Cross-language IPC sidecars & proprietary connector suites |
| **Best-Fit Scenario** | Building type-safe JVM agents with MCP, guardrails & `CostTracker` | Embedding parallel Ractor/fork agents directly into Ruby/Rails apps | Ingesting FileNet, Documentum, Alfresco, SharePoint & CMIS with OpenFGA | Time-travel RAG snapshots, zero-copy A/B embedding branches on JVM | Python-only greenfield apps or turnkey cloud SaaS |
| **Key Differentiator** | `~19k`-line core + SPI modules, LFX Insights tracked, Prometheus/Langfuse | `Ractor` + `fork()` parallelism, in-band error rescue, call/retry budgets | Native connectors for 10+ enterprise ECM/BPM systems + Kafka/Iceberg | Persistent immutable data structures, time travel, reflink branching | Managed cloud UI, high per-connector licensing fees |
| **Integration & Ops Effort** | Low (Maven Central `org.llm4s:llm4s-core_3` modular artifacts) | Very Low (`gem install llm.rb`, zero non-stdlib required gems) | Medium (`docker-compose-decoupled.yml` + `docker-compose-openfga.yml`) | Very Low (Clojars `org.replikativ/proximum`, pure JVM) | High (maintaining dual JVM/Ruby + Python container fleets) |
| **License** | MIT | MIT | Apache-2.0 | Apache-2.0 | Proprietary |
| **45-Eng Monthly TCO** | **Combined `$330.00/mo`** (`$80` shared JVM/Ruby compute + `2.5h` ops) | Included (runs in-process inside existing Ruby workers) | Included (Apache-2.0 replaces costly ECM connector licenses) | Included (CoW reflinks eliminate duplicate vector storage) | **`$3,790.00 – $7,920.00/mo`** |

---

## ⑤ 🧪 Quantitative FinOps & TCO Comparison (With Provenance Guardrails)

> **Provenance & Guardrails Declaration**:  
> - `provenance`: `"synthetic"` (`independently_reproduced: false`, closed-form FinOps model for a 45-engineer polyglot JVM and Ruby platform engineering team at `$100.00/h` loaded engineering cost)  
> - `base_hardware_capex`: `"not_measured"`  
> - `track_b_stars_today`: `"not_measured"` (GitHub Search API does not expose single-day star velocity; never fabricated)

| Cost Component (45-Engineer Team / Month) | Path A: Python Sidecar Sprawl + Commercial ECM Connectors + Full-Copy Vector Indexes | Path B: Managed Cloud Enterprise Connectors + Dedicated Cloud Vector Clusters | Path C: `llm4s` + `llm.rb` + `OpenCrawling` + `Proximum` Native Polyglot Stack |
| :--- | :--- | :--- | :--- |
| **Commercial ECM Connectors / Duplicate Vector Storage** | `$3,620.00 / mo` | `$2,340.00 / mo` | **`$80.00 / mo`** (shared JVM/Ruby compute + CoW reflink storage) |
| **Cross-Language IPC Maintenance, ACL Sync & Index Rebuilds** | `43.0 hours / mo` | `14.5 hours / mo` | **`2.5 hours / mo`** (OIS OpenFGA pipeline + Ractor in-band recovery) |
| **Engineering Labor Cost (`$100.00/h`)** | `$4,300.00 / mo` | `$1,450.00 / mo` | **`$250.00 / mo`** |
| **Total Monthly TCO** | **`$7,920.00 / mo`** | **`$3,790.00 / mo`** | **`$330.00 / mo`** |
| **Net Monthly Savings vs. Path A** | Baseline (`0.00%`) | `-$4,130.00 / mo` (`-52.15%`) | **`-$7,590.00 / mo` (`-95.83%`)** |

---

## ⑥ 🛠️ Enterprise Adoption & Architecture Review Checklist

- [ ] **Select Split Maven Modules & Enable `CostTracker` (`llm4s`)**: Target Scala 3.7.1 and JDK 21 with `v0.5.1` split modules (`llm4s-core_3`, `llm4s-agent`, `llm4s-observability-prometheus`), register providers via SPI, and enforce workspace isolation and `CostTracker` budgets.
- [ ] **Align Ruby Runtime Track & Tool Budgets (`r-uby-dev/llm`)**: Use `gem install llm.rb` (`v21`) on Ruby 4+ / JSON v3 to unlock `Ractor` and `fork()` parallel tool execution (or `v17.0.1` on Ruby 3.4+), and configure explicit retry budgets and tool-call budgets on `LLM::Agent`.
- [ ] **Enforce OpenFGA Document ACLs in ECM Ingestion (`opencrawling`)**: Deploy `opencrawling` with `docker-compose-openfga.yml` so permissions from SharePoint, IBM FileNet P8, OpenText Documentum, and Alfresco are enforced at vector retrieval time.
- [ ] **Use CoW Reflink Branches for Reproducible RAG Evals (`proximum`)**: Run `proximum` on a reflink-capable filesystem (XFS, Btrfs, or APFS) to branch vector indexes with zero-copy structural sharing and audit historical states via time-travel queries.
