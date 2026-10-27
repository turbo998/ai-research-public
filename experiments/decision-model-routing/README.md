# Decision-model routing experiment

**Offline by default；2026-10-14 用户批准四模型真实 pilot。** 主 harness 仍为 Python 3.12 标准库；仅本地 Strands 服务在忽略的隔离 venv 安装重依赖。四类决策任务、客服/RAG 两场景，Jev 不阻塞已启用的 `strands, decision1, small, strong`。研究入口：[Jev / Decision-1 / Strands / Foundry](../../docs/research/decision-model-routing/README.md)。

## 文件与无网络运行

| 文件 | 职责 |
| --- | --- |
| `contracts.py` | 严格 JSON/question/answer、hash、私有路径与脱敏 |
| `providers.py` | TypeSafe/Foundry/明确回环 Strands 协议、身份、health、attempt/usage/latency/pacing |
| `azure_auth.py` | 显式订阅/tenant 的 Entra 内存缓存、五分钟提前刷新；不登录、不取 key |
| `budget.py` | Decimal + SQLite US$50 原子预留/重试/unknown-charge/restart lock |
| `data.py` | 原创 bilingual corpus/rows、固定检索、mock 权限、有限独立验收 |
| `metrics.py` | 分母、质量/概率/成本/尾延迟和配对 template bootstrap |
| `runner.py` | dataset/preflight/management/smoke/freeze/oracle/decision/e2e/calibrate/ablation/analyze |
| `contract.json` | 用户批准的一轮 paired stratified 四模型 pilot；源码/配置/IDs 冻结 |
| `private-config.example.json` | 空安全模板，`pricing.verified=false`；不是可调用配置 |
| `data` | 920 SYNTHETIC rows、corpus、确定性 manifest |
| `results` | 仅脱敏的真实 rows/analysis 与离线 validation；状态以实际报告为准 |

从本隔离 worktree 根目录执行：

```powershell
python -B -m unittest discover -s tests -p test_decision_model_routing.py
python -B experiments\decision-model-routing\runner.py dataset --check
python -B experiments\decision-model-routing\runner.py preflight
python -B experiments\decision-model-routing\runner.py analyze
```

缺 private config 时 `preflight` **exit 2** 并写明 blocker；这是预期阻塞，不是成功 smoke。`dataset --check` 不改数据、不联网。`dataset` 可重建原创 artifacts；任何 code/data/contract 变化都使既有 freeze 失效。

## 私有配置与真实恢复

只接受 `.cache\decision-model-routing\private-config.json` 或该忽略目录内另一**用户选定**文件。不会加载 ambient `.env`、扫描其他项目、枚举订阅或查 Key Vault。先由用户提供安全路径或将空模板复制到此目录并填入已选配置；**不要将密钥/资源值贴入聊天或 commit**。

| 配置字段 | 必须核验的内容 |
| --- | --- |
| `schema_version` / `total_budget_usd` | `1` / `"50"`；不能扩额 |
| `client_region` | 粗粒度客户端地区；不含主机/用户名 |
| `approved_contract_sha256` | 用户审阅后的 exact `contract.json` SHA256，不自动确认 pilot |
| `models` / `enabled_models` | 明确启用四个 ready 角色；disabled Jev 不读取 key/pricing，不默换 provider |
| `endpoint` | 云端官方 HTTPS root；Strands 仅明确的 `http://127.0.0.1:<port>`，不允许 localhost/公开 HTTP/任意 path |
| `deployment` / `model` / `version` | 精确实际 deployment 与固定底层 model/version 分离 |
| `resource_id` / `region` / `sku` | 三 Azure 角色的现有 account ID、resource region、deployment SKU；仅留本地 |
| `auth.kind` / `auth.env` | 云端 `api-key` / `bearer`，只读 named env/scoped Entra；Strands 固定 `none` / 空 env，拒收 cloud credentials |
| `azure_identity` | 可选的显式 Entra 配置：`subscription_id`、`tenant_id`、`token_resource`、`credential_env`；所有 Azure 角色须匹配订阅和 bearer 名称 |
| `max_completion_tokens` / `reasoning_effort` | 现有生成部署支持的总输出/推理 cap 与 effort；native 不发送推理参数 |
| `pricing.verified` / `source` / `verified_at` | 用户本轮批准已核验公开 Standard Global estimate basis；不伪装账户报价或账单 |
| `billing_semantics` / `ceiling_evidence` | cache/read/write/output 语义和服务 hard bounds 的证据 |
| `input/cached/cache_write/output/reasoning_usd_per_million` | 显式 Decimal 字符串，未知不能设零；reasoning rate=output rate |
| `cache_write_policy` | 已核验 `not_applicable` 或 `exclusive_input_category` |
| `max_billable_input_tokens` | 至少完整服务 conservative bound：Jev 64,000、Decision-1 32,768、mini 400,000、Sol 1,050,000；smoke observed tokens 不是 hard ceiling |
| `max_billable_output_tokens` | 生成与 `max_completion_tokens` 相同，涵盖 reasoning/visible/format；native 收费语义需核验 |
| strong `context_price_policy` / `context_price_evidence` | `conservative_all_contexts` 与所选 SKU 全 context 类别费率上界；不猜 short/long 阈值 |
| Strands `checkpoint_revision` / `ordinal_smoothing` | 固定 public safetensors revision、0.1 smoothing，health + runtime/source receipt |
| `min_interval_seconds` | 本轮 Azure gen7s、Decision-1 1.1s；真实等待进入总延迟，network/server timing 分列 |

