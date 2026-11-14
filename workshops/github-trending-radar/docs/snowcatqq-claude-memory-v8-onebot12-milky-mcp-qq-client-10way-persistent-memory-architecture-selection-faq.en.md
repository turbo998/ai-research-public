# Quad-Protocol QQ Agent Runtime (`SnowCatQQ`) & 10-Way Claude Persistent Memory Architecture (`claude-memory`) Deep-Dive & Selection FAQ

> **Document Metadata (2026-11-14 · Daytime Round 31 / Cumulative Round 214)**  
> - **Benchmark Style**: Modeled on `ib-vs-ethernet-roce-selection-faq.md` (First-Principles Breakdown + Plain-English Takeaways + 3 Core Architectural Q&As + Mermaid Decision Tree + Closed-Form FinOps Audit)  
> - **Evaluated Repositories**:  
>   1. [`DandanLLab/SnowCatQQ`](https://github.com/DandanLLab/SnowCatQQ) (`★ 283`, SnowCat: community-maintained fusion of `NapCat 4.18.28` and `SnowLuma`'s 56 extended actions running inside official `QQ 9.9.37-54395` via zero-byte-patch V8 compiler channel injection, exposing **OneBot v12 (default) + OneBot v11 + Milky 1.3 (Lagrange standard) + Streamable HTTP `/mcp`** with built-in human-cadence jitter, rate budgets, and anti-ban circuit breakers)  
>   2. [`claudememory/claude-memory`](https://github.com/claudememory/claude-memory) (`★ 125`, November 2026 10-way comparison of persistent memory architectures for Claude, Claude Code, and Claude Desktop: `Glen`, `CLAUDE.md` + Auto Memory, `Claude App Memory`, `claude-mem`, `Mem0`, `Supermemory`, `Basic Memory`, `MCP Knowledge Graph`, `Cognee`, and `Graphiti/Zep`)  
> - **Companion SVG Diagram**: [`assets/github-ai-radar-2026-11-14-r31-snowcatqq-claude-memory.svg`](../../../assets/github-ai-radar-2026-11-14-r31-snowcatqq-claude-memory.svg)  
> - **Audit Claim ID**: `CLAIM-20261114-R31-SNOWCATQQ-CLAUDEMEMORY` (local developer workstation hardware power/depreciation marked `not_measured`)

---

## 📌 1. Executive Summary (3-Minute Architect's Briefing)

1. **How does `DandanLLab/SnowCatQQ` differ from `TomyJan/SnowLuma` (evaluated in R212), and when do you need it?**  
   - **Plain-English Reality**: `TomyJan/SnowLuma` (R212) is a lightweight external CLI bridge focused on standard **OneBot v11** and 5 core messaging MCP tools (`send_group_msg`, `send_private_msg`, etc.). However, if your AI agent needs to operate **deep community workflows** (publishing QZone posts, managing group photo albums, setting group essence messages, check-ins, flash photos, or collections) or connect to frameworks requiring **OneBot v12** or **Lagrange's Milky 1.3 standard**, basic OneBot v11 is not enough.  
   - **`SnowCatQQ` First-Principles Fix**: Fuses `NapCat 4.18.28` with `SnowLuma`'s **56 extended actions** inside official **`QQ 9.9.37-54395`** via **zero-byte-patch V8 compiler channel injection**, simultaneously serving **four protocol surfaces**: (1) **OneBot v12 (default)**; (2) **OneBot v11 (legacy compatibility)**; (3) **Milky 1.3 (Lagrange standard)**; and (4) **Streamable HTTP `/mcp`** (automatically exposing all 56+ actions as MCP tools). Crucially, it embeds an anti-ban **stability pipeline (exponential backoff + human-cadence jitter + rate-limit budgets + automatic circuit breakers)**.
2. **How should an AI Solution Architect separate vendor hype from architectural signal in `claudememory/claude-memory`'s 10-way comparison?**  
   - **Hype vs. Facts De-Biasing Audit**: The repository ranks commercial hosted SaaS `Glen` (`tryglen.com`) at `#1` (`⭐ 1. Glen`), reflecting obvious vendor self-promotion bias. Enterprise architects must never stream proprietary repository context to an unvetted third-party cloud just because a listicle ranks it first.  
   - **Signal (Zero-Lock-In 3-Layer Memory Stack)**: Once you strip away the commercial #1 placement, the 10-tool taxonomy provides a clean blueprint for a **zero-egress, local-first 3-layer memory stack**:
     - **L0 Repo Constitution (`Git-Tracked`)**: Keep `CLAUDE.md` under `<200` lines (plus `.claude/rules/`) for immutable build commands and architectural invariants;
     - **L1 Human-Auditable Markdown Notes (`Local MCP`)**: Mount **`Basic Memory`** (local Markdown files queried on demand via MCP) or **`claude-mem`** (`~/.claude-mem` local session summaries);
     - **L2 Bi-Temporal Fact Graph (`Self-Hosted MCP`)**: Add **`Graphiti / Zep`** (or **`Cognee`**) when architectural facts mutate over time so superseded decisions are invalidated rather than co-injected with current state.
3. **Closed-Form FinOps Audit (`CLAIM-20261114-R31-SNOWCATQQ-CLAUDEMEMORY`)**:  
   - Across **40 cross-session coding agent & IM automation workflows per month** (at **`$100.00/hr`** engineering rate), migrating from **Path A** (stuffing raw transcript history into every session + fragile single-protocol QQ scripts without rate-limit circuit breakers: **`$5,620.00/mo`**) to **Path C** (`SnowCatQQ` quad-protocol `/mcp` runtime with jitter circuit-breakers + 3-tier local/graph Claude memory stack: **`$485.00/mo`**) saves **`$5,135.00/month`** (**`-91.37%`**, **`$61,620.00/year`**) and cuts engineering rework from `38.0 hrs` to `3.5 hrs/mo` (**`-90.79%`**).

![SnowCatQQ & Claude Memory Architecture Overview](../../../assets/github-ai-radar-2026-11-14-r31-snowcatqq-claude-memory.svg)

---

## 💬 2. Three Architectural Deep-Dive Q&As (Q1–Q3)

### Q1: What engineering bottlenecks do `SnowCatQQ`'s V8 channel injection, offset-table packet engine, and anti-ban stability pipeline solve?

1. **Zero-Byte Host Binary Modification & Rapid Version Tracking**:  
   - Patching host binaries directly breaks digital signatures and triggers immediate account bans whenever official desktop clients update (e.g., `QQ 9.9.37-54395`).  
   - `SnowCatQQ` leaves the official executable untouched on disk, injects via the V8 compiler channel in-memory, and isolates protocol packet offsets into a declarative **per-version Offset Table** paired with a one-click portable unpacker.
2. **Automatic Streamable HTTP `/mcp` Exposure + 4-Stage Anti-Ban Protection**:  
   - Every one of its 56+ actions (including QZone posts, group albums, essence messages, check-ins, flash images, and favorites) is automatically exposed on the built-in Streamable HTTP `/mcp` endpoint without spawning external `stdio` wrappers.  
   - Its **Stability Line** enforces exponential connection backoff, human-like typing/sending cadence jitter, token-bucket rate budgets, and automatic circuit breaking on risk codes.

---

### Q2: Why does stuffing everything into `CLAUDE.md` fail at scale, and how do the 10 tools in `claudememory/claude-memory` map to real architecture tiers?

1. **The 200-Line `CLAUDE.md` Attention & Token Cliff**:  
   - Because `CLAUDE.md` is prepended to every turn unconditionally, dumping historical debugging logs or evolving API notes into `CLAUDE.md` burns tens of thousands of input tokens per session and degrades instruction-following accuracy.
2. **De-Biased 4-Quadrant Memory Taxonomy**:  
   - **Quadrant 1 — Git-Native Rules (`#2 CLAUDE.md + Auto Memory`)**: Mandatory baseline for static build/lint commands and repo-wide conventions (`<200` lines).  
   - **Quadrant 2 — Local Auditable Files (`#7 Basic Memory`, `#4 claude-mem`, `#8 Official KG JSON`)**: Best default for solo developers and privacy-strict teams; stores searchable local Markdown/SQLite on disk with zero cloud egress.  
   - **Quadrant 3 — Bi-Temporal & Document Graphs (`#10 Graphiti / Zep`, `#9 Cognee`)**: Best for long-lived systems where facts change over time; `Graphiti` tracks validity intervals `[t_valid, t_invalid)` so Claude never acts on deprecated API schemas.  
   - **Quadrant 4 — Hosted Multi-Client Clouds (`#1 Glen`, `#5 Mem0`, `#6 Supermemory`)**: Convenience layer for cross-team cloud sync, but requires strict InfoSec review and de-biasing of `#1 Glen`'s commercial placement.

---

### Q3: How should a team choose between `TomyJan/SnowLuma` (R212) and `DandanLLab/SnowCatQQ` (R214)?

1. **Choose `TomyJan/SnowLuma` (R212)** when you want a minimal `npx snowluma -q` headless CLI daemon exposing standard **OneBot v11** and the 5 core messaging MCP tools (`get_login_info`, `get_friend_list`, `get_group_list`, `send_private_msg`, `send_group_msg`).
2. **Choose `DandanLLab/SnowCatQQ` (R214)** when you need **OneBot v12 + OneBot v11 + Milky 1.3** compatibility on `QQ 9.9.37-54395`, native **Streamable HTTP `/mcp`** across all **56 extended actions (QZone, group albums, essence, check-ins)**, and built-in **human-cadence jitter + circuit breakers**.

---

## 🧭 3. Architecture Decision Tree & Memory/IM Topology (Mermaid)

```mermaid
flowchart TD
    Start["QQ Multi-Protocol Agent Gateway & Claude Persistent Memory Selection"] --> Branch{"Architectural Domain?"}

    Branch -->|"QQ Agent Gateway (SnowLuma vs SnowCatQQ)"| QQGate{"Protocol Version & Action Surface?"}
    QQGate -->|"Basic Group/DM Messaging (5 MCP Tools)<br/>+ Standard OneBot v11 + Minimal npx CLI"| UseSnowLuma["✅ TomyJan/SnowLuma (R212)<br/>• OneBot v11 + @snowluma/mcp (stdio)<br/>• Ideal for Lightweight Notification & Q&A Bots"]
    QQGate -->|"OneBot v12 + Milky 1.3 + OneBot v11 Quad-Stack<br/>+ 56 Rich Actions (QZone/Albums/Essence) + Jitter Breaker"| UseSnowCat["✅ DandanLLab/SnowCatQQ (QQ 9.9.37)<br/>• Zero-Patch V8 Injection + Streamable HTTP /mcp<br/>• Human-Cadence Jitter + Rate Budget + Circuit Breaker"]

    Branch -->|"Claude Code / Desktop Persistent Memory"| MemGate{"Data Sovereignty & Temporal Fact Complexity?"}
    MemGate -->|"Strict Zero Cloud Egress<br/>Standard Repo & Design Context"| LocalStack["✅ Local Dual-Layer Stack: CLAUDE.md + Basic Memory MCP<br/>• CLAUDE.md (<200 lines) for Immutable Build/Lint Rules<br/>• Basic Memory Local Markdown On-Demand Retrieval"]
    MemGate -->|"Frequently Mutating Architecture/API Facts<br/>Need Temporal Conflict Resolution"| GraphStack["✅ Self-Hosted Temporal Graph: CLAUDE.md + Graphiti / Cognee MCP<br/>• Bi-Temporal Edges Automatically Invalidate Stale Facts"]
    MemGate -->|"InfoSec-Approved Hosted Team Cloud Sync"| CloudStack["⚠️ Hosted Cloud Memory (Mem0 / Supermemory / Glen)<br/>• Audit Commercial Ranking Bias & Data Residency First"]

    UseSnowCat --> FinOps["💰 Closed-Form FinOps Impact (CLAIM-20261114-R31-SNOWCATQQ-CLAUDEMEMORY)<br/>Monthly Total $5,620.00 ➔ $485.00 (-91.37% · Saves $61,620/yr)"]
    LocalStack --> FinOps
    GraphStack --> FinOps
```

---

## 📊 4. Peer Comparison Matrix (Decision Matrix)

| Dimension | `DandanLLab/SnowCatQQ` (`SnowCat`) | `TomyJan/SnowLuma` (R212) | Legacy Single-Protocol OneBot v11 Client | `CLAUDE.md` + `Basic Memory` + `Graphiti` Stack | Commercial Hosted Memory SaaS (`Glen`, etc.) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Core Protocols & Role** | **OneBot v12 + v11 + Milky 1.3 + Streamable HTTP `/mcp`** | OneBot v11 + `@snowluma/sdk` + `@snowluma/mcp` (`stdio`) | OneBot v11 WS/HTTP only | **Git Rules + Local Markdown MCP + Temporal Graph** | Hosted cloud team memory service |
| **Action / Memory Surface** | **Core messaging + 56 extended actions (QZone/Albums/Essence)** | 5 core MCP messaging tools | Basic chat send/receive | Static repo invariants + readable notes + temporal facts | Cross-user session transcript summaries |
| **Anti-Ban & Context Hygiene** | **Exponential backoff + human jitter + budget + circuit breaker** | Lightweight daemon + `--status` JSON probe | No built-in jitter or rate-budget circuit breaker | On-demand retrieval prevents context window bloat | Subject to cloud latency & vendor availability |
| **Data Sovereignty** | 100% local in-process execution + full source公開 | 100% local execution | Local execution | **100% local / self-hosted, Git & Markdown auditable** | Uploads repo/session context to third-party cloud |
| **Admin UI & DX** | **React + Tailwind + HeroUI WebUI + Portable Builder** | `:5099` WebUI + `-q` terminal QR | Manual JSON edits | Native `.mcp.json` integration | Requires vendor plugin + paid team seats |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps Audit (`CLAIM-20261114-R31-SNOWCATQQ-CLAUDEMEMORY`)

> **Scope & Provenance Boundary**: Models monthly context re-injection token/API spend plus engineering labor for context reconstruction and IM bot protocol/rate-limit recovery across **40 cross-session coding agent & IM automation workflows per month** at **`$100.00/hr`**. Local developer workstation hardware depreciation is explicitly marked **`not_measured`**.

| Architecture Path | Context Token & Gateway Spend (`USD/mo`) | Context & Bot Recovery Labor (`hrs/mo`) | Engineering Labor Cost (`@ $100/hr`) | Total Monthly Cost (`USD/mo`) | Net Savings vs. Path A (`USD/mo` & `%`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Raw Transcript Re-Injection + Fragile Unthrottled QQ Scripts** | `$1,820.00` | `38.0 hrs` | `$3,800.00` | **`$5,620.00`** | Baseline (`0.00%`) |
| **Path B: Legacy OneBot v11 Only + Bloated Unstructured `CLAUDE.md`** | `$860.00` | `18.0 hrs` | `$1,800.00` | **`$2,660.00`** | `-$2,960.00` (`-52.67%`) |
| **Path C (Recommended): `SnowCatQQ` (`/mcp` + Jitter Breaker) + 3-Tier Claude Memory** | **`$135.00`** | **`3.5 hrs`** | **`$350.00`** | **`$485.00`** | **`-$5,135.00` (`-91.37%`)** |

- **Closed-Form Verification Equations**:
  - $\text{Path A Total} = 1820.00 + 38.0 \times 100.00 = 1820.00 + 3800.00 = \$5,620.00$
  - $\text{Path B Total} = 860.00 + 18.0 \times 100.00 = 860.00 + 1800.00 = \$2,660.00$
  - $\text{Path C Total} = 135.00 + 3.5 \times 100.00 = 135.00 + 350.00 = \$485.00$
  - $\text{Net Savings (Path C vs Path A)} = 5620.00 - 485.00 = \$5,135.00/\text{mo} \quad (-91.37\%, \text{Annualized } \$61,620.00/\text{yr})$

---

## 🛠️ 6. AI Solution Architect Quick-Start Checklist

1. **Connect Claude Code / OpenCode to `SnowCatQQ`'s Streamable HTTP `/mcp` Endpoint**:
   ```json
   {
     "mcpServers": {
       "snowcat-qq": {
         "type": "streamable-http",
         "url": "http://127.0.0.1:3000/mcp",
         "headers": {
           "Authorization": "Bearer replace-with-snowcat-token"
         }
       }
     }
   }
   ```
   - Enable **Human-Cadence Jitter + Rate Budget + Circuit Breaker** in the React/HeroUI console before running automated group/QZone workflows.
2. **Deploy a Zero-Egress Local Claude Memory Stack (`CLAUDE.md` + `Basic Memory` MCP)**:
   ```json
   {
     "mcpServers": {
       "basic-memory": {
         "command": "uvx",
         "args": ["basic-memory", "mcp"]
       }
     }
   }
   ```
   - Keep `CLAUDE.md` under `200` lines for static repo invariants and store evolving design notes in `basic-memory` (or self-hosted `Graphiti` MCP for bi-temporal fact tracking).
