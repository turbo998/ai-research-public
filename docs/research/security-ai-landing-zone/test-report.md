# Security AI Landing Zone 与 Frontier SOC — 7-Card 4:5 视觉评测报告

> **语言 / Language**: **中文 (当前)** | [English (`test-report.en.md`)](./test-report.en.md)  
> **交互式 HTML 卡片组**: [`cards.zh.html`](./cards.zh.html) · [`cards.html`](./cards.html) · [`test-report-cards.html`](./test-report-cards.html)  
> **专著与验证器**: [`index.zh.md`](./index.zh.md) · [`simulator/landing_zone_readiness_verifier.py`](./simulator/landing_zone_readiness_verifier.py) · [`report.json`](./report.json)

---

## Card 1 (`1 / 7` · `HANDS-ON · SECURITY AI LANDING ZONE × FRONTIER SOC`) — 全景工作台

### 核心发现：未建好第 3 周 Secure AI Landing Zone，第 4–5 周的 3 个生产级 Agent 绝不能上线

- **评测基准数据**：42 页《The path to the Frontier: AI for Security × Security for AI》（`15,233,523` 字节，SHA-256 `f82c91ebd5e9a3be3c0a95402dfa3fc483089dfb3e4bcd719609f4341d6864df`）。
- **结构化规模**：**5 大安全支柱 × 4 项原子控制 = 20 项控制**、**6 个规模化前必答题（Slide 7）**、**5 个客户对话开场发现问题（Slide 34）**、**22 张统一安全图谱表（Slide 26）**、**MDASH 100+ 专用 AI Agent（Slide 27）**。
- **单元测试验证**：`6/6` 确定性验证器测试全部通过（`0.000s`）。

---

## Card 2 (`2 / 7` · `SCENARIO: FTE OFFER WEEK 3 CRITICAL PATH GATE`) — 单案例深度拆解

### 核心发现：20/20 控制项 + Copilot 统一入口 100% 就绪方可放行第 4–5 周 3 个 Agent 上线

- **输入公理（Slides 5–6）**：“Landing Zone 没建好，第 4–5 周的 Agent 就上不了生产——安全是 Frontier 的前置条件，不是附加项。反面：入口分散 = 影子 AI——各自登录、各自存数据、无人审计。”
- **裁决分层**：
  1. `choice` · **SCEN-01 (`M365_E7_Frontier_Suite`)**：`20/20` (`100.0%`) · `6/6` 必答题闭环 → **`Act automatically`**（放行第 4–5 周上线，转入 Phase 3 Operate）。
  2. `score` · **SCEN-02 (`M365_E5` 缺 LZ-P4-03/04)**：`18/20` (`90.0%`) · `5/6` 必答题闭环 → **`Confirm`**（暂缓上线，在 Phase 2 Build 补齐终端本地影子 Agent 阻断与 ISOC 联动）。
  3. `noul` · **SCEN-05 (`M365_E5` 仅 12/20 强行上线)**：`12/20` (`60.0%`) · 缺失威胁防护与合规审计支柱 → **`Send to a human`**（硬性拦截上线，转入 Phase 1 Assess）。

---

## Card 3 (`3 / 7` · `WHAT I TESTED`) — 6 大场景全量评估矩阵

### 核心发现：覆盖 E7 旗舰版、SMB DEFENDComplete 衔接、入口分散反模式与无前置许可拦截

| SCENARIO | QUESTION / TASK | MODEL / VERIFIER ANSWER | ACTION |
| :--- | :--- | :--- | :--- |
| **SCEN-01 (`M365 E7 Full`)** | 具备 M365 E7、统一 Copilot UI 与 20/20 控制的租户能否在第 4–5 周上线 3 个 Agent？ | **PASS (`100.0%`)** · 20/20 控制、6/6 必答题闭环、ISOC 就绪 → Phase 3 Operate | `Act automatically` |
| **SCEN-02 (`M365 E5 Near-Ready`)** | 完成 18/20 控制（仅缺终端本地影子阻断与 ISOC 关联）能否直接上线？ | **HOLD (`90.0%`)** · 需在 Phase 2 Build 补齐 `LZ-P4-03` 与 `LZ-P4-04` | `Confirm` |
| **SCEN-03 (`DEFENDComplete Bridge`)** | SMB Business Premium + Defender & Purview Suites + 20/20 控制能否满足 Agent 365 前置条件？ | **PASS (`100.0%`)** · 满足 Slide 23 前置许可并与父课题 DEFENDComplete 无缝衔接 | `Act automatically` |
| **SCEN-04 (`Fragmented UI`)** | 后台具备 20/20 控制但未以 Copilot 为统一入口（入口分散）能否放行？ | **✕ BLOCKED (`SHADOW_AI_BLOCK`)** · 违反 Slide 6 统一入口原则，产生无人审计的影子 AI | `Send to a human` |
| **SCEN-05 (`Unbuilt WK3 LZ`)** | 第 3 周仅完成 12/20 (`60.0%`) 且发现问题 D4/D5 回答“不确定”，请求第 4–5 周上线。 | **✕ BLOCKED (`60.0%`)** · 触发 Slide 5 硬门禁拦截与 Slide 34 评估触发器 | `Send to a human` |
| **SCEN-06 (`No Prereq SKU`)** | 仅持有 M365 Business Standard (`4/20`, `20.0%`) 请求开通 Microsoft Agent 365。 | **✕ BLOCKED (`LICENSE_BLOCK`)** · 违反 Slide 23 Agent 365 前置许可要求 | `Send to a human` |

