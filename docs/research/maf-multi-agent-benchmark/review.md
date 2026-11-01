# Archive & Privacy Review (`maf-multi-agent-benchmark`)

- **Review Date**: 2026-11-01
- **Provenance**: `measured` (`independently_reproduced=true` via deterministic local Python 3.12 harness `benchmark/run_benchmark.py` and `benchmark/test_maf_benchmark.py`, grounded in the 53-slide Microsoft Foundry & MAF v1.0 specification).
- **Privacy & Security Check**:
  - Zero customer secrets, subscription IDs, tenant IDs, or private internal URLs included.
  - Synthetic PII (`ssn="123-45-6789"`) is used strictly inside unit tests to verify Layer-2 `FunctionInvocationMiddleware` auto-redaction (`***REDACTED_PII***`).
  - HTML 7-Card deck (`test-report-cards.html` / `cards.html`) enforces strict `Content-Security-Policy: default-src 'none'; style-src 'unsafe-inline'; img-src data:;` with zero external scripts or network calls.
- **Bilingual Parity**: Maintained in both Simplified Chinese (`README.md`, `test-report.md`) and English (`README.en.md`, `test-report.en.md`), plus same-page EN/ZH switching in the interactive H5 workbench (`index.html`).
