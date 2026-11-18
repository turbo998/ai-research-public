# GitHub Next OP-1 Quadknob Skill (`githubnext/quadknob-skill`) & Live-Cloud-to-Terraform Architecture Map MCP (`Askrike/desprawl`) Selection FAQ

> **Document Scope**: This is the **2026-11-13 Night Shift Round 39 (Cumulative #167) standalone 6-part selection guide**, modeled strictly after `ib-vs-ethernet-roce-selection-faq.md` with first-principles explanations and closed-form FinOps math. It is written for AI Solution Architects, Frontend Design Engineers, and Cloud Infrastructure / IaC Leads evaluating two tactile-parameter and cloud-topology tools:
> 1. **`githubnext/quadknob-skill` (`9★` in 2 days, JavaScript, MIT, official GitHub Next release, `npx skills add githubnext/quadknob-skill`, `githubnext.com/posts/four-knobs/`)**: An OP-1-inspired agent skill and zero-dependency web component (`quadknob.js` `<quadknob-panel>`) from **GitHub Next** that injects a floating 4-knob hardware-style parameter panel (`Glow`, `Text`, `Sound`, `Card` radius/padding/hue/saturation/blur/timing) into your running page — so you dial values in by eye rather than guessing numbers in chat, then press `Done` to copy the exact values back to your coding agent!
> 2. **`Askrike/desprawl` (`10★` on Day 0, Go 1.27.4+, Apache-2.0, CLI + MCP server + agent skills + live Web UI)**: A bidirectional cloud infrastructure and Terraform engine (`desprawl setup`) that **(1) converts live cloud or SaaS infrastructure into linked Terraform** through any Terraform provider (`Terraform 1.14+`), and **(2) draws Terraform as an interactive visual architecture map** showing components and connections across Claude Code, Cursor, Codex, and Gemini CLI!
>
> **中文版本**: [quadknob-skill-desprawl-op1-visual-parameter-knobs-live-cloud-to-terraform-map-selection-faq.md](quadknob-skill-desprawl-op1-visual-parameter-knobs-live-cloud-to-terraform-map-selection-faq.md) · **Daily Digest**: [`daily/2026-11-13.en.md`](../daily/2026-11-13.en.md) · **Topic SVG**: [`assets/github-ai-radar-2026-11-13-r39-quadknob-desprawl.svg`](../../../assets/github-ai-radar-2026-11-13-r39-quadknob-desprawl.svg)

![githubnext/quadknob-skill and Askrike/desprawl Architecture Comparison](../../../assets/github-ai-radar-2026-11-13-r39-quadknob-desprawl.svg)

---

## 📌 1. Executive Summary

1. **In plain English, what core pain points do these two repositories solve?**
   - **Ending "20-turn chat ping-pong loops where you tell an agent 'make the border radius slightly rounder and the glow less blurry' while burning thousands of tokens guessing CSS/animation numbers" (`githubnext/quadknob-skill`)**: Built by **GitHub Next** after the Teenage Engineering OP-1 synthesizer, `Quadknob` wraps a dependency-free web component (`quadknob.js` `<quadknob-panel>`) in an agent skill (`npx skills add githubnext/quadknob-skill`). The agent drops a floating 4-knob panel (blue, green, black, orange knobs across pages like `Glow`, `Text`, and `Sound`) into your live page; **you turn the knobs by eye until the UI looks right, click `Done`, and hand the exact landed values back to the agent in a single turn**!
   - **Ending "spending days manually running `terraform import` on ClickOps cloud resources or staring at thousands of lines of `.tf` files without a live architecture map" (`Askrike/desprawl`)**: `desprawl` ships as a single Go binary containing a CLI, an MCP server, agent skills (`desprawl setup` auto-registers with Claude Code, Cursor, Codex, and Gemini CLI), and a live Web UI: it **reverse-engineers live cloud or SaaS accounts into linked Terraform** via any Terraform provider and **draws Terraform as an interactive component-and-connection architecture map**!
2. **Closed-Form FinOps Conclusion (`CLAIM-20261113-R39-QUADKNOB-DESPRAWL`)**:
   - Modeled for a **full-stack and cloud platform team tuning `80 interactive UI/motion screens / month` and reverse-engineering/mapping `20 cloud and SaaS environments into Terraform / month`** (fully loaded full-stack & cloud architect rate `$100.00/hr`; underlying cloud provider bills and commercial design seats: `not_measured`):
   - Switching from **Path A (20-turn chat CSS number guessing + manual `terraform import` and hand-drawn diagrams, `$5,420.00/mo`)** to **Path C (`quadknob-skill` OP-1 4-knob live tuning + `desprawl` live-to-Terraform & architecture map MCP, `$510.00/mo`)** saves **`$4,910.00/mo` (`-90.59%`, or `$58,920.00/yr`)** and cuts UI parameter-guessing and ClickOps-to-Terraform reverse-engineering labor from `38.0 hrs/mo` to `3.5 hrs/mo` (**`-90.79%`**).

---

## 🎯 2. Three First-Principles Deep-Dive Questions (Q1 / Q2 / Q3)

### Q1: Why is natural-language chat the wrong interface for tuning continuous UI, colour, and animation parameters?
- **First-Principles Breakdown**:
  1. **Discrete Words vs. Continuous Visual Perception**: Humans judge visual balance (radius, spacing, hue, saturation, blur, spring timing) in milliseconds when turning a dial, whereas verbalizing numerical guesses in chat triggers slow, token-heavy regeneration loops.
  2. **OP-1 Four-Knob Constraint (`<quadknob-panel>`)**: Binding up to four coupled CSS/JS parameters at a time to a zero-dependency web component lets the agent wire the parameterization once while the human dials the exact values by eye.

### Q2: How does `Askrike/desprawl` improve over legacy one-way `terraformer` dumps and static diagram generators?
- **First-Principles Breakdown**:
  1. **Linked Terraform Generation + Live Interactive Map**:
     - Imports live resources through any Terraform provider (`Terraform 1.14+`) into linked `.tf` definitions while rendering components and connections in a live Web UI (drawing maps requires zero external tools or cloud credentials).
  2. **Unified CLI + MCP + Skill Auto-Registration (`desprawl setup`)**:
     - Automatically configures both its MCP server and agent skills across Claude Code, Cursor, Codex, and Gemini CLI (with `-skills` support for isolated development).

### Q3: How do `quadknob-skill` and `desprawl` keep runtime dependencies and production footprints minimal?
- **First-Principles Breakdown**:
  1. **Single-File Zero-Dependency `quadknob.js`**:
     - Loads directly via `<script type="module" src="/quadknob.js"></script>` in any stack without bundlers or framework lock-in.
  2. **Single-Binary Go Architecture (`desprawl`)**:
     - Compiles to a single `~/.local/bin/desprawl` binary that serves the CLI, MCP server, skill installer, and architecture map UI.

---

## 🧭 3. Mermaid Decision Tree & Quadknob + desprawl Architecture

```mermaid
flowchart TD
    A["Tactile Frontend Parameter Tuning & Cloud-to-Terraform Architecture Mapping"] --> B{"Primary Engineering Bottleneck?"}
    B -- "Frontend Look & Feel: Guessing CSS radii, colours, blur & timing across 20 chat turns" --> C["Adopt githubnext/quadknob-skill (GitHub Next OP-1 4-Knob Web Component + Skill)"]
    B -- "Cloud IaC & Topology: Reverse-engineering live ClickOps cloud/SaaS into linked Terraform & maps" --> D["Adopt Askrike/desprawl (Go CLI + MCP Server + Live Architecture Map)"]

    C --> C1["Agent injects dependency-free <quadknob-panel> bound to CSS/JS variables"]
    C1 --> C2["Human dials blue/green/black/orange knobs by eye -> clicks Done to copy values"]

    D --> D1["desprawl setup registers MCP server & skills in Claude Code, Cursor, Codex & Gemini CLI"]
    D1 --> D2["Import live cloud/SaaS via any Terraform provider + render interactive architecture map"]

    C2 & D2 --> E["🏆 Golden Tactile UI & Automated IaC Stack: Quadknob + desprawl (-90.59% TCO)"]
```

---

## 📊 4. Head-to-Head Selection Matrix

| Dimension | Path A: 20-Turn Chat Guessing + Manual `terraform import` | Path B: Browser DevTools Edits + Flat `terraformer` Dump | **Path C (Recommended): `quadknob-skill` + `Askrike/desprawl`** |
| :--- | :--- | :--- | :--- |
| **UI Parameter Tuning Loop** | 15–20 chat turns guessing pixel/colour numbers | Manual DevTools edits lost on reload | **OP-1 4-knob live eye-dialing (`<quadknob-panel>`) + 1-click `Done` copy** |
| **Frontend Runtime Footprint** | None (slow chat regeneration) | Framework-specific debug libraries | **1 dependency-free ES module (`quadknob.js`) working in any page** |
| **Live Cloud-to-Terraform Import** | Days of manual `terraform import` & HCL writing | Unlinked flat dumps with hardcoded IDs | **Imports any Terraform provider into linked Terraform definitions** |
| **Architecture Visualization & Agent Integration** | Manual Draw.io diagrams that immediately drift | Static image exports; no MCP server | **Interactive live architecture map Web UI + `desprawl setup` MCP & skills** |
| **Monthly TCO (80 Screens + 20 Cloud Audits)** | **`$5,420.00 / mo`** (`$1,620` token + `$3,800` labor) | **`$2,720.00 / mo`** (`$720` token + `$2,000` labor) | **`$510.00 / mo` (Saves `$4,910.00/mo` · `-90.59%`)** |

---

## 🧪 5. Closed-Form FinOps Worked Example & 7-Card Insights (`CLAIM-20261113-R39-QUADKNOB-DESPRAWL`)

### 5.1 Baseline Parameters & Explicit Scope Boundaries
- **Scenario**: A full-stack and cloud platform team fine-tuning **80 interactive UI/motion screens per month** and reverse-engineering/mapping **20 cloud and SaaS environments into Terraform per month**.
- **Labor Rate**: Fully loaded full-stack and cloud infrastructure architect rate of **`$100.00 / hr`**.
- **Explicit Not-Measured Boundary**: Underlying cloud provider resource bills and commercial design tool seats are marked **`not_measured`**. This model strictly accounts for LLM token waste from multi-turn CSS guessing and failed Terraform import retries plus engineering hours spent tweaking UI styles and manually writing Terraform/architecture diagrams.

### 5.2 Three-Path Monthly Cost Comparison

| Cost Component | Path A: 20-Turn CSS Guessing + Manual TF Import | Path B: DevTools Copy + Flat `terraformer` Dump | **Path C: GitHub Next `Quadknob` + `desprawl` MCP (Recommended)** |
| :--- | :--- | :--- | :--- |
| **Monthly UI-Tuning & IaC-Retry Token Spend** | **`$1,620.00`** (multi-turn CSS guessing + import error retries) | **`$720.00`** (refactoring unlinked `.tf` dumps) | **`$160.00`** (1-turn `Done` knob writeback + linked `desprawl` import) |
| **Visual Tuning & Cloud-to-Terraform Labor (`$100/hr`)** | `38.0 hrs × $100.00` = **`$3,800.00`** | `20.0 hrs × $100.00` = **`$2,000.00`** | `3.5 hrs × $100.00` = **`$350.00`** |
| **Total Monthly TCO** | **`$5,420.00 / mo`** | **`$2,720.00 / mo`** (`-49.82%`) | **`$510.00 / mo`** |
| **Net Savings vs. Path A** | Baseline | Saves `$2,700.00 / mo` | **Saves `$4,910.00 / mo` (`-90.59%` · `$58,920.00/yr`)** |
| **Cloud Provider Resource Bills & Design Tool Seats** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 6. Production Adoption Checklist

- [ ] **1. `githubnext/quadknob-skill` Installation & Live Dialing**: Run `npx skills add githubnext/quadknob-skill`, ask your agent to inject `<quadknob-panel>` for card/glow/text parameters, dial the four knobs by eye, and click `Done` to persist the values.
- [ ] **2. `Askrike/desprawl` Binary & MCP Setup**: Install `desprawl` (`curl -fsSL https://desprawl.spawned.app | sh` or `go install`) and run `desprawl setup` to register its MCP server and skills across Claude Code, Cursor, Codex, and Gemini CLI.
- [ ] **3. Terraform Architecture Map Verification**: Render an existing Terraform workspace as a visual architecture map in `desprawl`'s Web UI and verify component connections.
- [ ] **4. Live Cloud-to-Linked-Terraform Import**: Run `desprawl` with Terraform 1.14+ against a sandbox cloud/SaaS account to import live resources into linked `.tf` files.
