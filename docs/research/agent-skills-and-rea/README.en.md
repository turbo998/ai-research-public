# Agent Skills Engineering Spectrum (L1–L4), Critic Gatekeepers & AST Reverse-Engineering (`morluto/rea`)

> 🌐 **Language / 语言切换**: **[🇨🇳 中文版 (README.zh-CN.md)](./README.zh-CN.md)** | **[🇬🇧 English (README.en.md)](./README.en.md)**

## Solution Architect Executive Summary

When enterprise teams scale custom `SKILL.md` libraries across Claude Code or GitHub Copilot, stuffing hundreds of rules into monolithic prompts causes severe context dilution and inconsistent outputs. Written from an **Enterprise Cloud & AI Solution Architect** perspective, this module defines and validates a **4-Level Agent Skill Engineering Maturity Spectrum (`L1 → L4`)**:

1. **L2 · Declarative SOPs + Critic Subagent Gatekeepers (`Ryan Doser Skills`)**: Dissects 60+ production skills across 8 verticals, progressive context disclosure, deterministic `anti-slop.md` filters, and the **4-Agent Critic Gatekeeper** pipeline — directly transferable to enterprise Solution Architecture Document (SAD/ADR) and RFP review automation.
2. **L3 · Declarative Spec + Zero-Dependency Deterministic Verifier (`wheresryan22/anatomy` Pattern)**: Examines how pairing `SKILL.md` with a deterministic code verifier (`15.9K LOC` ES Modules + `audit.mjs` 3D ray-cast invariant checker) offloads exact topological/spatial constraints that LLMs fail to hand-calculate.
3. **L4 · AST Semantic Analysis & Cryptographic Evidence MCP Engine (`morluto/rea` v6.4.0)**: Evaluates REA's 4-layer DDD architecture and 64 CLI/MCP tools by reconstructing a minified `1.28 MB` production bundle into 17 typed TypeScript modules backed by SHA-256 cryptographic evidence (`ev_<sha256>`), demonstrating a clean-room pattern for **enterprise legacy application modernization**.

---

## 1. Live Interactive H5 Workbenches (GitHub Pages)

| Interactive Deliverable | Engineering Tier | Live Public URL (GitHub Pages) | Source Path |
|---|---|---|---|
| **🏠 Unified Showcase Portal** | L1–L4 Skill Spectrum Hub | **[👉 Open Showcase Portal](https://turbo998.github.io/ai-research-public/docs/research/agent-skills-and-rea/)** | [`index.html`](index.html) |
| **📊 Ryan Doser Skill Stack & Critic Gatekeeper Report** | L2 Declarative SOP + 4-Agent Critic | **[👉 Open Visual Interactive Report](https://turbo998.github.io/ai-research-public/docs/research/agent-skills-and-rea/h5/ryan-doser-skills-report/)** | [`h5/ryan-doser-skills-report/index.html`](h5/ryan-doser-skills-report/index.html) |
| **🔍 REA AST Reconstruction & Live Hot-Patch Workbench** | L4 AST MCP Engine + `ev_<sha256>` Ledger | **[👉 Open Interactive AST Workbench](https://turbo998.github.io/ai-research-public/docs/research/agent-skills-and-rea/h5/rea-scrap-swarm-clone/)** | [`h5/rea-scrap-swarm-clone/index.html`](h5/rea-scrap-swarm-clone/index.html) |

---

## 2. SVG Architecture Atlas

- [Figure 1: 8-Vertical Skill Matrix & 4-Agent Critic Gatekeeper Architecture](assets/01-ryan-doser-8category-skill-architecture.svg)
- [Figure 2: 6-Tier Skill Productization & Consulting Flywheel](assets/02-ryan-doser-6tier-monetization-funnel.svg)
- [Figure 3: L1–L4 Agent Skill Engineering Maturity Spectrum](assets/03-agent-skill-l1-to-l4-depth-spectrum.svg)

---

## 3. Deep-Dive Findings & Cryptographic Evidence Ledger

| Artifact | Focus | SA Key Takeaway |
|---|---|---|
| [`findings/01-morluto-rea-architecture.md`](findings/01-morluto-rea-architecture.md) | **L4 · AST & MCP Reverse Engine** | `morluto/rea` v6.4.0 4-layer DDD architecture, 64 CLI/MCP capabilities, lazy AST semantic analyzer, and 17-module bundle reconstruction |
| [`findings/02-ryan-doser-skill-business.md`](findings/02-ryan-doser-skill-business.md) | **L2 · Critic Gatekeeper Architecture** | Input/output skill contracts, `anti-slop.md` enforcement rules, 4-Agent Critic pipeline, and enterprise documentation governance patterns |
| [`findings/03-anatomy-mechanical-skill.md`](findings/03-anatomy-mechanical-skill.md) | **L3 · Deterministic Verifier Harness** | Architectural split between declarative `SKILL.md` intent and deterministic `audit.mjs` ray-cast verification (`0` invariant violations) |
| [`evidence/rea-evidence-ledger.json`](evidence/rea-evidence-ledger.json) | **Cryptographic Provenance** | SHA-256 evidence ledger (`ev_<sha256>`) generated and verified via REA v6.4.0 (`createEvidence` / `parseEvidence`) |

[Back to Research Index (EN)](../index.en.md) · [中文索引](../index.md) · [Repository Home](../../../README.en.md)
