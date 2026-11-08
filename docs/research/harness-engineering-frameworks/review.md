# Architecture & Adversarial Critique Review (`review.md`)

## 1. Scope & Verification Summary

- **Study Target**: Mainstream Agent Harness Engineering frameworks (`DeepSeek Harness (DSH)`, `Claude Code & Agent SDK`, and `Microsoft HVE Core`).
- **Determinism Audit**: `simulator/harness_architecture_verifier.py` and `simulator/test_harness_architecture_verifier.py` executed (`4/4` unit tests passing, `0` warnings).
- **7-Card Compliance**: Both `cards.zh.html` and `cards.html` enforce `Content-Security-Policy: default-src 'none'; style-src 'unsafe-inline'` and match every metric in `report.json`.

## 2. Resolved Pre-Publication Critique Items (`PC-001` – `PC-004`)

| ID | Category | Finding | Resolution | Status |
| :--- | :--- | :--- | :--- | :---: |
| **PC-001** | Provenance Precision | Ensure all three frameworks cite exact upstream commit SHAs rather than generic branch names. | Sealed `fcc0ad4621` (DSH), `0ed94698aa` (Claude Code), and `f425e943bf` (HVE Core) in `evidence.json` and `report.json`. | ✅ Resolved |
| **PC-002** | Context Math Grounding | Align the 10K-to-200K attention dilution numbers with HVE Core's `docs/rpi/context-engineering.md`. | Verified `3,000 / 10,000 = 30.0%` vs. `3,000 / 200,000 = 1.5%` (20.0x dilution) in `simulate_context_attention_and_kv_cache()`. | ✅ Resolved |
| **PC-003** | PTC Allowance Formula | Verify DSH `@deepseek-ai/dsh-tool-executor-ptc` subcall cap formula against source README. | Confirmed `floor(resolvedTimeoutMs / 60000 * maxSubCallsPerMinute)` (`120,000 ms => 2,048` calls; call `#2,049` aborts with `CODE_RUN_FAILED`). | ✅ Resolved |
| **PC-004** | Anti-Pattern Coverage | Include at least one explicit architectural anti-pattern rejection (`✕`) in Card 3 and Playground. | Added Scenario `S11` (rejecting distributed Team DAG + external persistence for a 3-turn ephemeral CLI script, recommending `dsh-sdk-minimal`). | ✅ Resolved |
