# 双插件实装与同题对决：FAF (`faf-agents` v2.0.1) vs. Microsoft `AGENT-FORGE` (`v0.3.0`) — “鹈鹕骑自行车”动画工程全链路评测

> 🌐 **Language / 语言**: **中文 (zh-CN)** | [English (`pelican-benchmark-comparison.en.md`)](pelican-benchmark-comparison.en.md)
> 🎮 **线上交互展厅 (Live GitHub.io Arena)**:
> - **⚔️ 双插件同屏对比竞技场 (`pelican-arena.html`)**: [https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/pelican-arena.html](https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/pelican-arena.html) （主站直达镜像：[https://turbo998.github.io/workshops/faf-vs-agent-forge/pelican-arena.html](https://turbo998.github.io/workshops/faf-vs-agent-forge/pelican-arena.html)）
> - **🟦 Demo A — FAF 架构规范驱动版 (`demo-faf-pelican.html`)**: [https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/demo-faf-pelican.html](https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/demo-faf-pelican.html)
> - **🟧 Demo B — AGENT-FORGE 多智能体创意剧场版 (`demo-agent-forge-pelican.html`)**: [https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/demo-agent-forge-pelican.html](https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/demo-agent-forge-pelican.html)
> - **📈 FAF 立项优先级评分仪表盘 (`prioritization-report.html`)**: [https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/artifacts/faf-sdlc/prioritization-report.html](https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/artifacts/faf-sdlc/prioritization-report.html)
> - **📊 7-Card 4:5 视觉评测报告 (`test-report-cards.html`)**: [https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/test-report-cards.html](https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/test-report-cards.html)

---

## 1. 实验设计：为什么用“动画版鹈鹕骑自行车”做双插件同题对决？

“**鹈鹕骑自行车（Pelican riding a bicycle）**”是生成式 AI 社区公认的高辨识度视觉与几何推理基准题。单次 Prompt 直接生成往往会出现三大典型缺陷：
1. **运动学脱节（Kinematic Detachment）**：鹈鹕脚掌与曲柄踏板在旋转过程中分离或穿模；
2. **解剖比例失真（Anatomical Distortion）**：缺少巨型弹性喉囊（Gular Pouch）、S 型弯曲长颈与双连杆逆运动学（2-Bone IK）膝关节折角；
3. **缺乏可验证的工程遥测与交互性**：只有静态 SVG 或简单 CSS 旋转，无法调节踏频、齿比、风阻或触发物理交互。

为了直观检验 **`customer-success-microsoft/faf-agents` (FAF v2.0.1)** 与 **`microsoft/agent-forge` (`@agent-forge-copilot/cli` v0.3.0)** 的真实工程差异，我们在本地完整安装了两套工具链，并用同一命题分别跑通了各自的全链路，记录下**真实安装输出、中间过程文档（Process Artifacts）与最终 Demo 动画效果**。

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

---

## 3. 过程文档（Process Artifacts）深度对比

两套插件在构建同一个“鹈鹕骑自行车”动画时，产出的**中间过程文档完完全全属于两个不同的抽象层**：

| 维度 | 🟦 FAF (`customer-success-microsoft/faf-agents`) | 🟧 Microsoft `AGENT-FORGE` (`microsoft/agent-forge`) |
|---|---|---|
| **过程文档的本质** | **软件工程全生命周期规范文档（SDLC Deliverables）**<br>关注“为什么要做、需求验收指标是什么、C4 数学/组件架构怎么设计、存量资产能否复用、Backlog 怎么拆”。 | **AI 编码代理的上下文工程配置（`.github/` Context Customization）**<br>关注“应该为这个前端动画项目派生哪几个专业子 Agent、每个 Agent 拥有什么工具权限、按什么 Handoff 顺序接力、遵循什么编码指令与 Hook”。 |
| **生成的文件清单**<br>*(均已归档至 [`artifacts/`](./artifacts/))* | 位于 [`artifacts/faf-sdlc/`](./artifacts/faf-sdlc/)：<br>1. [`scorecard.yaml`](./artifacts/faf-sdlc/scorecard.yaml) & [`history.yaml`](./artifacts/faf-sdlc/history.yaml)（28 项指标量化证据账本）<br>2. [`prioritization-report.html`](./artifacts/faf-sdlc/prioritization-report.html)（51.5KB 可视化立项报告）<br>3. [`scope.md`](./artifacts/faf-sdlc/scope.md)（P1 Go 立项与边界定义）<br>4. [`prd.md`](./artifacts/faf-sdlc/prd.md)（FR-01..FR-05 可测试验收标准）<br>5. [`spec.md`](./artifacts/faf-sdlc/spec.md)（C4 L1–L3 架构与双连杆余弦定理 IK 公式）<br>6. [`adr/adr-001-ik-svg-engine.md`](./artifacts/faf-sdlc/adr/adr-001-ik-svg-engine.md)（技术决策记录）<br>7. [`impl-rec.md`](./artifacts/faf-sdlc/impl-rec.md)（6 大企业加速器 8 域加权打分：`15.0% < 40%` → 路由至 **Path B 绿地自研**）<br>8. [`backlog.md`](./artifacts/faf-sdlc/backlog.md)（2 Epics / 6 Tasks） | 位于 [`artifacts/agent-forge-context/`](./artifacts/agent-forge-context/)：<br>1. [`forge-plan.json`](./artifacts/agent-forge-context/forge-plan.json)（`pipeline` 编排规划蓝图）<br>2. [`agents/pelican-character-artist.agent.md`](./artifacts/agent-forge-context/agents/pelican-character-artist.agent.md)（羽毛四色分层与喉囊美术 Agent）<br>3. [`agents/bicycle-kinematics-coder.agent.md`](./artifacts/agent-forge-context/agents/bicycle-kinematics-coder.agent.md)（巡航车架、IK 与翘头特技 Agent）<br>4. [`agents/scene-environment-director.agent.md`](./artifacts/agent-forge-context/agents/scene-environment-director.agent.md)（三幕海岸光影与 WebAudio 车铃 Agent）<br>5. [`agents/animation-qa-reviewer.agent.md`](./artifacts/agent-forge-context/agents/animation-qa-reviewer.agent.md)（60FPS 与 CSP 审查 Agent）<br>6. [`instructions/pelican-animation-standards.instructions.md`](./artifacts/agent-forge-context/instructions/pelican-animation-standards.instructions.md)<br>7. [`prompts/tune-pelican-choreography.prompt.md`](./artifacts/agent-forge-context/prompts/tune-pelican-choreography.prompt.md)<br>8. [`skills/pelican-svg-rigging/SKILL.md`](./artifacts/agent-forge-context/skills/pelican-svg-rigging/SKILL.md) & [`hooks/hooks.json`](./artifacts/agent-forge-context/hooks/hooks.json) |
| **关键路由/校验决策点** | **`FAF-impl-recommender` 阈值路由**：<br>由于预置企业加速器（Banking / RAG / Voice）在 2D 生物运动学动画上的最高加权分仅 **`15.0%`**（低于 `40%` 最低可行阈值），系统拒绝生搬硬套模板，确定性切换至 **Path B: Agentic Greenfield Development**。 | **`postGenerationValidateAndFix` 静态自愈**：<br>自动检查 YAML Frontmatter、工具名拼写（Levenshtein `<= 3`）、Handoff 双向引用闭环以及 `SKILL.md` 的 `USE FOR:` / `DO NOT USE FOR:` 触发契约。 |

---

## 4. 两套 Demo 动画效果与交互体验深度对比

由于两套插件的上游驱动机制不同（**FAF 由架构师 `spec.md` 与验收指标驱动** vs. **AGENT-FORGE 由角色美术、物理特技、环境导演 4 个专业 Agent 流水线驱动**），最终产出的两个鹈鹕骑自行车 Demo 呈现出鲜明且互补的风格差异：

| 视觉与工程维度 | 🟦 Demo A：FAF 架构驱动版 (`demo-faf-pelican.html`) | 🟧 Demo B：AGENT-FORGE 多智能体版 (`demo-agent-forge-pelican.html`) |
|---|---|---|
| **核心设计范式** | **工程动力学仿真工作台 (Engineering Kinematics Workbench)** | **多智能体创意互动剧场 (Multi-Agent Coastal Animation Studio)** |
| **腿部踩踏逆运动学 (IK)** | 严格实现 `spec.md` 中的余弦定理双连杆解析解（`AnalyticalTwoBoneIKSolver`），脚掌锚点与踏板轴心欧氏误差恒为 **`0.00 px`**。 | 同样共享零滑移双连杆解析 IK（由 `pelican-svg-rigging` Skill 注入），并额外耦合了**整车绕后轮轴仰角旋转（Wheelie Pitch $\theta \in [0, 24^\circ]$）**。 |
| **特色视觉图层** | **🔬 X-Ray 逆运动学骨骼与矢量透视层**：实时绘制曲柄圆轨迹、左右腿骨骼向量（青色实线/琥珀虚线）、髋/膝/踏板关节点实时角度标注（如 `K_L (94°)`）与喉囊弹簧形变矢量 `Δy_pouch`。 | **🌅 加州海滨木栈道三幕光影剧场**：支持一键切换 `☀️ 晴空栈道`、`🌅 落日余晖`、`🌙 星夜车灯（带车前灯锥形体积光束）`，配有多层海浪视差、伴飞海鸥、复古薄荷绿白边轮胎巡航车、车前藤编鱼篓、飞行员皮帽与随风飘动的红围巾。 |
| **特色物理与趣味交互** | • **踏频 RPM (`20–130`) × 变速齿比 (`1.0x–4.2x`)** 精确耦合车轮角速度 $\omega_w$<br>• **逆风风速 (`0–50 km/h`)** 驱动躯干前倾与流线粒子<br>• **喉囊载鱼量 (`0–3 条鱼`)** 改变二阶阻尼弹簧静平衡位置与整车滚动阻力功率（Watts） | • **🐟 点击画布/按钮抛沙丁鱼投喂**：沙丁鱼沿抛物线飞向鹈鹕，鹈鹕自动张开巨喙精准接鱼，触发喉囊吞咽弹性膨胀（`pouchGulp`）与鱼篓计数增加<br>• **🎪 翘前轮特技 (`Wheelie!`)** 与 **🚀 扇翅加速冲刺 (`Sprint Boost`)**<br>• **🔔 纯 WebAudio 双振荡器合成清脆铜车铃 (`Ding-Ding!`)** |
| **内置过程溯源面板** | 顶部内嵌 **5 阶段 SDLC 角色导航条**（点击可实时检视 `FAF-analyst` 至 `FAF-dev` 的核心产出物摘要）。 | 顶部内嵌 **4-Agent 流水线导航条**（点击可实时检视 4 个 `.agent.md` 与 `forge validate` 的源码与职责）。 |

---

## 5. 总结：通过同题实操得出的最佳实践范式

1. **FAF (`faf-agents`) 的不可替代性在于“工程严谨度与数学/架构契约先行”**：
   - 如果没有 `FAF-analyst` 的可测试验收标准（`FR-01: 0.0px pedal slip`）和 `FAF-architect` 在 `spec.md` 中先写清楚双连杆余弦定理 IK 方程，开发 Agent 极易退化为“画两条随便摆动的折线当腿”。
2. **Microsoft `AGENT-FORGE` 的不可替代性在于“多领域专家分工与 `.github/` 护栏自动化”**：
   - 将一个复杂创意任务拆解为 `pelican-character-artist`（羽毛/皮帽/红围巾）、`bicycle-kinematics-coder`（车架/翘头/抛鱼弹道）、`scene-environment-director`（三幕光影/海浪/WebAudio 车铃）与 `animation-qa-reviewer`（CSP 与 60FPS 校验），让动画在艺术表现力与趣味交互上远超单一通用 Agent。
3. **黄金组合（The Hybrid Power Pattern）**：
   - 先用 **FAF (`faf-genai`)** 完成立项评分（`compute_scores.py`）、PRD 与 C4 架构规范（`spec.md`），再用 **`@agent-forge-copilot/cli`** 根据架构规范一键生成项目专属的 `.github/agents/` 多智能体团队与 `hooks.json` 校验护栏——兼得**企业级 SDLC 架构深度**与**多智能体艺术/工程执行力**。
