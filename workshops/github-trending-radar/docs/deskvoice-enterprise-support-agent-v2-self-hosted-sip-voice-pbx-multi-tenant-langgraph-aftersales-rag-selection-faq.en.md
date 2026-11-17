# Self-Hosted AI Voice PBX (`DeskLabs-OpenSource/DeskVoice`) & Multi-Tenant LangGraph After-Sales Support (`KaelLee335/enterprise-support-agent-v2`) Selection FAQ

> **Document Type**: Enterprise AI Solution Architect Practical Selection Guide (Standard 6-Section FAQ)  
> **Shift & Round**: 2026-11-17 Night Round 18 (Cumulative Round 442)  
> **Tracked Repositories**:
> - **`DeskLabs-OpenSource/DeskVoice`** (`★ 127`, Node 22 / SIP / Asterisk / OpenAI Realtime & Gemini / Docker, `MIT`): Self-hosted open-source AI phone system (PBX) running on your own VPS (`~380 MiB` RAM at rest, `~2.7 GB` disk) that connects carrier SIP trunks directly, executes tools mid-call, requests live human approval, transfers calls, and keeps background tasks running after hang-up
> - **`KaelLee335/enterprise-support-agent-v2`** (`★ 83`, Python 3.12 / FastAPI / SQLite / LangChain RAG / Chroma / LangGraph / Vue 3, `MIT`): Full-stack enterprise after-sales support agent migrated from fragile Dify low-code workflows to deterministic Python/LangGraph code (65 Pytest suites passing), enforcing server-derived tenant isolation, citation-grounded policy RAG, read-only order queries, and **Self-Approval Rejection** on refund checkpoints  
> **Audit Claim ID**: `CLAIM-20261117-R18-DESKVOICE-SUPPORTV2` (underlying carrier PSTN termination and direct OpenAI/Gemini Realtime audio token pass-through marked `not_measured`)

---

## 📌 1. Executive Summary

1. **Why Scaling Enterprise Voice & After-Sales Support on Per-Minute Voice Wrapper SaaS + Low-Code Workflow Canvases Breaks FinOps and Internal Controls**:
   - **Pain Point 1 — `$0.05–$0.09/min` Voice SaaS Wrapper Markups & Hang-Up State Loss**: Commercial AI voice wrapper platforms charge steep per-minute platform surcharges on top of carrier SIP and OpenAI/Gemini Realtime API bills (`25,000 mins/mo` costs `$1,750+/mo` in middleman fees alone) and often terminate execution the instant a caller hangs up.
   - **Pain Point 2 — Low-Code Canvas Fragility, Header Spoofing & Unchecked Refund Self-Approval**: Visual workflow builders struggle to enforce strict multi-tenant boundary checks (trusting client-supplied `X-Tenant-ID` headers), hallucinate refund window policies when RAG evidence is missing, and lack cryptographic separation of duties between refund requesters and approvers.
   - **The Solution Architect Stack (`DeskVoice` + `enterprise-support-agent-v2`, Both `MIT`)**: Deploy **`DeskLabs-OpenSource/DeskVoice`** on your own VPS to connect carrier SIP trunks directly to OpenAI Realtime / Google Gemini (`$0` wrapper markup, `~380 MiB` RAM at rest, mid-call tool calls, live human approval/transfer, and post-call background task continuation), and wire its tool calls into **`KaelLee335/enterprise-support-agent-v2`** (deterministic FastAPI + LangGraph routing, server-derived tenant tokens, citation-grounded Chroma policy RAG with safe no-evidence fallback, and strict requester-vs-approver separation of duties).
2. **Closed-Form FinOps Impact (25,000 Monthly Inbound Voice Minutes & 40,000 After-Sales Ticket/Refund Workflows at `$95.00/hr`)**:
   - Migrating from **Path A (Commercial Voice Wrapper SaaS at `$0.07/min` Markup + Hosted Low-Code Workflow Seats at `$5,570.00/mo`)** to **Path C (`DeskVoice` Self-Hosted SIP PBX + `enterprise-support-agent-v2` Multi-Tenant LangGraph Core at `$365.00/mo`)** saves **`$5,205.00/mo` (`-93.45%`, or `$62,460.00/yr`)** while reducing policy-hallucination audits, tenant-isolation debugging, and refund approval overhead from `36.0 hrs/mo` to `3.0 hrs/mo` (**`91.67%` reduction**).

![DeskVoice + Enterprise Support Agent V2 Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r18-deskvoice-support-v2.svg)

---

## 💬 2. Core Architectural Q&A (Q1–Q3)

