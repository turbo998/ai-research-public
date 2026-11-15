# 96KB 单文件 WebGPU 两百万水草程序化世界（`Abyssal-Garden`）与逐顶点路径追踪烘焙 4K HDR10 曙光卧室（`Room-at-Dawn`）深度架构拆解与同类方案选型 FAQ

> **文档元数据（Document Metadata）**  
> - **评审日期**：2026-11-15（Night Round 26 · 累计第 328 轮独立选型专题）  
> - **对标项目**：[`Noniv/abyssal-garden`](https://github.com/Noniv/abyssal-garden)（`★904`，2026-11-12 创建，零图片/零模型/零音频外链、仅靠 `96 KB` 单个 HTML 文件与原生 WebGPU 生成 200 万片摇曳海藻、沉船、蝠鲼与实时 Web Audio 声景，RTX 5070 Ti 跑 `180 fps @ 1440p`，MIT） & [`Leonxlnx/room-at-dawn`](https://github.com/Leonxlnx/room-at-dawn)（`★83`，2026-11-12 创建，`6:51 — a room at dawn`，零外部模型/贴图/HDRI、基于 Three.js + Web Worker `three-mesh-bvh` CPU 路径追踪逐顶点定向全局光照 `gi.bin` 与 `4K HDR10 PQ/BT.2020` 电影级渲染器，MIT）  
> - **适用角色**：AI Solution Architect（AI 解决方案架构师）、WebGPU/Three.js 创意图形主程、零资产（Zero-Asset）程序化生成架构师  
> - **关联雷达日报**：[2026-11-15 全景洞察与飙升榜 (`daily/2026-11-15.md`)](../daily/2026-11-15.md) · [English Version (`abyssal-garden-room-at-dawn-96kb-webgpu-procedural-world-bvh-pathtraced-4k-hdr10-selection-faq.en.md`)](abyssal-garden-room-at-dawn-96kb-webgpu-procedural-world-bvh-pathtraced-4k-hdr10-selection-faq.en.md)  
> - **可视化总结图**：[`assets/github-ai-radar-2026-11-15-r26-abyssalgarden-roomatdawn.svg`](../../../assets/github-ai-radar-2026-11-15-r26-abyssalgarden-roomatdawn.svg)

![Abyssal-Garden + Room-at-Dawn Architecture Overview](../../../assets/github-ai-radar-2026-11-15-r26-abyssalgarden-roomatdawn.svg)

---

## 📌 一、核心结论速览（Executive Summary — 先看结论再看细节）

1. **一句话讲透本质（What & Why）**：
   - **`Noniv/abyssal-garden` 是什么？** 它是仅凭 **一个 `96 KB` 的单文件 `index.html`（0 张图片、0 个 3D 模型、0 个音频文件、0 个第三方 3D 引擎库）**，直接调用浏览器原生 **WebGPU (`WGSL`) + Web Audio API** 实时生成 **约 200 万片随洋流摇曳并闪烁金绿微光的海藻森林、穿透波浪水面的丁达尔光柱与海底焦散、木质沉船、巨型石雕鲸尾、滑翔蝠鲼、紫光洞穴与鲸鸣气泡合成音景** 的程序化神作。它在 RTX 5070 Ti 上以 `2560x1440` 跑出 **`180 fps`**，同时通过“**开始菜单背后模糊预运行自动定标 + 驱动崩溃自动降档记忆（`High -> Medium -> Low`）**”，让连 4GB 内存的百元低端手机（Galaxy A16）也能流畅游览！
   - **`Leonxlnx/room-at-dawn` (`6:51 — a room at dawn`) 是什么？** 它是用 **100% 纯代码（Three.js，同样 0 外部模型、0 图片贴图、0 HDRI）** 构建的 **照片级清晨 6:51 卧室交互漫游 + 4K HDR10（`3840x2160`，`PQ / BT.2020` 10-bit HEVC）电影母带渲染管线**。为什么一个没有任何实时光源（No real-time lights）的网页场景能呈现出令人屏息的清晨窗光漫反射与被褥褶皱质感？因为它内置了一个基于 Web Workers 与 `three-mesh-bvh` 的 **多重要性采样（MIS）窗口下一事件估计（NEE）CPU 路径追踪器**，将每个顶点的**辐照度（Irradiance）与主导光线方向（Dominant Direction）**烘焙进紧凑的 `public/bake/gi.bin`——不仅免去了噩梦般的 Lightmap UV 展开，更让 Canvas2D/噪声实时合成的亚麻编织、橡木地板与针织毛毯法线贴图（Normal Maps）依然具备真实高光凹凸响应！
2. **为什么值得 AI SA 今晚立刻掌握？**
   - 当我们让大模型（Claude / GPT / Gemini）生成 3D 网页或数字孪生场景时，最大的瓶颈是 **“大模型不会手绘 UV 贴图，也没法随代码附带 200MB 的 `.glb` 模型包”**。这两个项目给出了 Coding Agent 生成顶级 3D 视觉产物的终极答案：**用数学函数合成几何/纹理/声音 + 用自适应 WebGPU 治理帧率（`abyssal-garden`）+ 用免 UV 的逐顶点定向全局光照烘焙出电影级真实感（`room-at-dawn`）**。
3. **定量收益摘要（Closed-Form FinOps Ledger `CLAIM-20261115-R26-ABYSSALGARDEN-ROOMATDAWN`）**：
   - 在每月承载 `500,000` 次 3D 交互展厅页面访问与交付 `40` 个照片级 4K HDR10 建筑/产品数字场景下（图形/全栈工程师时薪 `$100.00/hr`，底层宿主机硬件成本 `not_measured`），从“分发 150MB glTF/KTX2 资源包高昂 CDN 流量 + 手工展 UV 烘焙光照贴图（Path A，`$6,040.00/mo`）”切换到“`abyssal-garden` 96KB 零资产 WebGPU + `room-at-dawn` 逐顶点定向 GI 与子帧累积 4K 渲染管线（Path C，`$460.00/mo`）”，**每月净省 `$5,580.00`（`-92.38%`），年化节省 `$66,960.00/yr`，每月释放 `36.5` 小时展 UV 与移动端闪退排障工时（`-91.25%`）**。

---

## 🔍 二、第一性原理灵魂三问（Q1–Q3 Deep Dive）

### Q1：`abyssal-garden` 是如何把 200 万片海藻、沉船、丁达尔光柱和立体声景塞进 `96 KB` HTML，还能从 RTX 5070 Ti（180fps）一直兼容到低端手机的？

- **三大底层系统工程秘诀（`source/src/`）**：
  1. **GPU 启动期地形雕刻与两百万实例化植被（`world.js` + `shaders.js`）**：
     - 页面打开瞬间，直接在显卡上用噪声与距离场雕刻出岩壁、拱门、隧道与海床，并散布约 `2,000,000` 片海藻叶片、数万块岩石与数千条游鱼；同时对岩壁施加**滑动碰撞响应（Sliding Collision）**，碰到礁石会顺滑擦过而不会卡死，且保证玩家能穿过每一个石拱与洞穴。
  2. **开始菜单背后的“隐形预校准”与崩溃自愈降级（`quality.js`）**：
     - 当用户刚打开网页停留在模糊的“Dive in”开始菜单时，**3D 场景其实已经在毛玻璃背景后全速运行并自动压测本机显卡**！渲染器按小步长优先微调内部分辨率，再微调远处植被/岩石裁剪距离以锁定 60 fps。
     - 如果在某台老设备上加载 `High` 档导致浏览器标签页崩溃或显卡驱动重置（Device Lost），下次打开页面时会自动降一档（`High -> Medium -> Low`）重启并持久化记忆该设备最佳档位。
  3. **内置确定性飞行基准测试（`dev.js`）**：
     - 运行 `npm run build:dev` 生成 `dev.html` 后，按 `F` 键沿预设的 1 分钟全局航线自动巡航，按 `B` 键将该航线作为确定性 GPU/帧耗时 Benchmark 跑分输出。

### Q2：为什么没有实时光源、也不展 UV 光照贴图的 `room-at-dawn`，能在核显（Radeon 780M）上跑出路径追踪级清晨卧室，并导出 4K HDR10 电影？

- **攻克“免 UV 全局光照 + 过程化纹理凹凸感”的核心武器**：
  1. **逐顶点辐照度 + 主导光向烘焙（Per-Vertex Irradiance + Dominant Direction in `gi.bin`）**：
     - 传统烘焙（Lightmap Baking）要求每个 3D 模型必须具备不重叠的 2D UV 展开图，对程序化生成的 11.8 万片树叶、悬垂绿萝藤蔓（悬链线 Catenary Curves）与褶皱被褥几乎不可行。
     - `room-at-dawn` 编写了一个运行在 Web Workers 中的轻量 CPU 路径追踪器（基于 `three-mesh-bvh`）：第一遍追踪完整天空光路径，第二遍针对**窗户开口执行下一事件估计（Next-Event Estimation，NEE）并通过多重重要性采样（MIS）融合**。
     - 最关键的一步：它在每个顶点上不仅存储漫反射颜色（Irradiance），还存储了**入射光的主导方向向量（Dominant Direction）**！因此，由 Canvas2D 和噪声函数在加载期实时绘制的亚麻布纹、粗针织毛毯与木屑壁纸法线贴图（Normal Maps），依然能根据主导光向算出细腻的明暗凹凸！
  2. **纯时间函数风场（Pure-Time Gust Shader）与子帧抖动 4K HDR10 离线渲染（`tools/film.mjs`）**：
     - 窗外树冠倾斜 -> 主干 -> 树枝 -> 11.8 万片树叶颤动完全写成时间 $t$ 的纯函数（无有状态物理累积）。这使得离线电影渲染器（`node tools/film.mjs`）可以在每一帧内部对空间位置、薄透镜景深光圈（Thin-Lens DoF）与 **180° 快门开角时间段** 进行多次抖动子帧采样求平均，最后通过 `ffmpeg` 直接封装为 `3840x2160` **HDR10（PQ / BT.2020，10-bit HEVC）** 大片！

### Q3：AI SA 如何将这两套“纯代码零外部资产 3D 架构”应用到日常技术方案演示与可视化交付中？

- **极速零依赖交付物（Single-File Deliverable）**：参考 `abyssal-garden`，将交互式 3D 拓扑/数据深海演示编译为 `<100 KB` 的单文件 `index.html`，邮件或内网双击即开，自带 `quality.js` 三档自适应降级与 `B` 键性能基准；
- **高画质产品/建筑数字孪生**：参考 `room-at-dawn`，用种子化程序几何 + `three-mesh-bvh` 逐顶点定向 GI 取代笨重的外部资产包，兼顾核显 60fps 实时漫游与 `film.mjs` 4K HDR10 宣传片一键渲染。

---

## 🧭 三、架构拓扑与选型决策树（Mermaid Decision Tree）

```mermaid
flowchart TD
    Start["AI SA 纯代码 3D 交互世界与电影级渲染选型需求"] --> SceneType{"核心场景诉求是什么？"}

    SceneType -->|"要求单个 <100KB HTML 离线双击即开<br/>承载百万级动态实例、碰撞漫游与自适应帧率"| Abyss["选用 Noniv/abyssal-garden<br/>(原生 WebGPU WGSL · 96KB 单文件 · 2M 海藻)"]
    SceneType -->|"要求照片级室内全局光照、复杂织物/植被纹理<br/>兼顾核显实时漫游与 4K HDR10 电影导出"| Dawn["选用 Leonxlnx/room-at-dawn<br/>(Three.js 程序几何 · BVH 逐顶点定向 GI · 4K HDR10)"]

    Abyss --> AStep1["1. 启动期 GPU 雕刻地形并实例化 200 万片海藻与生物"]
    AStep1 --> AStep2["2. 开始菜单毛玻璃背后预运行，自动校准分辨率与视距"]
    AStep2 --> AStep3["3. 遇驱动重置自动降档 (High -> Med -> Low) 并记忆"]
    AStep3 --> AStep4["4. 开发态按 F 巡航 / 按 B 运行确定性 GPU 帧时间基准"]

    Dawn --> DStep1["1. 程序化生成褶皱被褥、悬链线藤蔓与 11.8 万树叶 + Canvas2D 纹理"]
    DStep1 --> DStep2["2. Web Worker + three-mesh-bvh 窗户 MIS/NEE 烘焙逐顶点定向 gi.bin"]
    DStep2 --> DStep3["3. 实时模式：核显 (Radeon 780M) 60fps 漫游 + 法线贴图受光"]
    DStep3 --> DStep4["4. 电影模式：tools/film.mjs 子帧抖动累积 DoF/180° 快门 -> 4K HDR10"]
```

---

## 📊 四、同类方案核心能力对比矩阵（Comparison Matrix）

| 评估维度 | 传统 150MB glTF/KTX2 + 手工展 UV 烘焙 (Path A) | Draco 压缩静态网格 + 未烘焙实时阴影 (Path B) | `abyssal-garden` + `room-at-dawn` 纯代码管线 (Path C) |
| :--- | :--- | :--- | :--- |
| **首屏分发体积与外部资源依赖** | ❌ `50–200 MB` 模型/贴图/音频包，内网或弱网加载极慢 | ⚠️ `10–30 MB` 压缩网格，仍需外链纹理与 HDRI | ✅ **`96 KB` 单 HTML 文件（`abyssal-garden`），`0` 外部图片/模型/音频文件** |
| **Coding Agent 可编写性与版本控制友好度** | ❌ 二进制 `.glb`/`.png` 无法由文本 LLM 直接生成或 Diff | ⚠️ 依赖外部 DCC 工具导出 | ✅ **100% 纯 JS / WGSL 源码，Git Diff 清晰，Coding Agent 可直接调参重构** |
| **全局光照（GI）质量与 UV 展开成本** | ⚠️ 画质好但必须手工拆分不重叠 Lightmap UV，极易漏光 | ❌ 仅有生硬的实时阴影与廉价屏幕空间 AO | ✅ **`three-mesh-bvh` 窗户 MIS 路径追踪烘焙逐顶点辐照度+主导光向（免 UV 且保留法线凹凸）** |
| **跨设备抗崩溃自愈与核显流畅度** | ❌ 移动端/4GB 老电脑直接爆显存白屏 | ⚠️ 核显（如 Radeon 780M）帧率剧烈掉帧 | ✅ **菜单后预运行定标 + 崩溃自动降档记忆；Radeon 780M 核显流畅运行** |
| **电影级离线母带导出能力** | ❌ 需手动导入 Blender/Unreal 重新布光渲染 | ❌ 仅能录屏，存在锯齿且无真运动模糊 | ✅ **同一套 Web 代码通过 `tools/film.mjs` 子帧累积直出 4K HDR10 (`PQ/BT.2020`)** |

---

## 📈 五、7-Card 定量洞察与闭式 FinOps 账本（Quantitative Insights & FinOps Ledger）

### 5.1 7-Card 核心评测摘要（对标 Model Benchmark Report Standard）

1. **Card 1（Overview & Workbench）**：针对每月 `500,000` 次 3D Web 展厅访问与 `40` 个 4K HDR10 数字场景生产任务，Path C 将月度总成本从 `$6,040.00` 降至 `$460.00`（节省 `-92.38%`）。
2. **Card 2（Single-Case Deep Dive）**：`abyssal-garden` 在 `96 KB` 单文件中驱动 200 万海藻叶片并在 RTX 5070 Ti 达 `180 fps @ 1440p`（Galaxy A16 低端机 `20 fps`）；`room-at-dawn` 用纯代码生成 11.8 万片树叶与逐顶点 `gi.bin`，在 Radeon 780M 核显流畅漫游并导出 45 秒 4K HDR10 电影。
3. **Card 3（Evaluation Matrix）**：覆盖单文件打包体积（`96 KB`）、外部图片/模型/音频依赖数（`0`）、程序化植被规模（`2,000,000` 海藻叶片 / `118,000` 树叶卡）及导出母带规格（`3840x2160` HDR10 PQ BT.2020）。
4. **Card 4（Under the Hood）**：`abyssal-garden` 直接操作原生 WebGPU WGSL 与 Web Audio API；`room-at-dawn` 结合 `three-mesh-bvh` Web Workers 烘焙与子帧抖动累积管线。
5. **Card 5（Robustness Check）**：模拟显卡驱动超时重置后，`abyssal-garden` 的 `quality.js` 自动从 `High` 降级至 `Medium`/`Low` 并写入浏览器持久化存储，防止二次闪退。
6. **Card 6（Latency & Labor Scaling）**：每月因手工展 Lightmap UV、压缩百兆资产包与排查移动端显存崩溃耗费的工时从 `40.0h` 降至 `3.5h`（净省 `36.5h/mo`，`-91.25%`）。
7. **Card 7（My Take — Good Fit vs Not For）**：
   - ✅ **Good Fit**：需要极致轻量分发（`<100KB`）的 WebGPU 交互演示、由 Coding Agent 全代码生成的 3D 环境、以及需要从同一份 Web 代码同时产出实时漫游与 4K HDR10 宣传片的项目。
   - ⛔ **Not For**：必须精确还原特定工业 CAD 零件毫米级公差的非程序化静态展示（此类仍需导入 CAD 转换网格）。

### 5.2 闭式参数化 FinOps 账本（`CLAIM-20261115-R26-ABYSSALGARDEN-ROOMATDAWN`）

> **口径声明（Provenance & Parameter Disclosure）**：以下为基于显式参数构造的合成评估模型（`synthetic_model`，`independently_reproduced=false`）。设每月服务 `N_view = 500,000` 次 3D 页面访问、交付 `N_hdr = 40` 个 4K HDR10 场景渲染，工程师折算时薪 `R_eng = $100.00/hr`，底层宿主机硬件成本记为 `not_measured`。闭合方程：$\text{Total\_Monthly\_USD} = \text{Compute\_And\_Token\_USD} + (\text{Engineering\_Hours} \times \$100.00)$。

| 方案路径（Path） | 月度 CDN 流量与云渲染开销（USD） | UV 烘焙与跨端适配排障工时（Hours/mo） | 工程人工成本（`@ $100.00/hr`） | 月度总成本（Total Monthly USD） | 相对 Path A 净节省（USD / %） |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A：150MB 资产包 CDN 分发 + 手工展 UV 烘焙与云渲染** | `$2,040.00` | `40.0h` | `$4,000.00` | **`$6,040.00`** | Baseline (`0.00%`) |
| **Path B：Draco 压缩网格 + 未烘焙实时阴影手动调优** | `$950.00` | `19.0h` | `$1,900.00` | **`$2,850.00`** | `-$3,190.00` (`-52.81%`) |
| **Path C：`abyssal-garden` 96KB + `room-at-dawn` 管线（推荐）** | `$110.00` | `3.5h` | `$350.00` | **`$460.00`** | **`-$5,580.00` (`-92.38%`)** |

---

## 🛠️ 六、15 分钟极速落地 Checklist（15-Minute Rollout Checklist）

- [ ] **Step 1（3 分钟）：克隆 `abyssal-garden` 并编译 `96 KB` 单文件 `index.html` 与基准测试版 `dev.html`**
  ```bash
  git clone https://github.com/Noniv/abyssal-garden.git
  cd abyssal-garden/source
  npm install
  npm run build && npm run build:dev
  ```
- [ ] **Step 2（4 分钟）：在 Chrome/Edge 中打开 `dev.html`，按 `F` 巡航、按 `B` 运行 1 分钟确定性 WebGPU 基准跑分**
  ```bash
  # 在浏览器打开 dev.html，点击 Dive in 后按 H 查看实时统计，按 B 记录帧耗时与 GPU 耗时
  ```
- [ ] **Step 3（4 分钟）：克隆并启动 `room-at-dawn`，在 `http://127.0.0.1:5319` 体验逐顶点定向 GI 与 `C` 键电影运镜**
  ```bash
  git clone https://github.com/Leonxlnx/room-at-dawn.git
  cd room-at-dawn
  npm install && npm run dev
  ```
- [ ] **Step 4（4 分钟）：运行 CPU BVH 光照重烘焙与子帧累积 4K HDR10 镜头渲染**
  ```bash
  node tools/shot.mjs bed wide
  # 可选重烘焙：node tools/shot.mjs --bake 256
  # 渲染并合成 HDR10 + SDR 成片：node tools/film.mjs && node tools/film.mjs --concat
  ```
