# Physical AI Quota/Permission Desk Panel & "The Human Always Pays" (`ADR-0001`) Retail MCP Selection FAQ: `ersinkoc/phonebox` (113-Widget Claude/Codex/AGY Burn-Rate & Allow/Deny Deck) vs. `NJohansen/handle-mcp` (Multi-Store Basket Optimizer with Zero Checkout Code)

> **Document Scope**: Written for AI Solution Architects (AI SAs), High-Concurrency AI Developers, and Transactional Agent Security Leads. Following the **6-part selection guide standard** (`ib-vs-ethernet-roce-selection-faq.md`), this FAQ dissects two exemplary Human-in-the-Loop (HITL) repositories from the 2026-11-12 GitHub radar — **`ersinkoc/phonebox` (246★, MIT, `v0.9`, a .NET 10 PC agent + Android 9+ companion app turning an old phone into a zero-cloud USB/Wi-Fi/Tailscale desk panel with 113 widgets, live Claude Code / Codex / native Antigravity `agy` quota burn-rate forecasting, and physical `Allow / Deny` permission buttons)** and **`NJohansen/handle-mcp` (133★, MIT, a multi-store grocery basket optimizer MCP server governed by `ADR-0001: The Human Always Pays`, where order/payment code does not exist and a CI test fails if checkout logic is ever introduced)** — answering: **"Why do multi-session developers lose hours to buried CLI permission prompts and unexpected quota exhaustion while transactional shopping agents risk unauthorized purchases, and how does pairing a physical approval deck with a zero-checkout MCP architecture cut monthly TCO by `90.34%`?"**

![Physical AI Quota/Permission Desk Panel & Human-Always-Pays MCP SVG](../../../assets/github-ai-radar-2026-11-12-r26-phonebox-handlemcp.svg)

---

## 📌 1. Executive Summary

1. **Plain-Language First-Principles Definitions**:
   - **`ersinkoc/phonebox` (Turn an Old Android 9+ Phone into a Zero-Cloud Physical Desk Panel for AI Quotas, Session Telemetry & `Allow / Deny` Prompts)**: Consisting of a fullscreen Android `9+` app (`v0.7.3` added compatible immersive API + CI Android API lint) and a `.NET 10` PC agent for Windows, Linux, and macOS over USB, Wi-Fi, or Tailscale (zero cloud servers), `phonebox` offers **113 widgets (including 58 Control Deck widgets in `v0.8–v0.9` for Podman containers, OBS, audio, and displays) and 30 templates**. For AI engineers, it tracks **Claude Code, Codex, and native Antigravity (`agy` CLI)** quotas with burn-rate forecasts (`v0.7.2` strictly ensures missing readings are never displayed as unused quota), drills into per-session model/token/context/tool metrics, buzzes when an agent finishes or blocks, and uses rule-driven page switching to surface **Claude Code permission prompts with physical `Allow` / `Deny` buttons**.
   - **`NJohansen/handle-mcp` (A Multi-Store Basket Comparison & Cart-Filling MCP Server Governed by `ADR-0001: The Human Always Pays`)**: A Python `3.12+` MCP server for Claude, Grok, and Codex that reads weekly offers and recipes, plans meals on a budget, runs `compare_basket` across `nemlig.com`, `BilkaToGo`, and `REMA 1000` (accounting for pack sizes, offers, minimum orders, and delivery fees), and populates the cheapest cart. Crucially, under **`docs/adr/0001-the-human-always-pays.md`**, only two tools write state (`set_cart_quantities` and `add_recipe_to_cart`), **code to place an order or pay literally does not exist in the repository, and an automated test fails if checkout code ever shows up**.
2. **Core Selection Guardrails**:
   - When running **multiple concurrent Claude Code, Codex, `agy`, and Podman workloads where buried terminal permission prompts or surprise quota limits stall velocity**, repurpose any Android 9+ phone with **`ersinkoc/phonebox`** over USB or Tailscale.
   - When architecting **commerce, cloud-procurement, or financial MCP servers**, never rely on system prompts ("please ask before paying") to prevent unauthorized spend — enforce **`NJohansen/handle-mcp`'s `ADR-0001` pattern: expose read-only comparison + cart/draft staging tools only, omit checkout endpoints entirely from the binary, and guard that absence with a CI test**.
