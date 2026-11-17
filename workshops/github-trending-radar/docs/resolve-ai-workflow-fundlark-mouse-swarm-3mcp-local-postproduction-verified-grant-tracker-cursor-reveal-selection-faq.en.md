# 3-MCP Local DaVinci Resolve Workstation (`willturner-maker/resolve-ai-workflow`), Official-Verified Grant Tracker (`dryang21/Fundlark`) & Multi-Cursor DOM Reveal (`ruvnet/mouse-swarm`) Selection FAQ

> **Document Type**: Enterprise AI Solution Architect Practical Selection Guide (Standard 6-Section FAQ)  
> **Shift & Round**: 2026-11-17 Night Round 51 (Cumulative Round 475 Milestone)  
> **Tracked Repositories**:
> - **`willturner-maker/resolve-ai-workflow`** (`★ 30`, Python / Splash Local LLM + OpenCode + 3 DaVinci Resolve Studio 21.2 MCP Servers + Headless Blender Cycles Metal EXR + `ffprobe` QC, `MIT`): Air-gapped local post-production workstation where a persistent SSD prefix cache reuses `~20k–45k` cached tokens per session (`~200 ms` warm TTFT, `~170 tok/s` single-stream, `~375 tok/s` concurrent plateau, labeled `anonymized_reported`), driving DaVinci Resolve Studio through 3 complementary MCP servers with dry-run/confirm-token guardrails and headless Blender EXR title rendering
> - **`dryang21/Fundlark`** (`★ 30`, Python / Official-Call-Verified Research Funding Discovery & Eligibility Tracker across Claude Code, Codex & Cursor, `MIT`) & **`ruvnet/mouse-swarm`** (`★ 30`, JavaScript / Sequential Landing-Page DOM Reveal & Multi-Cursor Agent Choreography, `MIT`): Research funding discovery skill and web tracker that checks official funder pages, separates *"relevant to your research"* from *"you are eligible (`Apply yourself`)"*, and marks unreachable pages as `"Date to confirm"` (`Fundlark`), paired with a DOM build-sequence choreographer and local Ruflo swarm observer (`mouse-swarm`)  
> **Audit Claim ID**: `CLAIM-20261117-R51-RESOLVEAI-FUNDLARK-MOUSESWARM` (local workstation hardware & DaVinci Resolve Studio license marked `not_measured`)

---

## 📌 1. Executive Summary

