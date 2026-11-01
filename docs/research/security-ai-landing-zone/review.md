# Security AI Landing Zone & Frontier SOC (Sub-Topic Study) — Verification & Cryptographic Audit (`review.md`)

## 1. Source Provenance & Sanitization Verification

- **Primary Deck**: `Frontier Security Deck-10.26 final.pptx` (`15,233,523` bytes, SHA-256 `f82c91ebd5e9a3be3c0a95402dfa3fc483089dfb3e4bcd719609f4341d6864df`, 42 slides).
- **Parent Study**: `../defend-partner-playbook/` (`Microsoft DEFEND Partner Playbook & Security Partner Toolkit for SMB`).
- **Sanitization**: Stripped Slide 1 presenter personal name and any tracking parameters; preserved all architectural, licensing, and SOC telemetry data.

## 2. Deterministic Test Suite Status

- **Command**: `python -m unittest discover -s docs/research/security-ai-landing-zone/simulator -p "test_*.py" -v`
- **Result**: `Ran 6 tests in 0.000s — OK` (5 Pillars x 4 Controls = 20 atomic controls, 6 Pre-Scale Mandatory Questions, 5 Discovery Opener Questions, 22 Unified Security Graph tables, MDASH 100+ agents, and FTE Offer Week 3 Gate).

## 3. Deliverable Inventory & SHA-256 Checksums

| Relative Path | Size (Bytes) | SHA-256 Checksum |
| :--- | :---: | :--- |
| `assets/frontier-soc-mdash-isoc.svg` | `12355` | `8f255c1733feaed96c56c72f051aa7d55e0de4ceedb6589fceefffae33ebab11` |
| `assets/fte-sprint-assess-build-operate.svg` | `11643` | `a77bf46c79ca3f5abb9f3590c169d8e2270f9ad93b632370dae86e4424d12577` |
| `assets/landing-zone-5-pillars.svg` | `13460` | `895dadf877bae32ea0c5afd344516dc945a3da42ae6c1a08789907516df39471` |
| `cards.html` | `32062` | `84927afd85f18474f97a0727743f5fd915a07547a9af372bcb6d507f0cc71134` |
| `cards.zh.html` | `32610` | `f8cb6246c4d07a7b538da55e04bf84a2582b41ab89c0b2e65d6c648ed6ac46c1` |
| `evidence/test-batch-latency.csv` | `311` | `2b9e87b6ca8388496381648e7df2e091599155e07f3b83a9841b6a6db43ea4ed` |
| `evidence/test-robustness.csv` | `727` | `d32d9597e4261025a8e208cb8addc9a9283ce5e4c2609227791502c12e635f05` |
| `evidence/test-scenarios.csv` | `1765` | `b42c7eba5d2dd3a46e8f849a387f5e1ac1e53b6ed46bdcc2a203afdf88eeb982` |
| `evidence/verifier-summary.json` | `11506` | `71f1a19f6754601320765b7b3c743c690e8692fa855c5af183a3e34e7888e12a` |
| `evidence.json` | `1252` | `90c73af523ec0ef8da973b3021913860e1125f26b54e809c9938c0bb42896c16` |
| `index.md` | `16487` | `a3b611333cee31cfe1aa9038215081b508b6d3bfc0ede2cd5cb39cf49130b3d4` |
| `index.zh.md` | `34499` | `e91b4ff3cc981cef914b28ffbca63f845ffbc3b315faa097acdc088d37610c9d` |
| `README.en.md` | `16487` | `a3b611333cee31cfe1aa9038215081b508b6d3bfc0ede2cd5cb39cf49130b3d4` |
| `README.md` | `34499` | `e91b4ff3cc981cef914b28ffbca63f845ffbc3b315faa097acdc088d37610c9d` |
| `README.zh-CN.md` | `34499` | `e91b4ff3cc981cef914b28ffbca63f845ffbc3b315faa097acdc088d37610c9d` |
| `report.json` | `11506` | `71f1a19f6754601320765b7b3c743c690e8692fa855c5af183a3e34e7888e12a` |
| `simulator/generate_artifacts.py` | `54319` | `76033007a468cea1cd0f34f8a530b74ef83fb7b0a600565975de706ca08bf1ef` |
| `simulator/landing_zone_readiness_verifier.py` | `17917` | `7f7e8f92c7b50bac0ac6c71fcf0b9096138b67d3e169e94831b57652c60d3ac8` |
| `simulator/test_landing_zone_readiness_verifier.py` | `4683` | `974237f78c0de7f3133f7ee1311abfd9d5fe39e3912499c8473ece97f7a8ec8f` |
| `test-report-cards.html` | `32062` | `84927afd85f18474f97a0727743f5fd915a07547a9af372bcb6d507f0cc71134` |
| `test-report.en.md` | `7459` | `2a18d829803c6c44c281c6a5e58f75970eda38a144c724921cbb923cbe502922` |
| `test-report.md` | `7600` | `67d6d55d3266c44a8a819ab9c3ed4f474a3a7a54c8cfdcb4a26b9cc2928a1944` |
