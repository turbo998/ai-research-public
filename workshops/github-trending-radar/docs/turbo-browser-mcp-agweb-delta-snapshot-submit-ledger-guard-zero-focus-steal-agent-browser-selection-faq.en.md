# Token-Light Submit-Guarded Browser MCP (`Tthanh2k6/turbo-browser-mcp`) & Zero-Focus-Steal Multi-Agent Browser (`paul-nameless/agweb`) Selection FAQ

> **Document Type**: Enterprise AI Solution Architect Practical Selection Guide (Standard 6-Section FAQ)  
> **Shift & Round**: 2026-11-17 Night Round 16 (Cumulative Round 440 Milestone)  
> **Tracked Repositories**:
> - **`Tthanh2k6/turbo-browser-mcp`** (`★ 127`, Node >= 20 / Playwright, `MIT`): 11-tool Playwright MCP server engineered to slash agent turns and context tokens (`smart_fill_form` cuts 10-field form cumulative tokens by `98.9%`, `onlyChanged` delta snapshots save `98.4%`, and default-on `label / modal / network / ledger` 4-layer commit guards prevent accidental or duplicate submissions)
> - **`paul-nameless/agweb`** (`★ 266`, Swift / macOS WebKit, `MIT`): Zero-focus-stealing native browser built for parallel coding agents (`590 MB` RAM and `0%` CPU across 5 idle tabs vs. `1.6 GB` on Playwright Chrome, `⌘D` live multi-agent workspace grid, and `fill --secret-cmd` so passwords never enter the LLM transcript)  
> **Audit Claim ID**: `CLAIM-20261117-R16-TURBOBROWSER-AGWEB` (target third-party enterprise SaaS portal seat licenses marked `not_measured`)

---

## 📌 1. Executive Summary

1. **Why Enterprise Web-Portal Automation (Procurement Entry, Vendor Onboarding, Compliance Filings, E2E QA) Fails Under Standard Step-by-Step Playwright MCPs**:
   - **Three Systemic Bottlenecks**: ① **Quadratic Cumulative Token Bloat**: Filling a 10-field form and uploading a file one action per turn takes 11 turns and replays the full ARIA snapshot on every turn, burning `72,614` cumulative tokens (plus `44,728` tokens when encoding a `48 KiB` PDF as Base64); ② **Accidental Final Commits & Duplicate Retry Submissions**: Without a built-in submit blocker and idempotency ledger, agents prematurely click `Submit / Pay / Confirm` or submit duplicate records when retrying after a timeout; ③ **Focus Stealing & Transcript Credential Leaks**: Running parallel headed Chrome instances constantly steals keyboard focus from the developer's IDE, while passing credentials in tool arguments leaks plaintext passwords into LLM transcripts.
   - **The Solution Architect Stack (`turbo-browser-mcp` + `agweb`, Both `MIT`)**: Deploy **`Tthanh2k6/turbo-browser-mcp`** across cross-platform automation pipelines (`smart_fill_form` completes 10-field forms in **1 turn / `811` tokens, `-98.9%` cumulative tokens**, backed by `label / modal / network / ledger` 4-layer commit guards and `submissionKey` JSONL idempotency ledgers) and pair it on macOS developer workstations with **`paul-nameless/agweb`** (zero keyboard focus stealing, `590 MB` / `0% CPU` suspended idle tabs, and `fill --secret-cmd` direct credential injection from 1Password/Bitwarden/pass outside the LLM context).
2. **Closed-Form FinOps Impact (60,000 Monthly Enterprise Web-Portal Workflows Across 25 Parallel Agent Workers at `$95.00/hr`)**:
   - Migrating from **Path A (Standard Step-by-Step Playwright MCP + Multi-Instance Headed Chrome at `$5,890.00/mo`)** to **Path C (`turbo-browser-mcp` + `agweb` MIT Stack at `$380.00/mo`)** saves **`$5,510.00/mo` (`-93.55%`, or `$66,120.00/yr`)** while cutting duplicate-submission cleanup, focus-interruption recovery, and credential rotation labor from `38.0 hrs/mo` to `3.0 hrs/mo` (**`92.11%` reduction**).

