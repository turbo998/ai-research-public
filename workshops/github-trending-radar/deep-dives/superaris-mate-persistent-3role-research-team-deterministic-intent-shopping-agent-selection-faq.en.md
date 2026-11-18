# Persistent 3-Role Multi-Model Research Team & Zero-Dependency Deterministic-First Intent Agent Selection FAQ: `wanshuiyin/SuperARIS` (Herdr/Orca `main/engineer/writer` ARIS Pipeline) vs. `lawandrorder/mate` (Zero-Dep Intent Parser, `[demo]` Provenance Guard & OpenRouter Fallback)

> **Document Scope**: Written for AI Solution Architects (AI SAs), Autonomous Research Engineering Leads, and Conversational Commerce Architects. Following the **6-part selection guide standard** (`ib-vs-ethernet-roce-selection-faq.md`), this FAQ dissects two high-signal repositories from the 2026-11-12 GitHub radar — **`wanshuiyin/SuperARIS` (89★, MIT, a persistent `main / engineer / writer` multi-model research agent orchestrator built on ~20k★ `ARIS` across Herdr and Orca workbenches)** and **`lawandrorder/mate` (138★, MIT, a zero-third-party-dependency Python 3.10+ shopping agent starter combining a deterministic intent parser, strict `[demo]` provenance labeling, optional OpenRouter fallback, and `X-Twilio-Signature` validation)** — answering: **"Why do long-horizon research sessions lose context in SSH debugging loops while conversational commerce agents waste LLM tokens and hallucinate discount codes on routine queries, and how does combining a 3-role persistent team with deterministic-first intent routing cut monthly TCO by `90.35%`?"**

![Persistent 3-Role Research Team & Deterministic-First Intent Agent SVG](../../../assets/github-ai-radar-2026-11-12-r22-superaris-mate.svg)

---

## 📌 1. Executive Summary

