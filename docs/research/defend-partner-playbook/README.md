# DEFEND 合作伙伴指南与微软 SMB 安全合作伙伴工具包深度研究：基于 Microsoft 365 Business Premium 的五层托管安全、Purview AI 治理与全链路自动化交付体系

> **语言 / Language**: **中文 (当前)** | [English (`README.en.md`)](./README.en.md)  
> **7-Card 4:5 视觉评测报告**: [中文报告 (`test-report.md`)](./test-report.md) · [English Report (`test-report.en.md`)](./test-report.en.md) · [交互式 HTML 卡片 (`test-report-cards.html`)](./test-report-cards.html) ([中文卡片 (`cards.zh.html`)](./cards.zh.html) | [English Cards (`cards.html`)](./cards.html))  
> **确定性验证器与数据集**: [`simulator/defend_tier_readiness_verifier.py`](./simulator/defend_tier_readiness_verifier.py) · [`simulator/test_defend_tier_readiness_verifier.py`](./simulator/test_defend_tier_readiness_verifier.py) · [`report.json`](./report.json) · [`evidence.json`](./evidence.json) · [`review.md`](./review.md)  
> **专项子课题延伸 (`Child Sub-Topic`)**: 🔗 **[Security AI Landing Zone 与 Frontier SOC 深度研究 (`../security-ai-landing-zone/`)](../security-ai-landing-zone/index.zh.md)** ([English](../security-ai-landing-zone/index.md) | [中文 7 卡](../security-ai-landing-zone/cards.zh.html) | [English 7-Card](../security-ai-landing-zone/cards.html)) —— 聚焦 *Security for AI × AI for Security*、Copilot as UI、Microsoft Agent 365 五大安全支柱、M365 E7 Frontier Suite 与 Defender ISOC / MDASH  
> **所属研究支柱**: Pillar 04 — 零信任治理、红队演练与托管安全服务体系 (Zero-Trust Governance, Red Team & Managed Security)

---

## ⚠️ 重要边界声明与合规免责提示 (Important Governance & Commercial Boundary)

根据《DEFEND Partner Playbook》第 4、8、44、53 页（`© 2026 Microsoft Corporation`）的官方声明：
1. **非微软官方 SKU**：**DEFEND 框架（`DEFENDBase`、`DEFENDSecurity`、`DEFENDCompliance`、`DEFENDComplete`、`DEFENDExtend`）及其附录中的服务蓝图（SMB 交付蓝图、四层 Purview-as-a-Service 模型）以及 Microsoft Security Partner Toolkit for SMB 均属于合作伙伴交付的服务构建块与运营参考框架 (Partner-Delivered Service Constructs)，并非微软官方产品、SKU、授权捆绑包或强制性商业报价。**
2. **授权与配置责任**：相关安全与合规能力的实现取决于客户是否持有合格的微软授权（如 Microsoft 365 Business Premium、Microsoft Defender Suite 附加组件、Microsoft Purview Suite 附加组件、Microsoft Sentinel 消费计费等）以及合作伙伴是否完成显式的策略配置与运营接管。合作伙伴在对外发布商业提案或营销材料前，必须独立核实最新的 Microsoft Product Terms、授权规则与服务声明。
3. **隐私与脱敏声明**：本研究档案已对原始演示文稿及邮件材料中的所有个人作者署名、邮箱地址、电话号码及 Outlook SafeLinks 追踪参数完成 100% 脱敏剥离，仅保留公开可验证的技术架构、官方 `aka.ms` 链接与微软开源代码库结构。

---

## 1. 执行摘要：从“战略分层 (`DEFEND Playbook`)”到“工程落地 (`Security Partner Toolkit for SMB`)”

在中小型企业（SMB，通常为 1–300 席位）市场中，管理服务提供商（MSP）与安全服务合作伙伴面临三大核心结构性痛点（Slides 3, 6）：
- **静默配置漂移与基线缺失**：大量客户虽已采购 Microsoft 365 Business Premium，但未强制启用 MFA、条件访问（Conditional Access）、Intune 设备合规、BitLocker 或阻止旧版身份验证（Legacy Authentication），导致已付费的安全价值长期闲置。
- **Copilot 与生成式 AI 带来的敏感数据过曝风险**：客户迫切希望引入 Microsoft 365 Copilot 或使用网页端生成式 AI（如 ChatGPT、Gemini），但缺乏敏感度标签、自动分类、端点/聊天 DLP 与 AI 数据安全态势管理（DSPM for AI），极易触发内部越权检索（Oversharing）或外部 Shadow AI 泄密。
- **过早接入 SIEM 引发的 SOC 告警海啸**：部分合作伙伴在未完成基础身份、终端与数据策略调优前，直接将客户接入 Microsoft Sentinel，导致海量未降噪的原始遥测淹没分析师，推高日志摄取成本并引发告警疲劳（Alert Fatigue）。

本研究将两套高度互补的微软官方合作伙伴资产融合为统一的**“战略 + 执行”双引擎架构**：
1. **战略与治理引擎 ——《DEFEND Partner Playbook》（11 章 / 53 页 PPTX，SHA-256: `0298c3bb248a0465...`）**：定义了以 **Microsoft 365 Business Premium** 为底座的 **5 层阶梯式托管安全模型**、横跨 **41 项平台能力**的授权阶梯矩阵、**51 项强制层级准出标准（Exit Criteria）**、**Slide 40 硬性治理铁律**，以及针对 Copilot/AI 准备度的 **4 层 Purview-as-a-Service 数据治理蓝图**。
2. **全链路执行引擎 ——《Microsoft Security Partner Toolkit for SMB》（5 大交付阶段 / 6 大 `aka.ms` 核心资产）**：提供了可直接用于客户交付的 **7 份行业信息保护一页纸（14 页 PDF，含 8 级 DEFEND 敏感度标签体系与 LOB 免加密异常分支）**、**数据安全引导助手 (`microsoft/DataSecurityGuidedAssistant` v2.0.1572)**、**Purview SOW 工作说明书生成器 (`microsoft/SOWGenerator`，含 22 项模块化服务)**、**6 本最佳实践安全部署指南（总计 360 页 PDF）**，以及 **PowerShell 7+ 幂等自动化部署脚本 (`microsoft/BestPractice_Deploy-Scripts` / `SMBBestPracticeTool`)**。

![DEFEND 5-Tier Architecture Overview](./assets/overview.svg)

---

## 2. 《DEFEND Partner Playbook》全景架构拆解（11 章 / 53 页逐章映射）