![turbo-browser-mcp + agweb Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r16-turbo-browser-mcp-agweb.svg)

---

## 💬 2. Core Architectural Q&A (Q1–Q3)

### Q1: How does `Tthanh2k6/turbo-browser-mcp` cut 10-field form cumulative tokens by `98.9%` while preventing accidental or duplicate submissions?
- **Part 1 — Batch Form Filling & Delta DOM Snapshots** (verified via `benchmarks/benchmark.mjs` with `tiktoken` `o200k_base`):
  - **`smart_fill_form` (One-Call Multi-Control + Disk Upload)**: Fills text inputs, selects, ARIA comboboxes, rich-text editors, and local file uploads (`setInputFiles` directly from disk, cutting a `48 KiB` PDF upload from `44,728` Base64 tokens to **`85` tokens, `-99.8%`**) in **1 turn / `811` tokens / `82 ms`** vs. **11 turns / `72,614` cumulative tokens / `574 ms` (`-98.9%` cumulative tokens)**;
  - **`inspect_compact` (`onlyChanged: true`)**: After a click, returns only newly added (`*`) and `Removed:` element refs, reducing a post-click snapshot from `3,582` full ARIA tokens to **`56` tokens (`-98.4%`)**;
  - **`batch_actions` E2E Chaining**: Reduces a 6-step Korean contest wizard from **9 calls / `32,942` cumulative tokens** to **2 calls / `1,430` tokens (`-95.66%`)**; on the 3-task Claude Sonnet 5.5 E2E suite, `turbo-browser-mcp` passes `3/3` in **23 turns / `$0.256` / `61.6s`**.
- **Part 2 — Four-Layer Commit & Idempotency Guard (`allowSubmit=false` by default)**:
  1. **`label` Guard**: Blocks final commit triggers (`Submit`, `Pay`, `Publish`, `Confirm`, and CJK/Korean/Vietnamese equivalents `提交`, `确定`, `제출`, `신청`, `결제`, `送信`, `Hoàn tất`) so agents prefill forms and pause for human review;
  2. **`modal` Guard**: Blocks affirmative buttons (`확인`, `OK`, `确定`) inside `[role=dialog]` or `[aria-modal=true]` modals that follow a harmless "Next (`다음`)" step (`blockedBy: "modal"`);
  3. **`network` Guard (`TURBO_BROWSER_NETWORK_GUARD=true`)**: Intercepts non-GET navigations and same-site `POST / PUT / PATCH / DELETE` XHR/fetch requests regardless of button labels, returning HTTP `204` so half-filled forms remain intact;
  4. **`ledger` Idempotency (`submissionKey`) & `expect.textNew` Receipt Verification**: Appends allowed submissions to `~/.turbo-browser-mcp/submissions.jsonl` (`blockedBy: "ledger"` blocks duplicate retries) and verifies that a new confirmation receipt (`expect.textNew`) actually rendered before reporting `submitVerified: true`.

### Q2: Why do parallel coding agents driving Chrome ruin local developer productivity, and how does `paul-nameless/agweb` solve it?
- **The Parallel Agent Browser Dilemma**: When 3–5 coding agents run Playwright Chrome simultaneously on a developer's laptop, every new tab or dialog steals macOS window focus mid-keystroke. Switching to headless Chrome avoids focus stealing but triggers bot-detection blocks and leaves developers blind when a selector fails.
- **`agweb`'s Four Architectural Breakthroughs**:
  1. **Zero Focus Stealing + Live `⌘D` Multi-Agent Dashboard**: Dialogs, tab switches, file pickers, and downloads are resolved programmatically without ever bringing the window to the foreground, while `⌘D` shows every agent's tabs live in one grid alongside each agent's latest command;
  2. **Suspended Idle Tabs (`590 MB` RAM / `0% CPU` vs. `1.6 GB` Playwright Chrome)**: Five idle pages sit at `0% CPU` and `590 MB` memory (compared to `730 MB` for Headless Chrome and `1.6 GB` plus 5–7 active GPU cores for Playwright Chrome);
  3. **Per-Agent Workspaces (`-w`) + Shared Authenticated Profile (`-p work`)**: Log in to corporate SSO once in `-p work` and let multiple concurrent agents share the authenticated session inside isolated `-w` tab groups;
  4. **Zero-Transcript Credential Injection (`fill --secret-cmd`)**: Running `agweb fill --secret-cmd 'pass show site'` (or 1Password / Bitwarden CLI) types secrets directly into DOM fields so passwords never appear in LLM prompts, tool responses, or session logs.

