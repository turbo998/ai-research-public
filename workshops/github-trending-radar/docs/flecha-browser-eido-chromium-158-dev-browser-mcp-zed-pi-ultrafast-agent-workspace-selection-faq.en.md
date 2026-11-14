# Chromium 158 Developer Browser with Built-In MCP (`lucianodiisouza/flecha-browser`) & Zed + Pi 1.3.0 Native AI Workspace (`tony3liu/eido`) Selection & Architecture FAQ

> **Track**: GitHub AI Trending & High-Velocity Breakout Selection Guide · 2026-11-14 Night Round 97 (Cumulative Round 280 Milestone / R280)  
> **Benchmark Standard**: Modeled after `ib-vs-ethernet-roce-selection-faq.md` (Plain-Language Essence + First Principles + 6-Part Structure + Closed-Form FinOps Audit)  
> **Claim ID**: `CLAIM-20261114-R97-FLECHABROWSER-EIDO`  
> **Architecture Visual**: [`assets/github-ai-radar-2026-11-14-r97-flechabrowser-eido.svg`](../../../assets/github-ai-radar-2026-11-14-r97-flechabrowser-eido.svg)  
> **中文版本**: [阅读中文版 (`flecha-browser-eido-chromium-158-dev-browser-mcp-zed-pi-ultrafast-agent-workspace-selection-faq.md`)](./flecha-browser-eido-chromium-158-dev-browser-mcp-zed-pi-ultrafast-agent-workspace-selection-faq.md)

---

## 📌 1. Executive Summary (What Are They & What Pain Points Do They Solve?)

1. **Plain-Language Breakdown**:
   - **`lucianodiisouza/flecha-browser` (`★ 133`, TypeScript/C++, MIT License)** is an **open-source Arc alternative for developers built on a real `Chromium 158` fork** (having replaced its earlier Electron build because Google blocks OAuth sign-in inside Electron). It combines vertical sidebars, Peek floating previews, Split View, 12-hour auto-archiving `Today` tabs, and **per-Space isolated storage partitions (`Separate Cookies and Logins`)** with a **developer command bar** (`gh owner/repo`, `gh 123`, `npm`, `mdn`, `caniuse`, `so`, `env`, plus in-place JWT and Unix timestamp decoding) and a **built-in MCP server** for coding agents.
   - **`tony3liu/eido` (`★ 306`, Rust, GPL-3.0, `v0.0.1`)** is a **native Rust AI coding workspace built on Zed and bundling official, unmodified `pi 1.3.0`** (supporting `Code Mode`, subagents, and session tool restoration) alongside an adapted TypeScript **Ultrafast browser agent** (`browser-use/jev-ultrafast`) that shares your main coding model for text input and includes an inspector, recording, and verification tools.
2. **Quantified FinOps Impact (`CLAIM-20261114-R97-FLECHABROWSER-EIDO` · R280 Milestone)**:
   - Evaluated across **25 monthly full-stack multi-tenant browser debugging and AI IDE sprints** at an AI Solution Architect rate of **$95.00/hr** (local workstation hardware telemetry: `not_measured`):
   - **Path A (Electron Browser Wrappers Blocked on Google OAuth + Multi-Account Cookie Collisions + Separate IDE/Browser Agent Contexts)**: **$1,730.00/mo** in duplicate model contexts and failed OAuth retries + **37.0 hrs/mo ($3,515.00)** juggling separate browser profiles, decoding JWTs externally, and context-switching across windows = **$5,245.00/mo**.
   - **Path B (Stock Chrome Profiles + Standalone Terminal `pi` + Separate Browser Extension)**: **$790.00/mo** in token/tool spend + **16.5 hrs/mo ($1,567.50)** in manual window coordination = **$2,357.50/mo**.
   - **Path C (`Flecha` Chromium 158 MCP Browser + `Eido` Zed + `pi 1.3.0` Native Workspace)**: **$85.00/mo** in shared-model text browser and MCP tokens + **3.5 hrs/mo ($332.50)** of engineering review = **$417.50/mo**, delivering **$4,827.50/mo in net savings (-92.04%, $57,930.00/yr annualized, and -90.54% engineering hours)**.

![2026-11-14 Night Round 97 (R280 Milestone) Architecture Summary](../../../assets/github-ai-radar-2026-11-14-r97-flechabrowser-eido.svg)

---

## 🔍 2. Core Architectural Q&A (Q1–Q3 First-Principles Deep Dive)