| 章节 | 页码范围 | 章节标题 | 核心架构产出与关键机制 |
| :---: | :---: | :--- | :--- |
| **Ch 01** | Slides 1–7 | **Welcome to the DEFEND Partner Playbook** | 定义 DEFEND 五层架构（`DEFENDBase` → `DEFENDSecurity` / `DEFENDCompliance` → `DEFENDComplete` → `DEFENDExtend`）、MSP 四大核心收益（标准化交付、附加组件升级路径、降低配置漂移、提升续约率）及非官方 SKU 边界声明 |
| **Ch 02** | Slides 8–16 | **Licensing Building Blocks** | 拆解 **Microsoft 365 Business Premium** 核心底座、**Defender Suite** 附加组件（21 项能力对比表，Slides 10–11）、**Purview Suite** 附加组件（20 项能力对比表，Slides 13–14）与 **Microsoft Sentinel** SIEM/SOAR 扩展 |
| **Ch 03** | Slides 17–20 | **Start with Security Posture (Zero Trust Assessment)** | 强制要求在报价或配置前执行 **Microsoft Zero Trust Assessment（零信任评估）**，覆盖 **7 大评估维度**：`Identity`、`Devices`、`Applications`、`Data`、`Infrastructure`、`Networks`、`AI` |
| **Ch 04** | Slides 21–24 | **Core Operating Foundations (Lighthouse & Intune)** | 明确两大运营底座职责边界：**M365 Lighthouse**（基于 GDAP 的多租户基线可见性与漂移监控，**绝非 SOC/SIEM 或 Intune 替代品**）与 **Microsoft Intune Plan 1**（权威的设备合规强制执行引擎） |
| **Ch 05** | Slides 25–31 | **The DEFEND Service Model** | 逐层定义五大服务层级的目标客户画像、核心交付成果、商业价值与升级触发条件 |
| **Ch 06** | Slides 32–33 | **Mapping Capabilities Across Tiers** | 构建横跨身份、设备、邮件协作、数据保护、合规治理、SIEM/SOC 的跨层级责任推进矩阵 |
| **Ch 07** | Slides 34–40 | **Tier Exit Criteria & Governance Rules** | 制定 **51 项强制准出检查表（48 项原子控制 + 3 项跨层复合门禁，Slides 35–39）** 与 **Slide 40 治理铁律**（未满足准出或未签署正式风险接受严禁跨层；未完成 `DEFENDComplete` 严禁激活 `DEFENDExtend`） |
| **Ch 08** | Slides 41–42 | **Partner Readiness & Implementation Checklist** | 从商业包装（服务目录、SLA、风险接受流程）、技术就绪（GDAP、Lighthouse、Intune、LLD 低层设计）到运营就绪（告警路由、QBR 季度复盘）的上线清单 |
| **Ch 09** | Slides 43–46 | **Appendix A — Partner Offer Blueprint (SMB)** | 面向中小企业的标准化一页纸商业架构蓝图，明确每一层级的“包含服务 (Included)”与“明确排除项 (Excluded)”以防止范围蔓延 (Scope Creep) |
| **Ch 10** | Slides 47–51 | **Appendix B — Purview-as-a-Service Blueprint** | 将合规与 AI 数据治理拆解为 **4 个递进式服务层级**：`Tier 1 Data Protect` → `Tier 2 Data Govern` → `Tier 3 Data Control (AI Ready)` → `Tier 4 Data Assure (Managed)` |
| **Ch 11** | Slides 52–53 | **Summary, Next Steps & Official References** | 汇总合作伙伴落地路线图与 12 条微软官方 Microsoft Learn / `aka.ms` 权威参考链接 |

---

## 3. 授权构建块与 41 项能力矩阵精确量化分析 (Chapter 02 · Slides 8–16)

通过对原始 PPTX 底层 XML 表格（Slides 10–11 及 Slides 13–14）的逐格解析与确定性验证器（`defend_tier_readiness_verifier.py`）核算，**Microsoft 365 Business Premium 单底座覆盖了 41 项高阶安全与合规能力中的 15 项（`36.6%`）**；而叠加 **Defender Suite** 与 **Purview Suite** 后，覆盖率跃升至 **`41 / 41`（`100.0%`）**，在 SMB 授权体系下实现与 Enterprise E5 100% 对齐的安全与合规能力：

### 3.1 跨层级授权覆盖率汇总表

| 授权组合 / 对应 DEFEND 层级 | Defender 矩阵覆盖 (共 21 项, Slides 10–11) | Purview 矩阵覆盖 (共 20 项, Slides 13–14) | 41 项总能力覆盖率 | 相对 Business Premium 净增幅 |
| :--- | :---: | :---: | :---: | :---: |
| **Microsoft 365 Business Standard** *(参考对照组)* | `2 / 21` (`9.5%`) | `3 / 20` (`15.0%`) | **`5 / 41` (`12.2%`)** | `-24.4 pts` *(严重缺失零信任基线)* |
| **Microsoft 365 Business Premium (`DEFENDBase` / `Data Protect`)** | `8 / 21` (`38.1%`) | `7 / 20` (`35.0%`) | **`15 / 41` (`36.6%`)** | **基准线 (`0.0 pts`)** |
| **Business Premium + Defender Suite (`DEFENDSecurity`)** | **`21 / 21` (`100.0%`)** | `7 / 20` (`35.0%`) | **`28 / 41` (`68.3%`)** | **`+31.7 pts`** *(安全域 `+61.9 pts`)* |
| **Business Premium + Purview Suite (`DEFENDCompliance` / `Data Control`)** | `8 / 21` (`38.1%`) | **`20 / 20` (`100.0%`)** | **`28 / 41` (`68.3%`)** | **`+31.7 pts`** *(合规/AI 域 `+65.0 pts`)* |
| **Business Premium + 双套件 (`DEFENDComplete` / Enterprise E5 对齐)** | **`21 / 21` (`100.0%`)** | **`20 / 20` (`100.0%`)** | **`41 / 41` (`100.0%`)** | **`+63.4 pts`** *(100% 完整覆盖)* |

### 3.2 Defender Suite 21 项能力逐项矩阵 (Slides 10–11)

| 能力域 | 编号 | 具体安全能力项 (Capability) | Business Standard | Business Premium (`DEFENDBase`) | + Defender Suite (`DEFENDSecurity`) | Enterprise E5 |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: |
| **Email Protection (5 项)** | `D01` | Spam and malware protection (Exchange Online Protection) | ● | ● | ● | ● |
| **Email Protection** | `D02` | Advanced phishing, zero-day malware & link protection (MDO Plan 1: Safe Links / Safe Attachments) | ○ | ● | ● | ● |
| **Email Protection** | `D03` | Phishing simulation and end-user security training (Attack Simulation Training — MDO Plan 2) | ○ | ○ | **●** | ● |
| **Email Protection** | `D04` | Automated investigation and remediation for email threats (AIR — MDO Plan 2) | ○ | ○ | **●** | ● |
| **Email Protection** | `D05` | Cross-domain threat hunting across email, links and collaboration (Threat Explorer — MDO Plan 2) | ○ | ○ | **●** | ● |
| **Endpoint Protection (5 项)** | `D06` | Built-in OS antivirus protection | ● | ● | ● | ● |
| **Endpoint Protection** | `D07` | Next-gen endpoint protection, behavioral EDR & ASR rules (Defender for Business) | ○ | ● | ● | ● |
| **Endpoint Protection** | `D08` | Advanced endpoint threat hunting across devices (MDE Plan 2 Advanced Hunting) | ○ | ○ | **●** | ● |
| **Endpoint Protection** | `D09` | Extended alert retention (6 months) & deeper forensic investigation timelines (MDE Plan 2) | ○ | ○ | **●** | ● |
| **Endpoint Protection** | `D10` | Threat analytics and global threat intelligence insights (Defender Threat Intelligence / MDE P2) | ○ | ○ | **●** | ● |
| **Identity & Access (9 项)** | `D11` | Multi-factor authentication (MFA) | ○ | ● | ● | ● |
| **Identity & Access** | `D12` | Conditional Access policies (user, device, location, app — Entra ID P1) | ○ | ● | ● | ● |
| **Identity & Access** | `D13` | Risk-based Conditional Access & Identity Protection (sign-in risk & user risk — Entra ID P2) | ○ | ○ | **●** | ● |
| **Identity & Access** | `D14` | Self-service password reset (SSPR) for cloud and hybrid users (Entra ID P1) | ○ | ● | ● | ● |
| **Identity & Access** | `D15` | Automated remediation for compromised user accounts (Entra ID P2) | ○ | ○ | **●** | ● |
| **Identity & Access** | `D16` | Privileged Identity Management (PIM — just-in-time admin elevation & approval — Entra ID P2) | ○ | ○ | **●** | ● |
| **Identity & Access** | `D17` | Access reviews and entitlement management (Entra ID P2 Governance) | ○ | ○ | **●** | ● |
| **Identity & Access** | `D18` | Hybrid / on-premises Active Directory identity threat detection (Defender for Identity — MDI) | ○ | ○ | **●** | ● |
| **Identity & Access** | `D19` | Detailed identity risk investigation and workbook insights (Entra ID P2 + MDI) | ○ | ○ | **●** | ● |
| **Cloud App Security (2 项)** | `D20` | Basic cloud app visibility and OAuth app discovery | ○ | ● | ● | ● |
| **Cloud App Security** | `D21` | Full CASB: Shadow IT governance, real-time session control & SaaS posture (Defender for Cloud Apps) | ○ | ○ | **●** | ● |

### 3.3 Purview Suite 20 项能力逐项矩阵 (Slides 13–14)