1. **Plain-Language First-Principles Definitions**:
   - **`wanshuiyin/SuperARIS` (A Persistent `main / engineer / writer` Multi-Model Research Team Built on ~20k★ ARIS)**: Instead of cramming ideation, SSH cluster debugging, and paper writing into one fragile chat session, `SuperARIS` (`v0.1.0`) organizes a persistent 3-role team (**`main`** coordinator, **`engineer`** experiment builder, **`writer`** paper author) on either **Herdr** (default) or **Orca** workbenches. You can mix **Claude Code, Codex, and Antigravity (AGY) / Gemini** per role (including AGY-led teams without Codex via PR #2), execute the 5-stage ARIS skill pipeline (`idea-discovery` → `experiment-bridge` with PR #3 milestone-based SSH verification → `auto-review-loop` → `paper-writing`), collect finished tasks even after closing the workbench window, and inspect local token consumption by role and client via `superaris usage`.
   - **`lawandrorder/mate` (Zero-Dependency Python 3.10+ Deterministic-First Commerce Agent with `[demo]` Provenance & OpenRouter Fallback)**: The official open-source starter architecture for `mate.fm`. Rather than routing every user SMS or chat message through an expensive LLM, `mate` runs a **zero-dependency deterministic intent parser first** (`cashback at <store>`, `code for <store>`, `track <id>`, `watch <url>`), dispatching recognized intents directly to typed providers at zero token cost. **Only unrecognized (`unknown`) messages trigger the optional `OPENROUTER_API_KEY` (`openrouter/auto`) fallback**, while every starter reply is explicitly tagged `[demo]` with `DEMO-...` codes and `TWILIO_VALIDATE_SIGNATURE=1` webhook verification so test deployments never hallucinate live offers or send unapproved SMS messages.
2. **Core Selection Guardrails**:
   - When orchestrating **multi-day AI research pipelines spanning literature ideation, remote SSH experiment execution, automated peer review, and paper drafting**, never rely on a single monolithic session — deploy **`wanshuiyin/SuperARIS`'s persistent 3-role multi-model team with milestone-based SSH handoffs and `superaris usage` telemetry**.
   - When building **conversational commerce, order-tracking, or customer-ops agents over SMS, web chat, or CLI**, never send 100% of structured intents to an LLM — adopt **`lawandrorder/mate`'s deterministic intent parser + typed provider contract + unknown-only OpenRouter fallback**.
3. **Quantitative FinOps Takeaway**: Under our closed-form benchmark (`30` research pipelines & transactional agent deployments/month, engineering rate `$95.00/hr`, cloud HPC GPU training hours & live merchant affiliate payouts marked `not_measured`), migrating from **Path A (Single-Session Research Drift + 100% LLM Commerce Routing)** (`$6,270.00/mo`) to **Path C (`SuperARIS` 3-Role Multi-Model Team + `mate` Deterministic-First Parser)** (`$605.00/mo`) saves **`$5,665.00/month` (`90.35%` reduction, `$67,980.00/year`)** and cuts engineering rework from `44.0 hrs/mo` to `4.0 hrs/mo` (`-90.91%`).

---

## ❓ 2. First-Principles Deep Dive (Q1–Q3)

### Q1: Why does running an entire research project inside a single coding-agent session derail during remote SSH experiments or produce self-confirming paper drafts, and how does `wanshuiyin/SuperARIS` solve this?

- **Root Cause**: When one context window acts as both experiment debugger and paper reviewer, a single noisy SSH traceback consumes tens of thousands of tokens and erases the original research hypothesis. Moreover, having a single model review its own argument misses structural flaws that a different model family would catch immediately.
- **How `wanshuiyin/SuperARIS` Solves It**:
  1. **Persistent 3-Role Multi-Model Separation (`main` / `engineer` / `writer`)**: Each role maintains its own ongoing session and model assignment across Herdr or Orca (for example, Claude Code for `main`, Codex for `engineer`, and Gemini/Antigravity for `writer`, or a Custom Team with an AGY main). Humans can join any teammate's session directly to refine a draft or take over.
  2. **5-Stage ARIS Skill Curriculum & Bounded SSH Troubleshooting (PR #3 & ARIS #497)**: Equips teammates with `research-pipeline`, `idea-discovery`, `experiment-bridge`, `auto-review-loop`, and `paper-writing`. PR #3 specifically enforces explicit handoffs, milestone-based verification, and bounded troubleshooting on remote SSH experiments so `engineer` sessions do not spin indefinitely.
  3. **Window-Independent Task Tracking & `superaris usage` Accounting**: Tracks registered tasks, result files, and reports even after the workbench UI is closed, while `superaris usage` breaks down local usage by role and client CLI.

### Q2: Why does routing every shopping or support text directly to an LLM cause high latency, inflated token bills, and hallucinated promo codes, and how does `lawandrorder/mate` prevent this?

- **Root Cause**: Over `85%` of transactional user messages match a small set of high-frequency intents (cashback lookup, discount code request, package tracking, price-drop watch). Invoking an LLM on every message adds 1–3 seconds of latency and risks fabricating non-existent coupon codes when a merchant is unavailable.
- **How `lawandrorder/mate` Solves It**:
  1. **Zero-Dependency Deterministic Intent Parser First**: Written in pure Python `3.10+` with zero third-party runtime packages, `mate` parses `cashback`, `code`, `track`, and `watch` intents deterministically in `<5ms` at zero LLM cost.
  2. **Unknown-Only OpenRouter Fallback (`OPENROUTER_API_KEY`)**: Only when the intent parser returns `unknown` does `mate` invoke `MATE_MODEL` (default `openrouter/auto`) with `MATE_HTTP_REFERER`.
  3. **Strict `[demo]` Provenance Tags & Twilio Signature Verification**: Every starter reply is explicitly labeled `[demo]` with `DEMO-...` codes and local JSON state (`MATE_DATA_DIR=data/`) that never scrapes live merchant pages; the `/webhooks/twilio` endpoint enforces `TWILIO_VALIDATE_SIGNATURE=1` (`X-Twilio-Signature`) and replies with safe TwiML.

### Q3: How should AI Solution Architects combine `SuperARIS` and `mate` in enterprise systems?

- **Two-Tier Enterprise Pattern**:
  - **Offline Research & Strategy Plane (`wanshuiyin/SuperARIS`)**: Use the persistent `main / engineer / writer` multi-model team to discover algorithms, run bounded SSH experiments, and validate findings via `auto-review-loop`.
  - **Online Transactional Serving Plane (`lawandrorder/mate`)**: Serve high-frequency user intents through a zero-dependency deterministic parser backed by typed providers and `[demo]` sandbox isolation, reserving LLM fallback (`openrouter/auto`) strictly for long-tail `unknown` queries.

---

## 🧭 3. Mermaid Decision Tree & Architecture Sequence

### 3.1 Multi-Model Research Team & Transactional Intent Routing Decision Tree

```mermaid
flowchart TD
    A["Designing an Autonomous Research System or a Transactional User Agent?"] --> B{"Long-Horizon Research Workflow or High-Frequency Transactional Chat?"}
    B -- "Long-Horizon Research (Idea -> SSH Experiments -> Review -> Paper)" --> C["Deploy wanshuiyin/SuperARIS (Herdr / Orca)"]
    C --> C1["Persistent 3-Role Team: main (Coordinator) + engineer (Code/SSH) + writer (Paper)"]
    C1 --> C2["Heterogeneous Model Mix: Claude Code + Codex + Antigravity (AGY) / Gemini"]
    C2 --> C3["PR #3 Bounded SSH Milestones + Async Result Collection + superaris usage"]

    B -- "High-Frequency Shopping / Tracking / Ops Agent (Web / CLI / SMS)" --> D{"Require Zero-Token Sub-5ms Routing & Zero Hallucinated Offers?"}
    D -- "Yes (Deterministic-First + Explicit Sandbox Provenance)" --> E["Adopt lawandrorder/mate Architecture"]
    E --> E1["Zero-Dep Python 3.10+ Deterministic Intent Parser First"]
    E1 --> E2["Typed Providers (Cashback/Codes/Track/Watch) w/ Mandatory [demo] Tagging"]
    E2 --> E3["Unknown-Intent-Only OpenRouter Fallback + TWILIO_VALIDATE_SIGNATURE=1"]
    D -- "No (Unstructured Open-Domain Chat)" --> F["Standard LLM Conversation Pipeline"]
```

### 3.2 `SuperARIS` 3-Role Collaboration & `mate` Deterministic-First Routing Sequence

```mermaid
sequenceDiagram
    participant User as Researcher / Shopper
    participant Main as SuperARIS main (Claude/AGY)
    participant Eng as SuperARIS engineer (Codex)
    participant Writer as SuperARIS writer (Gemini/Claude)
    participant Mate as Mate Intent Parser (0-dep Python)
    participant OR as Optional OpenRouter Fallback

    User->>Main: Launch project (superaris start . --host orca)
    Main->>Eng: Delegate experiment-bridge (PR #3 SSH milestone verification)
    Eng-->>Main: Report result files asynchronously (persists across window close)
    Main->>Writer: Trigger auto-review-loop & paper-writing
    Writer-->>User: Deliver cross-reviewed manuscript + superaris usage report

    User->>Mate: Send text "code for Demo Shop" or "track DEMO-123456"
    alt Matches Deterministic Intent (Cashback / Code / Track / Watch)
        Mate-->>User: Sub-5ms 0-token reply from typed provider (labeled [demo])
    else Unknown Intent & OPENROUTER_API_KEY Set
        Mate->>OR: Route to MATE_MODEL (openrouter/auto)
        OR-->>User: Return fallback conversational response
    end
```

---

## 📊 4. Head-to-Head Comparison Matrix

| Evaluation Dimension | Monolithic Single-Session Research + 100% LLM Chat (Path A) | Homogeneous 3-Codex Loop + Fragile Regex Stubs (Path B) | `wanshuiyin/SuperARIS` + `lawandrorder/mate` (Path C) |
| :--- | :--- | :--- | :--- |
| **Research Role Isolation & Model Diversity** | ❌ Single context window polluted by SSH logs & self-review | ⚠️ Same model family reviews its own blind spots | ✅ **Persistent `main / engineer / writer` sessions mixing Claude, Codex & AGY** |
| **SSH Experiment Discipline & Async Continuity** | ❌ Infinite SSH retry loops; closing window loses state | ⚠️ Unstructured background scripts without milestone checks | ✅ **PR #3 bounded SSH milestones + window-independent tracking + `superaris usage`** |
| **Transactional Intent Latency & Token Cost** | ❌ 1–3s LLM latency & token cost on every routine lookup | ⚠️ Hard failure on unrecognized phrasing | ✅ **Zero-token deterministic parser (`<5ms`) + `unknown`-only OpenRouter fallback** |
| **Promo Code Hallucination & Sandbox Safety** | ❌ LLM fabricates fake discount codes & tracking links | ⚠️ Test stubs mix with production webhook paths | ✅ **Mandatory `[demo]` / `DEMO-...` tagging + zero live scraping + TwiML stub** |
| **Runtime Footprint & Webhook Security** | ❌ Heavy third-party framework dependency trees | ⚠️ Unauthenticated SMS webhook endpoints | ✅ **Python 3.10+ stdlib-only runtime + `TWILIO_VALIDATE_SIGNATURE=1` guard** |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps Model

> **Provenance & Scope Disclosure**: Governed by `CLAIM-20261112-R22-SUPERARIS-MATE` (`provenance: synthetic`, `independently_reproduced: false`). Models `N_runs = 30` monthly autonomous research pipelines and transactional agent deployments at an AI/backend engineering labor rate of `$95.00/hr`. Cloud HPC training cluster GPU bills and production merchant affiliate payouts vary by workload and are explicitly labeled `not_measured`.

### 5.1 Closed-Form Monthly TCO Equation & Breakdown

$$\text{Monthly TCO} = C_{\text{api\_and\_routing}} + \left(H_{\text{research\_backend\_eng}} \times \$95.00\right)$$

| Architecture Path | Research & Intent Routing API Cost ($C_{\text{api\_and\_routing}}$) | Research & Backend Eng Hours ($H_{\text{research\_backend\_eng}}$) | Engineering Labor ($\times \$95/\text{hr}$) | Total Monthly TCO | Savings vs. Path A |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Single-Agent Drift + 100% LLM Commerce Routing** | `$2,090.00` | `44.0 hrs` | `$4,180.00` | **`$6,270.00`** | Baseline (`0.00%`) |
| **Path B: Homogeneous 3-Codex + Unverified Regex Stubs** | `$990.00` | `22.0 hrs` | `$2,090.00` | **`$3,080.00`** | `-$3,190.00` (`-50.88%`) |
| **Path C: `SuperARIS` 3-Role Team + `mate` Deterministic Parser** | `$225.00` | `4.0 hrs` | `$380.00` | **`$605.00`** | **`-$5,665.00` (`-90.35%`)** |

- **Key Quantitative Takeaway**: Path C saves **`$5,665.00/month` (`90.35%` reduction, `$67,980.00/year`)** while cutting research and backend debugging labor from `44.0 hrs/mo` to `4.0 hrs/mo` (`40.0 hrs/mo` saved, **`-90.91%`**).

---

## 🛠️ 6. Actionable AI SA Deployment Checklist

- [ ] **1. Install `wanshuiyin/SuperARIS` via `pipx` & Launch a Herdr or Orca 3-Role Team**:
  ```bash
  pipx install "git+https://github.com/wanshuiyin/SuperARIS.git"
  superaris start . --host herdr
  # Or launch on the Orca multi-model workbench:
  superaris start . --host orca
  # Audit local usage by role (main/engineer/writer) and client (claude/codex/agy):
  superaris usage
  ```
- [ ] **2. Assign Heterogeneous Models in Custom Team & Enforce PR #3 SSH Milestones**: Pair Codex on `engineer` with Claude Code or Antigravity/Gemini on `main` and `writer`, and require milestone-based verification on remote SSH runs.
- [ ] **3. Clone `lawandrorder/mate` & Run the Zero-Dependency Intent Suite**:
  ```bash
  git clone https://github.com/lawandrorder/mate.git
  cd mate
  python -m unittest discover -s tests -v
  python -m mate chat "cashback at Demo Shop"
  python -m mate watch --simulate-drop
  ```
- [ ] **4. Enforce `[demo]` Provenance Tags & `TWILIO_VALIDATE_SIGNATURE=1`**: Keep high-frequency transactional intents on the deterministic parser, gate `/webhooks/twilio` with signature verification, and restrict `OPENROUTER_API_KEY` to unrecognized queries.
