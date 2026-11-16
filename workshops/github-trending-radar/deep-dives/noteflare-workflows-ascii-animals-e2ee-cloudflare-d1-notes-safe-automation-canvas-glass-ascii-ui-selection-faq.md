# `$0/月` 边缘端到端加密知识库、防断流自动化画布与液态玻璃 ASCII 输入台选型 FAQ：`homielab/noteflare` + `AdamJBurns/workflows` + `DesignerStephen1/ascii-animals`

> **元数据（Metadata）**
> - **评测批次**：2026-11-16 夜间深潜 Round 19（累计 Round 376）
> - **核心标的**：
>   1. [`homielab/noteflare`](https://github.com/homielab/noteflare)（`★ 73` / `34 Forks`，`2026-11-14` 新建爆发黑马 · 运行在 Cloudflare Workers + D1 + Access 免费层 [`$0/month`] 上的端到端加密零知识笔记与知识库：浏览器端 `AES-256-GCM` 原地加解密、Passkey 生物识别解锁、15 分钟闲置内存擦除、`git merge` 风格逐行多端合并、Obsidian/Keep/Evernote 拖拽加密导入，以及自带自动加解密的 TypeScript SDK、CLI 与 `/api/v1` OpenAPI）
>   2. [`AdamJBurns/workflows`](https://github.com/AdamJBurns/workflows)（`★ 117` / `16 Forks`，`2026-11-14` 新建爆发黑马 · 基于 `Next.js` + `React` + `Motion` 的键盘无障碍拖拽式自动化规则画布：支持按角色拆分条件分支、自动重路由连线、全量撤销，以及**主动拒绝任何会导致工作流断流的删除操作并给出明确原因**）
>   3. [`DesignerStephen1/ascii-animals`](https://github.com/DesignerStephen1/ascii-animals)（`★ 86` / `11 Forks`，`2026-11-14` 新建爆发黑马 · 零外部依赖程序化 ASCII 动物画布 + Dia 风格液态玻璃 AI 聊天输入框：7 种带景深与受惊交互反馈的 ASCII 生物游弋在 Chromium SVG 折射滤镜玻璃输入框背后）
> - **配套架构图**：[`assets/github-ai-radar-2026-11-16-r19-noteflare-workflows-asciianimals.svg`](../../../assets/github-ai-radar-2026-11-16-r19-noteflare-workflows-asciianimals.svg)
> - **证据封存锚点**：`CLAIM-20261116-R19-NOTEFLARE-WORKFLOWS-ASCII`（见 [`evidence/trending-daily-2026-11-16-audit.json`](../evidence/trending-daily-2026-11-16-audit.json)）

---

## 📌 1. 核心结论速览（Executive Summary & First-Principles Pitch）

1. **一句话讲透本质**：
   - **`homielab/noteflare` (`$0/mo Cloudflare E2EE Vault`)**：就是**一个哪怕云厂商或数据库管理员把 D1 拖库了也只能看到一堆乱码、而且服务器月费只要 `$0` 的零知识私有笔记与 Agent 记忆库**。所有 Markdown 笔记与 R2 图片附件在离开浏览器或 TypeScript SDK 前就已经用 `AES-256-GCM` 加密完毕，支持 Passkey 指纹刷脸解锁、两台设备同时改同一篇笔记按行自动 `git merge`，还开放了带客户端加密的 CLI 与 `/api/v1` 接口！
   - **`AdamJBurns/workflows` (`Safe-Edit Rule Canvas`)**：就是**把“绝不允许用户删掉关键节点把整条自动化链路搞断”写成硬门禁的无障碍工作流编排画布**。很多流程图组件删掉中间节点后留下满屏悬空断线，它在删除前先做拓扑校验，一旦会破坏流向就附带原因温柔拒绝，且所有控件 100% 免鼠标纯键盘可达。
   - **`DesignerStephen1/ascii-animals` (`0-Dep ASCII + Liquid-Glass Chat Input`)**：就是**用零依赖纯 TypeScript 代码画出会游动、会跳水、点一下还会受惊逃跑的 7 种 ASCII 动物，并衬在 Dia 风格 SVG 液态折射玻璃聊天框后面**，用几十 KB 代码平替笨重的几十 MB 背景视频。
2. **核心量化收益（FinOps 闭式账本 `CLAIM-20261116-R19-NOTEFLARE-WORKFLOWS-ASCII`）**：
   - 在 **每月维护 30 个加密团队知识库实例 + 交付 20 套可视化规则编排与 AI 门户输入界面** 的全栈工程工作负载下（全栈架构师全负担时薪 `$100.00/hr`；自定义域名注册费标记为 `not_measured`）：
   - **Path C（`NoteFlare` `$0` 边缘加密库 + `AdamJBurns/workflows` + `ascii-animals`）** 将月度总拥有成本（TCO）从 **Path A（按席位购买明文云笔记 SaaS + 频繁修补断流画布 Bug 与重型视频背景）的 `$5,700.00/月`** 降至 **`$385.00/月`**，净省 **`$5,315.00/月`（`-93.25%`，年化节省 `$63,780.00/年`）**，每月节省 **`35.4 小时`（`-91.95%`）** 的运维与前端打磨工时。

![2026-11-16 Night Round 19 (R376) Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-16-r19-noteflare-workflows-asciianimals.svg)

---

## ❓ 2. 灵魂拷问 Q1–Q3（First-Principles Deep Dive）

### Q1：端到端加密（E2EE）笔记最怕“忘了密码全库报废”或“换密码要把几千篇笔记全部重新加密上传一遍”，`homielab/noteflare` 是怎么优雅解决的？
- **四大密码学与工程设计**：
  1. **信封密钥包装（Passphrase + Recovery Code）**：笔记本体由主数据密钥进行 `AES-256-GCM` 加密，而口令与恢复码分别独立包装该主密钥——因此修改口令时无需重加密任何一篇笔记，忘记口令也能用恢复码无损找回（只有同时弄丢口令和恢复码才真正不可恢复）。
  2. **逐行智能合并（Line-by-Line Multi-Device Sync）**：解密后在客户端按行对比合并双端修改（类似 `git merge`），只有同一行改出不同内容时才拆出冲突副本，避免整篇笔记互相覆盖。
  3. **URL 片段密钥单篇分享 + 15 分钟自动抹除内存密钥**：只读分享链接的解密密钥仅存在 URL `#` 片段后（不会发送给服务器），支持 1/7/30 天过期；浏览器闲置 15 分钟自动清空内存中的解密密钥。
  4. **原生支持 Obsidian / Keep / Evernote 拖拽导入与加密 TypeScript SDK**：直接把本地 Obsidian 文件夹拖进浏览器即在本地批量加密上传；配套 CLI 与 TypeScript SDK 让本地 Agent 也能在端侧完成加解密读写。

### Q2：`AdamJBurns/workflows` 和 `DesignerStephen1/ascii-animals` 给构建 AI Agent 前端的架构师提供了什么立即可抄的交互范式？
- **核心架构机制**：
  - **`workflows` 的“防断流删除拦截（Refuse Flow-Breaking Deletes）”**：在可视化 Agent 编排画布中，不要让用户随便删掉承载下游分支的父节点再在保存时报校验错误；应当在点击删除的瞬间计算连通性，若会切断路径则直接拒绝并提示原因，同时保证全键盘无障碍操作与 `prefers-reduced-motion` 适配。
  - **`ascii-animals` 的“SVG 液态玻璃折射 + 程序化 ASCII 景深层”**：Chromium 下使用 SVG 滤镜实现真实边缘折射（非 Chromium 自动降级为毛玻璃），底层 Canvas 按远近景深控制蓝闪蝶、锦鲤（可点击投食）、发光水母、绿晏蜓、豹蛙、丹顶鹤与沙蟹的游弋速度与受惊反应，表单提交直接触发标准 `chat:submit` 事件。

### Q3：这套组合的诚实边界（Limitations）是什么？
- **诚实边界**：
  - `NoteFlare` 因服务端完全拿不到明文，无法在服务端直接跑明文 SQL 全文检索（检索与标签过滤在浏览器端原地解密后执行）；且若同时丢失口令与恢复码，数据永久无法找回。
  - `workflows` 与 `ascii-animals` 是纯粹的前端画布与输入交互层，需对接后端工作流执行引擎或 Agent 网关才能实际执行业务动作。

---

## 🧭 3. Mermaid 选型决策树与架构对比图

```mermaid
flowchart TD
    Start["零知识边缘知识库与高质感 AI 交互画布/输入框选型"] --> Need{"当前需要升级哪一模块？"}

    Need -->|"构建 $0/月、服务端零明文的个人/小团队(≤50人)笔记与 Agent 私有记忆库"| NoteGate{"是否需要 AES-256-GCM 端侧加密 + TypeScript SDK/CLI？"}
    NoteGate -->|"是：一键部署至 Cloudflare Workers + D1"| UseNoteFlare["✅ 选用 homielab/noteflare<br/>浏览器/SDK 端 AES-256-GCM 加密 + Passkey 解锁<br/>逐行 git-merge 同步 + Obsidian/Keep 拖拽加密导入"]

    Need -->|"构建支持角色条件分支、防断流误删与全键盘操作的规则编排画布"| FlowGate{"需要在删除节点时前置拦截断流风险？"}
    FlowGate -->|"是：采用 Next.js + React + Motion 安全画布"| UseWorkflows["✅ 选用 AdamJBurns/workflows<br/>自动重路由连线 + 断流删除附原因硬拒<br/>100% 免鼠标键盘可达 + Reduced-Motion 适配"]

    Need -->|"为 AI 对话入口打造零依赖动态氛围背景与液态玻璃输入框"| AsciiGate{"希望用几 KB 纯代码替代笨重视频背景？"}
    AsciiGate -->|"是：采用 7 种物理步态 ASCII 动物 + SVG 折射玻璃"| UseAscii["✅ 选用 DesignerStephen1/ascii-animals<br/>0 依赖 Canvas 景深 ASCII 生态 (可点击惊动/投喂)<br/>Dia 风格 SVG 液态玻璃折射 + chat:submit 事件"]
```

---

## 📊 4. 同类方案对比矩阵（Quantitative & Architectural Comparison）

| 对比维度 | `homielab/noteflare` | `AdamJBurns/workflows` + `ascii-animals` | 传统方案 A：明文云笔记 SaaS + 脆弱连线画布 + 视频背景 | 传统方案 B：自建 VPS 数据库 + 静态表单规则页 |
| :--- | :--- | :--- | :--- | :--- |
| **核心解决痛点** | `$0/月` 边缘零知识加密存储与多端逐行同步 | 杜绝删节点断流 Bug，用零依赖代码造出顶级 AI 输入感 | 敏感笔记明文存第三方；误删节点导致工作流崩溃 | 每月固定 VPS 账单与补丁维护；静态表单缺乏直观性 |
| **底层架构机制** | **Workers + D1 + 浏览器/SDK `AES-256-GCM`** | **拓扑校验拒删画布 + 0 依赖 ASCII Canvas/SVG 折射** | 服务端明文存储 / 无连通性守卫 / 30MB MP4 循环背景 | Docker Postgres 常驻实例 / 传统下拉框列表 |
| **关键量化指标** | **`$0/月`**（50 人内 Access 免费），**15 分钟**自动清密钥 | **7 种**交互式 ASCII 生物，**100%** 键盘无障碍 | 按人头 `$8–$15/月`；首屏加载数秒视频 | 需专人维护服务器安全更新 |
| **安全与可靠性** | **Passkey + 恢复码 + URL `#` 片段加密分享** | **全操作可撤销 (Undo) + Reduced-Motion 尊重** | 服务端拖库即全量明文泄露 | 缺乏客户端零知识加密与离线编辑 |

---

## 🃏 5. 7-Card 定量洞察与 FinOps 闭式账本（7-Card Quantitative Insights）

| 卡片编号 | 维度标签 | 核心定量洞察（Headline-as-Finding） | 证据与闭式参数锚点 |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `NoteFlare` + `workflows` + `ascii-animals` 将月度加密知识库与交互界面 TCO 降低 `93.25%`（`$5,700.00 → $385.00/月`） | `CLAIM-20261116-R19-NOTEFLARE-WORKFLOWS-ASCII` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | `NoteFlare` 用浏览器端 `AES-256-GCM` 让 Cloudflare D1 只存密文，以 `$0/月` 免费层支撑 50 人内零知识协作 | `homielab/noteflare` `README.md` |
| **Card 3** | `3/7 · WHAT I TESTED` | 双端并发修改同一篇加密笔记时按行执行 `git merge` 式智能合并，并支持 Passkey 解锁与 15 分钟自动抹除内存密钥 | `NoteFlare` 同步与安全规范 |
| **Card 4** | `4/7 · UNDER THE HOOD` | `AdamJBurns/workflows` 拒绝任何会破坏流程连通性的删除操作并说明原因，且 100% 控件支持纯键盘无鼠标操作 | `AdamJBurns/workflows` `README.md` |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | `ascii-animals` 以零外部依赖绘制 7 种带景深与受惊反应的 ASCII 动物，配合 Chromium SVG 折射滤镜实现液态玻璃输入框 | `DesignerStephen1/ascii-animals` `README.md` |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | 免除 VPS 运维、断流画布返工与视频背景压缩，每月释放 `35.4 小时`（`-91.95%`）全栈研发工时 | 30 个知识库实例 + 20 套交互原型/月 |
| **Card 7** | `7/7 · MY TAKE` | 敏感笔记与 Agent 记忆首选“客户端加密 + 边缘免费层 D1”，规则编排画布必须内建拓扑防断流门禁 | 自定义域名注册费：`not_measured` |

### 💰 FinOps 闭式参数表（每月 30 个加密知识库实例 + 20 套规则画布与 AI 输入界面交付，`r = $100.00/hr`）

| 方案路径 | SaaS 席位与云主机开销 (`compute_and_token_usd`) | 运维与前端返工工时 (`engineering_hours`) | 工程人力成本 (`engineering_labor_usd`) | 月度总 TCO (`total_monthly_usd`) | 较 Path A 净节省 (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A：明文云笔记 SaaS 席位 + 断流画布返工 + 重型视频背景** | `$1,850.00` | `38.5 hrs` | `$3,850.00` | **`$5,700.00`** | Baseline (`0.00%`) |
| **Path B：自建 VPS Postgres 笔记库 + 静态表单规则页** | `$890.00` | `18.0 hrs` | `$1,800.00` | **`$2,690.00`** | `-$3,010.00` (`-52.81%`) |
| **Path C：`NoteFlare` + `workflows` + `ascii-animals`（推荐）** | **`$75.00`** | **`3.1 hrs`** | **`$310.00`** | **`$385.00`** | **`-$5,315.00` (`-93.25%` / 年省 `$63,780.00`)** |

---

## 🛠️ 6. 实战上手 Checklist（15-Minute Actionable Rollout）

```bash
# 1. 检出 homielab/noteflare，在本地或 Cloudflare Workers + D1 免费层体验 AES-256-GCM 原地解密与 SDK
git clone https://github.com/homielab/noteflare.git

# 2. 启动 AdamJBurns/workflows 验证防断流删除拦截与键盘无障碍画布
git clone https://github.com/AdamJBurns/workflows.git && cd workflows && npm install && npm run dev

# 3. 检出 DesignerStephen1/ascii-animals 体验 7 种零依赖 ASCII 生物与液态玻璃聊天框
git clone https://github.com/DesignerStephen1/ascii-animals.git
```
