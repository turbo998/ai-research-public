# Microsoft DEFEND Partner Playbook & Security Partner Toolkit for SMB — Verification & Cryptographic Audit (`review.md`)

## 1. Source Provenance & Sanitization Verification

- **Primary Deck**: `DEFEND Partner Playbook.pptx` (`11,425,905` bytes, SHA-256 `0298c3bb248a0465d9a1c250ccb1fd1eb631ef5787137d6bbb9a3fc07babad46`, 53 slides across 11 chapters).
- **Supplemental Toolkit**: `Security Partner Toolkit for SMB — Accelerate Security and AI Readiness Engagements` (6 resolved `aka.ms` link assets, 7 Industry One-Pagers / 14 pages, 6 Deployment Guides / 360 pages, 3 official Microsoft GitHub repos).
- **Sanitization**: Zero personal email addresses, phone numbers, author bylines, or SafeLinks tracking tokens.

## 2. Deterministic Test Suite Status

- **Command**: `python -m unittest discover -s docs/research/defend-partner-playbook/simulator -p "test_*.py" -v`
- **Result**: `Ran 7 tests in 0.001s — OK` (41 capability rows, 51 mandatory exit criteria rows, Slide 40 governance lock, and 6-asset SMB Partner Toolkit catalog).

## 3. Deliverable Inventory & SHA-256 Checksums

| Relative Path | Size (Bytes) | SHA-256 Checksum |
| :--- | :---: | :--- |
| `assets/gating-matrix.svg` | `13016` | `01ea6a1900d2983696288656fafbeeca9b4a0dc1e72146c1dee94668453ed68b` |
| `assets/overview.svg` | `16607` | `51b9e7b4ef917aec05ac7f3fba4b8acc0ea2427b42fcd319b4e118b947f60525` |
| `assets/partner-toolkit-lifecycle.svg` | `17603` | `d281bb99f82cbe6af8b6176ce17097c5caea0d11fdf37d0301a027cbc94508e4` |
| `assets/purview-ai-bridge.svg` | `9320` | `c5a90fd421f05ab8c178691476c1b2cb1a9795237ca514d172d4abe886cfc33b` |
| `cards.html` | `84406` | `407317b826acd911eeb8bd52573341ac19629b7dd40eb8830d9ccd518efea146` |
| `cards.zh.html` | `84999` | `e88783099a583f604e8168d41093f1f0d37a5f3f9a0146055e672c1239225feb` |
| `evidence/test-batch-latency.csv` | `150` | `91518bdde892480a3bfb77a12ef1dcb810efac2476325cb63806373b07e4fec0` |
| `evidence/test-robustness.csv` | `1072` | `9fc1a97641989706678e107dc1f3a3bdd1d27f34c8ab610d302b6433a6a8f556` |
| `evidence/test-scenarios.csv` | `2426` | `214791b0b3b679229d6ff10d2fc677a60a8c19e8a202fcad28d1c9d8c5141ae3` |
| `evidence/verifier-summary.json` | `11361` | `09ff2e12698893219075004f7ffdb9372502c3e83688b1692413950d466f029b` |
| `evidence.json` | `11824` | `b9965141015bcc5d34147bfb8e31bd2b5d45a322a8e2bcd854cc9ea5de26eeb7` |
| `index.md` | `37957` | `625d52a4b5ba7ee0a45d772003f22fad8a7df405135ff910fb991f257b115213` |
| `index.zh.md` | `57693` | `c71153c2424dc09fc35be2a2b5ed195071faa8b6f3704aacee7db92bebb6dbed` |
| `README.en.md` | `37957` | `625d52a4b5ba7ee0a45d772003f22fad8a7df405135ff910fb991f257b115213` |
| `README.md` | `57693` | `c71153c2424dc09fc35be2a2b5ed195071faa8b6f3704aacee7db92bebb6dbed` |
| `README.zh-CN.md` | `57693` | `c71153c2424dc09fc35be2a2b5ed195071faa8b6f3704aacee7db92bebb6dbed` |
| `report.json` | `38943` | `69d48882261ba92052d5702fd53593044e48a2fd0463ffd41501ddc54e60dc63` |
| `simulator/defend_tier_readiness_verifier.py` | `31913` | `fa577c329439e56e4c813de01b81bb32ea4930d7a9ecfa418a7284feb9177d26` |
| `simulator/generate_artifacts.py` | `50552` | `621f630b182c3f1b28b54cb60eb798126765d1655e2984ea53bb9fa1cbf6ba45` |
| `simulator/test_defend_tier_readiness_verifier.py` | `7443` | `0427b82322c1060cf2ae16c10ef87e83a3f7622eebbc5e0b20e87781adba0f60` |
| `test-report-cards.html` | `84406` | `407317b826acd911eeb8bd52573341ac19629b7dd40eb8830d9ccd518efea146` |
| `test-report.en.md` | `17432` | `5714a0b0a51b1542a375d1a087c4388b863b0649ce742bcf5f764323d4c291f0` |
| `test-report.md` | `18180` | `1d719139eae69d45e4e1bcb558e78d2ae5048abe657a2dadf51ba750f48fc274` |