| 能力域 | 编号 | 具体数据安全与合规能力项 (Capability) | Business Standard | Business Premium (`DEFENDBase`) | + Purview Suite (`DEFENDCompliance`) | Enterprise E5 |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: |
| **Information Protection (6 项)** | `P01` | Manual sensitivity labels in Office apps | ● | ● | ● | ● |
| **Information Protection** | `P02` | Sensitivity labels with encryption, visual markings & rights management (Azure RMS) | ○ | ● | ● | ● |
| **Information Protection** | `P03` | Automatic sensitivity labeling in Office apps, SharePoint & OneDrive (Client + Service Auto-Labeling) | ○ | ○ | **●** | ● |
| **Information Protection** | `P04` | Classification using sensitive info types, trainable classifiers & fingerprinted templates | ○ | ○ | **●** | ● |
| **Information Protection** | `P05` | Customer-managed encryption keys (Bring Your Own Key — BYOK) | ○ | ○ | **●** | ● |
| **Information Protection** | `P06` | Double Key Encryption (DKE) for highly regulated workloads | ○ | ○ | **●** | ● |
| **Data Loss Prevention (6 项)** | `P07` | DLP for Exchange Online, SharePoint Online & OneDrive for Business | ○ | ● | ● | ● |
| **Data Loss Prevention** | `P08` | DLP for Teams chat and channel messages | ○ | ○ | **●** | ● |
| **Data Loss Prevention** | `P09` | Endpoint DLP (Windows & macOS file copy, print, USB, upload, browser transfer restrictions) | ○ | ○ | **●** | ● |
| **Data Loss Prevention** | `P10` | DLP for cloud apps and inline SaaS session controls (integrated with Defender for Cloud Apps) | ○ | ○ | **●** | ● |
| **Data Loss Prevention** | `P11` | **DLP for Microsoft 365 Copilot** (sensitivity label & SIT controls for AI prompts/grounding) | ○ | ○ | **●** | ● |
| **Data Loss Prevention** | `P12` | Adaptive DLP enforcement driven by user Insider Risk levels (Adaptive Protection) | ○ | ○ | **●** | ● |
| **Data Lifecycle Mgmt (3 项)** | `P13` | Manual retention and deletion labels | ● | ● | ● | ● |
| **Data Lifecycle Mgmt** | `P14` | Basic tenant-wide retention policies for Exchange, SharePoint & OneDrive | ○ | ● | ● | ● |
| **Data Lifecycle Mgmt** | `P15` | Automatic retention policies based on events, trainable classifiers & sensitive content (Records Mgmt) | ○ | ○ | **●** | ● |
| **Insider Risk & Comm (3 项)** | `P16` | Insider Risk Management (data theft, departing employee exfiltration, policy violations) | ○ | ○ | **●** | ● |
| **Insider Risk & Comm** | `P17` | Adaptive Protection (dynamic Conditional Access & DLP tightening based on insider risk score) | ○ | ○ | **●** | ● |
| **Insider Risk & Comm** | `P18` | Communication Compliance (detecting regulatory violations, harassment, sensitive sharing in Teams/Email) | ○ | ○ | **●** | ● |
| **eDiscovery & Audit (2 项)** | `P19` | Basic eDiscovery (Standard) and 90-day standard audit logs | ● | ● | ● | ● |
| **eDiscovery & Audit** | `P20` | **eDiscovery (Premium) & Audit (Premium)** (1-year+ log retention, legal hold notifications, review sets, AI-relevant high-value audit events) | ○ | ○ | **●** | ● |

---

## 4. 零信任姿态评估与双核心运营底座 (Chapters 03–04 · Slides 17–24)

### 4.1 Phase 0：Microsoft 零信任评估的 7 大核心维度 (Slides 17–20)
Playbook 强调：**“永远以安全姿态发现作为起点，而非直接推销许可证 (Start with Security Posture, Not Licensing)”**。通过运行官方零信任评估工具，合作伙伴可在单一视图中获取覆盖 **7 大维度**的实证基线差距：
1. **Identity（身份）**：MFA 覆盖率、特权账户数量、旧版认证残留、条件访问策略缺口。
2. **Devices（设备）**：Intune 纳管率、不合规设备放行风险、BitLocker 加密状态、操作系统补丁水位。
3. **Applications（应用）**：OAuth 第三方应用授权风险、Shadow IT 云应用暴露面。
4. **Data（数据）**：敏感数据分布、未标记文件占比、外部匿名链接与全员共享（Oversharing）风险。
5. **Infrastructure（基础设施）**：混合云与管理平面权限配置。
6. **Networks（网络）**：命名位置、会话控制与边界防护。
7. **AI（人工智能准备度）**：Copilot 及 AI 工具对底层数据的访问边界、DLP 与 DSPM for AI 准备情况。

### 4.2 M365 Lighthouse 与 Microsoft Intune Plan 1 的严格职责解耦 (Slides 21–24)
在多租户 MSP 运营中，最常见的架构误区是将 M365 Lighthouse 误认为全能安全控制台。Slide 21–24 明确划定了三者的工程边界：
- **Microsoft 365 Lighthouse = 跨租户可见性与治理控制平面 (Multi-Tenant Visibility Plane)**：通过 **GDAP（细粒度委派管理权限，强制绑定安全组与最小权限角色）** 聚合多个 SMB 客户租户的基线合规度、MFA/CA 覆盖率、风险账户与 Defender for Business 基础态势。**Slide 21 明确警告：Lighthouse 绝不是 SOC/SIEM 实时威胁检测平台，不能替代 Intune 设备管理，也不能替代 Entra ID P2 的 PIM 特权审批。**
- **Microsoft Intune Plan 1 = 租户内设备强制执行引擎 (Device Enforcement Authority)**：所有设备合规策略、BitLocker 全盘加密、防火墙与 ASR 攻击面减少规则、应用保护策略（MAM）以及基于设备合规性的条件访问（Device-based CA）均必须在 **Intune** 中定义并强制执行。

---

## 5. DEFEND 五层服务架构、51 项强制准出关卡与 Slide 40 治理铁律 (Chapters 05–07 · Slides 25–40)

![DEFEND 51-Gate State Machine](./assets/gating-matrix.svg)

### 5.1 五大服务层级完整技术规范与 51 项强制准出检查表 (Slides 35–39)

#### Tier 1: `DEFENDBase` — 夯实 Microsoft 365 Business Premium 核心防线 (Slide 27, 35 · 11 项准出标准)
- **核心目标**：100% 兑现客户已购买的 Business Premium 安全价值，消除静默配置错误与技术债。
- **11 项强制准出标准 (`B01–B11`)**：
  - `B01` [Identity]: 全员强制启用 MFA，且任何例外账户均已登记并具备补偿控制。
  - `B02` [Identity]: 基线条件访问（Conditional Access）策略已上线并完成测试。
  - `B03` [Identity]: **旧版身份验证（Legacy Authentication）已被完全阻止，或已通过正式风险接受流程签字豁免**。
  - `B04` [Devices]: 所有受管设备已成功注册至 Microsoft Intune。
  - `B05` [Devices]: 设备合规策略已生效，并配置了不合规设备的自动处置动作。
  - `B06` [Devices]: BitLocker 磁盘加密、主机防火墙与安全启动（Secure Boot）已强制执行。
  - `B07` [Devices]: Microsoft Defender for Business 已完成全量终端部署且传感器遥测上报正常。
  - `B08` [Email]: Defender for Office 365 Plan 1（Safe Links、Safe Attachments、反钓鱼策略）已激活。
  - `B09` [Email]: 邮件流保护策略已验证通过，高风险自动转发规则已受控阻断。
  - `B10` [Visibility]: Microsoft 365 Lighthouse 已完成租户接入并启用基线态势监控。
  - `B11` [Governance]: **客户风险登记册（Risk Register）已建立，所有残余风险与例外项均已记录并由客户签字确认**。