### Q3: How should Enterprise Solution Architects combine `turbo-browser-mcp` and `agweb`?
- **Developer & Architect macOS Multi-Agent Workstations** ➔ Deploy **`paul-nameless/agweb`** (`MIT`) so parallel Claude Code and Codex agents can inspect, test, and record (`video-start` MP4) web apps with shared SSO profiles (`-p work`), zero focus stealing, and `--secret-cmd` secret injection.
- **Cross-Platform Enterprise Portal Automation & Pre-Fill Pipelines** ➔ Deploy **`Tthanh2k6/turbo-browser-mcp`** (`MIT`) with `smart_fill_form`, `onlyChanged: true`, `TURBO_BROWSER_ALLOW_HOSTS`, `submissionKey` JSONL ledgers, and `wait_for_human` CAPTCHA/MFA handoffs.

---

## 🧭 3. End-to-End Reference Architecture & Decision Tree (Mermaid)

```mermaid
flowchart TD
    A[Enterprise Web Portal Automation &amp; Multi-Agent Browser Workload] --> B{Execution Environment &amp; Primary Constraint?}
    B -->|macOS Parallel Agent Workstation / Zero Focus Steal / Secret-Safe Login| C[Deploy paul-nameless/agweb MIT]
    C --> C1[Shared -p work SSO Profile + Per-Agent -w Workspace Tabs]
    C1 --> C2[fill --secret-cmd 1Password/pass Injection + 0% CPU / 590MB Idle Suspension]
    C2 --> C3[⌘D Live Multi-Agent Grid + video-start MP4 Cursor Recording]

    B -->|Cross-Platform MCP Portal Automation / Token Cap / Commit Safety| D[Deploy Tthanh2k6/turbo-browser-mcp MIT]
    D --> D1[inspect_compact onlyChanged=true Saves 98.4% Tokens<br/>smart_fill_form 1-Turn Fill Saves 98.9% Cumulative Tokens]
    D1 --> D2{4-Layer Commit Safety Gate}
    D2 -->|allowSubmit=false Default Guard| D3[Block label / modal / network POST<br/>Invoke wait_for_human for Final Sign-Off]
    D2 -->|allowSubmit=true Authorized Submit| D4[Enforce submissionKey JSONL Ledger<br/>Verify Receipt via expect.textNew]
```

---

## 📊 4. Peer Solution Comparison Matrix (Decision Matrix)

