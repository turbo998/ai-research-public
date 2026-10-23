# Quality, Bilingual Parity & Sanitization Review (`faf-vs-agent-forge`)

- **Review Date**: 2026-10-23
- **Verified Repositories**:
  - `customer-success-microsoft/faf-agents@a740ad88afa0b054e656207e72205002ca6744f0` (`590` blobs / `736` tree entries)
  - `microsoft/agent-forge@655ff3401d18bd000252907a512a3f674114f708` (`38` blobs / `48` tree entries)

## 1. Verification & Provenance Checklist

- [x] **Exact Git Anchors Recorded**: `evidence.json` and `evidence/report.json` record exact commit SHAs, tree SHAs, blob SHAs, and byte sizes for key files across both repositories.
- [x] **Zero Fabricated Coordinates**: All 12 contract scenario percentages, 6 perturbation checks, and 4 latency/timeout tiers in `test-report.md`, `test-report.en.md`, and `test-report-cards.html` come directly from `evidence/report.json` and source files (`accelerators-scoring-card.md`, `scoring-framework.yaml`, `README-faf-token-benchmark.md`, `src/lib/validator.ts`, `src/lib/merger.ts`).
- [x] **Bilingual Parity (`zh-CN` + `en`)**:
  - `README.zh-CN.md` / `README.md` <-> `README.en.md`
  - `comparison-matrix.md` <-> `comparison-matrix.en.md`
  - `test-report.md` <-> `test-report.en.md`
- [x] **Self-Contained CSP 7-Card 4:5 Visual Deck**: `test-report-cards.html` enforces `Content-Security-Policy: default-src 'none'; style-src 'unsafe-inline'; img-src data:;` with zero external scripts, fonts, or network calls.
- [x] **Strict Sanitization for Public Sync**: Zero internal customer names, employee emails, or internal nomination URLs are present in any generated file.