#### Tier 2A: `DEFENDSecurity` — 进阶身份、终端、邮件与云应用主动防御 (Slide 28, 36 · 12 项准出标准)
- **前置条件**：`DEFENDBase` (`11/11`) 达标 + **Microsoft Defender Suite** 附加组件。
- **12 项强制准出标准 (`S01–S12`)**：
  - `S01` [Identity]: 基于登录风险与用户风险的条件访问策略（Entra ID P2 Risk-based CA）已上线生效。
  - `S02` [Identity]: **Privileged Identity Management (PIM)** 已针对所有管理员角色启用（消除常驻全局管理员）。
  - `S03` [Identity]: 定期访问评审（Access Reviews）已针对特权组与关键业务组配置运行。
  - `S04` [Endpoint]: Defender for Endpoint Plan 2 高级威胁狩猎与自动调查修复（AIR）已启用。
  - `S05` [Endpoint]: 威胁与漏洞管理（TVM）修复工作流已建立并纳入月度运营。
  - `S06` [Endpoint]: 终端告警已完成调优，消除重复/良性噪音告警。
  - `S07` [Email]: Defender for Office 365 Plan 2 高级钓鱼防护与自动调查已上线。
  - `S08` [Email]: 钓鱼攻击模拟训练（Attack Simulation Training）已按计划周期性开展。
  - `S09` [Cloud]: Defender for Cloud Apps 已部署，完成 OAuth 应用治理与 Shadow IT 风险控制。
  - `S10` [Hybrid]: 针对存在本地 Active Directory 的混合环境，Defender for Identity (MDI) 传感器已部署并完成校准。
  - `S11` [Operations]: 安全告警分类分级、升级路径与 SLA 响应所有权已明确定义。
  - `S12` [Operations]: 高严重性安全事件已验证具备稳定的高信噪比。

#### Tier 2B: `DEFENDCompliance` — 数据生命周期、内部风险与法务审计治理 (Slide 29, 37 · 11 项准出标准)
- **前置条件**：`DEFENDBase` (`11/11`) 达标 + **Microsoft Purview Suite** 附加组件。
- **11 项强制准出标准 (`C01–C11`)**：
  - `C01` [Posture]: Microsoft Purview Compliance Manager 基线评估已完成。
  - `C02` [Posture]: 优先监管法规映射（如 GDPR、ISO 27001、NIS2、HIPAA、行业规范）已与客户对齐。
  - `C03` [Insider Risk]: Insider Risk Management（内部风险管理）策略已配置并上线。
  - `C04` [Insider Risk]: **内部风险告警审核工作流已与客户 HR、法务及隐私保护边界完成正式对齐**。
  - `C05` [Insider Risk]: 针对高风险角色的离职数据窃取与敏感数据外发检测已启用。
  - `C06` [Audit]: **Audit (Premium)** 已启用，保留周期已按客户监管要求完成扩展。
  - `C07` [Investigation]: **eDiscovery (Premium)** 工作流（案件管理、法律保全 Legal Hold、审查集）已配置并完成演练验证。
  - `C08` [Records]: 关键数据域的保留标签（Retention Labels）与生命周期自动处置策略已生效。
  - `C09` [Records]: 处置审查（Disposition Reviews）与合规证据导出机制已建立。
  - `C10` [Governance]: 合规管理角色与最小权限职责分离（RBAC Role Separation）已落实。
  - `C11` [Governance]: 合规态势报告模板与面向管理层/监管机构的汇报节奏已确立。

#### Tier 3: `DEFENDComplete` — 安全与合规跨域融合运营态 (Slide 30, 38 · 8 项准出标准)
- **前置条件**：同时具备 **Defender Suite + Purview Suite**，且 `DEFENDSecurity` 与 `DEFENDCompliance` 全部准出。
- **8 项强制准出标准 (`M01–M08`)**：
  - `M01` [Coverage — 复合门禁]: **`DEFENDSecurity` 全部 12 项准出标准均已满足**。
  - `M02` [Coverage — 复合门禁]: **`DEFENDCompliance` 全部 11 项准出标准均已满足**。
  - `M03` [Signal Quality]: 安全告警与合规告警均已完成降噪调优，信噪比达到 SOC 接入标准。
  - `M04` [Signal Quality]: 假阳性抑制规则与例外白名单已完成文档化并纳入版本控制。
  - `M05` [Governance]: 统一风险登记册已定期更新，同时涵盖网络安全威胁与数据合规风险。
  - `M06` [Governance]: 季度业务复盘（QBR）与高管姿态汇报节奏已稳定运行。
  - `M07` [Operations]: 安全团队与法务/合规团队之间的跨领域事件升级与协同调查路径已定义。
  - `M08` [Reporting]: 客户级与跨租户（Lighthouse）态势仪表盘已实现常态化运营监控。

#### Tier 4: `DEFENDExtend` — Microsoft Sentinel SIEM/SOAR 与 Security Copilot 托管 SOC (Slide 31, 39 · 9 项准出标准)
- **前置条件**：**必须先完成 `DEFENDComplete`（累计 42 项准出标准）** + **Microsoft Sentinel**（可选叠加 **Microsoft Security Copilot**）。
- **9 项强制准出标准 (`E01–E09`)**：
  - `E01` [Foundations — 复合硬锁]: **`DEFENDComplete` 全部准出标准均已满足（硬性门槛）**。
  - `E02` [SIEM]: Microsoft Sentinel 工作区已部署，且 Log Analytics RBAC 权限与数据保留策略已加固。
  - `E03` [Detection]: 核心数据源（Defender XDR、Entra ID、Purview、关键第三方日志）已接入并完成归一化解析。
  - `E04` [Detection]: 自定义分析规则（Analytics Rules）已部署并针对客户业务环境完成调优。
  - `E05` [Response]: 自动化响应剧本（Logic Apps SOAR Playbooks）已完成测试并上线运行。
  - `E06` [SOC]: 事件分类分级、升级矩阵、24x7/8x5 SLA 响应时效与客户沟通机制已签署生效。
  - `E07` [SOC]: Microsoft Sentinel 与 Microsoft Defender XDR 双向事件同步与统一调查已验证。
  - `E08` [AI]: **若客户或合作伙伴启用了 Microsoft Security Copilot，其辅助研判、KQL 狩猎与事件摘要用例已完成安全审查与验证**。
  - `E09` [Validation]: 已通过紫队桌面推演（Tabletop Exercise）或实景模拟告警完成端到端检测与响应闭环验证。

### 5.2 Slide 40 硬性治理铁律的形式化表达
Slide 40 定义了两条不可妥协的工程治理公理：
1. **跨层演进门禁公理**：任何客户在未满足当前层级全部准出标准（或未针对个别遗留项签署包含**补偿控制**、**问责人**与 **$\le 90$ 天季度复核周期**的正式风险接受单）之前，不得进入下一 DEFEND 层级。
2. **Sentinel 接入硬锁公理**：**除非 `DEFENDComplete` 控制项已全部就位，否则严禁激活 `DEFENDExtend`（Microsoft Sentinel）**。这从根本上杜绝了将未经调优的终端/邮件/身份告警直接倾倒进 SIEM 的行业反模式。

---

## 6. 附录 B 深潜：4 层 Purview-as-a-Service 与 Copilot / AI 数据治理蓝图 (Chapter 10 · Slides 47–51)

针对合作伙伴普遍面临的“Purview 组件过多、难以向中小企业解释清楚商业价值”的挑战，Playbook 附录 B 将数据安全与合规能力重构为 **4 个递进式服务包**，把“合规负担”转化为“安全启用 Microsoft 365 Copilot 的前置赋能器”：

| 服务层级 | 英文名称 | 授权需求 | 敏感度标签能力 | DLP 覆盖范围 | 审计与电子发现 | 内部风险与 AI 治理 (DSPM for AI / Copilot) |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| **Tier 1** | **Data Protect** *(基线数据保护)* | Business Premium | 手动、默认与强制标签 | 邮件 (Exchange) 与文件 (SharePoint/OneDrive) | 基础版（90 天审计、标准 eDiscovery） | 不包含 IRM；基于 Compliance Manager 完成基础自评 |
| **Tier 2** | **Data Govern** *(自动化分类与治理)* | BP + **Purview Suite** | **自动敏感度标签**（基于内容与分类器） | 扩展至 **终端 (Endpoint DLP)**、**Teams 聊天**与云应用 | **高级版 (Audit & eDiscovery Premium)** | **启用 Insider Risk Management**；自动化合规持续评估 |
| **Tier 3** | **Data Control** *(Copilot 与 AI 准备度)* | BP + **Purview Suite** | **AI 关联标签**与可训练分类器驱动 | **+ AI 交互面 (DLP for Microsoft 365 Copilot)** | AI 提示词/响应取证搜索与高价值审计事件 | **启用 DSPM for AI + Adaptive Protection**，治理 Copilot 过曝风险 |
| **Tier 4** | **Data Assure** *(全托管持续合规)* | BP + Purview + **合作伙伴托管服务** | 合作伙伴全生命周期代管与异常复核 | + 持续策略调优与新型外发通道封堵 | 托管合规报告、法务保全与监管协查代办 | 托管内部风险研判、月度姿态报告与季度治理委员会复盘 |