固定 public IDs/versions 已在模板中，不含 Azure 资源名。Jev 的供应商管理区域/账户 SKU 也需如实记录，不假装知道物理推理位置。未设置 `azure_identity` 时沿用显式静态环境认证；TypeSafe 始终使用 `TYPESAFE_API_KEY`。`verify-management` 另需用户已有 Azure CLI 身份与选定部署只读权限，每个 GET 显式指定所选 resource ID 的订阅。

若已选账户禁用 key auth，可在**忽略的私有配置**设置 `azure_identity`：`token_resource` 必须为 `https://cognitiveservices.azure.com`，`credential_env` 为共同的 `DECISION_ROUTING_*` 名称，三个 Azure 角色均设置 `auth.kind=bearer`。只使用已有 CLI 登录；不会执行 login、切换默认订阅、取 key 或变更角色/安全设置。

`load_config` / offline preflight 只校验 scope，不获取 Entra token，因此 `ready-for-budgeted-smoke` 不是 data-plane RBAC 证明。实际 client 在首次预留前及**每个 HTTP attempt（包括重试）**读取新鲜 headers；距离 UTC `expires_on` 不足或等于五分钟时刷新，并核对响应 subscription/tenant/token type。所有 Azure 角色和消融 worker 共享线程安全的内存 provider；刷新失败不会使用旧 token 或静态 key 兜底，不发送该 attempt。已发生调用的 unknown-charge 预留保留，错误显式记为 `authentication-refresh`；未发送记录标记 `http_attempted=false`，单列 `authentication_blocked_attempts`，不充作 API attempts 或供应商 HTTP 失败。

CLI token 输出仅在内存解析，不写配置/报告或更改 live process 环境。每个轮换 token 在 HTTP 发送前加入 raw/public redaction，包含 response echo 和 base64 raw body。fake-token/clock/transport 回归验证边界与错误行为；本轮已在真实 Azure 推理路径使用，不将其等同于生产身份保证。

