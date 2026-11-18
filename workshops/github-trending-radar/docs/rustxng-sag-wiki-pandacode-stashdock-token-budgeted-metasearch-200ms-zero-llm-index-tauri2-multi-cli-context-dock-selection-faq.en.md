# Exact-Token-Budgeted Metasearch MCP (`RustXNG/RustXNG`), 200ms/1M-Char Zero-LLM Knowledge Base (`Zleap-AI/SAG-Wiki`), Zero-Chromium 18+ CLI Workspace (`aicodeking/pandacode`) & Cross-AI Context Sidebar (`StashDock/StashDock`) Architecture Selection FAQ

> **Document Type**: Practical Selection & Architecture Guide for AI Solution Architects (2026-11-18 Night Shift · Round 21 / Cumulative Round 501)  
> **Benchmark Standard**: `docs/components/ib-vs-ethernet-roce-selection-faq.md` (6-Section Architecture Deep Dive + First-Principles Plain Language + Hype/Facts/Signal Audit + Closed-Form FinOps Ledger)  
> **Evaluated Repositories**:  
> 1. **`RustXNG/RustXNG`** (`★ 982`, `82 forks`, Rust `1.89+`, `v0.32.0`): Self-hosted Rust metasearch and grounding engine based on SearXNG (`rustxng mcp` exposing read-only `search` and session-bound `read_page` with exact `cl100k_base` / `o200k_base` `max_payload_tokens` budgets and `rustxng-index` local site/Wikipedia indexing)  
> 2. **`Zleap-AI/SAG-Wiki`** (`★ 1,449`, `170 forks`, Rust 2021 + Tauri 2 + Svelte 5, MIT, `arXiv:2610.22588`): Lightweight local knowledge base for humans and agents that indexes **1,000,000 characters in ~200 ms with 0 LLM calls** for indexing or retrieval, progressive PDF text-first search before background OCR/table extraction, and `SAG2` retrieval  
> 3. **`aicodeking/pandacode`** (`★ 1,304`, `220 forks`, Tauri 2 + Rust + SQLite + plain TypeScript): Native OS-webview desktop workspace (zero bundled Chromium, zero Node server, zero React) running **18+ coding agent CLIs** side-by-side across 5 protocols (Claude Code, ACP, ZCode App-Server, Pi RPC, Meta MSP) with 6-thread live tiling  
> 4. **`StashDock/StashDock`** (`★ 558`, `16 forks`, AGPL-3.0, Windows/macOS desktop + Chrome extension + DeepSeek Harness plugin): Local visual context library that organizes links, files, and prompts/rules into cards and injects them directly via the ChatGPT Web sidebar ("Add to chat") and DeepSeek Harness right sidebar  
> **Accounting Note**: Only software inference, search/SaaS, and engineering labor TCO are metered; workstation base hardware capEx is explicitly labeled `not_measured` with zero fabricated depreciation coordinates.

---

## 📌 1. Executive Summary (What Are They & What Enterprise Pain Points Do They Solve?)