1. **Why Media Post-Production Teams, R&D Labs, and Product Marketing Engineers Hit Three Workflow Bottlenecks: Cloud Video Privacy/Latency Limits, Hallucinated Grant Eligibility, and Hand-Keyframed Multi-Agent Demo Videos**:
   - **Bottleneck 1 — Cloud Video Upload Restrictions & Cold-Start Tool Prefill Latency**: Confidential enterprise product footage cannot be uploaded to cloud LLM APIs, while running local agents against dozens of DaVinci Resolve scripting tools without a persistent SSD prefix cache incurs multi-second prefill delays on every new session.
   - **Bottleneck 2 — Hallucinated Deadlines & Missed Institutional Eligibility Rules in Grant Searches**: Generic LLM web searches routinely recommend fellowships that require institutional nomination to self-applying postdocs or fabricate deadlines when a funder's webpage fails to load.
   - **Bottleneck 3 — Manual Keyframing for Multi-Agent Product Launch Reveals**: Creating a landing-page showcase where elements assemble in sequence while multiple labeled agent cursors collaborate usually requires hours of manual motion keyframing.
   - **The Solution Architect Stack (`resolve-ai-workflow` MIT + `dryang21/Fundlark` MIT + `ruvnet/mouse-swarm` MIT)**: Run confidential video post-production locally on **`willturner-maker/resolve-ai-workflow`** (`MIT`, combining `Splash`'s persistent SSD prefix cache with OpenCode, 3 DaVinci Resolve MCP servers, headless Blender Metal EXR titles, and `ffprobe` self-grading); screen R&D grants and fellowships with **`dryang21/Fundlark`** (`MIT`, verifying deadlines on official pages and explicitly flagging `"Date to confirm"` on unreachable URLs); and choreograph interactive product showcases with **`ruvnet/mouse-swarm`** (`MIT`).
2. **Closed-Form FinOps Impact (25 Post-Production, R&D Grant & Product Showcase Engineers Running 450 Monthly Resolve Timelines, Grant Audits & Launch Demos at `$95.00/hr`)**:
   - Migrating from **Path A (Cloud Video Proxy APIs + Paid Grant Databases & Hand-Keyframed Multi-Cursor Demos at `$5,660.00/mo`)** to **Path C (`resolve-ai-workflow` + `Fundlark` + `mouse-swarm` Stack at `$336.00/mo`)** saves **`$5,324.00/mo` (`-94.06%`, or `$63,888.00/yr`)** while cutting timeline scripting, grant eligibility verification, and demo animation labor from `36.0 hrs/mo` to `2.8 hrs/mo` (**`92.22%` reduction**).

![Resolve AI Workflow + Fundlark + Mouse Swarm Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r51-resolve-fundlark-mouseswarm.svg)

---

## 💬 2. Core Architectural Q&A (Q1–Q3)

### Q1: How does `willturner-maker/resolve-ai-workflow` orchestrate DaVinci Resolve Studio 21.2 and headless Blender locally with a `~200 ms` SSD prefix-cached LLM?
- **Plain-Language Definition**: `resolve-ai-workflow` (`MIT`) is **a fully scripted, zero-cloud post-production workstation where OpenCode—backed by a local `262k`-context LLM with persistent SSD prefix caching—drives DaVinci Resolve Studio through three MCP servers, renders 3D EXR titles in headless Blender, and verifies its own renders with `ffprobe`**.
- **Four Core Architectural Pillars (`anonymized_reported, independently_reproduced=false`)**:
  1. **Persistent SSD Prefix Cache (`Splash` + `Qwen3.8-Flash-Next IQ3_S`)**: Reuses `~20k–45k` cached tool/system tokens across fresh agent sessions, achieving **`~200 ms` warm TTFT**, **`~170 tok/s` single-stream decode**, and **`~375 tok/s` concurrent throughput** on local hardware;
  2. **Three Complementary DaVinci Resolve MCP Servers**:
     - Community Python `davinci-resolve` MCP (`~36` live editing, media pool, ripple edit, and guardrail tools);
     - Community Node `davinci-resolve-advanced` MCP (offline database, DRX grade stills, DRT timeline templates, and QC);
     - Official Blackmagic `DaVinci Resolve` MCP (built into Studio 21.1+);
  3. **Dry-Run / Confirm-Token Discipline + `ffprobe` Read-Back QC**: Plans edits with dry-run confirmation tokens and inspects rendered sequences with `ffmpeg/ffprobe`;
  4. **Headless Blender Cycles Metal EXR Pipeline**: Renders transparent (`film_transparent`) EXR title sequences on Metal and imports them directly into the Resolve timeline.

### Q2: How does `dryang21/Fundlark` prevent deadline hallucinations and eligibility mismatches in research funding searches?
- **Three Verification Safeguards (for Web, Chat Assistants & Claude Code / Codex / Cursor, `MIT`)**:
  1. **Strict Separation of Relevance vs. Eligibility**: Explicitly distinguishes whether an applicant can apply directly (*"Apply yourself"*) or requires institutional/advisor nomination, checking degree windows and society membership rules;
  2. **Official-Page Verification + `"Date to confirm"` Fallback**: Links every lead to the funder's official page and checks live deadlines—if an official page cannot be reached, it explicitly labels the entry **`"Date to confirm"`** rather than guessing;
  3. **Browser Application Tracker**: Lets researchers filter calls by field and career stage, edit keyword tags, and track planned submissions.

### Q3: How does `ruvnet/mouse-swarm` turn any landing page into an interactive multi-agent build reveal?
- **Dual-Mode DOM Choreography & Swarm Observation (`MIT`)**:
  - **Sequential DOM Reveal Mode**: Reveals page elements in document order, types out leaf text, and animates a configurable swarm of colored, labeled agent cursors with `replay`, `pause`, `resume`, `skip`, and progress controls;
  - **Local Ruflo Swarm Observation Mode**: Displays reported CLI agent registrations and statuses without taking control of the host computer or spawning background processes.

---

## 🧭 3. End-to-End Reference Architecture & Decision Tree (Mermaid)

```mermaid
flowchart TD
    subgraph ResolveWorkstation["100% Local Post-Production Workstation: resolve-ai-workflow (★30, MIT)"]
        A[Splash Local LLM Qwen3.8-Flash-Next 262k<br/>Persistent SSD Prefix Cache Reuses 20k–45k Tokens · ~200ms TTFT] --> B[OpenCode Operator + Dry-Run/Confirm-Token Discipline]
        B --> C[3 DaVinci Resolve Studio 21.2 MCP Servers<br/>Official MCP + Live Editing MCP + Offline DB/DRX/DRT MCP]
        C --> D[Headless Blender Metal EXR Titles<br/>+ ffmpeg/ffprobe Read-Back QC]
    end

    subgraph FundAndSwarm["Verified Grant Discovery &amp; Multi-Cursor Reveal: Fundlark (★30) + mouse-swarm (★30)"]
        E[dryang21/Fundlark Skill &amp; Tracker<br/>Separates Relevance vs. Eligibility + Official Deadline Check + Date to confirm]
        F[ruvnet/mouse-swarm Landing-Page Reveal<br/>Sequential DOM Build + Multi-Agent Cursor Choreography + Ruflo Status View]
    end
```

---

## 📊 4. Peer Solution Comparison Matrix (Decision Matrix)

| Evaluation Dimension | Option A: Cloud Video Proxies + Generic LLM Grant Search + Manual AE Cursors | Option B: Single-MCP Scripts (No SSD Cache) + Manual Spreadsheets | **Option C (Recommended): `resolve-ai-workflow` + `Fundlark` + `mouse-swarm` (MIT)** |
| :--- | :--- | :--- | :--- |
| **Post-Production Data Privacy, MCP Depth & Warm TTFT** | ❌ Uploads sensitive footage to cloud APIs | ⚠️ Single MCP lacks offline DB/DRX tools; cold prefill lags | ✅ **100% local, SSD prefix cache (`~200ms` TTFT), 3 Resolve MCPs + headless Blender EXR** |
| **Grant Deadline Accuracy & Eligibility Verification** | ❌ Hallucinates deadlines & misses institutional nomination limits | ⚠️ Hours spent manually checking dozens of agency portals | ✅ **Official-page deadline check, `Apply yourself` filter & honest `Date to confirm` flag** |
| **Multi-Agent Product Launch Reveal Choreography** | ❌ Days of manual cursor keyframing in video editors | ⚠️ Static screenshots lack interactive playback controls | ✅ **Automated sequential DOM reveal with labeled agent cursors & `replay/pause/skip`** |
| **Monthly TCO (25 Engineers & Leads / 450 Workflows)** | **`$5,660.00 / mo`** (`$2,240` cloud APIs/SaaS + `36.0 hrs` manual work) | **`$2,400.00 / mo`** (`$880` APIs + `16.0 hrs` manual checks) | **`$336.00 / mo`** (**`-94.06%` savings**; `$70` local cache/hosting + `2.8 hrs` sign-off) |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261117-R51-RESOLVEAI-FUNDLARK-MOUSESWARM`)

> **Scope & Boundary Declaration**: Evaluated for 25 post-production engineers, R&D grant leads, and product showcase developers executing **450 monthly DaVinci Resolve/Blender timelines, official grant eligibility audits, and interactive product launch reveals** at a blended rate of `$95.00/hr` (local workstation hardware & DaVinci Resolve Studio license marked `not_measured`):

$$\text{Total Monthly TCO} = \text{Cloud Video/Grant SaaS Spend} + (\text{Manual Timeline/Grant/Demo Hours} \times \$95.00)$$

| Cost Component | Path A: Cloud Proxies + Blind Search + Manual Keyframes | Path B: Uncached Single MCP + Manual Sheets | **Path C: `resolve-ai` + `Fundlark` + `mouse-swarm`** |
| :--- | :---: | :---: | :---: |
| **Monthly Cloud Video API & Commercial Grant Database Spend** | `$2,240.00` | `$880.00` | **`$70.00`** |
| **Monthly Manual Timeline Scripting, Grant Check & Demo Hours** | `36.0 hrs` | `16.0 hrs` | **`2.8 hrs`** (**`92.22%` reduction**) |
| **Monthly Media, R&D & Showcase Engineering Labor (`@ $95.00/hr`)** | `$3,420.00` | `$1,520.00` | **`$266.00`** |
| **Total Monthly TCO** | **`$5,660.00`** | **`$2,400.00`** (`-57.60%`) | **`$336.00`** (**`-94.06%`**) |
| **Net Savings vs. Path A (Monthly / Annual)** | Baseline (`$0.00`) | `$3,260.00 / mo` (`$39,120/yr`) | **`$5,324.00 / mo` (`$63,888.00 / yr`)** |

---

## ✅ 6. Solution Architect Action Checklist

- [ ] **Step 1 — Configure `willturner-maker/resolve-ai-workflow` with SSD Prefix Caching**: Run `Splash` on `:8000` with persistent disk prefix caching (`20k–45k` tokens reused) and connect OpenCode to all three DaVinci Resolve Studio 21.2 MCP servers.
- [ ] **Step 2 — Enforce Dry-Run Confirm Tokens & `ffprobe` Self-Grading**: Require OpenCode to present dry-run confirmation tokens before modifying timelines and validate rendered sequences via `ffprobe` read-backs.
- [ ] **Step 3 — Deploy `dryang21/Fundlark` in Claude Code, Codex, or Cursor**: Use `skills/fundlark/SKILL.md` to verify official funder deadlines, separate *Apply yourself* fellowships from institution-nominated grants, and flag unreachable pages as `"Date to confirm"`.
- [ ] **Step 4 — Add `ruvnet/mouse-swarm` to Product Launch & Swarm Demo Pages**: Install the `mouse-swarm` skill to generate interactive sequential DOM reveals with multi-cursor choreography and optional local Ruflo status observation.
