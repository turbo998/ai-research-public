# Omarchy Agent Architecture Audit: OS-Level Harness Integration, Event-Driven Diagnostics & Skill Contracts

> 🌐 **Language / 语言切换**: **[🇬🇧 English (README.en.md)](./README.en.md)** | **[🇨🇳 中文完整版 (README.md)](./README.md)** · **[📊 7-Card Report (ZH)](test-report.md)** | **[🃏 7-Card Visual HTML](test-report-cards.html)**  
> **Audit Date**: `2026-10-12` · **Pinned Upstream**: [`omacom/omarchy@9480d1b6a98156314dbabe6bfef08f39f8b9cd07`](https://github.com/omacom/omarchy/commit/9480d1b6a98156314dbabe6bfef08f39f8b9cd07) (MIT License)

---

## 1. Solution Architect Executive Summary

**Omarchy demonstrates an "Agentic OS Shell" integration pattern: instead of building another proprietary agent loop, it wires 14 third-party CLI coding harnesses into OS-level launchers, progressive skill directories, `systemd` crash telemetry, and multi-account quota panels.**

For Enterprise Developer Platform & AI Solution Architects designing internal AI engineering workstations or Cloud Dev Boxes, Omarchy provides **6 reusable architectural patterns** verified across **174 pinned source assertions**:

| Module | Verified Mechanism | Enterprise DevEx / SA Takeaway |
|---|---|---|
| **[00 · Architecture Overview](findings/00-summary.md)** | 8 OS-level integration patterns & 6-dimension platform matrix vs. Claude Code / Copilot | Decouple workstation UX, telemetry triggers, and credential switching from rapidly changing CLI agent binaries |
| **[01 · Multi-Harness Launcher](findings/01-launcher.md)** | Unified 14-branch launcher (`claude`, `codex`, `copilot`, `gemini`, `opencode`, `openclaw`, etc.) with lazy installation and prompt/cwd injection | Standardize invocation contracts (`argv`, working directory, initial prompt) across heterogeneous coding agents |
| **[02 · Progressive Skills](findings/02-skills.md)** | Separation of runtime deployment skills vs. contributor guides across 6 profile roots | Keep operational `SKILL.md` bundles lean and profile-scoped rather than polluting global system prompts |
| **[03 · Event-Driven Crash Pipeline](findings/03-crash-pipeline.md)** | `journalctl` crash filter → deduplicated desktop notification → user click → pre-populated diagnostic agent session | **Human-gated event-to-agent loop**: surface crashes automatically, but require explicit human click before spawning an agent with logs |
| **[04 · Multi-Account & Quota Panel](findings/04-accounts-usage.md)** | Provider account pinning, usage collectors, freshness caching, and status-bar telemetry | Prevent developer lockouts during high-burn agent runs via transparent quota observability and profile switching |
| **[05 · Agent-Native Repo](findings/05-agent-native-repo.md)** & **[06 · Safety Boundaries](findings/06-safety-model.md)** | Layered `AGENTS.md` instructions, headless acceptance contracts, and explicit OS trust boundaries | Note that desktop convenience shells are **not** hard security sandboxes — pair untrusted repo execution with MicroVM / container isolation (see [`azure-agent-infra`](../azure-agent-infra/README.en.md)) |

---

## 2. 7-Card 4:5 Contract Benchmark & Verifiable Evidence

- **7-Card Visual Report**: [`test-report-cards.html`](test-report-cards.html) · [`test-report.md`](test-report.md) · [`evidence/test-report.json`](evidence/test-report.json)
- **Contract Matrices**: [`evidence/test-scenarios.csv`](evidence/test-scenarios.csv) (12 scenarios) · [`evidence/test-robustness.csv`](evidence/test-robustness.csv) · [`evidence/test-batch-latency.csv`](evidence/test-batch-latency.csv)
- **Source Provenance**: [`evidence/source-index.md`](evidence/source-index.md) · [`evidence/assertion-index.csv`](evidence/assertion-index.csv) (174 SHA-verified assertions) · [`evidence.json`](evidence.json) · [`review.md`](review.md)

[Back to Research Index (EN)](../index.en.md) · [中文索引](../index.md) · [Repository Home](../../../README.en.md)