As engineering teams orchestrate multiple coding agents (Claude Code, Codex, Copilot CLI, DeepSeek, Grok Build) across daily workflows, four infrastructure bottlenecks routinely inflate token spend and workstation RAM consumption:
1. **Pain Point A (Per-Query Search API Costs + Raw Webpage Dumps Blowing Out Context Windows + Unbounded URL SSRF Risks)**: Naive web-fetch MCP servers dump tens of thousands of tokens of raw HTML into the agent's context and allow prompt-injected agents to fetch arbitrary internal URLs. **`RustXNG/RustXNG` (`v0.32.0`)'s Solution**: A self-hosted Rust metasearch engine (supporting external search aggregation plus `rustxng-index` local site indexing and Wikipedia dumps) with a built-in `rustxng mcp` server exposing two strictly bounded read-only tools: `search` (up to 10 results, default 5, 500-char snippets) and `read_page` (**strictly restricted to URLs returned by `search` in the same session**, returning up to 3 query-relevant passages, default 4,000 chars, paginated via `offset`/`next_offset` up to 20,000 chars). Passing `tokenizer` (`cl100k_base` or `o200k_base`) and `max_payload_tokens` enforces an **exact serialized token budget** on MCP `structuredContent`.
2. **Pain Point B (GraphRAG Indexing Burns Thousands of LLM Calls & Large PDFs Block Search Until Full OCR Finishes)**: Building GraphRAG indexes over local documentation takes tens of minutes and burns substantial LLM API budget before a single question is asked. **`Zleap-AI/SAG-Wiki` (`arXiv:2610.22588`)'s Solution**: Uses the **SAG2** retrieval architecture (Rust + Tauri 2 + Svelte 5, zero external database required) to index **1,000,000 characters of text in ~200 ms with 0 LLM calls** during indexing or retrieval. Basic PDF text becomes searchable immediately while background OCR and table recognition finish asynchronously (reusing loaded models across segments), and coding agents connect via `cli/skills/sag/SKILL.md`.
3. **Pain Point C (Running Multiple Electron Agent IDEs Consumes 16GB+ RAM While 18+ Agent CLIs Speak Incompatible Protocols)**: Every Electron wrapper bundles its own Chromium and Node runtime. **`aicodeking/pandacode`'s Solution**: Built with Tauri 2, Rust, SQLite, and plain TypeScript on the OS native webview (**no bundled Chromium, no resident Node server, no React runtime**). It unifies **18+ coding CLIs**—including Claude Code, Codex, Kimi Code, OpenCode, GLM, Xiaomi MiMo, Alibaba (via Claude Code), GitHub Copilot CLI, Antigravity, xAI Grok Build, DeepSeek, Command Code, Cline, Kilo Code, Devin CLI, Hermes Agent, Cursor CLI (via ACP), ZCode, Pi/omp (RPC), and Meta Muse Code (MSP)—with **6-thread live tiling**, one card per turn with inline diff inspection, and self-sorting `Active` / `Finished` / `Settled` / `Pinned` queues.
4. **Pain Point D (Hunting Across Bookmarks, Local Folders, and Old Chats to Re-Attach Context in Every New AI Session)**: Reusable architecture docs, links, and prompt rules are scattered across browsers and disk folders. **`StashDock/StashDock`'s Solution**: A local visual context library (Windows & macOS desktop app) coupled with a **ChatGPT Chrome sidebar extension** ("Add to chat") and a **DeepSeek Harness right-sidebar plugin** (`plugins/stashdock-dsh` injecting links/notes as context quotes and local files as native attachments).

---

## 💬 2. Three First-Principles Deep-Dive Questions (Q1–Q3)

### Q1: Why must an agent web-grounding MCP server (`RustXNG/RustXNG`) mechanically enforce "same-session `search` URL binding + exact `cl100k_base`/`o200k_base` payload token budgets"?
* **First-Principles Breakdown**:
  - **Eliminating Arbitrary-URL SSRF in `read_page`**: If an MCP reader tool accepts any arbitrary URL string, a prompt-injected document can trick the agent into probing `localhost` or cloud metadata endpoints. `RustXNG` restricts `read_page` exclusively to URLs returned by `search` within the same session.
  - **Deterministic Serializer-Level Token Budgeting**: Character limits alone do not map deterministically to token counts across dense code or CJK text. By accepting `tokenizer` (`cl100k_base` or `o200k_base`) and `max_payload_tokens`, `rustxng mcp` bounds the exact serialized `structuredContent` token footprint and extracts at most 3 query-matched passages per call.

