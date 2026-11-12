# Zero-Dependency Read-Only Node Health (`ValidatorStack/solana-vigil`) & $3 Arduino Hardware-in-the-Loop ECU Diagnostic Agent (`MZULALI/xj-scanner`) Selection FAQ

> **Document Scope**: This is the **2026-11-12 Night Shift Round 16 (Cumulative #115) standalone 6-part selection guide**, modeled strictly after `ib-vs-ethernet-roce-selection-faq.md` with first-principles explanations and closed-form FinOps math. It is written for High-Security Infrastructure Architects and Embedded Hardware-in-the-Loop (HIL) AI Engineers evaluating two exemplary repositories:
> 1. **`ValidatorStack/solana-vigil` (`241★`, Go 1.23+, Go standard library only with `CGO_ENABLED=0`, MIT)**: A single static Linux binary delivering 60-second validator health scores, leader duties, rewards, disk forecasts, and Prometheus metrics — **read-only by construction (never touches seed phrases, private keys, or host settings)**, reporting **honest `unknown` states** on missing RPC fields rather than fabricated healthy defaults, with built-in alert-storm deduplication!
> 2. **`MZULALI/xj-scanner` (`156★`, Python / Arduino C++ / `.claude/skills/`, GPL-3.0)**: Connects a 1991–95 Jeep Cherokee XJ 4.0L engine computer (`56030117` SBEC/OBD1) to a laptop via a **$3 Arduino Nano and three wires** so Claude Code or Codex can read fault codes, log live drives, and run actuator tests — featuring **disassembly-verified fuel-trim scaling**, a **`--cli DEMO` simulated vehicle mode**, and **strict multimeter verification guardrails (never connect to Cavity 6 +12V)**!
>
> **中文版本**: [solana-vigil-xj-scanner-zero-dep-readonly-node-health-arduino-ecu-agent-selection-faq.md](solana-vigil-xj-scanner-zero-dep-readonly-node-health-arduino-ecu-agent-selection-faq.md) · **Daily Digest**: [`daily/2026-11-12.en.md`](../daily/2026-11-12.en.md) · **Architecture Summary SVG**: [`assets/github-ai-radar-2026-11-12-r16-vigil-xjscanner.svg`](../../../assets/github-ai-radar-2026-11-12-r16-vigil-xjscanner.svg)

![solana-vigil and xj-scanner Architecture Comparison](../../../assets/github-ai-radar-2026-11-12-r16-vigil-xjscanner.svg)

---

## 📌 1. Executive Summary

1. **In plain English, what core pain points do these two repositories solve?**
   - **Ending "bloated monitoring agents that pull hundreds of third-party dependencies onto high-value production servers, request keypair access, fabricate '0 error' defaults when RPC calls fail, or trigger 200-message alert storms" (`ValidatorStack/solana-vigil`)**: On high-stakes Linux servers (validator nodes, signing hosts, financial gateways), every third-party dependency and write permission is an unacceptable supply-chain risk. `solana-vigil` demonstrates gold-standard infrastructure engineering: (1) **Go standard library only (`CGO_ENABLED=0`)** producing a single static Linux AMD64/ARM64 binary with zero hidden dependency tree; (2) **read-only by construction** with zero code paths for key loading, transaction signing, or host mutation; (3) **honest uncertainty** where missing RPC fields become `unknown` rather than fabricated healthy numbers; and (4) sustained-failure thresholds and deduplication that eliminate alert storms!
   - **Ending "paying thousands for vintage proprietary diagnostic scanners or letting an unguided AI tell you to wire by wire color — shorting +12V into a 5V microcontroller" (`MZULALI/xj-scanner`)**: Bringing AI agents into physical hardware debugging leaves zero room for halluncinated wiring. `xj-scanner` bridges a 1991–95 Jeep SBEC/OBD1 engine computer to Claude Code / Codex using a **$3 Arduino Nano** and `.claude/skills/` playbooks: (1) **physical-safety guardrails**: because Cavity 6 (+12V with key on) shares the same black/white wire color as Cavity 2 (ground) on the test car, `AGENTS.md` strictly forbids wiring by color and walks you through multimeter voltage checks first; (2) **simulated dry-run (`--cli DEMO`)** to verify the laptop stack before touching the vehicle; and (3) **ROM-disassembly-verified parameter scaling**!
2. **Closed-Form FinOps Conclusion (`CLAIM-20261112-R16-VIGIL-XJSCANNER`)**:
   - Modeled for a **10-person high-security node operations & embedded HIL diagnostics team monitoring `40 bare-metal servers` and executing `60 hardware diagnostic sessions` per month** (fully loaded senior infra/embedded engineer rate `$90.00/hr`; bare-metal server hosting and vintage proprietary scanner hardware: `not_measured`):
   - Upgrading from **Path A (heavy dependency-laden monitoring agents + unguided hardware wiring and hex debugging, `$5,820.00/mo`)** to **Path C (`solana-vigil` zero-dep static Go binary + `xj-scanner` `--cli DEMO` & multimeter-gated skill, `$650.00/mo`)** saves **`$5,170.00/mo` (`-88.83%`, or `$62,040.00/yr`)** and cuts alert-storm triage and hardware debugging labor from `48.0 hrs/mo` to `5.0 hrs/mo` (**`-89.58%`**).

---

## 🎯 2. Three First-Principles Deep-Dive Questions (Q1 / Q2 / Q3)

### Q1: Why is `ValidatorStack/solana-vigil`'s combination of `CGO_ENABLED=0` stdlib-only code, read-only construction, and honest `unknown` states a blueprint for critical infrastructure telemetry?
- **First-Principles Breakdown**:
  1. **Zero Supply-Chain Surface & Read-Only Construction**:
     - Compiles with Go's standard library only (`CGO_ENABLED=0`) and contains no key-loading, signing, failover, or host-mutation code paths, using only local RPC and public addresses.
  2. **Honest `unknown` Semantics & Sustained-Failure Deduplication**:
     - Never coerces failed observations to healthy defaults (`unknown` is explicit), and suppresses alert storms via sustained-failure thresholds, stable recovery windows, and env-only secret configuration.

### Q2: How does `MZULALI/xj-scanner` make physical hardware-in-the-loop (HIL) agent diagnostics safe for beginners and accurate for engineers?
- **First-Principles Breakdown**:
  1. **Multimeter Pre-Check Guardrail (Cavity 6 +12V Protection) & `--cli DEMO`**:
     - Enforces step-by-step multimeter measurements before connecting Nano pins `D10`, `D11`, and `GND` to cavities `4`, `3`, and `2`, and provides `python pc/xj_scan.py --cli DEMO` plus `xj_sniff` for safe software/wiring verification.
  2. **Disassembly-Verified SBEC Scaling**:
     - Resolves fuel-trim scaling discrepancies directly from disassembled SBEC ROM code (`56030117`), logging live drives to `pc/logs/` for agent-assisted analysis.

### Q3: How can Enterprise AI Solution Architects apply these patterns?
- **Architectural Takeaway**:
  - Build production telemetry agents as **zero-dependency, read-only binaries that report `unknown` rather than coerced zeros**;
  - Design physical/industrial hardware skills with **mandatory `--cli DEMO` dry-runs and instrument-verified voltage guardrails** before physical actuation!

---

## 🧭 3. Mermaid Decision Tree & Read-Only Telemetry + Safe HIL Diagnostics Pipeline

```mermaid
flowchart TD
    A["High-Security Node Telemetry & Hardware-in-the-Loop (HIL) Agent Diagnostics"] --> B{"Primary Engineering Target?"}
    B -- "Monitor high-value Linux validator/production servers with zero supply-chain or key risk" --> C["Adopt ValidatorStack/solana-vigil (CGO_ENABLED=0 Go Stdlib Binary)"]
    B -- "Bridge embedded/automotive serial ECUs to Coding Agents via a $3 microcontroller" --> D["Adopt MZULALI/xj-scanner ($3 Arduino Nano + Multimeter Skill)"]

    C --> C1["vigil init validates public addresses & local RPC (zero key/mutation code paths)"]
    C1 --> C2["Failed probes emit explicit unknown + sustained-failure dedup -> Prometheus/JSON"]

    D --> D1["Stage 1: Run xj_scan.py --cli DEMO simulated vehicle to verify laptop & agent stack"]
    D1 --> D2["Stage 2: Agent guides multimeter voltage check on all 6 cavities (avoid Cavity 6 12V)"]
    D2 --> D3["Stage 3: Flash xj_bridge -> read fault codes, log live drives & run actuator tests"]
```

---

## 📊 4. Head-to-Head Selection Matrix

| Dimension | Path A: Heavy Monitoring Daemons + Unguided Wiring | Path B: Custom Pollers + Manual Hex Decoding | **Path C (Recommended): `solana-vigil` + `xj-scanner`** |
| :--- | :--- | :--- | :--- |
| **Supply-Chain & Key Safety** | Hundreds of transitive deps; often requests key access | Hardcoded secrets in ad-hoc scripts | **Go stdlib only (`CGO_ENABLED=0`); read-only by construction** |
| **Missing-Data Honesty & Alerting** | Coerces timeouts to `0`; triggers alert storms | No deduplication or recovery hysteresis | **Explicit `unknown` state + sustained-failure dedup & escalation** |
| **Physical Hardware Safety** | Wiring by wire color risks +12V short into 5V logic | Manual schematic hunting | **Mandatory multimeter verification (Cavity 6 guardrail) + `--cli DEMO`** |
| **Protocol Scaling Accuracy** | Expensive proprietary scanners ($1,000+) | Uncalibrated byte guessing | **$3 Arduino Nano + ROM-disassembly-verified scaling formulas** |
| **Monthly TCO (40 Nodes + 60 Sessions)** | **`$5,820.00 / mo`** (`$1,500` SaaS/API + `$4,320` labor) | **`$2,940.00 / mo`** (`$780` compute + `$2,160` labor) | **`$650.00 / mo` (Saves `$5,170.00/mo` · `-88.83%`)** |

---

## 🧪 5. Closed-Form FinOps Worked Example & 7-Card Insights (`CLAIM-20261112-R16-VIGIL-XJSCANNER`)

### 5.1 Baseline Parameters & Explicit Scope Boundaries
- **Scenario**: A 10-person high-security node operations & embedded diagnostics team monitoring **40 bare-metal servers** and running **60 hardware-in-the-loop diagnostic sessions per month**.
- **Labor Rate**: Fully loaded senior infrastructure/embedded engineering rate of **`$90.00 / hr`**.
- **Explicit Not-Measured Boundary**: Bare-metal server hosting fees and vintage proprietary diagnostic scanner hardware costs are marked **`not_measured`**. This model strictly accounts for monitoring SaaS/API spend and engineering hours spent on alert-storm triage, false-healthy debugging, and hardware protocol decoding.

### 5.2 Three-Path Monthly Cost Comparison

| Cost Component | Path A: Heavy Monitoring SaaS + Unguided Wiring | Path B: Custom Pollers + Manual Hex Decoding | **Path C: `solana-vigil` + `xj-scanner` (Recommended)** |
| :--- | :--- | :--- | :--- |
| **Monthly Monitoring SaaS & Diagnostic Agent API Spend** | **`$1,500.00`** | **`$780.00`** | **`$200.00`** ($0 static `vigil` binary + structured `pc/logs/` analysis) |
| **Alert-Storm Triage, False-Zero & Hardware Debugging Labor (`$90/hr`)** | `48.0 hrs × $90.00` = **`$4,320.00`** | `24.0 hrs × $90.00` = **`$2,160.00`** | `5.0 hrs × $90.00` = **`$450.00`** |
| **Total Monthly TCO** | **`$5,820.00 / mo`** | **`$2,940.00 / mo`** (`-49.48%`) | **`$650.00 / mo`** |
| **Net Savings vs. Path A** | Baseline | Saves `$2,880.00 / mo` | **Saves `$5,170.00 / mo` (`-88.83%` · `$62,040.00/yr`)** |
| **Bare-Metal Server Hosting & Proprietary Scanners** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 6. Production Adoption Checklist

- [ ] **1. `solana-vigil` Zero-Dependency & Static Build Check**: Verify `go.mod` has zero external dependencies, build with `CGO_ENABLED=0`, and run `vigil init` and `vigil check` on testnet first.
- [ ] **2. Honest `unknown` & Alert-Storm Hysteresis Test**: Simulate an RPC timeout and confirm that metrics report `unknown` rather than healthy defaults.
- [ ] **3. `xj-scanner` `--cli DEMO` Dry-Run**: Execute `.venv/bin/python pc/xj_scan.py --cli DEMO` to validate the laptop and agent pipeline before connecting USB hardware.
- [ ] **4. Multimeter Cavity Verification**: Measure all 6 diagnostic plug cavities with a multimeter to isolate Cavity 6 (+12V key-on) before connecting Arduino Nano pins `D10`, `D11`, and `GND`.
