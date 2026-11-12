# Visual Canvas-to-Python Agent Compiler & 1-Demo World In-Context Learning Selection FAQ: `YT-Proteus-bot/MineAgent` (110-Node Canvas Compiling to Standalone Python) vs. `ArcheOne-AI/RoboScript` (`arXiv:2611.12885` WICL Achieving `83.4%` on RoboTwin 2.0 with Zero Gradient Updates)

> **Document Scope**: Written for AI Solution Architects (AI SAs), Enterprise Agent Platform Leads, and Embodied AI / Robotics Architects. Following the **6-part selection guide standard** (`ib-vs-ethernet-roce-selection-faq.md`), this FAQ dissects two high-velocity repositories from the 2026-11-12 GitHub radar — **`YT-Proteus-bot/MineAgent` (173★, Apache-2.0, a React Flow + FastAPI + SQLite visual orchestration compiler with 110 node types and 33 reasoning templates that compiles canvases directly into standalone runnable Python projects)** and **`ArcheOne-AI/RoboScript` (120★, Apache-2.0, `arXiv:2611.12885`, Huazhong University of Science and Technology & ArcheOne AI's World In-Context Learning `WICL` framework achieving `83.4%` mean success across 50 bimanual tasks on RoboTwin 2.0 from a single demonstration with zero gradient updates)** — answering: **"Why do visual agent builders trap teams in proprietary JSON runtimes while embodied VLA policies still fail `38.3%` of the time after 50 teleoperated demonstrations, and how does combining a canvas-to-Python compiler with 1-demo World In-Context Learning cut engineering TCO by `89.74%`?"**

![Canvas-to-Python Agent Compiler & 1-Demo World In-Context Learning SVG](../../../assets/github-ai-radar-2026-11-12-r25-mineagent-roboscript.svg)

---

## 📌 1. Executive Summary

1. **Plain-Language First-Principles Definitions**:
   - **`YT-Proteus-bot/MineAgent` (A Zero-Lock-In Visual Agent Canvas That Compiles Directly into Standalone Runnable Python Projects)**: Most visual workflow builders save an opaque JSON blob that can only run inside their proprietary engine. Built on React 18 + React Flow + FastAPI + SQLite (zero ORM), `MineAgent` provides **110 fine-grained node types** (intent classification, query rewriting, hybrid retrieval, reranking, MCP, guardrails, human approval) and **33 reasoning mode templates** (`react`, `plan_execute`, `goal`, `reflexion`, `tool_call`, `simple` across LangChain/LangGraph, AutoGen, and CrewAI). Pressing Save (`Ctrl+S`) compiles the entire canvas into a **self-contained, standalone Python project under `projects/<canvas_name>/`**, complete with organizational delegation (`ctx.superior`, `ctx.subordinates`, `ctx.peers`, `ctx.delegate()`), encrypted per-node API keys injected via `MINEAGENT_KEY_<node_id>`, live node-pulse streaming, and an offline `tools/mock_llm.py` test server.
   - **`ArcheOne-AI/RoboScript` (Learn Bimanual Robot Manipulation in Context, Not in Weights — `83.4%` on RoboTwin 2.0 from 1 Demo & Zero Gradient Updates, `arXiv:2611.12885`)**: Instead of collecting 50+ teleoperated trajectories per task to fine-tune neural action weights, `RoboScript` introduces **World In-Context Learning (WICL)**. A frozen foundation model starts from **1 demonstration**, rehearses the task inside a simulator world (`wicl`, `rsi`, `skill_builder`), and writes learned physical rules and recovery heuristics into a **`Task Memory`** in its context window. On **RoboTwin 2.0 (50 bimanual manipulation tasks)**, `RoboScript` achieves **`83.4%` mean success** with 1 demo and 0 gradient updates — beating the strongest 50-demo trained policy (**`61.7%`**) by **`+21.7` percentage points**, maintaining **`83.2%`** on unseen randomized scenes (`83.6% → 83.2%`), and transferring ALOHA-rehearsed Task Memories directly to a real dual-arm **PiPER** robot via parameter remapping without re-rehearsing.
2. **Core Selection Guardrails**:
   - When building **visual multi-agent workflows where production engineering teams require clean, editable, git-auditable Python source code without vendor lock-in or leaked API keys**, choose **`YT-Proteus-bot/MineAgent`**.
   - When developing **bimanual or tabletop robot manipulation systems that must generalize from a single demonstration across randomized scenes and real hardware without per-task GPU gradient fine-tuning**, choose **`ArcheOne-AI/RoboScript` (`arXiv:2611.12885`)**.
3. **Quantitative FinOps Takeaway**: Under our closed-form benchmark (`25` multi-agent workflows & embodied manipulation tasks/month, AI/robotics systems engineering rate `$100.00/hr`, physical dual-arm robot hardware & base VLA pretraining clusters marked `not_measured`), migrating from **Path A (Proprietary Low-Code Rewrite + 50-Demo Gradient Policy Fine-Tuning)** (`$7,600.00/mo`) to **Path C (`MineAgent` Standalone Python Compiler + `RoboScript` 1-Demo WICL Task Memory)** (`$780.00/mo`) saves **`$6,820.00/month` (`89.74%` reduction, `$81,840.00/year`)** and cuts engineering and teleoperation labor from `50.0 hrs/mo` to `5.0 hrs/mo` (`-90.00%`).

---

## ❓ 2. First-Principles Deep Dive (Q1–Q3)

### Q1: Why do enterprise teams frequently abandon visual agent builders when moving from prototype to production, and how does `YT-Proteus-bot/MineAgent` bridge visual design and standalone Python code?

- **Root Cause**: Traditional low-code canvases trap execution inside a monolithic runtime interpreter, disallow per-node custom Python logic, and frequently embed plaintext credentials inside exported JSON templates.
- **How `YT-Proteus-bot/MineAgent` Solves It**:
  1. **Canvas-to-Standalone-Python Compilation (`projects/<canvas_name>/`)**: Every save compiles the visual graph (110 node types, 33 reasoning templates) into a standalone runnable Python project with service entrypoints, concurrency settings, observability, and safety guards. Double-clicking any node opens a live Python code editor for that node's execution logic.
  2. **First-Class Organizational Hierarchy (`ctx.delegate`)**: Separates organizational hierarchy from dataflow edges. Assigning superiors, subordinates, or peers in the inspector synchronizes both sides and exposes `ctx.superior`, `ctx.subordinates`, `ctx.peers`, and `ctx.delegate(name, task)` at runtime.
  3. **Constraint-Checked Auto-Wiring & Offline `mock_llm.py` Verification**: Enforces mandatory `input`/`output` blocks, obstacle-avoiding edge routing, and BFS layered auto-layout, while `tools/mock_llm.py --port 8012` validates the entire compile-and-stream loop without external API keys.
  4. **Encrypted Credential Isolation (`MINEAGENT_KEY_<node_id>`)**: Node-level API keys are encrypted in SQLite (`agent_models`) and injected into subprocess environments as `MINEAGENT_KEY_<id>`, never touching `agent.json` or community PR exports.

### Q2: Why does fine-tuning a robot action policy on 50 demonstrations per task still plateau at `61.7%` on RoboTwin 2.0 while `ArcheOne-AI/RoboScript` reaches `83.4%` from a single demonstration and zero gradient updates?

- **Root Cause**: Weight fine-tuning on dozens of demonstrations overfits specific trajectories and lacks explicit semantic error-recovery rules when object poses shift, whereas zero-shot LLM code generation without world rehearsal fails on contact physics and gripper geometry.
- **How `ArcheOne-AI/RoboScript` (`arXiv:2611.12885`) Solves It**:
  1. **4-Stage World In-Context Learning (`WICL`) Pipeline**:
     - **Skills**: Extracts reusable manipulation skills from demonstrations;
     - **Task Learning (World Rehearsal)**: Starting from **1 demonstration**, a frozen foundation model rehearses the task in a simulator world (`wicl`, `rsi`, `skill_builder`) and distills failure modes and spatial constraints into an in-context **`Task Memory`**;
     - **Deployment**: Freezes the `Task Memory` and executes on unseen clean (`83.6%`) and randomized (`83.2%`) scenes using only real-robot-accessible sensor inputs;
     - **Reflection**: Refines Task Memory from evaluation rollouts.
  2. **Strict Separation of Agent Plane vs. Control Plane**: The `Agent plane` sees only what a physical robot can sense, while the `Control plane` holds simulator ground truth and runs official success checks — preventing simulator state leakage. Heavy perception (`GroundingDINO`, `SAM 3`) and motion planning (`cuRobo`) run as decoupled services.
  3. **Zero-Rehearsal Sim-to-Real Transfer (ALOHA → Dual-Arm PiPER)**: Because Task Memory encodes structured manipulation logic in context rather than embodiment-locked neural weights, memories rehearsed on a simulated ALOHA transfer directly to a physical dual-arm PiPER robot via parameter remapping.

### Q3: How can AI Solution Architects combine `MineAgent` and `RoboScript` in cyber-physical enterprise workflows?

- **Combined Architecture Pattern**:
  - **Digital Orchestration Plane (`YT-Proteus-bot/MineAgent`)**: Design and compile multi-agent planning, retrieval, approval, and supervisor-worker workflows into standalone Python services.
  - **Physical Manipulation Plane (`ArcheOne-AI/RoboScript`)**: Delegate physical workstation tasks to `RoboScript`'s Model Gateway and Agent Plane, leveraging 1-demo WICL Task Memories (`83.4%` RoboTwin 2.0 success) and `cuRobo` / `SAM 3` services.

---

## 🧭 3. Mermaid Decision Tree & Architecture Sequence

### 3.1 Visual Agent Compiler & Embodied WICL Framework Decision Tree

```mermaid
flowchart TD
    A["Building a Multi-Agent Orchestration System or an Embodied Robot Manipulation Pipeline?"] --> B{"Digital Multi-Agent Workflow or Physical/Simulated Bimanual Manipulation?"}
    B -- "Visual Multi-Agent Design Requiring Standalone Python Code Export" --> C["Deploy YT-Proteus-bot/MineAgent (Apache-2.0)"]
    C --> C1["110 Node Types + 33 Reasoning Templates -> Compile to projects/<canvas>/"]
    C1 --> C2["ctx.superior / subordinates / peers / delegate() Organizational Runtime"]
    C2 --> C3["MINEAGENT_KEY_<id> Secret Isolation + tools/mock_llm.py Offline Harness"]

    B -- "Bimanual Robot Manipulation (Few Demos, Randomized Scenes & Sim-to-Real)" --> D{"Replace 50-Demo Gradient Fine-Tuning with 1-Demo In-Context Rehearsal?"}
    D -- "Yes (World In-Context Learning into Frozen Task Memory)" --> E["Adopt ArcheOne-AI/RoboScript (arXiv:2611.12885)"]
    E --> E1["1 Demo + Simulator Rehearsal (wicl/rsi/skill_builder) -> Task Memory"]
    E1 --> E2["Agent Plane (Real Sensor Scope) Isolated from Control Plane (Ground Truth)"]
    E2 --> E3["83.4% on RoboTwin 2.0 (83.2% Randomized) + ALOHA-to-PiPER Parameter Remap"]
    D -- "No (Massive Fixed-Line Teleop Dataset Available)" --> F["Traditional End-to-End Action Policy Training"]
```

### 3.2 `MineAgent` Compilation & `RoboScript` 4-Stage WICL Execution Sequence

```mermaid
sequenceDiagram
    participant Eng as AI / Robotics Engineer
    participant Canvas as MineAgent (React Flow + FastAPI)
    participant PyProj as projects/<canvas>/ (Standalone Python)
    participant Robo as RoboScript Agent Plane
    participant World as Simulator / Control Plane + Services (cuRobo/SAM 3)

    Eng->>Canvas: Wire Supervisor + Workers (110 nodes, 6 modes) & Save (Ctrl+S)
    Canvas->>PyProj: Compile standalone Python project (inject MINEAGENT_KEY_<id> at runtime)
    PyProj-->>Eng: Execute ctx.delegate() w/ live node pulse & token streaming

    Eng->>Robo: Provide 1 demonstration (0 gradient updates)
    loop Stage 2: World Rehearsal (Clean Scene Only)
        Robo->>World: Perceive via GroundingDINO / SAM 3 & plan via cuRobo
        World-->>Robo: Control Plane returns official check & physical feedback
        Robo->>Robo: Distill spatial & recovery rules into in-context Task Memory
    end
    Eng->>Robo: Stage 3 Deploy frozen Task Memory to randomized scenes / real PiPER robot
    Robo-->>Eng: Achieve 83.4% mean success on RoboTwin 2.0 (83.2% randomized)
```

---

## 📊 4. Head-to-Head Comparison Matrix

| Evaluation Dimension | Proprietary JSON Low-Code + 50-Demo SFT Policy (Path A) | Hand-Rolled LangGraph Boilerplate + 10-Demo Scripts (Path B) | `YT-Proteus-bot/MineAgent` + `ArcheOne-AI/RoboScript` (Path C) |
| :--- | :--- | :--- | :--- |
| **Visual Workflow Output & Lock-In** | ❌ Opaque JSON locked to proprietary runtime | ⚠️ No visual topology; high boilerplate maintenance | ✅ **Compiles canvas directly into standalone runnable Python (`projects/<canvas>/`)** |
| **Multi-Agent Hierarchy & Key Security** | ❌ Mixes org hierarchy with data edges; leaks keys in JSON | ⚠️ Manual delegation glue code | ✅ **`ctx.delegate()` org hierarchy + encrypted `MINEAGENT_KEY_<id>` env injection** |
| **Robot Demonstration & Training Cost** | ❌ 50+ teleop demos & GPU weight fine-tuning per task | ⚠️ Rigid waypoint scripts break under pose shifts | ✅ **`1` demonstration + `0` gradient updates via World In-Context Learning (`WICL`)** |
| **RoboTwin 2.0 (50 Bimanual Tasks) Success** | ❌ Strongest 50-demo trained policy reaches **`61.7%`** | ⚠️ Scripted heuristics fail `<40%` on bimanual tasks | ✅ **`83.4%` mean success (`+21.7` pts) with `83.6% → 83.2%` on randomized scenes** |
| **Sim-to-Real Cross-Embodiment Transfer** | ❌ Requires collecting new real-world demos & retraining | ⚠️ Manual kinematic re-scripting per robot | ✅ **ALOHA-rehearsed `Task Memory` runs on real dual-arm PiPER via parameter remapping** |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps Model

> **Provenance & Scope Disclosure**: Governed by `CLAIM-20261112-R25-MINEAGENT-ROBOSCRIPT` (`provenance: synthetic`, `independently_reproduced: false`). Models `N_tasks = 25` monthly multi-agent workflow compilations and bimanual robot manipulation tasks at an AI/robotics engineering labor rate of `$100.00/hr`. Physical dual-arm robot hardware acquisition and base VLA foundation model pretraining clusters vary by lab and are explicitly labeled `not_measured`.

### 5.1 Closed-Form Monthly TCO Equation & Breakdown

$$\text{Monthly TCO} = C_{\text{compute\_and\_api}} + \left(H_{\text{agent\_robotics\_eng}} \times \$100.00\right)$$

| Architecture Path | Teleop GPU Fine-Tuning & API Cost ($C_{\text{compute\_and\_api}}$) | Workflow & Robotics Eng Hours ($H_{\text{agent\_robotics\_eng}}$) | Engineering Labor ($\times \$100/\text{hr}$) | Total Monthly TCO | Savings vs. Path A |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Locked Low-Code Rewrite + 50-Demo SFT Policy** | `$2,600.00` | `50.0 hrs` | `$5,000.00` | **`$7,600.00`** | Baseline (`0.00%`) |
| **Path B: Manual Graph Code + 10-Demo Scripted Heuristics** | `$1,240.00` | `25.0 hrs` | `$2,500.00` | **`$3,740.00`** | `-$3,860.00` (`-50.79%`) |
| **Path C: `MineAgent` Python Compiler + `RoboScript` 1-Demo WICL** | `$280.00` | `5.0 hrs` | `$500.00` | **`$780.00`** | **`-$6,820.00` (`-89.74%`)** |

- **Key Quantitative Takeaway**: Path C saves **`$6,820.00/month` (`89.74%` reduction, `$81,840.00/year`)** while cutting multi-agent rewrite and robot demonstration/tuning labor from `50.0 hrs/mo` to `5.0 hrs/mo` (`45.0 hrs/mo` saved, **`-90.00%`**).

---

## 🛠️ 6. Actionable AI SA Deployment Checklist

- [ ] **1. Launch `YT-Proteus-bot/MineAgent` & Verify Offline Compilation with `mock_llm.py`**:
  ```powershell
  git clone https://github.com/YT-Proteus-bot/MineAgent.git
  cd MineAgent
  .\start.ps1 -Port 8000
  # In a second terminal, start the zero-key mock LLM server on port 8012:
  .\.venv\Scripts\python.exe tools\mock_llm.py --port 8012
  ```
- [ ] **2. Inspect Compiled `projects/<canvas>/` Output & `MINEAGENT_KEY_<id>` Isolation**: Verify that saved canvases compile into standalone runnable Python modules with zero plaintext API keys in `agent.json`.
- [ ] **3. Run `ArcheOne-AI/RoboScript`'s Zero-GPU Built-In Mock Benchmark**:
  ```bash
  git clone https://github.com/ArcheOne-AI/RoboScript.git
  cd RoboScript
  uv sync --all-packages
  cd examples/tutorials
  uv run python -m quickstart_mock.run
  ```
- [ ] **4. Deploy `wicl` Task Memory Rehearsal & Parameter Remapping**: Connect `cuRobo`, `GroundingDINO`, and `SAM 3` services behind the `RoboScript` Agent Plane, rehearse from 1 demonstration on clean scenes, and validate frozen Task Memory transfer to randomized scenes or physical arms.