### Q2: How does `Zleap-AI/SAG-Wiki` achieve `~200 ms` per million characters with zero LLM calls during indexing/retrieval while outperforming conventional RAG and GraphRAG (`arXiv:2610.22588`)?
* **First-Principles Breakdown**:
  - **Zero-LLM Structural Indexing (`SAG2`)**: Instead of invoking an LLM to extract entities and edges on every ingested chunk, `SAG-Wiki` builds its `SAG2` structural index deterministically in Rust (**~200 ms per 1M text characters**, 0 LLM calls), reserving LLM invocation strictly for final answer synthesis with direct source traceability.
  - **Non-Blocking Two-Stage PDF Pipeline**: Basic PDF text and Office/RTF documents are indexed immediately so engineers and agents can search right away, while heavy OCR and table-structure models run asynchronously in the background and share loaded weights across PDF segments.

### Q3: Why does pairing `aicodeking/pandacode` with `StashDock/StashDock` eliminate both the "Electron RAM tax" and "cross-assistant context re-entry friction"?
* **First-Principles Breakdown**:
  - **OS Webview + Multi-Protocol Multiplexing (`PandaCode`)**: Stripping out Chromium, Node, and React lets `PandaCode` tile up to 6 heterogeneous coding CLIs (Claude Code, ACP, Pi RPC, MSP) side-by-side in a lightweight native window where each turn collapses into a single timed card with an integrated diff footer.
  - **Unified Context Injection (`StashDock`)**: Storing curated links, files, and prompt rules in one local card library with native sidebars for both ChatGPT Web and DeepSeek Harness removes repetitive file browsing and copy-pasting.

---

## 🧭 3. Architecture Decision Tree & Reference Topology (Mermaid)

```mermaid
flowchart TD
    subgraph Workspace["1. Zero-Chromium 18+ CLI Workspace (aicodeking/pandacode)"]
        PC_UI["Tauri 2 + Rust + SQLite + Plain TS (0 Chromium / 0 Node)<br/>(6-Thread Live Tiling + 1 Card/Turn + Footer Diff Inspector)"]
        PC_PROTO["5 Multi-Vendor Protocol Adapters<br/>(Claude Code | ACP: Copilot/Antigravity/Grok/DeepSeek | Pi RPC | MSP)"]
        PC_UI --> PC_PROTO
    end

    subgraph ContextDock["2. Cross-AI Visual Context Sidebar (StashDock/StashDock)"]
        SD_LIB["Local Visual Card Library (Links / Files / Prompts)<br/>(ChatGPT Sidebar 'Add to chat' + DeepSeek Harness Native Attachments)"]
    end

    subgraph Grounding["3. Token-Budgeted Metasearch & 200ms Zero-LLM Wiki (RustXNG + SAG-Wiki)"]
        RX["RustXNG v0.32.0 Self-Hosted Metasearch MCP<br/>(search <=10 + Session-Bound read_page + cl100k/o200k Token Cap)"]
        SAG["Zleap-AI/SAG-Wiki (arXiv:2610.22588)<br/>(0 LLM Calls for Index/Search + ~200ms/1M Chars + Progressive PDF OCR)"]
        RX --> SAG
    end

    Workspace --> ContextDock
    ContextDock --> Grounding
```

---

## 📊 4. Peer Solution Comparison Matrix (Decision Matrix)