---

## 7. Microsoft Security Partner Toolkit for SMB —— 五阶段全链路执行与 6 大官方链接资产深度拆解

如果说《DEFEND Partner Playbook》定义了五层托管安全的**顶层设计（What & Why）**，那么 **《Microsoft Security Partner Toolkit for SMB — Accelerate Security and AI Readiness Engagements》** 则提供了从首次客户拜访、范围界定、SOW 报价、详细规划到 PowerShell 7+ 自动化脚本落地的**完整工程工具箱（How）**。

![SMB Partner Toolkit 5-Stage Lifecycle](./assets/partner-toolkit-lifecycle.svg)

### 7.1 客户交付全生命周期与 6 大官方 `aka.ms` 链接解析总表

| 交付阶段 (Lifecycle Stage) | 核心工具包资产名称 | 官方短链 (`aka.ms`) | 解析后目标地址 / 微软官方开源仓库 | 资产形态与实测规模 |
| :--- | :--- | :--- | :--- | :--- |
| **Stage 1: 初次客户沟通**<br>*(Initial Conversations)* | **行业特定信息保护一页纸**<br>*(Industry-Specific IP One-Pagers)* | `https://aka.ms/MIP-Industry-OnePagers` | `Industry-Specific Information Protection Guides.zip` (`1.01 MB`) | **7 份双页行业指南 PDF（共 14 页）**：覆盖消费品、教育 [新增]、金融保险、医疗、制造分销、非营利 [新增]、专业服务；含 30/60/90 天路线图与 **8 级 DEFEND 敏感度标签体系** |
| **Stage 2: 发现与范围界定**<br>*(Discovery & Scoping)* | **数据安全引导助手**<br>*(Data Security Guided Assistant)* | `https://aka.ms/DataSecurityAssistant` | 在线应用: `https://microsoft.github.io/DataSecurityGuidedAssistant/`<br>开源仓库: `https://github.com/microsoft/DataSecurityGuidedAssistant` (`v2.0.1572`) | 纯前端零后端交互式决策树（单文件 `570 KB`，严格 CSP），包含 **Labeling Tool**、**DLP Tool** 与 **Combined Flow**，支持 8 大行业、8 大地区、6 档授权与 8 级/4 级标签模型切换及 Word/CSV 导出 |
| **Stage 3: 方案与报价生成**<br>*(Proposal Development)* | **Purview 数据安全 SOW 生成器**<br>*(Purview SOW Generator)* | `https://aka.ms/SOW-Generator` | 在线应用: `https://microsoft.github.io/SOWGenerator/`<br>开源仓库: `https://github.com/microsoft/SOWGenerator` (MIT License) | 浏览器端多步骤工作说明书（SOW）生成器，涵盖 **22 项模块化服务**（Priority 1 基础 9 项、Priority 2 进阶 1 项、Priority 3 高阶与 AI 护栏 12 项）+ 托管服务目录与加密 JSON 导出 |
| **Stage 4: 规划与实施手册**<br>*(Planning & Implementation)* | **SMB 最佳实践安全部署指南**<br>*(Security SMB Deployment Guides)* | `https://aka.ms/Security_SMBDeploymentGuides` | `Best Practice Security Deployment Guides for SMB.zip` (`31.82 MB`) | **6 本完整技术部署手册 PDF（总计 360 页）**：数据安全（92 页）、身份保护（90 页）、邮件与协作（52 页）、设备安全（51 页）、设备管理（40 页）、SaaS 安全（35 页） |
| **Stage 5: 自动化部署配置**<br>*(Deployment & Configuration)* | **PowerShell 最佳实践部署脚本**<br>*(SMBBestPracticeTool)* | `https://aka.ms/Deploy-Scripts` | 文档门户: `https://microsoft.github.io/BestPractice_Deploy-Scripts/`<br>开源仓库: `https://github.com/microsoft/BestPractice_Deploy-Scripts` | 基于 **PowerShell 7+ (`pwsh.exe`)** 的 4 大工作负载幂等自动化套件（`Products/Purview`、`Products/Entra`、`Products/Intune`、`Products/Defender`），支持 GDAP、`-WhatIf`、安全门禁与 HTML/JSON 报告 |
| **顶层总览与反馈闭环**<br>*(Umbrella Playbook)* | **SMB 安全合作伙伴工具包总览与问卷** | `https://aka.ms/SecurityPartnerToolkit_Playbook`<br>`https://aka.ms/SecurityPartnerToolkit-Survey` | `Partner Security Toolkit for Enabling SMB.pdf` & Microsoft Customer Voice | 端到端五阶段合作伙伴作战手册与产品团队反馈通道 |

---

### 7.2 资产一深潜：7 大行业信息保护一页纸与 8 级 DEFEND 敏感度标签体系 (`aka.ms/MIP-Industry-OnePagers`)

压缩包 `Industry-Specific Information Protection Guides.zip` 包含 **7 份两页装 PDF 行业剧本（共 14 页）**，每一份均精确映射到垂直行业的最高风险数据资产、内置敏感信息类型（SIT）与法规要求：

| # | 行业指南 PDF 文件名 | 覆盖子行业 (Sub-Verticals) | 高风险数据资产与核心业务场景 | 关键法规与内置 SIT / 自定义标识符 |
| :---: | :--- | :--- | :--- | :--- |
| **1** | `Consumer_Goods_SMB_Purview_One_Pager.pdf` (2p) | 食品饮料、美妆个护、服饰软线、消费电子、家居日化 (CPG) | 客户导出表、零售商联合商业计划 (JBP)、促销定价表、产品配方、代工厂 (Co-manufacturer) 规格书、FDA 召回文件 | GDPR / CCPA / PCI-DSS；信用卡号、税号、订单号与 SKU 配方标识 |
| **2** | `Education_SMB_Purview_One_Pager_MVP.pdf` (2p, *New*) | K-12 私立学校、高等教育、学前教育、职业培训、教育科技 (EdTech) | 学生档案、成绩单、IEP/504 特殊教育计划、助学金与财务记录、未成年人保护 (Safeguarding) 档案、董事会材料 | FERPA / COPPA / 州学生隐私法；SSN、学生学号 (Student ID)、医疗健康记录 |
| **3** | `Financial_Services_Insurance_SMB_Purview_One_Pager.pdf` (2p) | 资本市场/证券、银行业、直保机构、保险经纪、公共财政 | KYC 开户材料、贷款审批卷宗、理赔与核保文件、精算模型、反洗钱 (AML) 申报、监管机构函件 | GLBA / PCI-DSS / SOX / FCA；ABA 路由号、IBAN、SWIFT、信用卡号、保单/理赔号 |
| **4** | `Healthcare_SMB_Purview_One_Pager.pdf` (2p) | 医疗机构、生物医药、医保支付方 (Payor)、医疗器械、辅助医疗 | 患者接诊表、转诊单、实验室检验报告、临床试验数据、不良事件报告、医保编码与账单 | HIPAA / HITECH / FDA 21 CFR Part 11；PHI、患者病历号 (MRN)、NPI、医保号 |
| **5** | `Manufacturing_Distribution_SMB_Purview_One_Pager.pdf` (2p) | 化工材料、农业科技、工业机械、高科技电子、半导体 | CAD 工程图纸、物料清单 (BOM)、化学品配方、安全数据表 (SDS)、OEM/供应商技术规范、质量管理 (QMS) 记录 | ITAR / EAR / ISO 9001 / TISAX；零件编号 (Part/BOM ID)、专利与图纸编号 |
| **6** | `Nonprofit_SMB_Purview_One_Pager_MVP.pdf` (2p, *New*) | 社会服务、基金会与拨款机构、社区公益、行业协会、国际 NGO 与救援 | 捐赠人档案、大额捐赠协议、受助弱势群体个案卷宗、Form 990 与审计底稿、资助方合规报告 | 慈善监管法规 / GDPR / HIPAA；捐赠人 ID、银行账号、弱势群体保护记录 |
| **7** | `Professional_Services_SMB_Purview_One_Pager.pdf` (2p) | 会计与税务、管理咨询、IT 服务、外包服务、建筑与工程设计 | 客户尽职调查包、税务底稿、并购 (M&A) 备忘录、律师委托特权文件 (Privilege logs)、外部联席顾问协作区 | 行业保密准则 / AICPA / 律协规范；案件/项目编号 (Matter/Engagement ID)、税号 |

