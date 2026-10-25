# Review & Provenance Verification Record — `e2b-nomad-heartbeat-resilience`

- **Review Date**: `2026-10-25`
- **Topic**: Building E2B Sandbox Resilience: Discovering and Tuning Nomad Heartbeats (`构建 E2B 沙箱韧性：Nomad 心跳机制的发现与实践`)
- **Provenance Classification**: `anonymized_reported` + `static_source_verified` (`independently_reproduced = false`)
- **Format Standard**: 7-Card 4:5 Visual Report Deck (`900x1125` portrait cards, `Content-Security-Policy: default-src 'none'; style-src 'unsafe-inline'`)

---

## 1. Quality & Guardrail Checklist

| Check | Status | Notes |
| :--- | :---: | :--- |
| **Headline-as-Finding (Cards 1–7)** | PASS | Every card headline states a concrete quantitative or architectural finding from the E2B × Nomad fault-injection study. |
| **Zero Fabricated Coordinates** | PASS | All replacement ratios (`7/20`, `7/20`, `2/3`), log timestamps (`21s`, `39s`, `44s`), `unknown` durations (`1.7s–31.6s`), sandbox checks (`10/10`), NDJSON streams (`23/23`), short requests (`12,581` with `0` errors), and `heartbeat_grace` rounds (`20/20` across 2 rounds) match the published case study and deterministic verifier. |
| **Pinned Upstream Source Verification** | PASS | All 13 Nomad source file/line ranges (`hashicorp/nomad@bf24b0dd97430d3b364b68b1f7375e85e585778f`), `hashicorp/yamux@v0.1.2` (`session.go#L327-L379`), and `e2b-dev/runtime@afaaeaef96aae86f65ce60bf38fe083e7638a28e` discovery paths are documented and cross-checked. |
| **Bilingual Completeness (`zh-CN` + `en`)** | PASS | `README.md`, `README.zh-CN.md`, `README.en.md`, `test-report.md`, and `test-report.en.md` are complete and cross-linked. |
| **Self-Contained CSP HTML Deck** | PASS | `test-report-cards.html` rendered via `benchmark_harness.cards.render_card_deck` with strict inline-only CSS and zero external network requests. |
| **Deterministic Verifier Unit Tests** | PASS | `6 / 6` unit tests in `simulator/test_e2b_nomad_heartbeat_verifier.py` pass (`0.009s`). |

---

## 2. Artifact Manifest & SHA-256 Checksums

| Relative Path | Size (Bytes) | SHA-256 |
| :--- | ---: | :--- |
| `README.md` | `45,548` | `7a8c52afcd5331b82c37c3c0e7e8dadbc53dd9c5afe2f9a6ee9b2cee54fc663d` |
| `README.zh-CN.md` | `45,537` | `691f3bec4ad42b1ee19089b6f5875c9f0ccba2c76a1c507f6d236561e42c8df2` |
| `README.en.md` | `19,370` | `e49a0b5b0b83ef6fb0b0416e9757ca028657e9ef0ca8914ea0726b5551dac461` |
| `test-report.md` | `12,823` | `a229f75794fae65425a235337f8fbde36b7363a3eab252992b43b0c8c3b854fd` |
| `test-report.en.md` | `12,357` | `12967bd53f76c7806006a7867f6f1e19051d3c9d627ae63a1c0a5e8a4cb1687e` |
| `test-report-cards.html` | `67,937` | `482d9ee05d7794adcf0401d72acfef20af46a674e2b33ed1e78f5c71ec67fba0` |
| `report.json` | `26,885` | `38c592543756460a14bb74d660519a302afc8383dddeab149d182e9142424fd8` |
| `evidence.json` | `4,614` | `7dc3d8918f1b434e0fa5040a757ab363d9c3a73f8c87a96a286884d38780dc0a` |
| `evidence/verifier-summary.json` | `7,079` | `dcd8c8cef759cf0cb89a9f69164738e61735b82bccaf6c087047884d4ef88d10` |
| `evidence/test-scenarios.csv` | `2,070` | `57056d9ba259cfb8ed9f859692d286d71766e6aa8075e053e34a9a9d32cd658e` |
| `evidence/test-robustness.csv` | `1,019` | `230bed9fed251a75610c5643760af2e988f884352d7fc4caaed0c21dd389b2e9` |
| `evidence/test-batch-latency.csv` | `171` | `50d02cfedbd2d7fec6ab4c752d47eb86dfab57da59b8ca47e796137dbef3d790` |
| `simulator/e2b_nomad_heartbeat_verifier.py` | `13,613` | `93bc2e1872df1f28beb819481942153f10ee61edd7d7f5f4b3ccd994611a1bf3` |
| `simulator/test_e2b_nomad_heartbeat_verifier.py` | `6,671` | `ddb266a65a96ad755b904207582aeec8834fceb1dfdb5e7e515e0d04ec4bc63e` |
| `simulator/generate_artifacts.py` | `40,448` | `99b834d2af8bcfba8953f93ab464fe06d2a3f7e446b8cf6173cb1311ecb13eb0` |