3. **Quantitative FinOps Takeaway**: Under our closed-form benchmark (`30` AI developer seats & automated procurement workflows, engineering labor at `$95.00/hr`, dedicated Stream Deck hardware & raw grocery merchandise spend marked `not_measured`), migrating from **Path A (Buried CLI Permission Stalls + Auto-Checkout Rollbacks)** (`$6,160.00/mo`) to **Path C (`PhoneBox` Physical Quota/Approval Panel + `handle-mcp` ADR-0001 Zero-Checkout MCP)** (`$595.00/mo`) saves **`$5,565.00/month` (`90.34%` reduction, `$66,780.00/year`)** and cuts developer context-switching and rollback debugging from `44.0 hrs/mo` to `4.0 hrs/mo` (`-90.91%`).

---

## ❓ 2. First-Principles Deep Dive (Q1–Q3)

### Q1: Why do developers running 3–5 concurrent coding agents waste hours on stalled permission prompts and sudden quota walls, and how does `ersinkoc/phonebox` solve this without cloud telemetry or expensive hardware?

- **Root Cause**: Terminal tabs waiting on a tool-approval prompt sit hidden behind IDE windows, while checking token burn rates across Claude, Codex, and Antigravity (`agy`) requires disruptive context switches.
- **How `ersinkoc/phonebox` Solves It**:
  1. **Unified Quota Burn-Rate Forecasting & Honest Telemetry (`v0.7.0–v0.7.2`)**: Tracks Claude, Codex, and native signed-in `agy` CLI quotas on one Smart Stack screen, forecasting burn rate and exposing per-session model, timing, token counters, context window fullness, and recent tool calls — while strictly refusing to render missing quota readings as fake unused allowance.
  2. **Rule-Switched Physical `Allow / Deny` Prompts**: When an AI session blocks on a permission prompt or finishes a task, the phone buzzes and the rule engine calmly switches the display to the approval card with tactile **Allow** and **Deny** buttons, keeping keyboard focus inside the PC editor.
  3. **113 Widgets Across System, Podman & CI (`v0.8–v0.9`)**: Displays CPU/GPU/RAM/disk metrics, process termination (`end one / end all`), Podman containers, GitHub PR review requests, and CI status over local USB or paired Wi-Fi/Tailscale.

### Q2: Why is instructing an agent via prompt ("never pay without asking") insufficient for transactional MCP servers, and how does `NJohansen/handle-mcp` enforce `ADR-0001`?

- **Root Cause**: Prompt instructions are probabilistic; indirect prompt injection inside product descriptions or multi-turn state drift can trick an agent into invoking a `checkout` tool if that tool exists in the MCP server's schema.
- **How `NJohansen/handle-mcp` Solves It**:
  1. **Architectural Absence of Checkout Code (`ADR-0001`)**: `handle-mcp` physically omits order-submission and payment code from the codebase and enforces a unit test that fails if payment endpoints are ever added.
  2. **Full-Basket Total Cost Comparison (`compare_basket`)**: Evaluates 11 read-only tools (`search_products`, `list_offers`, `get_nutrition`, `compare_basket`, `list_delivery_slots`, etc.) across `nemlig.com`, `BilkaToGo`, and `REMA 1000`, normalizing unit prices (`per kg/l`), weekly offers, minimum order rules, and delivery fees before calling `set_cart_quantities` or `add_recipe_to_cart`.
  3. **Transparent Privacy-Preserving Telemetry (`HANDLE_TELEMETRY=0`)**: Rounds basket totals to the nearest `50 kr` after 30 quiet minutes with zero PII, user IDs, or product names, and supports complete opt-out via `HANDLE_TELEMETRY=0`.

### Q3: How should AI Solution Architects combine `phonebox` and `handle-mcp` patterns in enterprise HITL systems?

- **Two-Layer Human-in-the-Loop Architecture**:
  - **Out-of-Band Physical Approval Plane (`ersinkoc/phonebox`)**: Route developer tool approvals, container actions, and quota burn-rate alerts to a dedicated USB/Tailscale companion screen so humans approve reversible actions in `<1s` without losing IDE focus.
  - **Capability-Restricted Transactional Plane (`NJohansen/handle-mcp` `ADR-0001`)**: For irreversible financial or procurement workflows, restrict MCP servers to read-only optimization plus cart/draft staging, enforcing a CI test that guarantees final payment execution remains exclusively in human hands.