#### 核心架构创新：包含 LOB 免加密异常分支的“8 级 DEFEND 对齐敏感度标签体系”
在真实中小企业交付中，一刀切地对所有“机密/高度机密”文件启用 Azure RMS 加密，往往会导致 ERP、EHR（电子病历）、SIS（学生信息系统）、MRP（物料需求计划）或核心银行批处理任务无法读取文件而崩溃。为此，7 份行业一页纸与引导助手共同定义了 **8 级 DEFEND 对齐标签分类法**，专门引入第 5 级与第 8 级 **`INTERNAL EXCEPTION`（内部免加密异常子标签）**：

| 标签序号 | 标准标签路径 (Label Hierarchy) | 加密与权限策略 | 外部共享策略 | 默认应用范围与治理规则 |
| :---: | :--- | :--- | :--- | :--- |
| **1** | `PUBLIC` | 无加密 | 允许外部共享 | 公开宣传册、新闻稿、公开网站资料 |
| **2** | `GENERAL` | 无加密（仅内部页眉/页脚标记） | 允许受控外发 | **默认邮件标签 (Default Email Label)**；日常一般业务沟通 |
| **3** | `CONFIDENTIAL \ ALL EMPLOYEES` | **强制加密 + 视觉标记**（仅限租户内全员访问） | **禁止外部共享** | **默认文档与站点标签 (Default File/Site Label)**；内部业务文档 |
| **4** | `CONFIDENTIAL \ SPECIFIC PEOPLE` | **具名用户加密 (Named-User Permissions)** | 仅限受控外部协作方 | 与受信供应商、律所、经销商、家长的受控外部共享 |
| **5** | **`CONFIDENTIAL \ INTERNAL EXCEPTION`** | **仅视觉标记，不启用加密 (Marking Only, No Encryption)** | **禁止外部共享** | **专为加密会破坏 ERP/EHR/SIS/MRP 集成的 LOB 工作流设计；强制要求书面业务理由并每季度（90 天）复核** |
| **6** | `HIGHLY CONFIDENTIAL \ ALL EMPLOYEES` | **强加密 + 水印 + 禁止复制/打印/非受管共享** | **严禁外部访问** | 薪资表、PHI 病历、未成年人保护、AML 反洗钱、核心配方与源代码 |
| **7** | `HIGHLY CONFIDENTIAL \ SPECIFIC PEOPLE` | **显式具名用户强加密**（推荐绑定 SIT 自动标签） | 仅限指定审计/监管人员 | 监管问询回复、并购尽调包、法律保全卷宗、董事会绝密文件 |
| **8** | **`HIGHLY CONFIDENTIAL \ INTERNAL EXCEPTION`** | **仅视觉标记，不启用加密 (Marking Only, No Encryption)** | **严禁外部访问 + DLP 严密监控** | **专为强加密会导致 QMS 质量体系、临床合规或监管报送工具失效的极特殊场景设计；必须经 IT 负责人签字批准并每季度审计** |

---

### 7.3 资产二深潜：Data Security Guided Assistant (`aka.ms/DataSecurityAssistant`)

- **托管地址与版本**：`https://microsoft.github.io/DataSecurityGuidedAssistant/`（开源仓库 `microsoft/DataSecurityGuidedAssistant`，版本 `v2.0.1572`）。
- **零后端安全架构**：采用单文件静态 HTML 应用架构（`index.html`，`570 KB`），配置了极其严格的 `Content-Security-Policy: default-src 'none'` 与脚本/样式 SHA-256 哈希校验，所有客户访谈输入均保留在本地浏览器内存中，零外部遥测外发。
- **三大交互式引导工作流**：
  1. **Labeling Tool（标签决策树）**：通过业务场景问答引导顾问与客户确定正确的敏感度标签，实时渲染 **Reference Cards（参考卡片）**、**Explicit Exceptions（显式免加密异常条件）** 与 **Industry Examples（行业实例）**。
  2. **DLP Tool（DLP 范围界定引擎）**：采集客户授权档位（*Business Basic/Standard*、*Business Premium/E3*、*BP/E3 + Defender Suite*、*BP/E3 + Purview Suite*、*E5 / BP+DS+PS*、*E7*）、附加组件准备度（*是否已部署 MDE 终端*、*是否需要自动标签*、*是否已采购或计划部署 M365 Copilot*）、办公与设备形态以及敏感信息类型（SIT）簇，自动生成分阶段 DLP 实施蓝图。
  3. **Combined Flow（标签 → DLP 联动流）**：先完成敏感度标签体系设计（支持在 **8 级 DEFEND 模型** 与 **4 级简化模型** 间一键切换），随后将确认的标签集合直接注入 DLP 策略规划器，并支持一键导出为 Word 或 CSV 交付件。

---

### 7.4 资产三深潜：Microsoft Purview Data Security SOW Generator (`aka.ms/SOW-Generator`)

- **托管地址与开源协议**：`https://microsoft.github.io/SOWGenerator/`（开源仓库 `microsoft/SOWGenerator`，MIT License）。
- **核心功能**：将客户探索阶段的输入（席位规模 `1–50` / `51–150` / `151–300`、当前许可证、MIP/DLP 成熟度、项目周期 `2 周` 至 `>6 个月托管服务`）自动转化为包含工作量估算、里程碑、可勾选交付物与责任矩阵（RACI）的标准 **工作说明书（SOW）**，并支持使用口令加密（AES-GCM）导出项目 JSON 状态。
- **22 项模块化服务目录（横跨 Priority 1 / Priority 2 / Priority 3）**：
  - **Priority 1 — Foundation（基于 M365 Business Premium 即可交付，共 9 项工作流）**：
    1. `Enable Audit Logging`（开启统一审计日志）
    2. `Sensitivity Label Taxonomy Design`（敏感度标签分类体系设计）
    3. `Sensitivity Label Creation & Configuration`（标签创建、加密与水印配置）
    4. `Label Policy Deployment`（标签发布策略部署）
    5. `Mandatory & Default Label Enforcement`（强制标签与默认标签策略）
    6. `End-User Training & Adoption`（终端用户培训与采纳推广）
    7. `Enable Sensitivity Labels for SharePoint & OneDrive`（开启 SPO/OD 容器与文件标签支持）
    8. `Container Label Configuration`（配置 Teams、SharePoint 站点与 M365 组容器标签）
    9. `DLP Policies: Exchange, SharePoint & OneDrive`（核心工作负载 DLP 模拟、调优与告警看板）
  - **Priority 2 — Intermediate（治理与生命周期就绪，共 1 项核心工作流）**：
    10. `Retention Policy: Exchange Online`（Exchange 保留策略，并可扩展至 SharePoint、OneDrive 与 Teams）
  - **Priority 3 — Advanced & AI Guardrails（需解锁 Purview Suite 附加组件 🔒，共 12 项高阶工作流）**：
    11. `Custom Sensitive Information Types (SITs)`（正则表达式、关键字字典与 Exact Data Match 精确数据匹配）
    12. `Client-Side Auto-Labeling`（Office 客户端实时自动打标）
    13. `Service-Side Auto-Labeling Policies`（SharePoint/OneDrive/Exchange 静态数据自动打标模拟与强制）
    14. `Label-Based Encryption & Azure RMS`（深度权限管理与外部撤销控制）
    15. `Trainable Classifiers`（基于机器学习的可训练分类器）
    16. `Content Explorer & Activity Explorer`（敏感数据分布与用户操作行为猎寻）
    17. `On-Premises Purview Scanner`（本地文件服务器与 SMB 共享扫描器部署）
    18. `Double Key Encryption (DKE)`（双密钥加密）
    19. `MIP SDK / LOB Application Integration`（业务系统 SDK 集成）
    20. `Advanced Analytics & Compliance Reporting`（高管合规报表）
    21. **扩展与 AI 护栏工作流（Extended & AI Guardrails — 包含 5 大专项子能力）**：
        - **DLP for Endpoints**：管控 Windows/macOS 终端上的复制、打印、USB 拷贝与浏览器上传。
        - **DLP for Teams**：实时拦截 Teams 内部及外部访客聊天/频道中的敏感信息发送。
        - **DLP for Copilot（内部受控 AI 护栏）**：**配置两条专属 Purview DLP 规则（一条基于 SIT 敏感信息类型，一条基于敏感度标签），并在正式阻断前对 Copilot 提示词（Prompts）与生成响应（Responses）执行全量模拟测试**。
        - **DLP for Microsoft Edge / Inline Web Traffic（外部 Shadow AI 护栏）**：**通过 Edge for Business 内联流量控制，阻止员工将公司敏感数据粘贴或上传至 ChatGPT、Gemini 等未受管第三方生成式 AI 网站**。
        - **Activate DSPM (Data Security Posture Management)**：**全面盘点租户内的过度共享（Oversharing）风险与 AI 准备度态势**。
    22. **Managed Services（持续托管服务包）**：提供 **30 天上线护航 (Hypercare)** 与 **持续托管服务**（月度健康监控、季度策略调优、事件响应支持），直接对应 Playbook 的 `DEFENDCompliance` 与 `Data Assure`（Purview Tier 4）。