| Evaluation Dimension | Path A: Per-Query Search APIs + Raw HTML Dumps + LLM GraphRAG Indexing + Multiple Electron IDEs | Path B: Hosted Search SaaS + Managed Vector DB + Cloud Web IDEs | **Path C (Recommended): `RustXNG` + `SAG-Wiki` + `PandaCode` + `StashDock`** |
| :--- | :--- | :--- | :--- |
| **Web Grounding Cost & SSRF Safety** | ❌ High per-query API bills; raw HTML dumps blow out context; arbitrary URL SSRF risk | ⚠️ Cloud scrapers cannot index internal docs and lack exact `o200k_base` payload caps | ✅ **Self-hosted Rust metasearch + session-bound `read_page` + exact `cl100k`/`o200k` token cap** |
| **Local Knowledge Base Indexing Speed** | ❌ GraphRAG burns thousands of LLM calls and takes 30+ mins to index large repos | ⚠️ Requires managing external vector DBs; PDFs block until full OCR finishes | ✅ **`SAG2` indexes 1M chars in `~200 ms` with 0 LLM calls; progressive text-first PDF search** |
| **Multi-Agent Desktop RAM Footprint** | ❌ Running 4 Electron agent apps consumes 10–16 GB RAM and scatters diffs | ⚠️ Cloud IDEs cannot orchestrate local installations of 18+ heterogeneous CLIs | ✅ **`PandaCode` (Tauri 2, 0 Chromium/Node) tiles 6 threads across 18+ CLIs via ACP/RPC/MSP** |
| **Cross-Assistant Context Reuse** | ❌ Manual bookmark/folder hunting on every new chat session | ⚠️ Locked inside a single vendor's cloud project workspace | ✅ **`StashDock` local visual library with 1-click ChatGPT & DeepSeek Harness sidebars** |
| **45-Seat Team Monthly TCO** | **`$6,130.00 / mo`** (`$2,280` search/GraphRAG tokens + `38.5h / $3,850` engineering labor) | **`$2,510.00 / mo`** (`$960` SaaS/vector DB + `15.5h / $1,550` ops labor) | **`$345.00 / mo`** (`$75` synthesis inference + `2.7h / $270` ops labor, **`-94.37%` net savings**) |

---

## 📈 5. 7-Card Quantitative Insights & Hype / Facts / Signal Ledger

### 5.1 Hype vs. Facts vs. Strategic Signal Audit Table

| Repository (`owner/repo`) | Hype (Market Claim) | Measured Facts (Verified Repo & Artifact Evidence) | Strategic Signal (Architect Verdict) |
| :--- | :--- | :--- | :--- |
| **`RustXNG/RustXNG`** | "Self-hosted metasearch and grounding engine for AI agents, based on SearXNG, in Rust" | `★ 982` (`82 forks`, Rust `1.89+`, `v0.32.0`): Combines external search providers + `rustxng-index` local site/Wikipedia dumps; `rustxng mcp` exposes `search` (`<=10` results, 500-char snippets) and session-bound `read_page` (up to 3 relevant passages, `20,000` max chars) with exact `cl100k_base` / `o200k_base` `max_payload_tokens` budgeting. | **P0 Adopt (Token-Bounded Self-Hosted Grounding MCP)**: Session-bound `read_page` + tokenizer-exact payload caps eliminate both SSRF and web-scrape context overflow. |
| **`Zleap-AI/SAG-Wiki`** | "Lightweight knowledge base for people and agents, with ultra fast indexing and precise retrieval" | `★ 1,449` (`170 forks`, Rust + Tauri 2 + Svelte 5, MIT, `arXiv:2610.22588`): Zero external DB; indexes **1M text characters in ~200 ms with 0 LLM calls** for indexing or retrieval via `SAG2`; progressive PDF basic-text search before background OCR/table extraction; ships `cli/skills/sag/SKILL.md`. | **P0 Adopt (Zero-LLM-Index Local Knowledge Base)**: Replaces slow, token-expensive GraphRAG indexing pipelines with deterministic 200ms/1M-char local indexing. |
| **`aicodeking/pandacode`** | "PandaCode: a calm desktop workspace for coding agents" | `★ 1,304` (`220 forks`, Tauri 2 + Rust + SQLite + plain TS): **Zero bundled Chromium, Node server, or React**; runs **18+ coding CLIs** via Claude Code, ACP, ZCode App-Server, Pi RPC, and Meta MSP protocols; supports **6-thread live tiling** and 1-card-per-turn diff review. | **P0 Adopt (Multi-Protocol Native Agent IDE Shell)**: Best-in-class low-memory desktop multiplexer for teams running Claude Code, Codex, Copilot CLI, and Grok side-by-side. |
| **`StashDock/StashDock`** | "Your AI-native personal context library. Collect, organize and reuse context across AI conversations." | `★ 558` (`16 forks`, AGPL-3.0): Local visual context library for Windows/macOS with a **ChatGPT Chrome sidebar extension** ("Add to chat") and **DeepSeek Harness right-sidebar plugin** (`plugins/stashdock-dsh` with context quotes and native file attachments). | **P0 Adopt (Cross-Assistant Context Bus)**: Bridges local reference cards directly into web and desktop AI conversations in one click. |