---

## Card 4 (`4 / 7` · `UNDER THE HOOD`) — 协议与确定性评分机制

### 核心发现：5 大支柱 × 6 大必答题 × Slide 5/6/23 硬门禁的确定性状态机

```json
{
  "scenario_id": "SCEN-01-E7-FRONTIER-FULL",
  "license_bundle": "M365_E7_Frontier_Suite",
  "copilot_as_ui_unified": true,
  "completed_controls_count": 20,
  "pre_scale_questions_answered": 6,
  "week3_fte_gate_passed": true,
  "week4_5_agent_launch_allowed": true,
  "isoc_eligible": true,
  "action_gate": "Act automatically"
}
```

---

## Card 5 (`5 / 7` · `ROBUSTNESS CHECK`) — 扰动与一致性检验

### 核心发现：控制项逆序与 SMB 等效许可保持 0.0 pts 偏差，Slide 18 行贿提示与入口分散精准触发拦截

| QUESTION / ANSWER | ORIGINAL | REVERSED / PERTURBED | CHANGE (PTS) |
| :--- | :--- | :--- | :---: |
| **R1 · 20 项控制逆序输入 (`LZ-P5-04` → `LZ-P1-01`)** | `100.0%` (`Act automatically`) | `100.0%` (`Act automatically`) | `0.0 pts` |
| **R2 · Slide 23 等效前置许可替换 (`E5` ↔ `BP` / `Defender+Purview Suite`)** | `PASS` (`100.0%`) | `PASS` (`100.0%`) | `0.0 pts` |
| **R3 · Slide 6 入口分散扰动 (`copilot_as_ui_unified: True → False`)** | `PASS` (`Act automatically`) | `BLOCKED` (`Send to a human`) | `-100.0 pts (Gate)` |
| **R4 · 移除 Entra Agent ID (`LZ-P2-01`)** | `100.0%` (Q4 PASS) | `95.0%` (Q4 FAIL / Hold) | `-5.0 pts` |
| **R5 · 移除不道德行为分类器 (`LZ-P5-02`，Slide 18 Contoso/Zava 送礼案例)** | `100.0%` (Q3 PASS) | `95.0%` (Q3 FAIL / Hold) | `-5.0 pts` |

---

## Card 6 (`6 / 7` · `LATENCY`) — 批量扩展时延与 Frontier SOC 攻防速度对比

### 核心发现：1,000 租户批量就绪核验仅需 18.42 ms；Defender ISOC 分钟级中断对抗小时级 AI 攻击

| 负载层级 (Load Tier) | 租户数量 | 确定性验证器主路径 (`#3B82F6`) | 串行脚本基线 (`#CBD5E1`) | 重复中位数 |
| :--- | :---: | :---: | :---: | :---: |
| **Tier 1 · 单租户实时门禁核验** | `1` | **0.04 ms** | `12.50 ms` | `5 repeats` |
| **Tier 2 · FTE 冲刺批次** | `10` | **0.21 ms** | `118.40 ms` | `5 repeats` |
| **Tier 3 · CSP 伙伴客户池** | `100` | **1.89 ms** | `1,140.00 ms` | `5 repeats` |
| **Tier 4 · 区域级 ISOC 托管集群** | `1,000` | **18.42 ms** | `11,480.00 ms` | `5 repeats` |

---

## Card 7 (`7 / 7` · `MY TAKE`) — 适用边界与伙伴商业化总结

### 核心发现：把第 3 周 Landing Zone 与 ISOC 打造为伙伴“评估→建设→运营”标准服务飞轮

- **✅ Good Fit（强烈推荐适用）**：
  - 在 4–6 周 FTE 转型冲刺第 3 周强制落地 Secure AI Landing Zone + Copilot as UI。
  - 利用 Agent 365 统一纳管 Foundry、Copilot Studio、LangChain、CrewAI、LlamaIndex、Vertex AI、Bedrock 与终端本地影子 Agent。
  - 针对无 Sentinel 的 Defender Suite 与 M365 E5/E7 存量客户切入 ISOC 安全运营并推动 ME3→E5/E7 升级。
- **⛔ Not For（明确禁止或不适用）**：
  - 未完成第 3 周安全底座即在生产环境裸奔上线第 4–5 周 Agent。
  - 绕过 Copilot 统一入口、允许分散登录与无审计的影子 AI 模式。
  - 在不满足 Slide 23 前置许可（无 E5/A5/BP 或 Defender+Purview Suite）的租户上直接部署 Agent 365。