本轮选定管理核验、本地 owned health、公开费率证据和用户执行批准均已准备，真实 smoke、calibration 与全部544个formal jobs已完成，三个Azure数据面实际可用，本地服务已停止。未取 keys、未修改 RBAC/网络安全；目录角色查询失败不被冒充权限证明。Jev 仍未注入，不计本轮结果。每个请求前按 hard bounds 预留全部 retry/in-flight，共享原 SQLite；unknown failures 不释放成假余额，不删账本恢复。公开 estimate basis 不等于已对账账户收费。脱敏records可在新clone中离线复算，示例见[Results](../../docs/research/decision-model-routing/results.md#离线复算与当前-hashes)。

### 本地 Strands runtime

安装/权重/venv/receipt 均在 `.cache\decision-model-routing`。使用固定官方源码 commit 与固定 Hub/base revisions；Apache-2.0、公有非 gated 权重，禁止隐式 HF token 搜索。CPU 以 fp32 运行，6 threads、prefix cache、text-only；`--strict-window` 防止超长 state 被静默截断。`/health` 只有元数据，不作 benchmark 输出。

```powershell
# 已安装的官方 CLI；SNAPSHOT 为已核验的固定 revision 本地目录，不是移动 Hub main。
.cache\decision-model-routing\venv-strands\Scripts\strands-decider.exe serve $SNAPSHOT `
  --device cpu --host 127.0.0.1 --port 8000 --strict-window --max-batch 8 `
  --model-name strands-decider-2B-qwen3.5-v1-2610
```

Windows ARM64 没有可用 native torch wheel，本轮使用该目录内的 x64 CPython 3.12.10 / torch2.14.1+cpu。安装中遇到 TLS transport 和 Windows long-path 错误，使用 Python 的验证 TLS 及 `\\?\` 路径解决，未关闭证书检查、改注册表、全局 PATH 或换模型。权重加载 offline，不临时拉取未固定 base；后台进程仅用于本任务并在结束后停止。具体 installed source / safetensors hashes 在忽略 receipt，公开 checkpoint/source IDs 在 research evidence。

### 干净起点的顺序命令

以下为真实执行与复现顺序；实际完成阶段见 Results。不得在已有 formal phase claim 上重跑；每行非零立即停止。`verify-management` 只读取三个精确部署/所选 account 加本地 health，不做 discovery/provisioning；`preflight` 不联网，失败 smoke 返回非零且不能 freeze。

```powershell
python -B experiments\decision-model-routing\runner.py dataset --check
python -B experiments\decision-model-routing\runner.py verify-management --config .cache\decision-model-routing\private-config.json
python -B experiments\decision-model-routing\runner.py preflight --config .cache\decision-model-routing\private-config.json
python -B experiments\decision-model-routing\runner.py smoke --live --config .cache\decision-model-routing\private-config.json
python -B experiments\decision-model-routing\runner.py freeze --config .cache\decision-model-routing\private-config.json
python -B experiments\decision-model-routing\runner.py run --live --suite oracle --split calibration --config .cache\decision-model-routing\private-config.json
python -B experiments\decision-model-routing\runner.py run --live --suite decision --split calibration --config .cache\decision-model-routing\private-config.json
python -B experiments\decision-model-routing\runner.py run --live --suite e2e --split calibration --config .cache\decision-model-routing\private-config.json
python -B experiments\decision-model-routing\runner.py calibrate
python -B experiments\decision-model-routing\runner.py run --live --suite oracle --split test --config .cache\decision-model-routing\private-config.json
python -B experiments\decision-model-routing\runner.py run --live --suite decision --split test --config .cache\decision-model-routing\private-config.json
python -B experiments\decision-model-routing\runner.py run --live --suite e2e --split test --config .cache\decision-model-routing\private-config.json
python -B experiments\decision-model-routing\runner.py analyze
```

freeze 需完整 real smoke、price-based projection ×2、matching code/data/contract/config hash、exact reviewed contract SHA。test 需完整 calibration 与 frozen thresholds。当前模板样本不支持 2pp 非劣/速度成本胜出，即使能运行也只是 pilot。

Formal phase 一次性 claim；**不支持对中断 phase 自动续跑**。发生中断保留 attempts/raw/ledger/claims，分析 partial/unattempted；不能删 claims 重跑挑结果或新建账本重置累计 US$50。本轮 auxiliary cap=0；调用 ablation 明确 blocked，不额外扩展消融。

## 协议、证据与解释

Jev / Strands：`/v1/systemone`；Decision-1：`/providers/microsoft/v1/systemone`，均使用 state+questions。生成：`/openai/v1/chat/completions`，strict schema、stream=false、n=1、explicit total-output cap，不添加未验证温度/tools 参数。相同生成池/local retrieval，无 response cache。Strands native4dp 字段使用有证据的半单位误差边界验证，原值不归一化；其它 provider 保留原 strict tolerance。native cache details 如可得则记录。

本地 `.cache\decision-model-routing\runs` 保留 per-attempt raw（剔除认证）、identity、usage、tokens、latency、cost、exact selected IDs 和 manifests。commit 仅允许审阅的脱敏 records/analysis，不提交 raw/config/resource IDs、权重或 venv。分析核对 raw hashes/phase/arm/case，拒绝 replay/mock 冒充 live timing。server-reported Strands latency、network latency、auth/pacing/retry/e2e latency 不混为 GPU compute benchmark。

原生 probabilities/confidence 不是测得正确率；LLM-generated probabilities 不是 logits；Noul 不 invent confidence。有限验收不是完整人类语义/安全判断，English machine identifiers 不等于自然语言未本地化。失败保留质量分母；缺概率不补概率；accepted=0 返回 NA。详情见[benchmark](../../docs/research/decision-model-routing/benchmark.md)和[results](../../docs/research/decision-model-routing/results.md)。
