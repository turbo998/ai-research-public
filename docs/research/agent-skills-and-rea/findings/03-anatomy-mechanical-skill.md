# L3 确定性校验器型 Agent Skill 架构解析：以 `wheresryan22/anatomy` 为例

> **参考开源仓库**：[`wheresryan22/anatomy`](https://github.com/wheresryan22/anatomy)  
> **关联架构图**：[`../assets/03-agent-skill-l1-to-l4-depth-spectrum.svg`](../assets/03-agent-skill-l1-to-l4-depth-spectrum.svg) · **返回专题首页**：[`../README.md`](../README.md)

---

## 一、 核心架构问题：为什么纯提示词（L1/L2）在精确拓扑生成中必然失效？

在 AI Solution Architect 的日常交付（如**云架构拓扑图自动生成、网络子网/路由策略编排、UI 组件无重叠布局**）中，大语言模型暴露出一个结构性短板：**LLM 擅长推理组件之间的逻辑与因果拓扑，但直接手写二维/三维坐标、SVG 路径或复杂状态不变量时，极易产生透视畸变、节点遮挡错乱与边界越界。**

`wheresryan22/anatomy` 代表了 **Agent Skill 工程化演进光谱中的 L3 范式（Declarative Intent + Deterministic Code Verifier）**——不再强迫大模型在 Token 生成阶段靠“心算”保证几何/拓扑精确性，而是将技能拆分为**声明式规范层（`SKILL.md`）**与**零依赖确定性代码引擎及校验器（`kit/*.mjs`）**。

---

## 二、 双层解耦架构拆解（Intent Layer × Deterministic Verifier）

| 架构层级 / 模块 | 代码规模 | 核心工程职责 | 对企业级 Agent Skill 设计的启示 |
|---|---|---|---|
| **声明式规范层 (`SKILL.md`)** | ~280 行 | 定义视觉焦点唯一性（单焦点 `lit` + 四阶单色层次）、命名契约与组装流程 | `SKILL.md` 只规定**业务意图、设计品味与调用契约**，避免堆砌底层算术细节 |
| **原语编译器 (`kit/iso-kit.mjs` / `lathe.mjs` / `tube.mjs`)** | ~4,300 行 | 提供高阶语义原语（板件、容器、连接线束），自动计算正交投影轮廓与分段画家序 | 为 Agent 提供**高阶语义 DSL/SDK**，而非让模型裸写底层 SVG path 或原始配置块 |
| **确定性不变量校验器 (`kit/audit.mjs`)** | ~1,200 行 | **Ray-Cast Verifier（光线投射校验器）**：在静态与动态过渡态上自动审计 7 类空间不变量（重叠间隙 `clearance`、悬空端口 `loose ends`、深度环路 `depth order`、自交 `self-overlap`），输出精确违例定位 | **核心护城河**：必须为生成工具配套返回结构化 Diagnostics 的确定性验证脚本，驱动 Agent 自闭环修复直至 `0 problems` |
| **自包含交付打包器 (`scripts/inline-kit.mjs`)** | ~220 行 | 将运行时交互内核内联编译为单文件离线 HTML，满足 `default-src 'none'` 零外部依赖分发 | 企业架构汇报与安全内网环境优先采用零外部 CDN 依赖的单文件 HTML/SVG 交付物 |

---

## 三、 Solution Architect 落地选型指南（L1–L4 技能分级决策）

并非所有企业技能都需要重型引擎；架构师应根据**容错边界与可验证性**按需分级建设：

| 技能等级 | 架构形态 | 典型代表 | 适用企业场景 | 维护成本与质量上限 |
|---|---|---|---|---|
| **L1 · 裸提示词模板** | 单一 Markdown Prompt | 个人日常快捷指令 | 会议纪要润色、头脑风暴草稿 | 零开发成本，但长上下文下合规率波动大 |
| **L2 · 声明式 SOP + Critic 子智能体** | `SKILL.md` + 渐进参考文档 + 独立审查子智能体 | Ryan Doser Skills (`anti-slop.md`)、HVE Core RPI | 架构设计说明书（SAD/ADR）、客户方案书、招投标技术应答审校 | 低代码成本；通过独立 Critic 门禁显著降低空话与遗漏 |
| **L3 · 原语 SDK + 确定性校验器** | `SKILL.md` + 领域原语库 + CLI Verifier (`exit 0/1`) | `wheresryan22/anatomy`、Bicep/Terraform Policy Gate | **云架构图自动生成、IaC 网络与 RBAC 蓝图合成、数据契约编译** | 中等研发投入；**由确定性代码保障 100% 语法与拓扑合规** |
| **L4 · AST / 状态机 + 密码学证据 MCP** | 多层领域引擎 + MCP Server + SHA-256 证据账本 | `morluto/rea` (`v6.4.0`)、`cloudflare/security-audit-skill` | **遗留系统现代化逆向重构、大规模代码库安全覆盖审计、生产排障取证** | 高工程壁垒；具备跨百万行代码或混淆产物的可复核证据链 |

---

## 四、 架构师复用清单（Actionable Checklist）

1. **控制入口上下文体积**：将主 `SKILL.md` 严格控制在 `150–250` 行以内，详细 API 表与反例清单放入按需读取的子文档（Progressive Disclosure）。
2. **禁止让 LLM 裸算坐标与配额**：凡涉及架构图布局、子网 CIDR 划分、GPU 显存/并发容量测算，一律封装为确定性脚本工具（如本库 `azure-agent-infra/simulator/agent_infra_sizer.py`），让模型填参数而非心算结果。
3. **构建“生成 → 确定性 Audit → 定向修复”闭环**：校验器报错必须输出**具体违例实体 ID 与修复方向**（而非笼统报错），使 Agent 能在 1–3 轮工具调用内收敛至零违例状态。
