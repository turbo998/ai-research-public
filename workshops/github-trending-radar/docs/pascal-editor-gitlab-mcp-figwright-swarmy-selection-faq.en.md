# Browser WebGPU 3D AECO/Scan-to-BIM Editor (`pascalorg/editor`), 288-Tool Enterprise GitLab MCP (`zereight/gitlab-mcp`), Seat-Free Two-Way Figma MCP (`awdr74100/figwright`) & Real-Time Multi-CLI Terminal Analytics (`koorchik/swarmy`) Selection & Integration Architecture FAQ

> **Document Type**: Enterprise AI Solution Architect Selection Decision Guide (GitHub Trending AI Radar — 2026-11-25 Night Round 7 / Cumulative Round 889)
> **Covered Repositories**: [`pascalorg/editor`](https://github.com/pascalorg/editor) (`★ 25,747`, `3,209 forks`, `MIT`: browser-first, local-first 3D architecture and **Scan-to-BIM** software for AECO built with React Three Fiber and WebGPU [`@pascal-app/core`, `@pascal-app/viewer`], featuring native CLI and MCP server integration so AI agents can read, model, validate, and save sites, levels, walls, slabs, roofs, openings, rooms, and furniture) · [`zereight/gitlab-mcp`](https://github.com/zereight/gitlab-mcp) (`★ 2,126`, `376 forks`, `MIT`: comprehensive GitLab MCP Server [`@zereight/mcp-gitlab`] exposing **288 tools** across projects, merge requests, issues, CI/CD pipelines, and wikis via GitLab REST/GraphQL APIs) · [`awdr74100/figwright`](https://github.com/awdr74100/figwright) (`★ 1,552`, `100 forks`, `MIT`: free, two-way Figma MCP server [`@figwright/mcp`] paired with a local WebSocket Figma plugin—requiring no paid Figma Dev Mode seat—to both read de-duplicated design context into framework-aware code and write generated code back onto the Figma canvas) · [`koorchik/swarmy`](https://github.com/koorchik/swarmy) (`★ 49`, `5 forks`, `MIT OR Apache-2.0`: single-binary, local-only, read-only Rust terminal analytics dashboard uniting Claude Code, OpenAI Codex, and Google Antigravity on one screen with live subagent trees, API-equivalent spend, weekly project limits, worktrees, and login vault)
> **Core Enterprise Scenario**: Connecting **3D AECO/BIM spatial modeling and two-way 2D Figma UI design directly into self-managed GitLab CI/CD delivery pipelines while monitoring multi-vendor coding agent fleets in real time**.

---

## 1. 📌 Executive Summary (One-Line Selection Verdict)

1. **Need browser-native WebGPU 3D building modeling and Scan-to-BIM where AI agents can read, edit, and validate architectural scenes via MCP** ➔ Choose **[`pascalorg/editor`](https://github.com/pascalorg/editor) (`★ 25,747`, `3,209 forks`, `MIT`)**.
   - **Plain-English Mechanism**: Runs locally in the browser on WebGPU or via CLI, allowing teams to import 3D point-cloud scans as reference layers and let MCP-connected agents model editable walls, slabs, roofs, openings, and rooms with automated validation.
2. **Need full-lifecycle DevSecOps automation on Self-Managed GitLab or GitLab.com covering Merge Requests, CI/CD pipelines, issues, and wikis** ➔ Choose **[`zereight/gitlab-mcp`](https://github.com/zereight/gitlab-mcp) (`★ 2,126`, `376 forks`, `MIT`)**.
   - **Plain-English Mechanism**: Provides **288 production-tested tools** (`@zereight/mcp-gitlab`) over GitLab's REST and GraphQL APIs, verified by CodeQL and OpenSSF Scorecard checks.
3. **Need two-way synchronization between Figma canvases and production frontend code without buying expensive per-developer Figma Dev Mode seats** ➔ Choose **[`awdr74100/figwright`](https://github.com/awdr74100/figwright) (`★ 1,552`, `100 forks`, `MIT`)**.
   - **Plain-English Mechanism**: Pairs `@figwright/mcp` with a lightweight Figma plugin over a local WebSocket relay—reading de-duplicated layout/typography/variable tokens into code AND pushing code-side component updates back onto the Figma canvas.
4. **Need a single-binary terminal dashboard to watch every live agent and subagent across Claude Code, OpenAI Codex, and Google Antigravity along with API-equivalent spend and worktrees** ➔ Choose **[`koorchik/swarmy`](https://github.com/koorchik/swarmy) (`★ 49`, `5 forks`, `MIT OR Apache-2.0`)**.
   - **Plain-English Mechanism**: Runs 100% locally and read-only as a static Rust binary across Linux, macOS, Windows, and Raspberry Pi, highlighting blocked subagents awaiting human input and tracking weekly project budgets.

---

## 2. 🎯 Architect & Customer Deep-Dive Q&A

### Q1: How does this open-source design-to-delivery stack compare against commercial enterprise suites (e.g., Autodesk Cloud + Figma Dev Mode Enterprise + GitLab Duo Enterprise)?

- **Four-Stage Open-Source Workflow (Path C)**:
  1. **3D Spatial & Scan-to-BIM Authoring ➔ `pascalorg/editor`**: Browser WebGPU 3D building editor + agent MCP scene manipulation.
  2. **Bi-Directional 2D UI Design-to-Code ➔ `awdr74100/figwright`**: Seat-free two-way Figma canvas read/write over local WebSocket.
  3. **Self-Managed GitLab DevSecOps Automation ➔ `zereight/gitlab-mcp`**: 288 tools for MRs, CI/CD job logs, issues, and wikis.
  4. **Multi-CLI Fleet & Spend Observability ➔ `koorchik/swarmy`**: Unified terminal HUD across Claude Code, Codex, and Antigravity.
- **When to choose Commercial Suites vs. Path C?**
  - Choose commercial vendor add-ons if your organization is locked into proprietary desktop CAD formats and already pays for enterprise-wide Figma Dev Mode and GitLab Duo seats.
  - Choose **Path C** when eliminating per-seat Figma Dev Mode fees, requiring two-way code-to-Figma writeback, building WebGPU 3D digital-twin/AECO apps, or orchestrating multi-vendor coding CLIs against self-hosted GitLab.

### Q2: How do these four tools wire together in production?

1. **Bi-Directional 3D & 2D Design Plane (`pascalorg/editor` + `awdr74100/figwright`)**:
   - Spatial layouts are modeled and validated via `Pascal Editor` MCP while UI component specs are synced bi-directionally between Figma and React/Vue via `Figwright`.
2. **Multi-CLI Execution & Budget Tracking (`koorchik/swarmy`)**:
   - Engineers run parallel subagents across isolated Git worktrees while `swarmy` tracks live status, human-input prompts, and weekly spend caps.
3. **Automated GitLab Merge Request & CI Loop (`zereight/gitlab-mcp`)**:
   - Agents open MRs, inspect failing GitLab CI jobs, push fixes, and update project documentation via `@zereight/mcp-gitlab`'s 288 tools.

### Q3: What are the critical security guardrails?

- **Architect Redlines**:
  1. **Bind `figwright` WebSocket relay strictly to `127.0.0.1`**: Never expose the local Figma plugin relay socket to external network interfaces.
  2. **Enforce GitLab Protected Branch rules**: Scope `zereight/gitlab-mcp` tokens so agents can open MRs and comment on diffs but cannot force-push to protected production branches.

---

## 3. 🧭 Visual Architecture Diagrams (Mermaid Decision Tree + Architecture + Sequence)

![Night Round 7 (R889) pascalorg/editor + gitlab-mcp + figwright + swarmy Architecture](../../../assets/github-ai-radar-2026-11-25-r7-r889-pascaleditor-gitlabmcp-figwright-swarmy.svg)

### 3.1 Architect Selection Decision Tree

```mermaid
flowchart TD
    A["Enterprise 3D BIM/UI Design, GitLab DevSecOps & Multi-CLI Fleet Selection"] --> B{"Primary Workflow Bottleneck?"}
    B -- "Browser WebGPU 3D building modeling, Scan-to-BIM & agent MCP scene editing" --> C["pascalorg/editor<br/>(★25,747 · MIT · WebGPU 3D AECO Editor + CLI/MCP)"]
    B -- "Full automation across self-managed GitLab MRs, CI/CD pipelines, issues & wikis" --> D["zereight/gitlab-mcp<br/>(★2,126 · MIT · 288-Tool REST/GraphQL GitLab MCP)"]
    B -- "Two-way Figma design-to-code & code-to-canvas sync without Dev Mode seats" --> E["awdr74100/figwright<br/>(★1,552 · MIT · Local WebSocket Two-Way Figma MCP)"]
    B -- "Live terminal dashboard for Claude Code, Codex & Antigravity subagents/spend" --> F["koorchik/swarmy<br/>(★49 · Apache-2.0 · Read-Only Single-Binary Fleet HUD)"]
```

### 3.2 End-to-End Enterprise Integration Architecture

```mermaid
flowchart LR
    subgraph Design_Plane["1. 3D BIM & 2D UI Bi-Directional Design"]
        PASCAL["pascalorg/editor (MIT · ★25.7k)<br/>WebGPU 3D AECO / Scan-to-BIM · @pascal-app MCP"]
        FIG["awdr74100/figwright (MIT)<br/>Seat-Free Two-Way Figma MCP (Read Code / Write Canvas)"]
    end

    subgraph Agent_Monitor["2. Multi-CLI Fleet & Spend HUD (swarmy)"]
        PASCAL --> SWARM["koorchik/swarmy (Apache-2.0 · Rust)<br/>Live Claude Code + Codex + Antigravity · Worktrees & Spend"]
        FIG --> SWARM
    end

    subgraph GitLab_Delivery["3. Self-Managed GitLab Delivery (gitlab-mcp)"]
        SWARM --> GL["zereight/gitlab-mcp (MIT)<br/>288 Tools · Merge Requests · CI/CD Pipelines · Issues · Wikis"]
    end
```

### 3.3 End-to-End Execution Sequence

```mermaid
sequenceDiagram
    participant Dev as Designer / Engineer
    participant Design as Pascal 3D Editor + Figwright Figma MCP
    participant Agent as Coding Agent Fleet (Monitored by swarmy)
    participant GitLab as zereight/gitlab-mcp (288 Tools)

    Dev->>Design: 1. Update 3D Scan-to-BIM layout in Pascal & select UI frame in Figma
    Design-->>Agent: 2. Stream structured 3D scene & de-duplicated Figma tokens via MCP
    Agent->>Agent: 3. Execute parallel implementation in Git worktrees (tracked live in swarmy)
    Agent->>Design: 4. Push updated component variants back to Figma canvas via Figwright Write
    Agent->>GitLab: 5. Open Merge Request & monitor CI/CD pipeline jobs via gitlab-mcp (288 tools)
    GitLab-->>Dev: 6. Deliver passing MR & updated GitLab project wiki
```

---

## 4. 📊 Horizontal Selection Matrix

| Dimension | `pascalorg/editor` (`★ 25,747`) | `zereight/gitlab-mcp` (`★ 2,126`) | `awdr74100/figwright` (`★ 1,552`) | `koorchik/swarmy` (`★ 49`) | Commercial Enterprise Stack (Desktop BIM + Figma Dev Mode + GitLab Duo) | One-Way Screenshot Prompting + Unmonitored CLI Tabs (Path B) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Primary Role** | WebGPU 3D AECO/Scan-to-BIM editor & MCP | 288-tool GitLab REST/GraphQL MCP | Seat-free two-way Figma MCP server | Multi-CLI terminal fleet & spend HUD | High-cost per-seat proprietary SaaS/desktop stack | Screenshot-to-CSS guessing & manual tab switching |
| **Key Differentiator** | **Browser WebGPU + Scan-to-BIM + native MCP scene editing** | **288 tools covering MRs, pipelines, issues & wikis** | **Two-way Read/Write Figma sync with zero Dev Mode seats** | **Unites Claude Code, Codex & Antigravity live in 1 binary** | Vendor-supported, but high per-seat cost & one-way Figma lock-in | Loses design variables; stalled background subagents go unnoticed |
| **License** | `MIT` | `MIT` | `MIT` | `MIT OR Apache-2.0` | Proprietary | Ad-hoc scripts |
| **Monthly TCO (45-Eng Team)** | **`$305.00/mo` combined** (`$65.00` runner compute + `2.4h` ops) | Included in `$305.00/mo` stack | Included in `$305.00/mo` stack | Included in `$305.00/mo` stack | **`$9,350.00/mo`** (`$4,800.00` BIM/Dev Mode/Duo seats + `45.5h` sync labor) | `~$3,150.00/mo` (manual UI/BIM drift fixes & pipeline debugging) |

---

## 5. 🧪 Quantitative FinOps & TCO Comparison (45-Person Enterprise Team)

> **📊 Provenance & Closed-Form Schema**:
> - **provenance**: `synthetic` (`independently_reproduced = false`; `base_hardware_capex = not_measured`; `track_b_stars_today = not_measured`).
> - **Closed-Form Formula**:
>   - **Path A (Commercial BIM & Per-Seat Figma Dev Mode + Commercial GitLab Add-Ons + Manual Two-Way Design/Code Sync & Multi-Terminal Triage)**: **`$4,800.00`** monthly seat licenses + **`45.5h × $100.00/h = $4,550.00`** engineering/design sync labor = **`$9,350.00/mo`**.
>   - **Path C (`pascalorg/editor` + `zereight/gitlab-mcp` + `awdr74100/figwright` + `koorchik/swarmy` Stack)**: **`$65.00`** shared CI runner compute + **`2.4h × $100.00/h = $240.00`** plugin/MCP maintenance = **`$305.00/mo`**.
>   - **Net Savings vs. Path A**: **`-$9,045.00/mo`** (**`96.74%`** TCO reduction).

| Evaluation Path | Commercial Seat Licenses & Compute | Design-Code Sync & CI Triage Labor (`$100/h`) | Monthly Total TCO | Net Savings vs. Path A | Key Architectural Outcome |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Path A: Commercial BIM + Figma Dev Mode Seats + Manual Sync** | `$4,800.00` | `45.5h` (`$4,550.00`) | **`$9,350.00`** | Baseline | Expensive per-seat licensing; manual code-to-Figma redraws |
| **Path B: One-Way Screenshots + Manual GitLab Web UI Ops** | `$1,400.00` | `17.5h` (`$1,750.00`) | **`$3,150.00`** | `-$6,200.00` (`-66.31%`) | Lost design tokens; zero visibility across concurrent CLI subagents |
| **Path C: `pascalorg/editor` + `gitlab-mcp` + `figwright` + `swarmy`** | **`$65.00`** | **`2.4h` (`$240.00`)** | **`$305.00`** | **`-$9,045.00` (`-96.74%`)** | **WebGPU 3D BIM MCP + 288-tool GitLab + 2-way Figma + 3-CLI live HUD** |

- 🔗 **7-Card 4:5 Visual Benchmark Deck**: [`workshops/github-trending-radar/cards.en.html`](../cards.en.html) · [`cards.html`](../cards.html)

---

## 6. 🛠️ Enterprise Adoption & Architecture Review Checklist

- [ ] **Scene Validation Gate in `pascalorg/editor`**: Run automated spatial and structural validation before committing agent-edited 3D BIM models.
- [ ] **Scoped Project Tokens for `zereight/gitlab-mcp`**: Restrict agent GitLab tokens to MR creation, CI log inspection, and comment posting while keeping branch merges human-approved.
- [ ] **Staging Frame Isolation in `awdr74100/figwright`**: Configure two-way Figma writes to target dedicated staging frames rather than overwriting locked design-system master components.
- [ ] **Weekly Spend Alerts in `koorchik/swarmy`**: Track API-equivalent spend and subagent stalls across Claude Code, Codex, and Antigravity worktrees.