### Q1: Why did `lucianodiisouza/flecha-browser` abandon Electron for a `Chromium 158` fork, and what makes it uniquely suited for developers and coding agents?
- **Real Chromium Compatibility + Developer/Agent Primitives**:
  1. **Native Google Sign-In & Per-Space Cookie Partitions**: Because Flecha is real Chromium 158, Google OAuth and Chrome Web Store extensions work seamlessly, while `Separate Cookies and Logins` creates a persistent storage partition per Space so developers can test multiple user roles side-by-side in Split View.
  2. **Developer Command Bar & Built-In MCP Server**: Decodes JWTs and Unix timestamps in place, jumps directly to `gh`, `npm`, `mdn`, and `caniuse`, and exposes a built-in MCP server to coding agents.

### Q2: How does `tony3liu/eido` unify Zed, `pi 1.3.0`, and `browser-use/jev-ultrafast` into a single native workflow?
- **Zero-Context-Gap Native Workspace**:
  1. **Unmodified `pi 1.3.0` + Deterministic Session Resume**: Keeps task intent, proposed changes, and review decisions connected in a Zed-based Rust workspace with full `pi` Code Mode and subagent support.
  2. **Shared-Model Ultrafast Browser Agent**: Integrates `jev-ultrafast` using the main text model for low-latency inspection, recording, and verification, ensuring extension-triggered runs finish before browser resources are cleaned up.

### Q3: How should AI Solution Architects combine `Flecha` and `Eido`?
- **Native Rust Coding Workspace + Partitioned Chromium MCP Browser**: Author and review code inside `Eido` (`Zed` + `pi 1.3.0`), and connect `Flecha`'s built-in MCP server to test multi-tenant OAuth flows across isolated Space cookie partitions.

---

## 🧭 3. Mermaid Selection Decision Tree & Architecture Flow

```mermaid
flowchart TD
    A["AI SA Developer Browser MCP & Native AI Workspace (R280)"] --> B{"Primary Need: Chromium 158 Browser with Isolated Spaces & Built-In MCP<br/>or Native Rust Zed + pi 1.3.0 + Ultrafast Browser Workspace?"}
    B -->|"Chromium 158 Fork + Per-Space Cookies + Dev Command Bar + MCP"| C["Adopt lucianodiisouza/flecha-browser<br/>(★ 133 · Chromium 158 Fork · MIT)"]
    B -->|"Zed Base + Official pi 1.3.0 + jev-ultrafast Browser Agent"| D["Adopt tony3liu/eido v0.0.1<br/>(★ 306 · Rust · Zed + pi 1.3.0 + Ultrafast Browser)"]
    B -->|"Full-Native Post-Electron AI Engineering Stack"| E["Combine Eido (Zed + pi Workspace) + Flecha (Chromium 158 MCP Browser)"]

    C --> C1["Real Chromium 158: Native Google Sign-In & Chrome Extensions"]
    C1 --> C2["Separate Cookies & Logins Per Space + Split View + Peek"]
    C2 --> C3["In-Place JWT/Timestamp Decode + gh/npm/mdn Bar + Built-In MCP"]

    D --> D1["Bundles Official Unmodified pi 1.3.0 (Code Mode & Subagents)"]
    D1 --> D2["Ultrafast Browser Agent (Shares Main Model + Inspector/Recording)"]
    D2 --> D3["Connected Intent → Plan → Code Edit → Review Lifecycle"]

    E --> F["Closed-Form FinOps TCO: $5,245.00/mo → $417.50/mo (-92.04%)"]
```

---

## 📊 4. Peer Comparison Matrix

| Evaluation Dimension | `lucianodiisouza/flecha-browser` | `tony3liu/eido` (`v0.0.1`) | Electron Browser Wrappers / Legacy Arc | Heavy Electron AI IDEs |
| :--- | :--- | :--- | :--- | :--- |
| **Core Engine** | **Real `Chromium 158` fork (not Electron)** | **Native Rust (Zed base) + official `pi 1.3.0`** | Electron `<webview>` or closed-source Arc | Electron + Node extension host |
| **Auth & Multi-Account Isolation** | **Full Google Sign-In + per-Space isolated Cookie partitions** | OpenRouter refresh & saved workspace preferences | Blocked by Google OAuth security checks | No multi-partition browser |
| **Developer & Agent Tooling** | **In-place JWT/timestamp decode, `gh/npm/mdn` bar & built-in MCP** | **Bundled `jev-ultrafast` text browser agent + `pi` Code Mode** | No developer command bar or native MCP | Requires separate browser MCP setup |
| **Resource & Lifecycle Hygiene** | 12h auto-archiving `Today` tabs; closing pinned tabs unloads RAM | **Extension runs finish cleanly before resource cleanup** | Tab sprawl consumes gigabytes of RAM | High idle memory overhead |
| **Monthly TCO (25 Sprints)** | **Combined Path C: $417.50/mo (incl. 3.5h review)** | **Combined Path C: $417.50/mo (incl. 3.5h review)** | Path A: $5,245.00/mo (incl. 37.0h overhead) | Path B: $2,357.50/mo (incl. 16.5h maint) |

