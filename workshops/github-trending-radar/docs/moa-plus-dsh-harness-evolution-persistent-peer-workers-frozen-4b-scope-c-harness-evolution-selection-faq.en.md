# Persistent Peer-Messaging Multi-Agent Plugin (`Burns1028/moa-plus`) & Frozen-4B Cross-Hook Harness Evolution (`HuangShengZeBlueSky/dsh-harness-evolution`) Deep-Dive & Selection FAQ

> **Document Metadata (2026-11-14 · Night Round 61 / Cumulative Round 244)**  
> - **Benchmark Style**: `ib-vs-ethernet-roce-selection-faq.md` (First-Principles + Plain-Language Deconstruction + 3 Architect Core Questions + Mermaid Decision Tree + Closed-Form FinOps Audit)  
> - **Primary Evaluated Repositories**:  
>   1. [`Burns1028/moa-plus`](https://github.com/Burns1028/moa-plus) (`★ 114`, MIT Mixture-of-Agents collaboration plugin for DeepSeek Harness, `v0.2.7` stable / `v0.2.8` candidate: connects a Coordinator with **persistent Workers that maintain independent conversations, exchange messages directly peer-to-peer, challenge/review each other's work, and run inside macOS Seatbelt / Linux `bubblewrap` / Windows Job containment** via an isolated `project-mode.mjs` runtime)  
>   2. [`HuangShengZeBlueSky/dsh-harness-evolution`](https://github.com/HuangShengZeBlueSky/dsh-harness-evolution) (`★ 104`, MIT empirical research & artifact suite across **36 model–scope profiles on 4 benchmarks**: keeps a **`Qwen3-4B` executor completely frozen** and evolves the surrounding DeepSeek Harness plugins across **Scopes A (skill text), B (single component), and C (coordinated mechanisms sharing episode-local state across hooks)** — reaching **ALFWorld `95.41 ± 0.00%`, DBBench `70.56 ± 0.38%`, WebShop `48.17 ± 0.29%`, and OSBench `41.67 ± 1.84%`** without fine-tuning model weights)  
> - **Visual Architecture Diagram**: [`assets/github-ai-radar-2026-11-14-r61-moaplus-dshevolution.svg`](../../../assets/github-ai-radar-2026-11-14-r61-moaplus-dshevolution.svg)  
> - **Audit Contract ID**: `CLAIM-20261114-R61-MOAPLUS-DSHEVOLUTION` (local workstation base hardware depreciation is explicitly marked `not_measured`)

---

## 📌 1. Executive Summary (Understand the Essence in 3 Minutes)

1. **Why do one-shot hub-and-spoke subagents turn the coordinator into a message-relay bottleneck and lose codebase context after every task — and how does `Burns1028/moa-plus` (`MoA+`) solve both?**  
   - **Plain-Language Essence**: In standard subagent frameworks, workers cannot talk to each other directly (every question routes through the parent coordinator) and are destroyed as soon as a subtask finishes, forcing the next task to re-discover the repository from scratch.  
   - **First-Principles Breakthrough in `MoA+`**:
     - **Coordinator + Persistent Peer-Messaging Workers**: A Coordinator holds the high-level goal while persistent Workers investigate, build, challenge, and independently review in their own long-lived conversations — **exchanging messages directly worker-to-worker** and carrying their accumulated knowledge into subsequent assignments.
     - **OS-Level Worker Containment & Reversible Isolated Runtime**: Protected Workers enforce macOS Seatbelt, Linux `bubblewrap`, or native Windows Job containment (refusing unadapted persistent terminals), while `apply-native-compat.mjs --backup` and `project-mode.mjs setup --dir` create a self-contained runtime that leaves your personal `~/.dsh` profile untouched.
2. **How much can a frozen `Qwen3-4B` small model improve solely by evolving the plugin harness around it instead of fine-tuning weights? What did `HuangShengZeBlueSky/dsh-harness-evolution` prove across 36 model–scope profiles?**  
   - **Plain-Language Essence**: When a 4B local model fails on database or OS tasks, teams often assume they need expensive GPU fine-tuning. In reality, small models fail because they repeat write queries or submit prematurely without checking execution receipts.  
   - **First-Principles Breakthrough in `dsh-harness-evolution`**:
     - **A/B/C Editable Scope Hierarchy + `L4` Capability-Guided Evolution**: Keeping `Qwen3-4B` frozen, an improver loop (`Observe and attribute → propose candidate → evaluate and select → retain feedback`) evolves DSH plugins across three scopes:
       - **Scope A**: Edits skill text only.
       - **Scope B**: Edits one independent component per round (skill, memory, action checking, or receipt interpretation).
       - **Scope C**: Evolves **coordinated mechanisms sharing episode-local state across hooks**. For example, the evolved DBBench `L4` harness (**`70.56 ± 0.38%`** test success) records database write receipts in episode state, exposes that state in subsequent context prompts, and uses an action-check hook to block duplicate writes and premature submission!
     - **Measured Peaks on Frozen `Qwen3-4B`**: Achieves **ALFWorld `95.41 ± 0.00%`**, **DBBench `70.56 ± 0.38%`**, **WebShop `48.17 ± 0.29%`**, and **OSBench `41.67 ± 1.84%`** (`C-sol61-narrow v01`) purely via harness evolution.
3. **Closed-Form FinOps Audit Conclusion (`CLAIM-20261114-R61-MOAPLUS-DSHEVOLUTION`)**:  
   - Modeled for **36 domain agent workflows and multi-agent engineering tasks/month** (at **`$100.00/hr`** engineering labor): migrating from **Path A** (repeated 70B+ model fine-tuning + hub-bottlenecked ephemeral subagents: **`$5,920.00/mo`**, comprising `$2,120.00` GPU/token spend + `38.0h` fine-tuning and manual coordination labor `$3,800.00`) to **Path C** (`dsh-harness-evolution` Scope-C evolved harnesses on frozen `Qwen3-4B` + `MoA+` persistent peer Workers: **`$505.00/mo`**, comprising `$155.00` lean inference/evolution spend + `3.5h` review labor `$350.00`) saves **`$5,415.00/mo`** (**`-91.47%`**, or **`$64,980.00/yr`**) and cuts engineering hours by **`90.79%`**.

![MoA+ & dsh-harness-evolution Architecture Overview](../../../assets/github-ai-radar-2026-11-14-r61-moaplus-dshevolution.svg)

---

## 💬 2. Three Architect Core Questions (Q1–Q3 Deep Dive)

### Q1: Why does `Scope C` (shared episode-local state across hooks) outperform `Scope A` (skill text only) so dramatically on a frozen `Qwen3-4B` executor?

1. **Coupling Receipt Recording with Deterministic Action Guards**:  
   - Prompt instructions alone (`Scope A`) cannot stop a 4B model from losing track of whether a database mutation succeeded five turns ago. Under `Scope C`, tool-execution hooks write structured receipts into `episode-local state` while pre-action hooks read that exact state to deterministically block duplicate mutations or premature task submission.

---

### Q2: How does `Burns1028/moa-plus` patch 22 native DSH packages across 50 file paths without breaking the developer's main DeepSeek Harness installation?

1. **Audited Compatibility Profiles + `--backup` + Isolated `project-mode.mjs` Directories**:  
   - `apply-native-compat.mjs` validates target file hashes (`--dry-run`) and backs up original files before applying the pinned `DSH 0.2.1-rc.3` or `2.0.22-next` profile, while `project-mode.mjs setup --dir` provisions a separate home/config directory outside `~/.dsh`.

---

### Q3: How does `MoA+` enforce security across macOS, Linux, and Windows when persistent Workers execute shell commands?

1. **Platform-Native Process Sandboxing**:  
   - Protected Workers require macOS Seatbelt, Linux `bubblewrap`, or Windows Job containment (with nonpersistent PowerShell/Bash in the rc.2 Desktop Next profile) and automatically refuse execution on unadapted persistent terminal providers.

---

## 🧭 3. Architecture Decision Tree & Topology (Mermaid)

```mermaid
flowchart TD
    Start["DeepSeek Harness Multi-Agent Collaboration & Small-Model Accuracy Optimization"] --> Goal{"Primary Architectural Objective?"}

    Goal -->|"Multi-Role Engineering (Investigate + Build + Challenge + Independent Review)"| CollabGate{"Worker Topology?"}
    CollabGate -->|"Persistent Worker Contexts + Direct Peer-to-Peer Messaging<br/>+ Seatbelt/bwrap/Windows Job Containment"| UseMoAPlus["✅ Burns1028/moa-plus (MIT · v0.2.7 / v0.2.8)<br/>• Coordinator + persistent Workers communicating directly<br/>• Isolated project-mode.mjs runtime leaving ~/.dsh untouched"]
    CollabGate -->|"Simple one-off stateless summary"| EphemeralSub["🔄 Standard Ephemeral Subagent"]

    Goal -->|"Maximize Domain Benchmark/Production Accuracy on a Frozen 4B Executor"| EvolveGate{"Optimization Surface?"}
    EvolveGate -->|"Evolve Coordinated Multi-Hook Episode-State Plugins (Scope C / L4)"| UseDSHEvolve["✅ HuangShengZeBlueSky/dsh-harness-evolution (MIT · 36 Profiles)<br/>• Episode-state write receipts + action-check premature-submit guards<br/>• Frozen Qwen3-4B: ALFWorld 95.41% · DBBench 70.56% · OSBench 41.67%"]
    EvolveGate -->|"Prompt text edits only (Scope A)"| ScopeAOnly["⚠️ Scope A Skill-Text Only (Plateaus on stateful tasks)"]

    UseMoAPlus --> FinOps["💰 Closed-Form FinOps Impact (CLAIM-20261114-R61-MOAPLUS-DSHEVOLUTION)<br/>Monthly Total $5,920.00 ➔ $505.00 (-91.47% · Saves $64,980/yr)"]
    UseDSHEvolve --> FinOps
```

---

## 📊 4. Peer Comparison Matrix (Decision Matrix)

| Evaluation Dimension | `Burns1028/moa-plus` (Persistent Peer MoA Plugin) | Hub-and-Spoke Ephemeral Subagents | `dsh-harness-evolution` (`Scope C / L4` Harness Search) | Weight Fine-Tuning / `Scope A` Prompting |
| :--- | :--- | :--- | :--- | :--- |
| **Communication & State** | **Direct worker-to-worker messaging + persistent sessions** | All messages bottleneck through coordinator; state lost | **Shared `episode-local state` across context & action hooks** | Uncoordinated stateless prompts or expensive weight updates |
| **Containment & Provenance** | **macOS Seatbelt / Linux `bubblewrap` / Windows Job** | Often runs unsandboxed in host shell | **36 versioned model×scope profiles with full evaluation JSONs** | Opaque checkpoint weights or unversioned prompt tweaks |
| **Small-Model Accuracy** | Independent peer review catches bugs before Coordinator merge | Single-agent blind spots | **Frozen `Qwen3-4B` hits `95.41%` ALFWorld & `70.56%` DBBench** | 4B base model fails on repeated writes & premature submits |
| **Deployment Safety** | **`--backup` + isolated `project-mode.mjs` runtime directory** | Modifies global agent configuration | **MIT open-source; evolved harnesses mount as standard plugins** | Requires GPU cluster retraining on every schema change |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261114-R61-MOAPLUS-DSHEVOLUTION`)

> **Scope & Boundary Declaration**: This synthetic FinOps model covers monthly GPU fine-tuning and API token spend across **36 domain agent workflows and multi-agent engineering tasks** plus engineering labor for **manual hook state-machine coding and multi-agent context relaying** (at **`$100.00/hr`**); local workstation base hardware depreciation is explicitly marked **`not_measured`**.

| Architecture Path | GPU & Token Spend (`USD/mo`) | Tuning & Coordination Labor (`hrs/mo`) | Engineering Labor Cost (`@ $100/hr`) | Total Monthly Cost (`USD/mo`) | Net Savings vs. Path A (`USD/mo` & `%`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Repeated 70B+ Fine-Tuning + Hub-Bottlenecked Swarm** | `$2,120.00` | `38.0 hrs` | `$3,800.00` | **`$5,920.00`** | Baseline (`0.00%`) |
| **Path B: `Scope A` Prompt Tweaks + Uncontained Workers** | `$980.00` | `18.0 hrs` | `$1,800.00` | **`$2,780.00`** | `-$3,140.00` (`-53.04%`) |
| **Path C (Recommended): `Scope C` Evolution + `MoA+` Peer Workers** | **`$155.00`** | **`3.5 hrs`** | **`$350.00`** | **`$505.00`** | **`-$5,415.00` (`-91.47%`)** |

- **Closed-Form Verification Equations**:
  - $\text{Path A Total} = 2120.00 + 38.0 \times 100.00 = 2120.00 + 3800.00 = \$5,920.00$
  - $\text{Path B Total} = 980.00 + 18.0 \times 100.00 = 980.00 + 1800.00 = \$2,780.00$
  - $\text{Path C Total} = 155.00 + 3.5 \times 100.00 = 155.00 + 350.00 = \$505.00$
  - $\text{Net Savings (Path C vs Path A)} = 5920.00 - 505.00 = \$5,415.00/\text{mo} \quad (-91.47\%, \text{Annualized } \$64,980.00/\text{yr})$

---

## 🛠️ 6. AI Solution Architect Actionable Checklist

1. **Set up an isolated `Burns1028/moa-plus` runtime directory**:
   ```bash
   git clone --branch v0.2.7 --single-branch https://github.com/Burns1028/moa-plus.git && cd moa-plus
   npm ci && node scripts/apply-native-compat.mjs --backup "$PWD/.superpowers/native-backup"
   npm run build && node scripts/project-mode.mjs setup --dir /tmp/isolated-moa-runtime
   ```
2. **Apply `dsh-harness-evolution` `Scope C` episode-state receipts to production tool loops**:
   - Record mutation receipts in `episode-local state` and wire pre-action check hooks to reject duplicate writes or premature task completion.