---

### 7.5 资产四深潜：6 本 SMB 最佳实践安全部署指南（总计 360 页 PDF · `aka.ms/Security_SMBDeploymentGuides`）

压缩包 `Best Practice Security Deployment Guides for SMB.zip` (`31.82 MB`) 提供了 **6 本总计 360 页的图文步进式工程实施手册**。每本手册均严格遵循 `前置条件 (Prerequisites) → Priority 1 (Must-do 基线必做) → Priority 2 (Enhanced 增强保护) → Priority 3 (Strengthened 强化控制) → Advanced Security (Defender / Purview Suite 高阶升级)` 的统一工程结构：

| 序号 | 部署指南 PDF 名称 | 页数 | 版本日期 | 核心章节与页码分布 | 对应 DEFEND 层级 |
| :---: | :--- | :---: | :---: | :--- | :--- |
| **1** | **Data Security Deployment Guide for Small Business** (`Data Security Deployment Guide for Small Business_Final.pdf`) | **92 页** | 2026-06-24 | • **Priority 1 "Good"** (pp. 9–34)：审计开启、敏感度标签、SPO/OD 标签启用、核心 DLP<br>• **Priority 2 "Better"** (pp. 35–41)：保留策略与数据生命周期管理<br>• **Priority 3 "Advanced"** (pp. 42–90)：自动标签、Endpoint DLP、Teams DLP、**DLP for Copilot**、**Edge 内联 Web AI 阻断**、**DSPM for AI**、Insider Risk | `DEFENDBase` → `DEFENDCompliance` & Purview Tiers 1–3 |
| **2** | **Identity Protection Best Practice Deployment** (`Identity Protection Best Practice Deployment_Final030626.pdf`) | **90 页** | 2026-03-06 | • **Entra ID P1 Priority 1 & 2** (pp. 8–31)：Break-glass 应急账户、MFA、SSPR、阻止旧版认证、基线条件访问<br>• **Entra ID P2 Best Practices** (pp. 32–70)：基于登录风险与用户风险的 CA、**PIM 特权身份管理**、访问评审<br>• **Defender for Identity (MDI)** (pp. 71–87)：本地 AD 传感器部署与混合身份威胁检测 | `DEFENDBase` → `DEFENDSecurity` |
| **3** | **Email & App + Collaboration Protection Best Practice Deployment** (`Email & App + Collaboration Protection Best Practice Deployment_Final030926.pdf`) | **52 页** | 2026-03-16 | • **MDO Plan 1 Priority 1–3 & Advanced** (pp. 9–41)：预设安全策略、反钓鱼 (Anti-Phishing)、Safe Links、Safe Attachments（覆盖邮件、Teams、SharePoint、OneDrive）、SPF/DKIM/DMARC<br>• **MDO Plan 2 Collaboration Security** (pp. 42–51)：自动调查与修复 (AIR)、Threat Explorer 威胁猎寻、Attack Simulation 钓鱼模拟训练 | `DEFENDBase` → `DEFENDSecurity` |
| **4** | **Device Security Best Practice Deployment** (`Device Security Best Practice Deployment_Final030926.pdf`) | **51 页** | 2026-03-16 | • **Prerequisites & Onboarding** (pp. 8–13)<br>• **Defender for Business Priority 1 & 2** (pp. 14–41)：NGAV 下一代防病毒、ASR 攻击面减少规则、勒索软件防护、网络保护、TVM 漏洞管理<br>• **Defender for Endpoint Plan 2** (pp. 42–52)：高级狩猎、6 个月告警保留、威胁情报分析 | `DEFENDBase` → `DEFENDSecurity` |
| **5** | **Device Management Best Practice Deployment** (`Device Management Best Practice Deployment_Final030726.pdf`) | **40 页** | 2026-03-16 | • **Mobility Management Approach** (p. 7)<br>• **Intune Priority 1–3 Tasks** (pp. 8–37)：设备注册限制、默认与自定义合规策略、MAM 应用保护策略、BitLocker 加密、Windows 更新环、M365 应用部署<br>• **Device-Based Conditional Access** (p. 38) | `DEFENDBase` |
| **6** | **SaaS Security Best Practice Deployment** (`SaaS Security Best Practice Deployment_Final030926.pdf`) | **35 页** | 2026-03-16 | • **Shadow IT Discovery via MDE** (pp. 9–13)：打通 MDE 与 Defender for Cloud Apps 自动发现影子应用<br>• **App Discovery & OAuth Governance** (pp. 14–25)：应用发现告警、高权限 OAuth 应用审计与吊销<br>• **Cross-SaaS Data & Threat Protection** (pp. 26–34)：跨 SaaS 敏感数据防护与异常会话阻断 | `DEFENDSecurity` → `DEFENDComplete` |

---

### 7.6 资产五深潜：PowerShell 7+ 自动化部署工具包 `SMBBestPracticeTool` (`aka.ms/Deploy-Scripts`)

开源仓库 `https://github.com/microsoft/BestPractice_Deploy-Scripts`（文档门户 `https://microsoft.github.io/BestPractice_Deploy-Scripts/`）将上述 360 页指南中的基础配置转化为可重复、可审计、幂等的 **PowerShell 7+ (`pwsh.exe`)** 自动化工程代码：

1. **核心运行时与多租户安全架构**：
   - **强制 PowerShell 7+ 运行时**：在 Windows PowerShell 5.1 下会立即主动报错退出（因为 Exchange Online v3 REST 与 Microsoft.Graph SDK 依赖 .NET Core 连接池与现代 TLS API），同时通过 `Import-Module Microsoft.Online.SharePoint.PowerShell -UseWindowsPowerShell` 将旧版 SharePoint 模块隔离在隐藏的 PS 5.1 子进程中，彻底避免 MSAL DLL 程序集冲突。
   - **原生支持 MSP GDAP 委派管理**：支持直接管理员模式（`-TenantAdminUpn`）与合作伙伴委派模式（`-DelegatedOrganization <customer.onmicrosoft.com>`），并在每次写入前通过 `Get-MgOrganization` 校验目标租户身份。
   - **全局 `-WhatIf`、瞬态重试与 HTML/JSON 证据包**：所有变更均封装在 `Invoke-WithTransientRetry.ps1` 中，执行后执行回读校验（Post-Write Readback Verification），并自动生成 `Reports/<product>-run-report.html` 与 `.json` 审计证据包。
