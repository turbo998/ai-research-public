# Provenance & Methodology Audit — `docs/research/terminal-bench-4-1/`

## 1. Data Provenance & Attribution
- **Benchmark**: `terminal-bench@4.1.0` (`tbench.ai` / `harbor-framework/terminal-bench`, `Apache-2.0`)
- **Snapshot Frozen**: `2026-11-19T03:41:57Z` (`SHA-256: 2f612504302183339b0b6e37938aa7adcb2728279ac839a8d548f052a47959cc`)
- **Provenance Classification**: `anonymized_reported` / `public_leaderboard_snapshot` (`independently_reproduced = false`). All 65 leaderboard entries, 66 task records, token counters, dollar totals, and domain percentages are reported directly from the public `tbench.ai` / Harbor Hub v4.1.0 snapshot without synthetic interpolation.
- **Anti-Contamination Canary Check**: Audited every artifact (`data/tbench_4_1_summary.json`, `README.md`, `README.en.md`, `test-report-cards.*.html`, `assets/overview.svg`) to verify **zero** task prompt bodies, **zero** verifier source files, and **zero** benchmark canary GUIDs are stored in this repository.

## 2. Methodological Guardrails Verified
1. **Unique `Model × Agent` Pareto Deduplication (`52` Pairs)**:
   - The 65 leaderboard rows include multi-effort submissions for identical `(model, agent)` pairs (e.g., `GPT-6 Astra + Codex` at `max`, `high`, `xhigh`; `Fable 5.1 + Claude Code` at `xhigh`, `max`). Deduplicating to the highest-accuracy configuration per unique `(model, agent)` yields `52` pairs (`51` commercially priced + `1` unpriced `$0.00` preview `Muse Spark 1.3 + Muse Code` at `14.85%`).
   - Excluding the `$0.00` unpriced preview so it does not artificially collapse the low-cost anchor yields **exact `7 / 52` (`13.46% ≈ 13.5%`) Pareto-optimal configurations** and `45 / 52` (`86.54% ≈ 86.5%`) dominated configurations.
2. **Per-Trial vs Per-Task Denominator Clarity**:
   - Each leaderboard submission runs `66 tasks × 5 repeats = 330 trials` (`65 × 330 = 21,450` row-level trial slots; upstream task breakdown aggregates `325` trials per task × `66` tasks = `21,450` total trials across `7,867` passes, `12,852` failures, `147` timeouts, and `584` errors). Both figures are preserved verbatim from upstream metadata.
3. **7-Card HTML Self-Containment & CSP**:
   - Both `test-report-cards.en.html` and `test-report-cards.zh-CN.html` enforce `<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'">`, contain zero `<script>` elements and zero external font/image/stylesheet URLs, and compute every bar width proportionally from `data/tbench_4_1_summary.json`.