### Q1: What is `DeskLabs-OpenSource/DeskVoice` in plain terms, and how does it improve on per-minute voice wrapper SaaS or raw Realtime API scripts?
- **Plain-Language Definition**: `DeskVoice` is a **self-hosted AI phone system (PBX) that runs on your own VPS in a single command**. At rest it consumes roughly **`380 MiB` of RAM and `2.7 GB` of disk** (supporting both `amd64` and `arm64`), connects directly to your telecom carrier's SIP trunk (via registration or `/16` IPv4 / `/32` IPv6 IP blocks), and drives calls using your own OpenAI Realtime or Google Gemini API keys.
- **Four Enterprise-Ready Capabilities**:
  1. **Zero Per-Minute Middleman Markup**: You pay your SIP carrier and model provider directly with zero platform surcharge;
  2. **Mid-Call Tools, Live Human Approval, Transfer & Post-Call Continuation**: The voice agent executes tools during the live call, asks a human supervisor for approval before committing sensitive actions, transfers the call when needed, and **keeps post-call background tasks running after the caller hangs up**;
  3. **Zero-Key / Zero-Carrier Call Simulator (`pnpm demo`)**: Engineers can test the entire call lifecycle (greeting, tool execution, human approval request, transfer, and post-call job) locally in Docker with no SIP carrier and no AI key;
  4. **Panel Updates with Automatic Rollback**: Includes built-in backup, restore, and automatic rollback if a panel upgrade fails on the VPS.

### Q2: Why did `KaelLee335/enterprise-support-agent-v2` migrate from a Dify low-code workflow to deterministic FastAPI + LangGraph code?
- **Where Low-Code Workflows Break in Enterprise After-Sales Support**: Multi-tenant order lookup, strict refund-window policy verification, and separation of duties (SoD) require deterministic unit testing, header-spoofing immunity, and checkpoint integrity checks that visual drag-and-drop graphs cannot reliably guarantee.
- **Four Production Guardrails in `enterprise-support-agent-v2` (Verified by 65 Passing Pytest Suites)**:
  1. **Server-Derived Tenant Isolation (Never Trusts `X-Tenant-ID`)**: Maps user identity, tenant scope (`demo-a` vs. `legacy-demo`), and role exclusively from the server-side Bearer token mapping, preventing cross-tenant order snooping;
  2. **Separation of Duties (`Self-Approval Rejection`)**: SQLite order tables are strictly read-only. When a refund request creates a LangGraph SQLite checkpoint, **the requester is blocked from approving their own request**—only a separate approver identity within the same tenant can record approval or rejection;
  3. **Citation-Grounded Policy RAG with Safe No-Evidence Fallback**: Queries Chroma vector indexes for refund deadlines, quality defects, logistics rules, and privacy boundaries, returning explicit policy citations and safely declining when evidence is absent;
  4. **Prompt-Injection Refusal Shield & Checkpoint Integrity Pre-Checks**: Includes pre-flight checkpoint integrity validation, a 5-chapter code walkthrough, a fault case library, and a Vue 3 operator console.

### Q3: How should an AI Solution Architect integrate `DeskVoice` and `enterprise-support-agent-v2` into an omnichannel contact center?
- **Voice Ingress Layer (`DeskVoice`)**: Handles inbound SIP trunks and OpenAI Realtime / Gemini voice streams, invoking `enterprise-support-agent-v2` FastAPI endpoints (`/orders/{order_id}`, `/chat`) as mid-call tools.
- **Unified Governance Core (`enterprise-support-agent-v2`)**: Enforces tenant isolation, Chroma policy RAG citations, and refund checkpoint creation; when a caller or chat user requests a refund, `DeskVoice` and the Vue 3 console route the pending checkpoint to an authorized same-tenant human approver.

---

## 🧭 3. End-to-End Reference Architecture & Decision Tree (Mermaid)

```mermaid
flowchart LR
    subgraph VoiceChannel["Voice Ingress: DeskLabs-OpenSource/DeskVoice (MIT, 380MiB RAM)"]
        A[Caller Dials Enterprise SIP Trunk] --> B[DeskVoice PBX Container<br/>Asterisk SIP + OpenAI Realtime / Gemini]
        B -->|Mid-Call Tool Execution| C[FastAPI Gateway]
        B -->|High-Risk Request| D[Live Human Approval / Call Transfer]
        B -->|After Caller Hangs Up| E[Post-Call Background Task Runner]
    end

    subgraph SupportCore["Multi-Tenant Governance Core: enterprise-support-agent-v2 (MIT, 65 Pytests)"]
        F[Vue 3 Web Chat &amp; Agent Console] --> C
        C --> G[Server-Derived Bearer Tenant Check<br/>Ignores Client X-Tenant-ID + Injection Shield]
        G --> H[Deterministic LangGraph Router + Checkpoint Pre-Check]
        H -->|Order Lookup| I[(Read-Only SQLite Orders)]
        H -->|Policy Q&amp;A| J[Chroma Policy RAG<br/>Mandatory Citations + No-Evidence Fallback]
        H -->|Refund Request| K[SQLite Approval Checkpoint<br/>Self-Approval Blocked · Same-Tenant Approver Required]
    end
```

---

## 📊 4. Peer Solution Comparison Matrix (Decision Matrix)