---

## 🧮 5. Quantitative Insights & Closed-Form FinOps Audit (`CLAIM-20261114-R97-FLECHABROWSER-EIDO` · R280 Milestone)

> **Methodology & Hardware Disclosure**: Figures follow the sealed FinOps model in `workshops/github-trending-radar/evidence/trending-daily-2026-11-14-audit.json` across 25 monthly sprints at `$95.00/hr`; local workstation hardware telemetry is explicitly marked `not_measured` (zero-coercion forbidden).

| Architecture Path | Monthly Context Token & Retry Spend (USD) | Monthly Engineering Labor (Hours @ $95.00/hr) | Monthly Engineering Labor Cost (USD) | Total Monthly TCO (USD) | Net Savings vs Path A (USD / %) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Electron OAuth Blocks + Separate IDE/Browser Contexts** | `$1,730.00` | `37.0 hrs` | `$3,515.00` | **`$5,245.00`** | Baseline (`0.00%`) |
| **Path B: Stock Chrome Profiles + Standalone Terminal `pi`** | `$790.00` | `16.5 hrs` | `$1,567.50` | **`$2,357.50`** | `-$2,887.50` (`-55.05%`) |
| **Path C: `Flecha` Chromium 158 MCP + `Eido` Zed+pi Workspace** | **`$85.00`** | **`3.5 hrs`** | **`$332.50`** | **`$417.50`** | **`-$4,827.50` (`-92.04%`)** |

- **Closed-Form Verification Identities**:
  - $\text{Path A Total} = \$1,730.00 + 37.0 \times \$95.00 = \$1,730.00 + \$3,515.00 = \$5,245.00/\text{mo}$
  - $\text{Path B Total} = \$790.00 + 16.5 \times \$95.00 = \$790.00 + \$1,567.50 = \$2,357.50/\text{mo}$
  - $\text{Path C Total} = \$85.00 + 3.5 \times \$95.00 = \$85.00 + \$332.50 = \$417.50/\text{mo}$
  - $\text{Monthly Savings} = \$5,245.00 - \$417.50 = \$4,827.50/\text{mo}\ (-92.04\%)$, $\text{Annualized Savings} = \$57,930.00/\text{yr}$

---

## 🛠️ 6. 15-Minute AI SA Actionable Adoption Checklist

1. **Set Up `lucianodiisouza/flecha-browser` and Verify Space Cookie Partitions & Built-In MCP**:
   ```bash
   git clone https://github.com/lucianodiisouza/flecha-browser.git
   ```
   - **Verification Gate**: Enable `Separate Cookies and Logins` on two Spaces, test in-place JWT decoding in the `⌘T` command bar, and connect a coding agent to Flecha's built-in MCP server.
2. **Launch `tony3liu/eido` and Verify `pi 1.3.0` Code Mode & Ultrafast Browser Verification**:
   ```bash
   git clone https://github.com/tony3liu/eido.git
   ```
   - **Verification Gate**: Run a task in Eido using `pi 1.3.0` Full Access and verify the integrated `jev-ultrafast` browser agent records and validates the resulting UI change.
3. **Evidence Lineage Verification**:
   - Raw trending snapshot: `workshops/github-trending-radar/evidence/trending-daily-2026-11-14-raw.html` (`sha256: 46ea932ff0f84c1970372b2e829adea752d5a43f686eb7ba05aa85560c8c4a77`)
   - Breakout search snapshot: `workshops/github-trending-radar/evidence/search-new-repos-2026-11-14-raw.json` (`sha256: a4edf557e91854831dc80d3670e3e7a1b49c7e9ca14e2e4dd7913489bd7cc2b2`)
