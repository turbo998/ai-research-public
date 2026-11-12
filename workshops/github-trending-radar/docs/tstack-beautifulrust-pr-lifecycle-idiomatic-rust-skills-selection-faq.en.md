# Autonomous PR Lifecycle Skills (`t3dotgg/tstack` 3-Model Council & CI Babysitter) & Idiomatic 5-Guide Rust Skills (`morganlinton/BeautifulRust`) Selection FAQ

> **Positioning**: This standalone guide is **Round 34 of the 2026-11-11 Night Shift (Cumulative Guide #79)**, written in the plain-language, first-principles, closed-form FinOps style of `ib-vs-ethernet-roce-selection-faq.md` for AI-Native SDLC and Systems Engineering Solution Architects evaluating two high-velocity (`5,200+★` combined) Agent Skills repositories:
> 1. **`t3dotgg/tstack` (`3,479★`, Python, MIT, by Theo / T3)**: Nine composable PR lifecycle skills for `Claude Code` and `Codex`—chaining **`sol-loop` (iterative GPT Sol review consensus)**, **`council` (3-provider multi-model consensus loop)**, **`file-pr` (problem-first PR descriptions)**, **`babysit-pr` (`pr-wait` CI and review-bot loop that fixes real findings)**, and credit-preserving **`takeover` + `modernize`** behind one-word triggers (`full-send` and `full-stop`);
> 2. **`morganlinton/BeautifulRust` (`1,792★`, Python/Rust, MIT)**: Three Agent Skills (`rust-best-practices`, `rust-review`, `rust-port`) distilled from **five canonical Rust style guides** (Google, Official Rust API Guidelines, Effective Rust, Rust Design Patterns, Microsoft Pragmatic Rust) plus a **violation-tested Clippy configuration (`lints/` + `scripts/check-lints.sh`)** and **Bevy 0.20 ECS specialization (`references/bevy.md`)**, lifting evaluated agent code quality from `24/30` to **`29/30`**.
>
> **中文版 FAQ**: [tstack-beautifulrust-pr-lifecycle-idiomatic-rust-skills-selection-faq.md](tstack-beautifulrust-pr-lifecycle-idiomatic-rust-skills-selection-faq.md) · **Architecture Summary SVG**: [`assets/github-ai-radar-2026-11-11-r34-tstack-beautifulrust.svg`](../../../assets/github-ai-radar-2026-11-11-r34-tstack-beautifulrust.svg)

![tstack & BeautifulRust Architecture Summary](../../../assets/github-ai-radar-2026-11-11-r34-tstack-beautifulrust.svg)

---

## 📌 1. Executive Summary

1. **In plain English, what problems do these two repositories actually solve?**
   - **Eliminating Manual PR Babysitting, File-Inventory PR Descriptions & Single-Model Blind Spots (`t3dotgg/tstack`)**: Writing the code is only half the battle—developers lose hours waiting on CI, triaging noisy review-bot comments, rebasing stale branches, or writing PR descriptions that merely list touched files instead of stating the problem. `tstack` packages 9 composable skills: saying `"full stop"` (or unattended `"full send"`) runs **`sol-loop`** (looping with GPT Sol until both agents agree) or **`council`** (looping across three models from different providers until consensus), files a problem-first PR via **`file-pr`**, and runs **`babysit-pr`** (`pr-wait`) to watch CI and review bots and fix real issues automatically. Meanwhile, **`takeover`** + **`modernize`** rebases stale PRs, evaluates whether they should still exist, and finishes abandoned branches while preserving the original author's credit.
   - **Stopping Coding Agents from Writing "C/Python-in-Rust" & Breaking Bevy ECS (`morganlinton/BeautifulRust`)**: Without specialized guidance, coding agents write Rust with `pub` struct fields (`C-GETTER` violation), `.unwrap()` in doctests, missing `# Errors` docs, and unordered `HashMap`s when porting ordered Python `dict`s—or conversely, apply naive lint rules that break **Bevy 0.20 ECS** system signatures (`Res<Time>`) while missing runtime `B0001` dual-mutable-query panics. `BeautifulRust` distills five authoritative Rust guides into `rust-best-practices`, 3-tier rule-citing `rust-review`, and test-first `rust-port` (with `PORTING.md` audit logs and `references/bevy.md`), backed by a drop-in Clippy configuration (`lints/lints.toml`) verified against a deliberate-violation crate (`lints/check`).
2. **Closed-Form FinOps Verdict (`CLAIM-20261111-R34-TSTACK-BEAUTIFULRUST`)**:
   - For a 16-engineer Systems & Full-Stack Engineering Team shipping **300 pull requests** and porting/reviewing **40 Rust crates/modules per month** (senior systems engineer loaded rate `$90.00/hr`; GitHub Enterprise seat licenses and build servers: `not_measured`):
   - Upgrading from **Path A (Manual PR babysitting + single-model self-review + naive LLM Rust ports with `unwrap()`/`HashMap` bugs, `$5,970.00/mo`)** to **Path C (`tstack` `full-stop`/`council`/`babysit-pr` + `BeautifulRust` skill trio [`29/30` checks] & `check-lints.sh` CI gate, `$850.00/mo`)** saves **`$5,120.00/mo` (`-85.76%`, `$61,440.00/yr`)** and cuts senior engineering PR babysitting and Rust refactoring labor from `48.0 hrs/mo` to `6.0 hrs/mo` (**`-87.50%`**).

---

## 🎯 2. Three Core Architectural Questions (Q1 / Q2 / Q3 Deep-Dive)

### Q1: How do `t3dotgg/tstack`'s 9 composable skills automate the journey from a local diff to a green, consensus-reviewed PR?
- **First-Principles Breakdown**:
  1. **Composable Skill Dependency Graph (`full-send` / `full-stop` / `takeover`)**:
     - `full-send` orchestrates `sol-loop` -> `file-pr` -> `babysit-pr` (`pr-wait` Python watcher that monitors GitHub Actions and review bots, fixing real bugs while ignoring bot noise) -> auto-merge;
     - `full-stop` executes the exact same verification and CI-babysitting pipeline but stops as soon as the PR is green and ready for human merge;
     - `takeover` chains `modernize` (rebasing old branches and explicitly deciding whether the PR is still warranted), `file-pr`, `babysit-pr`, and `leaving-pr-comments` while preserving the original contributor's attribution.
  2. **Dual-Tier Cross-Model Consensus (`sol-loop` vs. `council`)**:
     - `sol-loop` pairs your primary agent with GPT Sol in an iterative review loop until both agree;
     - `council` dispatches the diff to **three models from distinct providers** (using `delegate_task` in T3 Code or subagent harnesses) and iterates until all three models converge.

### Q2: How does `morganlinton/BeautifulRust` achieve `29/30` on Rust evaluation tasks, handle Bevy 0.20 ECS exceptions, and prove that its Clippy lints never silently stop firing?
- **First-Principles Breakdown**:
  1. **5-Source Synthesis & Test-First `rust-port` (`PORTING.md`)**:
     - Synthesizes the Google Rust Style Guide, Official Rust API Guidelines, Effective Rust, Rust Design Patterns, and Microsoft Pragmatic Rust Guidelines—explicitly resolving disagreements across sources.
     - `rust-port` ports the source C/C++/Python/Go/JS test suite **first**, maps `NULL`/`None` to `Option`, exceptions to typed error enums, and ordered dicts to order-preserving collections (preventing silent `HashMap` reordering bugs), and writes a complete `PORTING.md`.
  2. **Framework-Aware `references/bevy.md` (Bevy 0.20 ECS)**:
     - When `Cargo.toml` depends on `bevy` or `bevy_ecs`, the writing and review skills load `references/bevy.md` first: leaving valid Bevy idioms alone (by-value `Res<Time>`, `use bevy::prelude::*`, public plain-data component fields) while catching compile-clean ECS bugs (`B0001` conflicting mutable queries, unapplied `Commands` ordering, and `.single().unwrap()` crashes on entity death).
  3. **Violation-Verified Clippy Configuration (`lints/check` + `scripts/check-lints.sh`)**:
     - Enforces `lints/clippy.toml` and `lints/lints.toml` (`rust-version = "1.81"+` for `#[expect]` and `allow_attributes_without_reason`), verified by running `bash scripts/check-lints.sh` against `lints/check/src/lib.rs`—a dedicated crate containing one deliberate violation per lint so CI fails immediately if any lint stops firing.

### Q3: How should Solution Architects deploy `tstack` and `BeautifulRust` together across engineering teams?
- **Deployment Pattern**:
  - Install all 9 `tstack` skills into `~/.claude/skills/` and `~/.codex/skills/` (keeping custom `council` model lists inside repo-level `CLAUDE.md` / `AGENTS.md` so skill updates stay clean).
  - Install `BeautifulRust` (`npx skills add morganlinton/BeautifulRust` or `/plugin install beautiful-rust@beautiful-rust`) and embed `lints/lints.toml` into `Cargo.toml` so `full-stop` / `babysit-pr` automatically enforces idiomatic Rust and zero-warning Clippy checks on every PR.

---

## 🧭 3. Mermaid Decision Tree & Autonomous PR + Idiomatic Rust Pipeline

```mermaid
flowchart TD
    A["AI Agent PR Lifecycle Automation & Idiomatic Rust Engineering Workload"] --> B{"Current Workflow Stage?"}
    B -- "Writing, Reviewing, or Porting C/C++/Py/Go/JS to Rust (or Bevy 0.20)" --> C["Adopt morganlinton/BeautifulRust (3 Skills + Verified Clippy Suite)"]
    B -- "Multi-Model Review, Filing PRs, Babysitting CI/Bots & Branch Takeover" --> D["Adopt t3dotgg/tstack (9 Composable PR Lifecycle Skills)"]

    C --> C1{"Does Cargo.toml depend on bevy or bevy_ecs?"}
    C1 -- "Yes" --> C2["Load references/bevy.md (Preserve Res<T> idioms + catch B0001 & .single() panics)"]
    C1 -- "No" --> C3["rust-best-practices (Private fields C-GETTER / # Errors docs / ? in doctests)"]
    C2 & C3 --> C4["rust-port (Port tests first + ordered maps + PORTING.md) & 3-tier rust-review"]
    C4 --> C5["CI Gate: lints.toml + bash scripts/check-lints.sh (rust-version >= 1.81)"]

    D --> D1{"Select PR Execution Mode?"}
    D1 -- "High-stakes architectural change" --> D2["council: 3-provider model review loop until consensus"]
    D1 -- "Standard feature / abandoned branch" --> D3["full-stop / full-send (runs sol-loop) or takeover (runs modernize)"]
    D2 & D3 --> D4["file-pr (problem-first body) -> babysit-pr (pr-wait watches CI & fixes real bugs)"]
```

---

## 📊 4. Architectural Comparison Matrix

| Evaluation Dimension | Path A: Manual PR Babysitting + Naive LLM Rust | Path B: Basic PR Template + Stock `cargo clippy` | **Path C (Recommended): `tstack` + `BeautifulRust`** |
| :--- | :--- | :--- | :--- |
| **PR Review Depth & CI Babysitting** | Single-model blind spots; humans manually poll CI and bots | Static PR template; no multi-model loop or `pr-wait` | **`council` (3 providers) / `sol-loop` + `babysit-pr` automated CI fixer** |
| **Stale Branch Takeover & Attribution** | Manual rebase; agent rewrites often drop original author credit | No structured `modernize` check on whether PR should exist | **`takeover` + `modernize` rebases, evaluates viability & keeps credit** |
| **Rust Idiomaticity & Cross-Language Ports** | Public fields, `unwrap()` doctests, `HashMap` ordering bugs (`24/30`) | Stock Clippy misses API design & test-first porting rules | **5-guide synthesis (`29/30` score) + test-first `rust-port` (`PORTING.md`)** |
| **Bevy ECS Safety & Lint Verification** | Generic advice breaks Bevy systems and misses `B0001` panics | Lints silently stop firing across Rust toolchain upgrades | **Dedicated `references/bevy.md` + `lints/check` deliberate-violation test** |
| **Monthly TCO (300 PRs + 40 Modules)** | **`$5,970.00 / mo`** (`$1,650` CI/tokens + `$4,320` labor) | **`$3,160.00 / mo`** (`$820` compute + `$2,340` labor) | **`$850.00 / mo` (Saves `$5,120.00/mo` · `-85.76%`)** |

---

## 🧪 5. Closed-Form FinOps Example & 7-Card Insights (`CLAIM-20261111-R34-TSTACK-BEAUTIFULRUST`)

### 5.1 Workload & Scope Boundary
- **Workload**: A 16-engineer Systems & Full-Stack team shipping **300 pull requests** and porting/reviewing **40 Rust crates and modules per month**.
- **Rates**: Senior systems engineer loaded rate at **`$90.00 / hr`**.
- **Explicit Scope Boundary**: GitHub Enterprise seat subscriptions and self-hosted Rust build server hardware are marked **`not_measured`**.

### 5.2 Closed-Form Monthly Cost Breakdown

| Cost Component | Path A: Manual CI Babysitting + Naive LLM Rust Rework | Path B: Basic PR Prompts + Stock Clippy | **Path C: `tstack` + `BeautifulRust` (Recommended)** |
| :--- | :--- | :--- | :--- |
| **CI Re-Runs & Multi-Model Review Tokens** | **`$1,650.00`** | **`$820.00`** | **`$310.00`** (`sol-loop`/`council` catches bugs pre-CI) |
| **PR Babysitting, Branch Takeover & Rust QA (`$90/hr`)** | `48.0 hrs × $90.00` = **`$4,320.00`** | `26.0 hrs × $90.00` = **`$2,340.00`** | `6.0 hrs × $90.00` = **`$540.00`** |
| **Total Monthly TCO** | **`$5,970.00 / mo`** | **`$3,160.00 / mo`** (`-47.07%`) | **`$850.00 / mo`** |
| **Net Savings vs. Path A** | Baseline | Saves `$2,810.00 / mo` | **Saves `$5,120.00 / mo` (`-85.76%` · `$61,440.00/yr`)** |
| **GitHub Seats & Build Server Hardware** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 6. Production Verification Checklist

- [ ] **1. Full `tstack` Skill Graph Installation**: Copy all 9 skills (`tstack/skills/*`) into `~/.claude/skills/` and `~/.codex/skills/` so composite workflows (`full-send`, `full-stop`, `takeover`) can invoke `sol-loop`, `file-pr`, `babysit-pr`, `modernize`, and `leaving-pr-comments`, and verify `gh` CLI authentication and `python3`.
- [ ] **2. Externalized `council` Configuration**: Define your preferred 3-provider council models inside `CLAUDE.md` or `AGENTS.md` rather than editing skill files directly so upstream updates pull cleanly.
- [ ] **3. `BeautifulRust` Multi-Agent Installation**: Install via `/plugin install beautiful-rust@beautiful-rust` in Claude Code (which does not read `.agents/skills/`) and via `npx skills add morganlinton/BeautifulRust` or native plugin commands for Codex, Copilot, Cursor, and Gemini CLI.
- [ ] **4. `lints.toml` (`rust-version >= 1.81`) & `check-lints.sh` CI Gate**: Copy `lints/clippy.toml` beside `Cargo.toml`, merge `[lints]` from `lints/lints.toml` (adding the 4 Bevy allows from `references/bevy.md` for Bevy crates), and enforce `cargo clippy --all-targets --all-features -- -D warnings` + `bash scripts/check-lints.sh`.
- [ ] **5. Test-First `PORTING.md` Audit**: When running `rust-port`, verify that original unit tests are ported and passing before implementation sign-off and that `PORTING.md` documents all collection-ordering and error-enum mappings.
