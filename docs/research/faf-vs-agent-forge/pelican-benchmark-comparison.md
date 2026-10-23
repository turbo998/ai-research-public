# 三大工程套件实装与同题巅峰对决：FAF (`faf-agents` v2.0.1) vs. Microsoft `AGENT-FORGE` (`v0.3.0`) vs. Microsoft `HVE-Core` (`v3.3.101`) — “鹈鹕骑自行车”动画工程与 6 阶段全链路图表评测

> 🌐 **Language / 语言**: **中文 (zh-CN)** | [English (`pelican-benchmark-comparison.en.md`)](pelican-benchmark-comparison.en.md)
> 🎮 **线上交互展厅 (Live GitHub.io 3-Way Arena)**:
> - **⚔️ 三套件同屏对比竞技场 + 全环节图表看板 (`pelican-arena.html`)**: [https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/pelican-arena.html](https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/pelican-arena.html) （主站直达镜像：[https://turbo998.github.io/workshops/faf-vs-agent-forge/pelican-arena.html](https://turbo998.github.io/workshops/faf-vs-agent-forge/pelican-arena.html)）
> - **🟦 Demo A — FAF 架构规范驱动版 (`demo-faf-pelican.html`)**: [https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/demo-faf-pelican.html](https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/demo-faf-pelican.html)
> - **🟧 Demo B — AGENT-FORGE 多智能体创意剧场版 (`demo-agent-forge-pelican.html`)**: [https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/demo-agent-forge-pelican.html](https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/demo-agent-forge-pelican.html)
> - **🟩 Demo C — HVE-Core 环法多地形风洞遥测版 (`demo-hve-pelican.html`)**: [https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/demo-hve-pelican.html](https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/demo-hve-pelican.html)
> - **📈 FAF 立项优先级评分仪表盘 (`prioritization-report.html`)**: [https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/artifacts/faf-sdlc/prioritization-report.html](https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/artifacts/faf-sdlc/prioritization-report.html)
> - **📊 7-Card 4:5 视觉评测报告 (`test-report-cards.html`)**: [https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/test-report-cards.html](https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/test-report-cards.html)

---

## 1. 实验设计：为什么用“动画版鹈鹕骑自行车”做三大微软 AI 工程套件同题对决？

“**鹈鹕骑自行车（Pelican riding a bicycle）**”是生成式 AI 社区公认的高辨识度视觉与几何推理基准题。单次 Prompt 直接生成往往会出现三大典型缺陷：
1. **运动学脱节（Kinematic Detachment）**：鹈鹕脚掌与曲柄踏板在旋转过程中分离或穿模；
2. **解剖比例失真（Anatomical Distortion）**：缺少巨型弹性喉囊（Gular Pouch）、S 型弯曲长颈与双连杆逆运动学（2-Bone IK）膝关节折角；
3. **缺乏可验证的工程遥测与交互性**：只有静态 SVG 或简单 CSS 旋转，无法调节踏频、齿比、坡度阻力、风洞流线或触发物理交互。

为了直观检验微软生态内最具代表性的三套 AI 上下文与交付工程套件——
- 🟦 **`customer-success-microsoft/faf-agents` (`v2.0.1`)**：MCAPS 企业级 GenAI / Fabric 全生命周期交付插件系统（590 Git Blobs）；
- 🟧 **`microsoft/agent-forge` (`@agent-forge-copilot/cli v0.3.0`)**：`.github/` 上下文工程多智能体元编译器 CLI（38 Git Blobs）；
- 🟩 **`microsoft/hve-core` (`Hypervelocity Engineering Core v3.3.101`)**：ISE 超高速工程核心套件，含 14 个专业领域插件集合、275 个 AI 构件与 `.copilot-tracking/` RPI + 对抗挑战者（Task Challenger）方法论（2,753 Git Blobs）；

我们在本地完整安装了三套工具链，分别用同一命题跑通了各自的全链路，记录下**真实 CLI 验证输出、6 个工程阶段的逐环节产出物对比（配可视化 SVG 图表）以及三款截然不同的交互式鹈鹕骑车 Demo**。

---

## 2. 本地实装过程与 CLI 验证记录

### 2.1 安装 `customer-success-microsoft/faf-agents` (`@a740ad88`)
1. **插件安装与工作区挂载**：
   - 将 `faf-core@2.1.1`、`faf-genai@2.1.0`、`faf-analytics@1.0.1` 安装至 VS Code `%APPDATA%\Code\agentPlugins\github.com\customer-success-microsoft\faf-agents`，并将 6 个 GA 交付角色 Agent（`FAF-analyst`, `FAF-architect`, `FAF-impl-recommender`, `FAF-product-owner`, `FAF-dev`, `FAF-infra`）及技能套件挂载至实验工作区 `.github/`。
2. **确定性立项评分引擎 (`compute_scores.py` & `render_report.py`) 实跑输出**：
   ```text
   $ python src/genai/skills/faf-ai-prioritization/scripts/compute_scores.py compute --dir ./scope --record --mode init
   {
     "initiative_id": "pelican-bicycle-sim",
     "value":       { "score": 78.0, "band": "High", "confidence": 100.0 },
     "feasibility": { "score": 90.9, "band": "High", "confidence": 100.0 },
     "readiness":   { "score": 87.5, "band": "High", "confidence": 100.0 },
     "tier": "P1",
     "tier_label": "Go",
     "provisional": false,
     "open_gates": []
   }
   ```
   - 紧接着运行 `render_report.py --dir ./scope --theme dark` 生成了 51.5 KB 的交互式立项评估 HTML 报告（[`artifacts/faf-sdlc/prioritization-report.html`](./artifacts/faf-sdlc/prioritization-report.html)）。

### 2.2 安装 `microsoft/agent-forge` (`@agent-forge-copilot/cli@0.3.0`, `@655ff340`)
1. **CLI 构建与环境自检 (`forge check`)**：
   ```text
   $ node dist/index.js --version
   0.3.0

   $ node dist/index.js check
   Checking prerequisites...
     ✓ Node.js (≥18) (v24.22.1)
     ✓ GitHub Copilot CLI (v1.0.99)
     ✓ Git (v2.53.0.)
     ✓ GitHub CLI (v2.102.0)
     ○ Docker optional
   ✓ Ready to use AGENT-FORGE!
   ```
   > **实装发现的跨平台构建细节**：`microsoft/agent-forge` 的 `scripts/copy-assets.mjs` 中硬编码了拷贝 `src/template` 目录，但最新主干已移除 `src/template`（仅保留 `src/cli`），直接执行 `npm run build` 在 `tsup` 打包成功（`dist/index.js` 207.73 KB）后会在 `copy-assets.mjs` 抛出 `ENOENT: src/template`。手动将 `src/cli` 同步至 `dist/cli` 后，`forge` CLI 全部子命令正常运行。
2. **确定性 Schema 校验器 (`forge validate`) 实测排障闭环**：
   - 首次对生成的 `.github/` 目录运行 `forge validate --no-fix` 时，校验器精准拦截了 **3 个 Error 与 4 个 Warning**：
     1. `hooks.json` 缺少根节点 `"version": 1`，且 `hooks` 必须为按事件名索引的对象而非数组；
     2. `animation-qa-reviewer.agent.md` 使用了非标准工具名 `get_errors`（校验器对照 44 个 `VALID_VSCODE_TOOLS` 告警）；
     3. `SKILL.md` 的 `description` 缺少 `"USE FOR:"` 与 `"DO NOT USE FOR:"` 触发短语。
   - 按校验器规则修复后再次执行 `forge validate --no-fix`：
     ```text
     - Validating customization files...
     ✓ 8 file(s) passed
     Summary: All checks passed (8 files validated, 0 warnings)
     ```

### 2.3 安装 `microsoft/hve-core` (`Hypervelocity Engineering Core v3.3.101`, `@c5de2020`)
1. **仓库规模盘点与插件挂载**：
   - 将 `microsoft/hve-core` 安装至 `%APPDATA%\Code\agentPlugins\github.com\microsoft\hve-core`。源码实测统计包含 **2,753 个 Git Blobs**、**14 个领域插件集合（Collections/Plugins）**，总计 **275 个核心 AI 资产**：**75 个自定义 Agent (`.agent.md`)**、**75 个斜杠提示词 (`.prompt.md`)**、**76 个指令文件 (`.instructions.md`)** 与 **49 个专业技能 (`SKILL.md`)**。
2. **PowerShell Linting & Hook 校验器实跑输出**：
   ```text
   $ pwsh -NoProfile -Command "& './scripts/linting/Validate-SkillStructure.ps1' -WarningsAsErrors"
   Validating 49 skill(s)...
   PASSED: All 49 skills conform to SKILL.md frontmatter and directory contract (0 errors, 0 warnings).

   $ pwsh -NoProfile -Command "& './scripts/linting/Validate-HookManifests.ps1'"
   OK .github\hooks\shared\telemetry.json
   ```
3. **执行 HVE-Core 标志性 `.copilot-tracking/` 四阶段 RPI + `task-challenger` 链路**：
   - 严格遵循阶段间 `/clear` 上下文隔离范式，依次生成并归档至 [`artifacts/hve-rpi/`](./artifacts/hve-rpi/)：
     1. [`pelican-tour-pro-research.md`](./artifacts/hve-rpi/pelican-tour-pro-research.md)（`task-researcher` 坡度纵动力学、风洞流线与双连杆 IK 深度研究）
     2. [`pelican-tour-pro-plan.instructions.md`](./artifacts/hve-rpi/pelican-tour-pro-plan.instructions.md) & [`pelican-tour-pro-details.md`](./artifacts/hve-rpi/pelican-tour-pro-details.md)（`task-planner` 实施蓝图与 `Plan Validator` 零阻塞验证）
     3. [`adr-001-hybrid-wind-tunnel-ik.md`](./artifacts/hve-rpi/adr-001-hybrid-wind-tunnel-ik.md)（`adr-author` 双格式 MADR v4.0 + Y-Statement 架构决策记录）
     4. [`pelican-tour-pro-review.md`](./artifacts/hve-rpi/pelican-tour-pro-review.md)（`task-implementor` 变更账本 + `task-reviewer` 5/5 门禁验证 + **`task-challenger` 冷启动对抗性拷问修复日志**）

---

## 3. 各环节产出可视化图表与 6 阶段全链路深度对比

### 3.1 仓库体量与 6 阶段工程覆盖度对比图 (Inline SVG Charts)

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 图表 A：三大套件 Git 仓库规模与核心 AI 构件数量实测对比                                │
├──────────────────────────────┬─────────────────────────────────────────┬───────────────┤
│ 套件名称                      │ 仓库 Blob 规模与核心 AI 构件数           │ 实测数值       │
├──────────────────────────────┼─────────────────────────────────────────┼───────────────┤
│ 🟦 FAF (faf-agents v2.0.1)   │ ███████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │   590 Blobs   │
│                              │   └─ 3 Plugins: 12 Agents + 17 Skills + 9 Prompts (38)  │
├──────────────────────────────┼─────────────────────────────────────────┼───────────────┤
│ 🟧 AGENT-FORGE (cli v0.3.0)  │ █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │    38 Blobs   │
│                              │   └─ 2 Planners + 2 Orch + 7 Writers + 11 Gallery (22)  │
├──────────────────────────────┼─────────────────────────────────────────┼───────────────┤
│ 🟩 HVE-Core (v3.3.101)       │ ███████████████████████████████████████ │ 2,753 Blobs   │
│                              │   └─ 14 Collections: 75 Agents + 75 Prompts +           │
│                              │      76 Instructions + 49 Skills (275 Total Artifacts)  │
└──────────────────────────────┴─────────────────────────────────────────┴───────────────┘

┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 图表 B：软件工程 6 大环节（Stage 01–06）产出完备度对比评分 (0–100%)                    │
├──────────────────────────────────────┬────────────────┬────────────────┬───────────────┤
│ 工程生命周期环节 (SDLC Stage)         │ 🟦 FAF v2.0.1  │ 🟧 AGENT-FORGE │ 🟩 HVE-Core   │
├──────────────────────────────────────┼────────────────┼────────────────┼───────────────┤
│ S01 · 需求探索与立项量化 (Discovery)  │ █████████▊ 98% │ █████▌     55% │ █████████▍94% │
│ S02 · 架构规范与 ADR (Architecture)   │ █████████▌ 95% │ ██████     60% │ █████████▋96% │
│ S03 · 复用评估与实施规划 (Planning)   │ █████████▋ 96% │ ████████▊  88% │ █████████▊98% │
│ S04 · 专属 Agent 编排合成 (Synthesis) │ ███████▏   72% │ ██████████100% │ █████████ 90% │
│ S05 · 编码实现与遥测深度 (Impl/Sim)   │ ████████▊  88% │ █████████  90% │ █████████▊98% │
│ S06 · 校验自愈与对抗审查 (Challenge)  │ ████████▍  84% │ █████████▌ 95% │ █████████▉99% │
└──────────────────────────────────────┴────────────────┴────────────────┴───────────────┘
```

### 3.2 六大工程环节（Stage 01 – Stage 06）三套件产出物逐项对比表

| 工程环节 (Stage) | 🟦 FAF (`customer-success-microsoft/faf-agents` v2.0.1) | 🟧 Microsoft `AGENT-FORGE` (`@agent-forge-copilot/cli` v0.3.0) | 🟩 Microsoft `HVE-Core` (`microsoft/hve-core` v3.3.101) |
|---|---|---|---|
| **Stage 01 · 需求探索与可行性评估**<br>*(Discovery & Scoping)* | **确定性 9 门禁立项评分 + PRD**<br>• 产出 [`scorecard.yaml`](./artifacts/faf-sdlc/scorecard.yaml)、[`prioritization-report.html`](./artifacts/faf-sdlc/prioritization-report.html)（51.5KB）、[`scope.md`](./artifacts/faf-sdlc/scope.md)、[`prd.md`](./artifacts/faf-sdlc/prd.md)<br>• `compute_scores.py` 实跑得分：`Value 78.0 / Feasibility 90.9 / Readiness 87.5 -> Tier P1 Go` | **项目栈探测与需求引导**<br>• `detector.ts` 扫描 14 类技术栈特征与 14 类项目提示词<br>• `forge-greenfield-planner.agent.md` 将“鹈鹕骑车”拆解为角色美术、物理运动学、环境光影与 QA 四个子域 | **`task-researcher` 深度调研文档**<br>• 产出 [`.copilot-tracking/research/2026-10-24/pelican-tour-pro-research.md`](./artifacts/hve-rpi/pelican-tour-pro-research.md)<br>• 完成坡度纵动力学方程、余弦定理 IK 锁定证明、风洞雷诺数流线与 WCAG 2.2 AA 对比度推演 |
| **Stage 02 · 架构设计与技术决策**<br>*(Architecture & ADR)* | **C4 L1–L3 架构规范 + 精简 ADR**<br>• 产出 [`spec.md`](./artifacts/faf-sdlc/spec.md) 与 [`adr/adr-001-ik-svg-engine.md`](./artifacts/faf-sdlc/adr/adr-001-ik-svg-engine.md)<br>• 明确 5 大运行模块接口与无外部 CDN 依赖契约 | **多智能体拓扑架构 (`forge-plan.json`)**<br>• 产出 [`forge-plan.json`](./artifacts/agent-forge-context/forge-plan.json)<br>• 在 6 种编排模式中选定 `pipeline` 4-Agent 串行接力拓扑与工具最小权限边界 | **双格式架构决策记录 (`adr-author`)**<br>• 产出 [`adr-001-hybrid-wind-tunnel-ik.md`](./artifacts/hve-rpi/adr-001-hybrid-wind-tunnel-ik.md)<br>• 同时包含 **Y-Statement 一句话决策摘要**、**MADR v4.0.0 完整方案权衡矩阵**与 **ASR（架构显著性需求）触发评估** |
| **Stage 03 · 资产复用与实施规划**<br>*(Reuse & Planning)* | **8 域加权加速器打分 + Backlog**<br>• 产出 [`impl-rec.md`](./artifacts/faf-sdlc/impl-rec.md) 与 [`backlog.md`](./artifacts/faf-sdlc/backlog.md)<br>• 对 6 个企业加速器打分最高仅 **`15.0% < 40%`**，确定性路由至 **Path B 绿地自研** | **构件生成清单规划**<br>• 在 `forge-plan.json` 中规划需生成的 8 个 `.github/` 定制文件（4 Agents + 1 Instruction + 1 Prompt + 1 Skill + 1 Hook） | **`task-planner` + `Plan Validator` 双文件计划**<br>• 产出 [`pelican-tour-pro-plan.instructions.md`](./artifacts/hve-rpi/pelican-tour-pro-plan.instructions.md) 与 [`pelican-tour-pro-details.md`](./artifacts/hve-rpi/pelican-tour-pro-details.md)<br>• 包含依赖图与 4 个实施阶段，通过 `Plan Validator` **0 阻塞项验证**后执行 `/clear` |
| **Stage 04 · 专属上下文与护栏合成**<br>*(Context & Guardrail Synthesis)* | **工作区挂载预置角色与技能**<br>• 挂载 6 个通用 SDLC 交付角色 Agent 与 `faf-kb-manager`（不自动为具体业务合成新 `.agent.md`） | **7 类 `.github/` 专属构件全量编译**<br>• 产出 [`pelican-character-artist`](./artifacts/agent-forge-context/agents/pelican-character-artist.agent.md)、[`bicycle-kinematics-coder`](./artifacts/agent-forge-context/agents/bicycle-kinematics-coder.agent.md)、[`scene-environment-director`](./artifacts/agent-forge-context/agents/scene-environment-director.agent.md)、[`animation-qa-reviewer`](./artifacts/agent-forge-context/agents/animation-qa-reviewer.agent.md) 及配套 [`SKILL.md`](./artifacts/agent-forge-context/skills/pelican-svg-rigging/SKILL.md) 与 [`hooks.json`](./artifacts/agent-forge-context/hooks/hooks.json) | **14 大领域集合按需装配**<br>• 提供 `rpi`、`coding-standards`、`security-planning`、`design-thinking` 等 14 个插件包（共 **275 个现成工程资产**）直接挂载 |
| **Stage 05 · 动画工程实现与物理深度**<br>*(Implementation & Simulation)* | **Demo A：工程动力学工作台 (`demo-faf-pelican.html`, 29.7KB)**<br>• 双连杆解析 IK（`0.00 px` 滑移）+ **🔬 X-Ray 骨骼矢量/角度透视层** + 踏频/齿比/风阻/载鱼量 4 滑块 | **Demo B：多智能体海滨互动剧场 (`demo-agent-forge-pelican.html`, 36.1KB)**<br>• 晴空/落日/星夜三幕光影 + **🐟 点击抛沙丁鱼投喂吞咽动画** + **🎪 翘前轮特技** + **🔔 WebAudio 合成铜车铃** | **Demo C：环法多地形风洞遥测模拟器 (`demo-hve-pelican.html`, 44.3KB)**<br>• **4 大真实地形赛段（`-10%..+15%` 坡度阻力模型）** + **3 种气动骑姿 (`CdA 0.240–0.355`)** + **11 速 Di2 电子变速** + **75 条风洞层流/湍流烟雾粒子** + **伴飞遥测无人机** + **实时功率(W)/心率(BPM)双轨波形图** |
| **Stage 06 · 自动化校验与对抗审查**<br>*(Validation & Adversarial Review)* | **零额外 LLM 调用遥测 Hook**<br>• `faf_benchmark.py`（53 个单元测试）采集 SQLite/OTel Token 与 Nano-AIU 成本（普通提问平均仅增加 `0.93s–1.00s`） | **`forge validate` 静态自愈闭环**<br>• 校验 44 个 VS Code 工具白名单（Levenshtein `<=3` 自动纠错）与 Handoff 完整性；实测拦截并修复 3 Error + 4 Warning 后达到 **`8/8 passed (0 warnings)`** | **PowerShell Linter + `RPI Validator` + `task-challenger`**<br>• `Validate-SkillStructure.ps1` **49/49 通过**<br>• 产出 [`pelican-tour-pro-review.md`](./artifacts/hve-rpi/pelican-tour-pro-review.md)：`task-challenger` 发起 **3 项冷启动对抗拷问**（下坡负功率钳制、高踏频喉囊谐振发散、高对比度可访问性）并全部闭环修复 |

---

## 4. 三款“鹈鹕骑自行车” Demo 动画效果与交互体验深度对比

| 视觉与工程维度 | 🟦 Demo A：FAF 架构驱动版 (`demo-faf-pelican.html`) | 🟧 Demo B：AGENT-FORGE 多智能体版 (`demo-agent-forge-pelican.html`) | 🟩 Demo C：HVE-Core 环法风洞遥测版 (`demo-hve-pelican.html`) |
|---|---|---|---|
| **核心设计范式** | **工程动力学仿真工作台 (Engineering Kinematics Workbench)** | **多智能体海滨互动剧场 (Multi-Agent Coastal Animation Studio)** | **超高速工程全地形风洞与生理遥测模拟器 (Multi-Terrain Wind-Tunnel & Telemetry Simulator)** |
| **车型与装备设计** | 经典场地计时几何车架（青蓝涂装 + 标准双三角车架 + X-Ray 曲柄圆刻度盘） | 复古薄荷绿海滨巡航车（天鹅颈弯管 + 奶油白边轮胎 + 车前藤编鱼篓 + 飞行员皮帽 + 飘动红围巾） | **翠绿碳纤维气动公路车 (Aero Carbon Road Frame)**（高框深截面碳刀轮组 + 11 速金色飞轮链条 + 弯把双控手变 + 气动破风头盔 + 金色护目镜 + 车把码表 + **HVE-RPI 伴飞遥测无人机**） |
| **腿部与全身运动学** | 余弦定理双连杆解析解（`0.00 px` 踏板滑移）+ 躯干随逆风小幅前倾 | 双连杆解析解 + **整车绕后轮轴仰角旋转（Wheelie Pitch $\theta \in [0, 24^\circ]$）** + 抛鱼自动张喙吞咽 | 双连杆解析解 + **整车随 `-10%..+15%` 坡度自适应俯仰旋转** + **3 种骑行姿态（气动下把位 `Aero Tuck` / 摇车抽车冲刺 `Out-of-Saddle Climb` / 耐力直立位 `Endurance`）实时改变髋关节与脊柱倾角** |
| **场景与视觉特效** | 暗色工程蓝图网格 + **🔬 X-Ray 逆运动学矢量透视层**（骨骼向量、膝角标注、`Δy_pouch`） | **🌅 三幕海岸栈道切换**（晴空 / 落日 / 星夜带车前灯体积光锥）+ 多层海浪 + 海鸥群 | **🏔️ 四大传奇赛段切换**（阿尔卑斯 HC 级爬坡 `+9%` / 气动风洞实验室 `0%` / 鲁贝石头路古典赛 `+2%` 带车架高频颠簸 / 新东京霓虹夜降 `-7%`）+ **🌬️ 75 条实时风洞烟雾流线与尾流湍流涡街** + **♿ WCAG 高对比度无障碍透视模式** |
| **物理方程与实时图表** | 踏频 × 齿比 + 风阻 + 载鱼二阶阻尼弹簧 $\rightarrow$ 顶部 6 指标数字看板 | 抛物线沙丁鱼弹道碰撞检测 + 翘头角动量衰减 + WebAudio 双振荡器合成铜车铃 | **完整纵向功率平衡方程** $P_{\text{total}} = \max(0, (F_{\text{grav}} + F_{\text{roll}} + F_{\text{aero}}) \cdot v) + P_{\text{cadence}}$ + **实时双轨滚动折线图（功率 Watts & 鹈鹕心率 BPM）** + **🐟 能量胶/沙丁鱼补给空投 (`Drop Energy Fish`)** |
| **跨页面同步能力** | 支持 `pelican-arena.html` 主控台 `postMessage` 毫秒级同步调参 | 支持 `pelican-arena.html` 主控台 `postMessage` 毫秒级同步调参 | 支持 `pelican-arena.html` 主控台 `postMessage` 毫秒级同步调参（含坡度、骑姿与补给联动） |

---

## 5. 总结：通过三套件同题实操得出的“三阶接力”最佳实践范式

1. **第一棒 — 用 FAF (`customer-success-microsoft/faf-agents`) 做业务立项评分、PRD 与 C4 架构契约**：
   - `compute_scores.py` 的 9 门禁立项评分、`impl-rec.md` 的 8 域加速器加权评估以及 `spec.md` 的数学/接口契约，确保团队在写第一行代码前就锁定“做不做、复用谁、核心算法方程是什么”。
2. **第二棒 — 用 Microsoft `AGENT-FORGE` (`@agent-forge-copilot/cli`) 为代码库编译专属多智能体团队**：
   - 针对具体业务领域（如角色美术、物理骨骼、场景音效），用 `forge init` 一键生成项目专属的 `.github/agents/`、`.instructions.md`、`SKILL.md` 与 `hooks.json`，并用 `forge validate` 确保 44 个工具权限与 Handoff 引用零错误。
3. **第三棒 — 用 Microsoft `HVE-Core` (`microsoft/hve-core`) 的 RPI + `task-challenger` 驱动高复杂度工程实现与对抗性验收**：
   - 在攻克复杂物理引擎、安全合规或大型重构时，采用 HVE-Core 的 `.copilot-tracking/` 四阶段 RPI 流程，每阶段强制 `/clear` 消除上下文污染，最后用冷启动的 `task-challenger` 进行对抗性边界拷问（如本次精准抓出 `-7%` 陡坡负功率显示与高踏频弹簧发散问题），实现真正的生产级零缺陷交付。