2. **四大产品线自动化套件与安全门禁 (`Safety Gates`)**：
   - **`Products/Purview/` (`Deploy-PurviewBestPractice.ps1`)**：幂等部署敏感度标签与核心 DLP 策略；仓库内随附 **《Day-30 DLP 模拟准出手册》(`docs/DLP-Simulation-Exit-Runbook.md`)**、**《7 年默认保留风险提示》(`docs/Retention-Default-Risk.md`)** 与 **《终端用户推广邮件模板 (`T-7` / `T-0` / `T+30`)》**，强制要求经过 30 天模拟期与误报清理后方可切入生产阻断。
   - **`Products/Entra/` (`Deploy-EntraBestPractice.ps1`)**：内置 **13 个标准化条件访问 JSON 策略模板**（阻止设备代码流 `block-device-code-flow.json`、阻止旧版认证 `block-legacy-authentication.json`、阻止不受支持设备平台、禁止持久化浏览器会话、保护安全信息注册、要求批准的客户端应用、要求合规设备或 MFA、要求管理门户 MFA、要求管理员 MFA、要求全员 MFA、要求 Azure 管理平面 MFA、要求访客 MFA、要求管理员使用抗钓鱼 MFA `require-phishing-resistant-mfa-admins.json`）。**关键安全门禁：全部 13 条策略默认以 `Report-Only`（仅报告模式）创建，脚本在写入前强制检查是否存在真实的永久 Global Administrator 应急（Break-Glass）排除账户，且绝不自动关闭 Security Defaults。**
   - **`Products/Intune/` (`Deploy-IntuneBestPractice.ps1`)**：自动化 6 项基线设备任务，并将可能影响生产访问的高风险变更（默认合规策略、设备注册限制、关联 CA 策略）锁定在显式的 `-IncludeHighRisk` 开关之后。
   - **`Products/Defender/` (`Deploy-DefenderBestPractice.ps1`)**：默认执行只读预检（`Setup-DefenderPreflight.ps1`、权限规划与配置差距分析），并提供经过试点验证的 **ASR 攻击面减少规则 Audit（审计模式）下发通道**（`DefenderAsrConfiguration.ps1` + `DefenderSafetyGates.ps1`），将具有潜在业务中断风险的强制阻断保留为 `GuidedOnly` 人工受控变更。

---

## 8. 架构师视角：从 M365 DEFEND 与 SMB 工具包到云原生 Agentic AI 安全架构的跨栈映射

![Purview 4-Tier to Cloud-Native Agentic AI Security Bridge](./assets/purview-ai-bridge.svg)

在本研究仓库（`turbo998/ai-research-public`）的四支柱体系中，**DEFEND Partner Playbook + SMB Security Partner Toolkit** 构成了 **企业租户与生产力侧（M365 / SaaS Plane）** 的零信任与 AI 治理基石，并与 **Pillar 01（Azure 云原生智能体基础设施）** 的运行时沙箱控制形成严密的 1:1 纵深防御映射：

| 安全控制维度 | M365 租户侧控制 (`DEFEND Playbook` + `SMB Partner Toolkit`) | 云原生 Agent 运行时侧控制 (`Pillar 01 Azure Agent Infra`) | 协同防御目标 |
| :--- | :--- | :--- | :--- |
| **1. 身份与最小权限治理** | **Entra ID P1/P2**：13 个标准化 CA 模板、登录/用户风险策略、**PIM 即时特权激活**、访问评审 (`S01–S03`) | **Microsoft Entra Agent ID**：On-Behalf-Of (OBO) 双重身份归因（User + Agent Identity）、短期令牌与工作负载身份联邦 | 防止凭据盗用、横向移动与智能体越权代理（Confused Deputy） |
| **2. 执行环境与计算隔离** | **Intune Plan 1 + Defender for Business / MDE P2**：设备合规强制、BitLocker、ASR 攻击面减少规则、EDR 行为阻断 (`B04–B07`, `S04–S06`) | **AKS Kata Containers / Confidential Containers (AMD SEV-SNP) & E2B Firecracker microVMs**：硬件级虚拟化内核隔离 + **Tetragon eBPF** 系统调用阻断 | 隔离不可信代码执行与工具调用，阻断容器逃逸与宿主机污染 |
| **3. 内部受控 AI 与外部 Shadow AI 双重数据护栏** | **Purview Tier 3 (`Data Control`) + SOW Priority 3**：8 级敏感度标签（含 LOB 免加密异常分支）、**DLP for Copilot（SIT+标签双规则模拟）**、**Edge 内联网页 DLP（拦截向 ChatGPT/Gemini 粘贴上传）**、**Activate DSPM** | **Azure APIM AI Gateway + Microsoft Purview SDK + Web IQ**：实时提示词/工具输出脱敏、MCP/A2A 协议载荷审计、恶意域名/高危 URL 电路熔断器 | 内部防止 Copilot 越权检索敏感文件，外部阻断网页端 Shadow AI 泄密与间接提示词注入 |
| **4. 集中式 SIEM/SOAR 与 AI 辅助 SOC 运营** | **DEFENDExtend (`E01–E09`)**：在完成 `DEFENDComplete` 降噪后接入 **Microsoft Sentinel + Defender XDR + Security Copilot** | **Azure Monitor + Sentinel + Prometheus/Grafana**：汇聚智能体推理轨迹、沙箱生命周期指标、APIM 网关拦截日志与自动隔离剧本 | 在确保高信噪比的前提下，实现跨生产力租户与云原生智能体集群的统一可观测性与秒级自动遏制 |

---

## 9. 复现实验与确定性验证指南 (Reproducibility & Verification)

本研究目录内置零外部依赖的确定性 Python 验证器与单元测试套件，可一键复现全部 41 项授权能力核算、51 项准出关卡状态机、Slide 40 治理规则门禁以及 7 卡 4:5 视觉评测报告：

```powershell
# 1. 运行确定性单元测试套件（7 项测试：校验页数/章节/能力表/51 项准出关卡/风险接受/Slide 40 硬锁/SMB 工具包目录）
python -m unittest discover -s docs\research\defend-partner-playbook\simulator -p "test_*.py" -v

# 2. 重新生成 verifier-summary.json、report.json、evidence.json、CSV 数据集与中英双语 7 卡 HTML 报告
python docs\research\defend-partner-playbook\simulator\generate_artifacts.py
```

### 目录文件清单 (Artifact Manifest)
- `README.md` / `README.zh-CN.md` / `index.zh.md`：中文深度技术专著（含 DEFEND 53 页全解与 SMB 安全合作伙伴工具包 6 大链接资产深潜）
- `README.en.md` / `index.md`：英文深度技术专著 (English Full Technical Monograph)
- `test-report.md` / `test-report.en.md`：中英双语 7-Card 4:5 视觉基准评测报告（Markdown 版）
- `test-report-cards.html` / `cards.html` / `cards.zh.html`：自包含交互式 7-Card 4:5 视觉卡片组（严格内联 CSS，零外部网络依赖）
- `assets/overview.svg`：DEFEND 五层服务架构、零信任 7 维评估与双运营底座全景图
- `assets/gating-matrix.svg`：51 项强制准出标准（48 项原子控制 + 3 项复合门禁）与 Slide 40 治理状态机图
- `assets/purview-ai-bridge.svg`：附录 B 四层 Purview-as-a-Service 与云原生 Agentic AI 安全架构跨栈映射图
- `assets/partner-toolkit-lifecycle.svg`：Microsoft Security Partner Toolkit for SMB 五阶段执行流、6 大资产与 8 级敏感度标签架构图
- `simulator/defend_tier_readiness_verifier.py` & `simulator/test_defend_tier_readiness_verifier.py`：确定性验证器与单元测试
- `report.json` / `evidence.json` / `evidence/*.csv` / `evidence/verifier-summary.json` / `review.md`：结构化评测数据与 SHA-256 校验清单