---

## 🧭 3. Mermaid Decision Tree & Architecture Sequence

### 3.1 Human-in-the-Loop Desk Panel & Transactional MCP Decision Tree

```mermaid
flowchart TD
    A["Designing Human-in-the-Loop (HITL) Controls for AI Coding or Transactional Agents?"] --> B{"Developer Multi-Session Supervision or Financial/Retail Procurement?"}
    B -- "Supervising Concurrent Claude/Codex/AGY Sessions & PC Resources" --> C["Deploy ersinkoc/phonebox (.NET 10 + Android 9+)"]
    C --> C1["Zero-Cloud USB / Wi-Fi / Tailscale Link + 113 Widgets (58 Control Deck)"]
    C1 --> C2["Claude + Codex + Native agy Quota Burn-Rate Forecast (No Fake Unused Quota)"]
    C2 --> C3["Rule-Switched Page + Physical Allow / Deny Buttons on Permission Prompts"]

    B -- "Retail / Procurement MCP Server Touching Real Money" --> D{"How to Guarantee the Agent Can Never Place an Unauthorized Order?"}
    D -- "Enforce ADR-0001 Architectural Absence of Payment Code" --> E["Adopt NJohansen/handle-mcp Pattern"]
    E --> E1["11 Read-Only Optimization Tools (compare_basket w/ Fees, Offers & Pack Sizes)"]
    E1 --> E2["2 Cart-Only Write Tools (set_cart_quantities / add_recipe_to_cart)"]
    E2 --> E3["Zero Checkout/Payment Code in Repo + Automated CI Absence Test"]
    D -- "Rely on System Prompt Warning Only" --> F["Anti-Pattern: Vulnerable to Indirect Prompt Injection & Drift"]
```

### 3.2 `phonebox` Physical Approval & `handle-mcp` Cart-Only Optimization Sequence

```mermaid
sequenceDiagram
    participant Human as Developer / Buyer
    participant Phone as PhoneBox Android Panel (USB/Tailscale)
    participant Agent as Claude Code / Codex / AGY
    participant Handle as handle-mcp (Python 3.12+ MCP)
    participant Stores as Retail APIs (nemlig / BilkaToGo / REMA 1000)

    Agent->>Phone: Stream live token/context metrics & Claude/Codex/agy burn-rate forecast
    Agent->>Phone: Emit tool permission prompt -> Rule engine switches page & buzzes
    Phone-->>Human: Render tactile Allow / Deny buttons on desk companion screen
    Human->>Phone: Tap Allow (zero IDE window switching)
    Phone-->>Agent: Resume tool execution

    Human->>Agent: "Plan this week's meals on a 4,000 kr budget & fill the cheapest cart"
    Agent->>Handle: list_offers + compare_basket (pack sizes, minimum order, delivery fees)
    Handle->>Stores: Query real-time prices & delivery slots across all 3 chains
    Stores-->>Handle: Return total basket costs (e.g., 693 kr vs 712 kr vs 741 kr)
    Agent->>Handle: set_cart_quantities (populate cheapest store's cart only)
    Note over Handle: ADR-0001 Hard Boundary: Checkout code does not exist; Human pays in store UI
```

---

## 📊 4. Head-to-Head Comparison Matrix