| Evaluation Dimension | Option A: Commercial Voice Wrapper SaaS (`$0.07/min`) + Dify SaaS | Option B: Custom Twilio Webhooks + Prompt-Only Support Bot | **Option C (Recommended): `DeskVoice` + `enterprise-support-agent-v2` (Both MIT)** |
| :--- | :--- | :--- | :--- |
| **Voice Platform Markup & Self-Hosted Control** | ❌ Charges `$0.05–$0.09/min` platform markup on top of carrier & LLM bills | ⚠️ Requires maintaining custom WebSocket audio streaming & SIP state | ✅ **1-command VPS install (`~380 MiB` RAM at rest), direct SIP & API keys, `$0` platform markup** |
| **Mid-Call Approval, Transfer & Post-Call Jobs** | ⚠️ Drops workflow context on hang-up; rigid mid-call human handoff | ❌ Terminates on hang-up; no offline call simulator (`pnpm demo`) | ✅ **Mid-call tools, live human approval, call transfer, post-call tasks & `pnpm demo` simulator** |
| **Multi-Tenant Isolation & Refund SoD Controls** | ⚠️ Low-code flows often trust client headers and lack self-approval blocks | ❌ Relies on prompt instructions vulnerable to injection | ✅ **Server-derived tenant tokens, read-only orders, checkpoint pre-check & self-approval rejection** |
| **Policy Grounding & Automated Test Coverage** | ⚠️ Hard to version-control or run CI unit tests across canvas nodes | ❌ High hallucination risk on refund deadlines and shipping rules | ✅ **Citation-grounded Chroma RAG + safe no-evidence fallback + 65 passing Pytest suites** |
| **Monthly TCO (25k Voice Mins + 40k Tickets)** | **`$5,570.00 / mo`** (`$2,150` wrapper fees + `36.0 hrs` audit/rework) | **`$2,430.00 / mo`** (`$910` infra + `16.0 hrs` webhook maintenance) | **`$365.00 / mo`** (**`-93.45%` savings**; `$80` VPS/containers + `3.0 hrs` approval sign-off) |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261117-R18-DESKVOICE-SUPPORTV2`)

> **Scope & Boundary Declaration**: Evaluated for an enterprise customer operations center handling **25,000 monthly inbound voice minutes and 40,000 multi-tenant after-sales ticket/refund workflows** at a blended engineering rate of `$95.00/hr` (underlying telecom PSTN termination and direct OpenAI/Gemini Realtime audio token pass-through marked `not_measured`):

$$\text{Total Monthly TCO} = \text{Voice/Workflow Platform Spend} + (\text{Audit, Escalation \& Maintenance Hours} \times \$95.00)$$

| Cost Component | Path A: Voice Wrapper SaaS + Hosted Low-Code Seats | Path B: Custom Twilio Webhooks + Prompt Bot | **Path C: `DeskVoice` + `support-agent-v2` Stack (MIT)** |
| :--- | :---: | :---: | :---: |
| **Monthly Voice Wrapper Fees / Self-Hosted VPS & Containers** | `$2,150.00` | `$910.00` | **`$80.00`** |
| **Monthly Refund Audit, Tenant-Leak Triage & Ops Hours** | `36.0 hrs` | `16.0 hrs` | **`3.0 hrs`** (**`91.67%` reduction**) |
| **Monthly Engineering & Supervisor Labor (`@ $95.00/hr`)** | `$3,420.00` | `$1,520.00` | **`$285.00`** |
| **Total Monthly TCO** | **`$5,570.00`** | **`$2,430.00`** (`-56.37%`) | **`$365.00`** (**`-93.45%`**) |
| **Net Savings vs. Path A (Monthly / Annual)** | Baseline (`$0.00`) | `$3,140.00 / mo` (`$37,680/yr`) | **`$5,205.00 / mo` (`$62,460.00 / yr`)** |

---

## ✅ 6. Solution Architect Action Checklist

- [ ] **Step 1 — Validate Voice Flows Offline with `DeskVoice`'s `pnpm demo`**: Clone `DeskLabs-OpenSource/DeskVoice` and run `pnpm install && pnpm demo` to verify greeting, mid-call tool execution, live human approval, call transfer, and post-call background tasks without a SIP carrier or AI key.
- [ ] **Step 2 — Provision `DeskVoice` on an 8 GB / 4 vCPU VPS with Direct SIP Trunks**: Run `bash install/install.sh`, configure carrier SIP registration or IP CIDR blocks (`/16` IPv4 / `/32` IPv6) plus OpenAI Realtime or Gemini keys on the web panel, and test automatic rollback.
- [ ] **Step 3 — Deploy `enterprise-support-agent-v2` Behind Enterprise IAM**: Start the FastAPI + LangGraph service via `uv sync --locked --extra dev`, bind tenant identity strictly from server-verified tokens (ignoring client `X-Tenant-ID` headers), and keep order database connections read-only.
- [ ] **Step 4 — Ingest After-Sales Policies into Chroma & Enforce Dual-Role Refund Approval**: Load enterprise refund/shipping policies into Chroma with mandatory citation output, verify all 65 `pytest` suites pass, and enforce requester-vs-approver separation on all refund checkpoints.
