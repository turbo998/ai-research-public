# 127-Test Traceable RAG/PromptLens/NL2SQL Suite (`8hjkkwikl8/ai-portfolio`) & 39,000 Real-World-Sized Free 3D Assets MCP (`kanaworksai-hue/sozai-search-mcp`) Selection FAQ

> **Document Scope**: This is the **2026-11-13 Night Shift Round 13 (Cumulative #141) standalone 6-part selection guide**, modeled strictly after `ib-vs-ethernet-roce-selection-faq.md` with first-principles explanations and closed-form FinOps math. It is written for AI Solution Architects, RAG/NL2SQL Platform Leads, and 3D Simulation Engineers evaluating two reproducible engineering repositories:
> 1. **`8hjkkwikl8/ai-portfolio` (`100★` in 2 days, Python 3.13, MIT, 127 passing tests via `python verify_all.py`)**: Three runnable, offline-first AI engineering systems — (1) **`InsightRAG` (30 tests)**: character-offset chunking with `source`/`chunk_id` span replay, BM25 + hash char n-gram RRF fusion, **per-sentence citation validation that falls back to an offline extractive summary if any sentence fails**, and SHA-256 answer fingerprint faithfulness scoring (reporting `N/A` rather than fabricating `100%` on unannotated or zero-citation outputs); (2) **`PromptLens` (39 tests)**: content-hash immutable prompt registry, input SHA-256 pinning, failure isolation/retry, and repeat-run stability HTML reports; (3) **`DataChat BI` (58 tests)**: natural language to read-only SQL with full safety boundaries and controlled multi-table JOINs!
> 2. **`kanaworksai-hue/sozai-search-mcp` (`51★` in 5 days, Python 3.10–3.14, MIT)**: Gives Claude Code, Claude Desktop, Cursor, and any MCP client a unified library of **39,000 free (mostly CC0) 3D assets with real-world physical dimensions**: photoreal models, PBR materials, and HDRIs from Poly Haven and ambientCG; low-poly game assets from Kenney, Quaternius, KayKit, and Polygonal Mind; rigged VRM avatars from Open Source Avatars; NASA spacecraft/rovers/telescopes; and Quixel Megascans listings!
>
> **中文版本**: [ai-portfolio-sozai-search-mcp-traceable-rag-nl2sql-39k-3d-assets-selection-faq.md](ai-portfolio-sozai-search-mcp-traceable-rag-nl2sql-39k-3d-assets-selection-faq.md) · **Daily Digest**: [`daily/2026-11-13.en.md`](../daily/2026-11-13.en.md) · **Topic SVG**: [`assets/github-ai-radar-2026-11-13-r13-aiportfolio-sozai.svg`](../../../assets/github-ai-radar-2026-11-13-r13-aiportfolio-sozai.svg)

![8hjkkwikl8/ai-portfolio and kanaworksai-hue/sozai-search-mcp Architecture Comparison](../../../assets/github-ai-radar-2026-11-13-r13-aiportfolio-sozai.svg)

---

## 📌 1. Executive Summary

1. **In plain English, what core pain points do these two repositories solve?**
   - **Ending "hallucinated RAG citation numbers, fabricated 100% faithfulness scores on unannotated test sets, unversioned prompt edits, and unsafe NL2SQL queries" (`8hjkkwikl8/ai-portfolio`)**: `ai-portfolio` ships three reproducible reference systems verified by **127 automated tests (`python verify_all.py`)** with zero API keys required for the offline stdlib baseline: `InsightRAG` (30 tests) enforces **sentence-by-sentence citation validation** (falling back to an extractive summary if any sentence fails) and matches human faithfulness labels by **answer SHA-256 fingerprint** (reporting `N/A` when unannotated); `PromptLens` (39 tests) pins prompt content hashes and dataset SHA-256 digests; and `DataChat BI` (58 tests) enforces a strict read-only SQL boundary with controlled multi-table JOINs!
   - **Ending "manual multi-site 3D asset hunting and mismatched unit scales when coding agents build Blender, Three.js, Godot, or Unity scenes" (`kanaworksai-hue/sozai-search-mcp`)**: `sozai-search-mcp` indexes **39,000 free 3D assets with real-world physical dimensions** across Poly Haven, ambientCG, Kenney, Quaternius, KayKit, Polygonal Mind, Open Source Avatars (VRM), NASA, and Quixel Megascans — letting agents query *"a wooden crate under 1 m tall"*, inspect preview thumbnails, and drop properly scaled files straight into the project!
2. **Closed-Form FinOps Conclusion (`CLAIM-20261113-R13-AIPORTFOLIO-SOZAI`)**:
   - Modeled for an **enterprise AI and 3D simulation team executing `300 RAG/prompt/NL2SQL evaluation runs per month` and sourcing `400 real-world-sized 3D assets per month`** (fully loaded AI/simulation engineer rate `$90.00/hr`; commercial vector DB cluster leases and paid 3D marketplace subscriptions: `not_measured`):
   - Upgrading from **Path A (unchecked RAG/SQL scripts + manual multi-site 3D asset hunting and scale fixing, `$5,250.00/mo`)** to **Path C (`8hjkkwikl8/ai-portfolio` 127-test traceable suite + `kanaworksai-hue/sozai-search-mcp` 39k real-world-sized CC0 3D MCP, `$525.00/mo`)** saves **`$4,725.00/mo` (`-90.00%`, or `$56,700.00/yr`)** and cuts engineering debugging and asset-sourcing labor from `40.0 hrs/mo` to `4.0 hrs/mo` (**`-90.00%`**).

---

## 🎯 2. Three First-Principles Deep-Dive Questions (Q1 / Q2 / Q3)

### Q1: Why do typical RAG/NL2SQL demos and unindexed 3D asset workflows fail under production scrutiny?
- **First-Principles Breakdown**:
  1. **Unverified Citations & Silent Metric Inflation**: Without per-sentence citation checks and SHA-256 answer fingerprinting, RAG pipelines emit dangling `[99]` citations and coerce missing human labels into fake `100%` scores.
  2. **Scale Discrepancies Across 3D Asset Repositories**: Mixing raw models from disparate sites without physical bounding-box dimensions results in props that import at 10× or 0.01× real-world scale.

### Q2: How does `8hjkkwikl8/ai-portfolio` enforce zero-fabrication engineering rigor across 127 tests?
- **First-Principles Breakdown**:
  1. **`InsightRAG` Span Replay, Per-Sentence Citation Fallback & SHA-256 Faithfulness**:
     - Preserves `source`, `chunk_id`, and exact character spans; validates citations sentence-by-sentence with automatic fallback to offline extractive summaries; records `N/A` whenever an answer's SHA-256 hash lacks human annotation.
  2. **`PromptLens` Content-Hash Registry & `DataChat BI` Read-Only JOIN Guard**:
     - Pins prompt hashes, dataset SHA-256 digests, and repeat-run stability metrics in `PromptLens` (39 tests), while `DataChat BI` (58 tests) restricts NL2SQL to read-only queries and controlled JOIN paths (`start_all.py` binds strictly to `127.0.0.1`).

### Q3: How does `kanaworksai-hue/sozai-search-mcp` unify 39,000 free 3D assets with real-world physical sizing for MCP agents?
- **First-Principles Breakdown**:
  1. **Multi-Catalog Aggregation with Physical Bounding-Box Metadata**:
     - Unifies photoreal models, 4K PBR materials, and HDRIs (Poly Haven, ambientCG), low-poly game kits (Kenney, Quaternius, KayKit, Polygonal Mind), rigged VRM avatars (Open Source Avatars), and NASA 3D models with real-world dimensions.
  2. **Keyword + Semantic Search & Thumbnail Preview Loop**:
     - Lets MCP clients filter by size and meaning, inspect preview images, and download assets directly into the workspace across macOS, Windows, and Linux.

---

## 🧭 3. Mermaid Decision Tree & 127-Test AI Suite + 39K 3D Asset MCP Architecture

```mermaid
flowchart TD
    A["Traceable AI Application Evaluation & 3D Asset Sourcing Selection"] --> B{"Primary Engineering Track?"}
    B -- "Build & audit citation-verified RAG, immutable prompt evals & read-only NL2SQL" --> C["Adopt 8hjkkwikl8/ai-portfolio (127 Tests · python verify_all.py)"]
    B -- "Equip coding agents with 39,000 real-world-sized free CC0 3D models, PBR & VRM assets" --> D["Adopt kanaworksai-hue/sozai-search-mcp (39k 3D Assets MCP)"]

    C --> C1["InsightRAG: char-offset replay + per-sentence citation fallback + SHA-256 faithfulness"]
    C1 --> C2["PromptLens immutable hash registry + DataChat BI 58-test read-only NL2SQL"]

    D --> D1["Unified index across Poly Haven, ambientCG, Kenney, KayKit, NASA & VRM Avatars"]
    D1 --> D2["Query by real-world size (<1m) & meaning -> inspect preview -> drop into project"]

    C2 & D2 --> E["🏆 Golden Engineering Stack: 127-Test Zero-Fake Baseline + 39K Sized 3D MCP (-90.00% TCO)"]
```

---

## 📊 4. Head-to-Head Selection Matrix

| Dimension | Path A: Unchecked RAG/SQL + Manual 3D Hunting | Path B: Heavy Boilerplate + Unindexed Folders | **Path C (Recommended): `ai-portfolio` + `sozai-search-mcp`** |
| :--- | :--- | :--- | :--- |
| **Citation Verification & Honest Scoring** | Hallucinates citations; fakes 100% on missing labels | Expensive LLM-as-Judge loops | **Per-sentence citation fallback + SHA-256 faithfulness (`N/A` on unannotated)** |
| **Prompt Versioning & NL2SQL Safety** | Unpinned prompt edits; raw SQL injection risks | Heavy external dependencies | **Content-hash PromptLens + 58-test read-only NL2SQL (`127` tests total)** |
| **3D Asset Coverage & Real-World Sizing** | Manual browsing across 8 sites; broken scales | Small static local folders | **39,000 free/CC0 models, PBR, HDRIs & VRM avatars with physical dimensions** |
| **Offline Reproducibility & Host Safety** | Fails without paid API keys | Binds `0.0.0.0` & leaks background processes | **Stdlib offline `verify_all.py` + `127.0.0.1`-only `start_all.py` cleanup** |
| **Monthly TCO (300 Evals + 400 3D Assets)** | **`$5,250.00 / mo`** (`$1,650` API/assets + `$3,600` labor) | **`$2,640.00 / mo`** (`$750` API + `$1,890` labor) | **`$525.00 / mo` (Saves `$4,725.00/mo` · `-90.00%`)** |

---

## 🧪 5. Closed-Form FinOps Worked Example & 7-Card Insights (`CLAIM-20261113-R13-AIPORTFOLIO-SOZAI`)

### 5.1 Baseline Parameters & Explicit Scope Boundaries
- **Scenario**: An AI application and 3D simulation team executing **300 RAG/prompt/NL2SQL evaluation runs per month** and sourcing **400 real-world-sized 3D assets/materials per month**.
- **Labor Rate**: Fully loaded AI / simulation engineering rate of **`$90.00 / hr`**.
- **Explicit Not-Measured Boundary**: Commercial vector database cluster leases and paid 3D marketplace subscriptions are marked **`not_measured`**. This model strictly accounts for evaluation API spend, mismatched asset purchase waste, and engineering hours spent debugging hallucinated citations, SQL boundaries, and 3D scale mismatches.

### 5.2 Three-Path Monthly Cost Comparison

| Cost Component | Path A: Unchecked RAG/SQL + Manual 3D Hunting | Path B: Heavy Boilerplate + Unindexed Assets | **Path C: `ai-portfolio` + `sozai-search-mcp` (Recommended)** |
| :--- | :--- | :--- | :--- |
| **Monthly Evaluation API & Asset Spend** | **`$1,650.00`** (online-only evals + mismatched paid 3D assets) | **`$750.00`** (repeated online eval runs) | **`$165.00`** (offline stdlib smoke gate + 39,000 free CC0 3D assets) |
| **Citation Triage, SQL Guard & 3D Scale Fix Labor (`$90/hr`)** | `40.0 hrs × $90.00` = **`$3,600.00`** | `21.0 hrs × $90.00` = **`$1,890.00`** | `4.0 hrs × $90.00` = **`$360.00`** |
| **Total Monthly TCO** | **`$5,250.00 / mo`** | **`$2,640.00 / mo`** (`-49.71%`) | **`$525.00 / mo`** |
| **Net Savings vs. Path A** | Baseline | Saves `$2,610.00 / mo` | **Saves `$4,725.00 / mo` (`-90.00%` · `$56,700.00/yr`)** |
| **Commercial Vector DBs & Paid 3D Store Subscriptions** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 6. Production Adoption Checklist

- [ ] **1. `8hjkkwikl8/ai-portfolio` 127-Test Verification**: Run `python verify_all.py` on Python 3.13 to execute all 127 tests (InsightRAG 30 + PromptLens 39 + DataChat BI 58) and regenerate `evaluation.json`, `report.html`, and `datachat_report.html`.
- [ ] **2. Sentence-Citation Fallback & `127.0.0.1` Service Check**: Launch `python start_all.py`, verify `:8001` and `:8002` bind strictly to `127.0.0.1`, and confirm that invalid citation IDs trigger automatic fallback to extractive summaries.
- [ ] **3. `kanaworksai-hue/sozai-search-mcp` Client Registration**: Register `sozai-search-mcp` in Claude Code or Cursor and query 3D models, PBR materials, HDRIs, and VRM avatars with physical dimension filters (e.g., `"under 1 m tall"`).
- [ ] **4. Thumbnail Preview & License Audit**: Have the agent inspect asset preview thumbnails and verify CC0/attribution metadata before importing files into Blender, Three.js, Godot, or Unity scenes.