| Evaluation Dimension | Buried Terminal Prompts + Auto-Checkout Scripts (Path A) | Browser Tab Polling + Single-Store Scripts (Path B) | `ersinkoc/phonebox` + `NJohansen/handle-mcp` (Path C) |
| :--- | :--- | :--- | :--- |
| **Permission Prompt Response Latency** | ❌ Hidden behind IDE windows; stalls agents for 20–40m | ⚠️ Requires manual `Alt+Tab` window hunting | ✅ **Phone buzzes & rule engine switches page to physical `Allow / Deny` keys** |
| **Multi-CLI Quota & Burn-Rate Visibility** | ❌ Blind until hard rate-limit error interrupts flow | ⚠️ Missing API reads falsely shown as 100% available | ✅ **Live Claude + Codex + native `agy` burn-rate forecast (`v0.7.2` honest reads)** |
| **Transactional Payment Safety Guarantee** | ❌ Exposed checkout API vulnerable to prompt injection | ⚠️ Relies on LLM obedience not to call pay endpoint | ✅ **`ADR-0001`: checkout code does not exist + CI test fails if added** |
| **Cross-Store Basket Optimization** | ❌ Compares unit stickers without delivery fees or minimums | ⚠️ Locked to a single store's catalog | ✅ **`compare_basket` prices pack sizes, weekly offers, minimums & delivery fees** |
| **Hardware Cost & Telemetry Privacy** | ❌ Expensive proprietary deck + cloud account sync | ⚠️ Third-party trackers logging personal shopping items | ✅ **Repurposes any Android 9+ phone over local USB/Tailscale + `HANDLE_TELEMETRY=0`** |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps Model

> **Provenance & Scope Disclosure**: Governed by `CLAIM-20261112-R26-PHONEBOX-HANDLEMCP` (`provenance: synthetic`, `independently_reproduced: false`). Models `N_seats = 30` AI developer seats and automated procurement workflows at an engineering rate of `$95.00/hr`. Dedicated Stream Deck hardware purchases and underlying retail grocery basket spend are explicitly labeled `not_measured`.

### 5.1 Closed-Form Monthly TCO Equation & Breakdown

$$\text{Monthly TCO} = C_{\text{quota\_and\_rollback}} + \left(H_{\text{hitl\_ops\_eng}} \times \$95.00\right)$$

| Architecture Path | Quota Overrun & Order Rollback Cost ($C_{\text{quota\_and\_rollback}}$) | Context-Switch & Ops Hours ($H_{\text{hitl\_ops\_eng}}$) | Engineering Labor ($\times \$95/\text{hr}$) | Total Monthly TCO | Savings vs. Path A |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Buried CLI Stalls + Auto-Checkout Rollbacks** | `$1,980.00` | `44.0 hrs` | `$4,180.00` | **`$6,160.00`** | Baseline (`0.00%`) |
| **Path B: Browser Tab Polling + Single-Store Cart Scripts** | `$950.00` | `22.0 hrs` | `$2,090.00` | **`$3,040.00`** | `-$3,120.00` (`-50.65%`) |
| **Path C: `PhoneBox` Desk Panel + `handle-mcp` ADR-0001** | `$215.00` | `4.0 hrs` | `$380.00` | **`$595.00`** | **`-$5,565.00` (`-90.34%`)** |

- **Key Quantitative Takeaway**: Path C saves **`$5,565.00/month` (`90.34%` reduction, `$66,780.00/year`)** while cutting developer context-switching and rollback handling from `44.0 hrs/mo` to `4.0 hrs/mo` (`40.0 hrs/mo` saved, **`-90.91%`**).

---

## 🛠️ 6. Actionable AI SA Deployment Checklist

- [ ] **1. Install `ersinkoc/phonebox` (.NET 10 Agent + Android 9+ App) Over USB or Tailscale**:
  ```powershell
  winget install Microsoft.DotNet.SDK.10 Google.PlatformTools
  git clone https://github.com/ersinkoc/phonebox
  cd phonebox
  .\scripts\install.ps1 -Apk -Autostart
  ```
- [ ] **2. Configure Smart Stack Quotas & Permission Rule Switching**: Add Claude Code, Codex, and native Antigravity (`agy`) quota widgets plus a rule that switches to the `Allow / Deny` prompt page whenever a session awaits approval.
- [ ] **3. Register `NJohansen/handle-mcp` with `uvx` & Configure Privacy Controls**:
  ```bash
  export HANDLE_TELEMETRY=0
  uvx handle-mcp@latest login nemlig
  claude mcp add handle -- uvx handle-mcp@latest
  ```
- [ ] **4. Enforce `ADR-0001` Checkout-Absence Tests in Enterprise Transactional MCPs**: Restrict write tools to cart/draft staging (`set_cart_quantities`) and add a CI test asserting that no payment or order-submission endpoints exist in the MCP server.