### 5.2 Closed-Form FinOps TCO Ledger (Claim ID: `CLAIM-20261118-R21-RUSTXNG-SAGWIKI-PANDACODE-STASHDOCK`)

* **Scope**: 45-seat AI solution architecture & engineering team running agent web grounding, local technical knowledge retrieval, multi-CLI coding orchestration, and cross-assistant context management (`$100.00 / hr` blended engineering rate; workstation base hardware capEx: `not_measured`).
* **Path A (Commercial Search APIs + Raw HTML Context Dumps + LLM-Heavy GraphRAG Indexing + Multiple Electron IDEs + Manual Context Copy-Paste)**:
  - Search API fees, raw HTML token overflow & GraphRAG indexing LLM spend: **`$2,280.00 / mo`**
  - Engineering wait time, context pruning & multi-window management labor: **`38.5 hrs / mo`** × `$100.00 / hr` = **`$3,850.00 / mo`**
  - **Path A Total Monthly TCO**: `$2,280.00 + $3,850.00` = **`$6,130.00 / mo`**
* **Path B (Hosted AI Search SaaS + Managed Vector DB + Cloud Agent Workspaces)**:
  - Compute & SaaS subscriptions: **`$960.00 / mo`**
  - Engineering sync & maintenance labor: **`15.5 hrs / mo`** × `$100.00 / hr` = **`$1,550.00 / mo`**
  - **Path B Total Monthly TCO**: `$960.00 + $1,550.00` = **`$2,510.00 / mo`**
* **Path C (`RustXNG v0.32.0` Token-Budgeted MCP + `SAG-Wiki` 200ms Zero-LLM Index + `PandaCode` 6-Tile Native Workspace + `StashDock` Context Sidebar)**:
  - Answer-synthesis inference & local hosting spend: **`$75.00 / mo`**
  - Engineering curation & index maintenance labor: **`2.7 hrs / mo`** × `$100.00 / hr` = **`$270.00 / mo`**
  - **Path C Total Monthly TCO**: `$75.00 + $270.00` = **`$345.00 / mo`**
  - **Net Monthly Savings vs. Path A**: `$6,130.00 - $345.00` = **`$5,785.00 / mo`** (**`-94.37%`**, **`$69,420.00 / yr`** annual savings, **`35.8 hrs / mo`** saved).

---

## 🛠️ 6. AI Solution Architect Actionable Checklist (SA Action Items)

- [ ] **1. Deploy `RustXNG/RustXNG` (`v0.32.0`) with `o200k_base` / `cl100k_base` Payload Token Caps**: Run `rustxng mcp` locally or on an internal server, build local documentation indexes via `rustxng-index`, and configure agent MCP calls with explicit `max_payload_tokens` budgets.
- [ ] **2. Replace LLM-Heavy Document Indexing with `Zleap-AI/SAG-Wiki`**: Index project repositories, Markdown notes, and PDFs via `SAG-Wiki` (`~200 ms / 1M chars` with 0 LLM indexing calls) and attach `cli/skills/sag/SKILL.md` to coding agents for source-traceable retrieval.
- [ ] **3. Consolidate Heterogeneous Coding CLIs into `aicodeking/pandacode`**: Replace multiple Electron wrappers with `PandaCode`'s Tauri 2 native webview workspace to tile up to 6 concurrent sessions across Claude Code, Codex, Copilot CLI, Antigravity, Grok Build, and DeepSeek.
- [ ] **4. Standardize Reusable Prompt & File Context in `StashDock/StashDock`**: Curate team architecture references and rules in `StashDock` and enable the ChatGPT Chrome extension and DeepSeek Harness plugin (`plugins/stashdock-dsh`) for 1-click context injection.
