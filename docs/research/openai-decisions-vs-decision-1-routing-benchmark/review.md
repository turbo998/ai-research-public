# Governance, Privacy & Verification Review — `openai-decisions-vs-decision-1-routing-benchmark`

## 1. Scope & Taxonomy Placement

- **Topic Directory**: `docs/research/openai-decisions-vs-decision-1-routing-benchmark/`
- **Category in `docs/research/index.md`**: `评测与治理` × `Agent 与编排` → **决策模型与多模型路由评测（Decision Models & Model Routing）**
- **Relationship to Baseline & Companion Research**:
  - Preserves 100% of existing repository topics and public governance guardrails without modification.
  - Complements [`docs/research/decision-model-routing/`](../decision-model-routing/README.md) by adding the full 8-way comparison (`OpenAI Decisions /v1/decisions`, `gpt-6-luna` with `reasoning_effort="none"` vs default reasoning) and the `Switchyard v2.4.1` 4-variant instruction sensitivity study (`2,760` decisions).

## 2. Provenance & Numerical Verification (`Zero Fabricated Coordinates`)

- **Provenance**: `anonymized_reported` (`independently_reproduced=false`).
- **Verification**: All metrics in `README.md`, `test-report.md`, `test-report-cards.html`, and `report.json` were computed and cross-checked directly from the sealed raw evaluation datasets (`summary8.json`, `summary241.json`, `rows8.json`, `rows241.json`, `sensitivity.json`, `sensitivity-systemone.json`):
  - `v2.4.0` (`summary8.json`): 8 approaches × 40 prompts × 3 rounds = `960` decisions.
  - `v2.4.1` (`summary241.json`): 8 approaches under `neutral` (`960` decisions) + 5 dedicated engines across `cheap`, `strong`, and `bare` (`1,800` decisions) = `2,760` decisions.
  - Direct API diagnostic (`sensitivity.json` + `sensitivity-systemone.json`): `80 + 80 = 160` decisions.

## 3. Privacy, Anonymization & Licensing Audit

- **Redacted Identifiers**:
  - Personal author names, organizational titles, and private Notion workspace URLs have been completely omitted.
  - Private Azure AI Foundry resource hostnames in diagnostic scripts have been redacted to `https://<resource>.services.ai.azure.com/providers/microsoft/v1/systemone`.
  - No API keys, tokens, or raw external zip archives are committed.
- **Model & Code Licensing**:
  - `satomic/model-router` (Switchyard): public GitHub repository (`commits b58bfd31, 3408c39c, 8a20a7b6`).
  - `OpenJev 27B` (`openjev/openjev`): `CC BY-NC 4.0` (non-commercial restriction explicitly flagged in all tables and recommendations).
  - `Laya 0.3.20` (`NandhaKishorM/laya`): `Apache-2.0`.
  - `Microsoft Decision-1`, `TypeSafe Jev`, `OpenAI Decisions`: commercial cloud APIs.