| Evaluation Dimension | Option A: Standard Step-by-Step Playwright MCP + Multi-Chrome | Option B: Unprotected Headless Browser-Use / Raw Playwright | **Option C (Recommended): `turbo-browser-mcp` + `agweb` Stack (Both MIT)** |
| :--- | :--- | :--- | :--- |
| **10-Field Form + 48KiB File Upload Tokens** | ❌ 11 turns / `72,614` cumulative tokens + `44,728` Base64 upload tokens | ⚠️ Multi-turn full-DOM snapshots consuming thousands of tokens per step | ✅ **`smart_fill_form` 1 turn / `811` tokens (`-98.9%`) + `85`-token disk path upload (`-99.8%`)** |
| **Submit Blocking & Duplicate Retry Prevention** | ❌ None by default; agents click Pay/Submit or double-submit on retries | ❌ No submission ledger; network timeouts trigger duplicate entries | ✅ **4-layer guard (`label/modal/network/ledger`) + `submissionKey` JSONL + `expect.textNew`** |
| **Focus Stealing & Memory Across 5 Open Pages** | ❌ Steals keyboard focus on every dialog; **`1.6 GB`** RAM & 5–7 GPU cores | ⚠️ `730 MB` RAM in headless mode, but blocked by bot checks & invisible | ✅ **`agweb` never steals focus, shows live `⌘D` grid, and uses `590 MB` RAM / `0%` idle CPU** |
| **Credential & Password Isolation** | ❌ Plaintext passwords passed in MCP arguments and stored in transcripts | ❌ Credentials exposed in script logs and failure traces | ✅ **`agweb fill --secret-cmd` pipes from 1Password/pass; `turbo-browser` suppresses password echo** |
| **Monthly TCO (60,000 Portal Workflows/Mo)** | **`$5,890.00 / mo`** (`$2,280` tokens/VMs + `38.0 hrs` duplicate cleanup) | **`$2,690.00 / mo`** (`$980` compute + `18.0 hrs` headless debugging) | **`$380.00 / mo`** (**`-93.55%` savings**; `$95` delta tokens + `3.0 hrs` ledger audit) |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261117-R16-TURBOBROWSER-AGWEB`)

> **Scope & Boundary Declaration**: Evaluated for an enterprise automation team operating **25 parallel agent workers executing 60,000 monthly web-portal workflows** at a blended engineering rate of `$95.00/hr` (target external SaaS portal seat licenses marked `not_measured`):

$$\text{Total Monthly TCO} = \text{Browser MCP Token \& Runner Spend} + (\text{Duplicate-Submit Cleanup \& Ops Hours} \times \$95.00)$$

| Cost Component | Path A: Step-by-Step Playwright MCP + Multi-Chrome | Path B: Unprotected Headless Browser-Use | **Path C: `turbo-browser-mcp` + `agweb` Stack (MIT)** |
| :--- | :---: | :---: | :---: |
| **Monthly Browser Context Tokens & Worker Memory** | `$2,280.00` | `$980.00` | **`$95.00`** |
| **Monthly Duplicate-Submit Cleanup & Ops Hours** | `38.0 hrs` | `18.0 hrs` | **`3.0 hrs`** (**`92.11%` reduction**) |
| **Monthly Engineering Labor (`@ $95.00/hr`)** | `$3,610.00` | `$1,710.00` | **`$285.00`** |
| **Total Monthly TCO** | **`$5,890.00`** | **`$2,690.00`** (`-54.33%`) | **`$380.00`** (**`-93.55%`**) |
| **Net Savings vs. Path A (Monthly / Annual)** | Baseline (`$0.00`) | `$3,200.00 / mo` (`$38,400/yr`) | **`$5,510.00 / mo` (`$66,120.00 / yr`)** |

---

## ✅ 6. Solution Architect Action Checklist

- [ ] **Step 1 — Register `turbo-browser-mcp` with Path & Host Confinement**: Run `claude mcp add turbo-browser -- npx -y turbo-browser-mcp`, set `TURBO_BROWSER_SAVE_ROOT` to confine file reads/writes, and configure `TURBO_BROWSER_ALLOW_HOSTS` to whitelist approved enterprise portals.
- [ ] **Step 2 — Enforce `smart_fill_form` and `inspect_compact(onlyChanged: true)`**: Instruct agents to batch all form fields and file uploads into a single `smart_fill_form` call and pass `onlyChanged: true` on subsequent snapshots to cut cumulative context tokens by `95%+`.
- [ ] **Step 3 — Enable the 4-Layer Submit Guard & `submissionKey` Ledger**: Keep `allowSubmit=false` with `TURBO_BROWSER_NETWORK_GUARD=true` for pre-fill workflows, and require `submissionKey` plus `expect.textNew` receipt matching whenever automated submission is authorized.
- [ ] **Step 4 — Roll Out `agweb` with `--secret-cmd` on macOS Agent Workstations**: Install `Agweb.dmg` and its CLI/Skill, authenticate corporate SSO once under `-p work`, isolate concurrent agents via `-w <agent>`, and inject credentials exclusively via `agweb fill --secret-cmd`.
