# 企业级 Azure Cloud & AI 解决方案架构师（SA）技术选型指南库（62 篇中英双语）

> 🌐 **Language / 语言切换**: **[🇨🇳 中文目录 (README.md)](README.md)** | **[🇬🇧 English Catalog (README.en.md)](README.en.md)** | **[⬅️ 返回 Azure AI Agent Infra 主手册](../README.md)**

本目录汇集 **62 篇面向企业级云与 AI 解决方案架构师（Cloud & AI Solution Architect）的实战架构选型 FAQ**（全部提供中英双语版本）。每篇指南均围绕真实客户架构评审中的高频权衡问题展开，统一包含：**一页纸执行摘要、多维选型对比矩阵、推荐参考架构、反模式避坑清单与上线验收准则**。

## 1. Agent 计算运行时与沙箱托管选型

| 选型主题 | 中文版 | English |
| :--- | :---: | :---: |
| **Foundry Agent Service vs ACA Dynamic Sessions vs AKS vs Functions：企业 Agent 运行时托管选型 FAQ** | [中文](foundry-agent-service-vs-aca-vs-aks-vs-functions-runtime-hosting-selection-faq.md) | [EN](foundry-agent-service-vs-aca-vs-aks-vs-functions-runtime-hosting-selection-faq.en.md) |
| **Round 1108 / Cycle 2513 · Azure AI Agent Infra FAQ（zh-CN）** | [中文](foundry-aca-aks-functions-enterprise-hosting-selection-faq.md) | [EN](foundry-aca-aks-functions-enterprise-hosting-selection-faq.en.md) |
| **ACA Dynamic Sessions vs Foundry Code Interpreter vs AKS Sandbox：企业代码执行与不可信沙箱选型 FAQ** | [中文](aca-dynamic-sessions-vs-foundry-code-interpreter-vs-aks-sandbox-selection-faq.md) | [EN](aca-dynamic-sessions-vs-foundry-code-interpreter-vs-aks-sandbox-selection-faq.en.md) |
| **Durable Functions vs Logic Apps vs Temporal vs Service Bus：长周期 Agent 编排与 HITL 引擎选型 FAQ** | [中文](durable-functions-vs-logic-apps-vs-temporal-vs-service-bus-long-running-agent-selection-faq.md) | [EN](durable-functions-vs-logic-apps-vs-temporal-vs-service-bus-long-running-agent-selection-faq.en.md) |
| **Round 1107 / Cycle 2512 · Azure AI Agent Infra FAQ（zh-CN）** | [中文](enterprise-agent-framework-runtime-memory-rag-platform-selection-faq.md) | [EN](enterprise-agent-framework-runtime-memory-rag-platform-selection-faq.en.md) |
| **Copilot Studio Computer Use vs PAD RPA vs Playwright MCP vs 绞杀者：无 API 老系统自动化选型 FAQ（Round 1146）** | [中文](copilot-studio-computer-use-rpa-vs-power-automate-vs-playwright-mcp-legacy-ui-automation-selection-faq.md) | [EN](copilot-studio-computer-use-rpa-vs-power-automate-vs-playwright-mcp-legacy-ui-automation-selection-faq.en.md) |

## 2. 模型托管、分层路由与 FinOps 成本优化

| 选型主题 | 中文版 | English |
| :--- | :---: | :---: |
| **Round 1124 · Cycle 2529** | [中文](foundry-aoai-ptu-vs-serverless-maas-vs-aks-vllm-kaito-model-serving-selection-faq.md) | [EN](foundry-aoai-ptu-vs-serverless-maas-vs-aks-vllm-kaito-model-serving-selection-faq.en.md) |
| **ACA Serverless GPU vs Foundry Managed Endpoint vs AKS+KAITO：企业专精模型托管选型 FAQ（Round 1150）** | [中文](aca-serverless-gpu-vs-foundry-managed-endpoints-vs-aks-kaito-custom-model-hosting-selection-faq.md) | [EN](aca-serverless-gpu-vs-foundry-managed-endpoints-vs-aks-kaito-custom-model-hosting-selection-faq.en.md) |
| **aoai-nano-mini-vs-foundry-phi4-slm-vs-aks-kaito-vs-store-edge-tiered-routing-selection-faq-r1135** | [中文](aoai-nano-mini-vs-foundry-phi4-slm-vs-aks-kaito-vs-store-edge-tiered-routing-selection-faq.md) | [EN](aoai-nano-mini-vs-foundry-phi4-slm-vs-aks-kaito-vs-store-edge-tiered-routing-selection-faq.en.md) |
| **Round 1127 · Cycle 2532** | [中文](apim-semantic-cache-vs-aoai-prompt-caching-vs-batch-api-finops-optimization-selection-faq.md) | [EN](apim-semantic-cache-vs-aoai-prompt-caching-vs-batch-api-finops-optimization-selection-faq.en.md) |
| **Prompt+Structured Output vs RAG vs SFT vs RFT：企业模型定制与领域适配选型 FAQ** | [中文](prompt-structured-output-vs-rag-vs-aoai-finetuning-sft-rft-selection-faq.md) | [EN](prompt-structured-output-vs-rag-vs-aoai-finetuning-sft-rft-selection-faq.en.md) |
| **Round 1123 · Cycle 2528** | [中文](global-standard-vs-datazone-vs-regional-ptu-multi-region-bcdr-residency-selection-faq.md) | [EN](global-standard-vs-datazone-vs-regional-ptu-multi-region-bcdr-residency-selection-faq.en.md) |
| **Azure Load Testing + LLM 仿真靶场 vs PTU 溢出 + Chaos Studio：洪峰就绪选型 FAQ（Round 1154）** | [中文](azure-load-testing-llm-simulator-vs-ptu-overflow-chaos-studio-peak-readiness-selection-faq.md) | [EN](azure-load-testing-llm-simulator-vs-ptu-overflow-chaos-studio-peak-readiness-selection-faq.en.md) |
| **b2b-isv-saas-agent-monetization-apim-metering-marketplace-chargeback-architecture-selection-faq-r1139** | [中文](b2b-isv-saas-agent-monetization-apim-metering-marketplace-chargeback-architecture-selection-faq.md) | [EN](b2b-isv-saas-agent-monetization-apim-metering-marketplace-chargeback-architecture-selection-faq.en.md) |

## 3. 企业级 RAG、Microsoft Fabric IQ 与状态记忆底座

| 选型主题 | 中文版 | English |
| :--- | :---: | :---: |
| **Azure AI Search（Agentic Retrieval + Hybrid + Semantic Ranker）vs GraphRAG vs Microsoft Fabric OneLake/IQ vs Copilot Studio SharePoint Knowledge：企业级知识库、ACL 权限裁剪与混合 RAG 选型 FAQ** | [中文](ai-search-hybrid-vs-graphrag-vs-fabric-iq-enterprise-rag-selection-faq.md) | [EN](ai-search-hybrid-vs-graphrag-vs-fabric-iq-enterprise-rag-selection-faq.en.md) |
| **fabric-iq-ontology-vs-foundry-iq-knowledge-vs-graphdb-enterprise-semantic-layer-selection-faq-r1144** | [中文](fabric-iq-ontology-vs-foundry-iq-knowledge-vs-graphdb-enterprise-semantic-layer-selection-faq.md) | [EN](fabric-iq-ontology-vs-foundry-iq-knowledge-vs-graphdb-enterprise-semantic-layer-selection-faq.en.md) |
| **Round 1126 · Cycle 2531** | [中文](fabric-data-agent-vs-powerbi-semantic-dax-vs-nl2sql-warehouse-analytics-selection-faq.md) | [EN](fabric-data-agent-vs-powerbi-semantic-dax-vs-nl2sql-warehouse-analytics-selection-faq.en.md) |
| **Fabric OneLake Medallion vs Purview Lineage：企业 AI 知识库 Data Readiness 与垃圾进垃圾出防护选型 FAQ（Round 1160）** | [中文](fabric-onelake-medallion-data-quality-vs-purview-lineage-garbage-in-prevention-ai-readiness-selection-faq.md) | [EN](fabric-onelake-medallion-data-quality-vs-purview-lineage-garbage-in-prevention-ai-readiness-selection-faq.en.md) |
| **Azure Cosmos DB vs Azure Managed Redis vs PostgreSQL (pgvector) vs Blob Storage：企业级 Agent 会话状态与记忆分层选型 FAQ** | [中文](cosmos-vs-managed-redis-vs-pgvector-agent-state-memory-selection-faq.md) | [EN](cosmos-vs-managed-redis-vs-pgvector-agent-state-memory-selection-faq.en.md) |
| **Azure SQL Hyperscale Vector vs PostgreSQL pgvector vs Cosmos DiskANN vs 拆库检索：事务融合选型 FAQ（Round 1148）** | [中文](azure-sql-hyperscale-vector-vs-cosmos-diskann-vs-postgres-pgvector-transactional-htap-agent-selection-faq.md) | [EN](azure-sql-hyperscale-vector-vs-cosmos-diskann-vs-postgres-pgvector-transactional-htap-agent-selection-faq.en.md) |
| **cosmos-changefeed-vs-ai-search-pull-indexer-vs-eventgrid-push-realtime-rag-freshness-selection-faq-r1137** | [中文](cosmos-changefeed-vs-ai-search-pull-indexer-vs-eventgrid-push-realtime-rag-freshness-selection-faq.md) | [EN](cosmos-changefeed-vs-ai-search-pull-indexer-vs-eventgrid-push-realtime-rag-freshness-selection-faq.en.md) |
| **Cosmos Gremlin vs Fabric Graph vs GraphRAG：企业多跳关系推理选型 FAQ（Round 1152）** | [中文](azure-cosmos-gremlin-vs-fabric-graph-vs-ai-search-graphrag-supply-chain-risk-agent-selection-faq.md) | [EN](azure-cosmos-gremlin-vs-fabric-graph-vs-ai-search-graphrag-supply-chain-risk-agent-selection-faq.en.md) |
| **ai-search-multimodal-rag-vs-cu-figure-captioning-vs-colpali-engineering-drawing-selection-faq-r1129** | [中文](ai-search-multimodal-rag-vs-cu-figure-captioning-vs-colpali-engineering-drawing-selection-faq.md) | [EN](ai-search-multimodal-rag-vs-cu-figure-captioning-vs-colpali-engineering-drawing-selection-faq.en.md) |
| **Azure AI Content Understanding vs Azure AI Document Intelligence vs Azure OpenAI Vision（gpt-4.1/gpt-4o）vs 自建 MinerU/Docling/Unstructured：企业多模态文档与音视频智能（IDP）选型 FAQ** | [中文](content-understanding-vs-doc-intelligence-vs-gpt4o-vision-vs-mineru-idp-selection-faq.md) | [EN](content-understanding-vs-doc-intelligence-vs-gpt4o-vision-vs-mineru-idp-selection-faq.en.md) |
| **Document Intelligence Layout vs Foundry Content Understanding vs GPT-4o Vision：企业 IDP 选型 FAQ（Round 1156）** | [中文](document-intelligence-layout-vs-foundry-content-understanding-vs-gpt4o-vision-idp-selection-faq.md) | [EN](document-intelligence-layout-vs-foundry-content-understanding-vs-gpt4o-vision-idp-selection-faq.en.md) |
| **sharepoint-embedded-vs-blob-cmk-vs-cosmos-artifact-store-enterprise-document-lifecycle-selection-faq-r1140** | [中文](sharepoint-embedded-vs-blob-cmk-vs-cosmos-artifact-store-enterprise-document-lifecycle-selection-faq.md) | [EN](sharepoint-embedded-vs-blob-cmk-vs-cosmos-artifact-store-enterprise-document-lifecycle-selection-faq.en.md) |
| **Round 1104 / Cycle 2509 · Azure AI Agent Infra FAQ（zh-CN）** | [中文](storage-blob-abac-sas-delegation-worm-agent-artifacts-faq.md) | [EN](storage-blob-abac-sas-delegation-worm-agent-artifacts-faq.en.md) |

## 4. 多智能体编排框架、交互渠道与事件流架构

| 选型主题 | 中文版 | English |
| :--- | :---: | :---: |
| **Round 1109 / Cycle 2514 · Azure AI Agent Infra FAQ（zh-CN）** | [中文](maf-vs-langgraph-vs-crewai-vs-copilot-studio-orchestration-selection-faq.md) | [EN](maf-vs-langgraph-vs-crewai-vs-copilot-studio-orchestration-selection-faq.en.md) |
| **migration-autogen-semantic-kernel-langgraph-to-microsoft-agent-framework-enterprise-modernization-faq-r1132** | [中文](migration-autogen-semantic-kernel-langgraph-to-microsoft-agent-framework-enterprise-modernization-faq.md) | [EN](migration-autogen-semantic-kernel-langgraph-to-microsoft-agent-framework-enterprise-modernization-faq.en.md) |
| **Foundry Deep Research vs MAF Map-Reduce vs Agentic RAG：企业尽调深度研究选型 FAQ（Round 1149）** | [中文](foundry-deep-research-agent-vs-multi-agent-parallel-map-reduce-vs-rag-enterprise-due-diligence-selection-faq.md) | [EN](foundry-deep-research-agent-vs-multi-agent-parallel-map-reduce-vs-rag-enterprise-due-diligence-selection-faq.en.md) |
| **Round 1125 · Cycle 2530** | [中文](m365-copilot-agent-vs-copilot-studio-vs-teams-custom-app-vs-agui-web-channel-selection-faq.md) | [EN](m365-copilot-agent-vs-copilot-studio-vs-teams-custom-app-vs-agui-web-channel-selection-faq.en.md) |
| **salesforce-agentforce-vs-servicenow-nowassist-vs-dynamics-copilot-vs-custom-foundry-enterprise-crm-erp-selection-faq-r1133** | [中文](salesforce-agentforce-vs-servicenow-nowassist-vs-dynamics-copilot-vs-custom-foundry-enterprise-crm-erp-selection-faq.md) | [EN](salesforce-agentforce-vs-servicenow-nowassist-vs-dynamics-copilot-vs-custom-foundry-enterprise-crm-erp-selection-faq.en.md) |
| **eventhubs-fabric-rti-vs-servicebus-vs-eventgrid-proactive-streaming-agent-selection-faq-r1134** | [中文](eventhubs-fabric-rti-vs-servicebus-vs-eventgrid-proactive-streaming-agent-selection-faq.md) | [EN](eventhubs-fabric-rti-vs-servicebus-vs-eventgrid-proactive-streaming-agent-selection-faq.en.md) |
| **Round 1106 / Cycle 2511 · Azure AI Agent Infra FAQ（zh-CN）** | [中文](eventgrid-mqtt-servicebus-iot-edge-physical-ai-agent-telemetry-faq.md) | [EN](eventgrid-mqtt-servicebus-iot-edge-physical-ai-agent-telemetry-faq.en.md) |

## 5. 统一 AI 网关 (APIM)、MCP 工具治理与多云联邦

| 选型主题 | 中文版 | English |
| :--- | :---: | :---: |
| **Azure API Management（APIM AI Gateway）vs Azure AI Foundry Model Router vs LiteLLM / 开源自建 AI 网关 vs 应用直连 SDK：企业级多模型路由、PTU+PAYGO 溢出与 FinOps 选型 FAQ** | [中文](apim-ai-gateway-vs-litellm-vs-foundry-router-model-governance-selection-faq.md) | [EN](apim-ai-gateway-vs-litellm-vs-foundry-router-model-governance-selection-faq.en.md) |
| **apim-multi-cloud-aws-bedrock-gcp-vertex-azure-foundry-ai-gateway-selection-faq-r1145** | [中文](apim-multi-cloud-aws-bedrock-gcp-vertex-azure-foundry-ai-gateway-selection-faq.md) | [EN](apim-multi-cloud-aws-bedrock-gcp-vertex-azure-foundry-ai-gateway-selection-faq.en.md) |
| **Remote MCP on APIM vs OpenAPI Tools vs Logic Apps Agent Actions vs Power Platform Connectors：企业 Agent 工具集成与核心系统连接选型 FAQ** | [中文](mcp-on-apim-vs-openapi-tools-vs-logic-apps-vs-power-connectors-selection-faq.md) | [EN](mcp-on-apim-vs-openapi-tools-vs-logic-apps-vs-power-connectors-selection-faq.en.md) |
| **API Center+APIM vs Foundry Connected Tools vs 自建 MCP Registry：企业工具泛滥治理选型 FAQ（Round 1158）** | [中文](apim-mcp-registry-api-center-vs-custom-tool-gateway-enterprise-agent-tool-sprawl-selection-faq.md) | [EN](apim-mcp-registry-api-center-vs-custom-tool-gateway-enterprise-agent-tool-sprawl-selection-faq.en.md) |
| **apim-a2a-protocol-vs-foundry-connected-agents-vs-event-grid-cross-org-multi-agent-selection-faq-r1130** | [中文](apim-a2a-protocol-vs-foundry-connected-agents-vs-event-grid-cross-org-multi-agent-selection-faq.md) | [EN](apim-a2a-protocol-vs-foundry-connected-agents-vs-event-grid-cross-org-multi-agent-selection-faq.en.md) |
| **Round 1105 / Cycle 2510 · Azure AI Agent Infra FAQ（zh-CN）** | [中文](apim-wfq-token-bucket-tenant-fairness-slo-faq.md) | [EN](apim-wfq-token-bucket-tenant-fairness-slo-faq.en.md) |
| **Round 1103 / Cycle 2508 · Azure AI Agent Infra FAQ（zh-CN）** | [中文](afd-waf-botmanager-apim-agent-ingress-ddos-token-drain-faq.md) | [EN](afd-waf-botmanager-apim-agent-ingress-ddos-token-drain-faq.en.md) |

## 6. 零信任身份、网络隔离与 Purview / Defender 安全合规

| 选型主题 | 中文版 | English |
| :--- | :---: | :---: |
| **Round 1102 / Cycle 2507 · Azure AI Agent Infra FAQ（zh-CN）** | [中文](entra-agent-id-workload-federation-cae-jit-pim-faq.md) | [EN](entra-agent-id-workload-federation-cae-jit-pim-faq.en.md) |
| **Entra External ID CIAM vs B2B Guest vs OIDC换票网关：对客与伙伴智能体身份选型 FAQ（Round 1151）** | [中文](entra-external-id-ciam-vs-b2b-guest-vs-apim-subscription-b2c-partner-agent-identity-selection-faq.md) | [EN](entra-external-id-ciam-vs-b2b-guest-vs-apim-subscription-b2c-partner-agent-identity-selection-faq.en.md) |
| **graph-obo-vs-postgres-rls-vs-ai-search-trimming-vs-opa-abac-agent-authorization-selection-faq-r1142** | [中文](graph-obo-vs-postgres-rls-vs-ai-search-trimming-vs-opa-abac-agent-authorization-selection-faq.md) | [EN](graph-obo-vs-postgres-rls-vs-ai-search-trimming-vs-opa-abac-agent-authorization-selection-faq.en.md) |
| **private-link-vnet-standard-agent-setup-vs-managed-vnet-vs-apim-waf-zero-trust-network-selection-faq-r1136** | [中文](private-link-vnet-standard-agent-setup-vs-managed-vnet-vs-apim-waf-zero-trust-network-selection-faq.md) | [EN](private-link-vnet-standard-agent-setup-vs-managed-vnet-vs-apim-waf-zero-trust-network-selection-faq.en.md) |
| **Shared Hub vs Spoke Subscription vs Deployment Stamp：企业多租户 AI Landing Zone 选型 FAQ** | [中文](shared-hub-vs-spoke-subscription-vs-deployment-stamp-ai-landing-zone-selection-faq.md) | [EN](shared-hub-vs-spoke-subscription-vs-deployment-stamp-ai-landing-zone-selection-faq.en.md) |
| **企业 AI CoE Hub-Spoke Landing Zone vs 联邦业务线运营模式选型 FAQ（Round 1155）** | [中文](enterprise-ai-coe-hub-spoke-landing-zone-vs-federated-bu-operating-model-selection-faq.md) | [EN](enterprise-ai-coe-hub-spoke-landing-zone-vs-federated-bu-operating-model-selection-faq.en.md) |
| **Azure AI Content Safety vs NeMo Guardrails / Guardrails AI vs Microsoft Purview AI Hub vs Entra Agent Identity（OBO / Managed Identity）：企业级 Guardrails、数据安全与 Agent 身份治理选型 FAQ** | [中文](content-safety-vs-nemo-guardrails-vs-purview-agent-security-identity-selection-faq.md) | [EN](content-safety-vs-nemo-guardrails-vs-purview-agent-security-identity-selection-faq.en.md) |
| **purview-ai-compliance-vs-defender-for-cloud-ai-vs-custom-redteam-regulated-governance-selection-faq-r1131** | [中文](purview-ai-compliance-vs-defender-for-cloud-ai-vs-custom-redteam-regulated-governance-selection-faq.md) | [EN](purview-ai-compliance-vs-defender-for-cloud-ai-vs-custom-redteam-regulated-governance-selection-faq.en.md) |
| **Purview AI Hub DSPM vs Defender for Cloud AI Threat Protection vs Content Safety：企业 AI SecOps 选型 FAQ（Round 1159）** | [中文](purview-ai-hub-dspm-vs-defender-for-cloud-ai-threat-protection-vs-content-safety-secops-selection-faq.md) | [EN](purview-ai-hub-dspm-vs-defender-for-cloud-ai-threat-protection-vs-content-safety-secops-selection-faq.en.md) |
| **Purview DLP+CMK vs 可逆脱敏网关 vs 机密清洁室：主权隐私 AI 选型 FAQ（Round 1153）** | [中文](purview-dlp-cmk-vs-presidio-tokenization-gateway-vs-confidential-cleanroom-sovereign-ai-selection-faq.md) | [EN](purview-dlp-cmk-vs-presidio-tokenization-gateway-vs-confidential-cleanroom-sovereign-ai-selection-faq.en.md) |

## 7. LLMOps 评测门禁、自主 SRE 运维与实时语音/多语言智能体

| 选型主题 | 中文版 | English |
| :--- | :---: | :---: |
| **Foundry Eval + AppInsights vs LangSmith vs Langfuse vs Phoenix：企业 Agent 评测、可观测与 LLMOps 选型 FAQ** | [中文](foundry-eval-appinsights-vs-langsmith-vs-langfuse-vs-phoenix-llmops-selection-faq.md) | [EN](foundry-eval-appinsights-vs-langsmith-vs-langfuse-vs-phoenix-llmops-selection-faq.en.md) |
| **Round 1100 / Cycle 2505 · Azure AI Agent Infra 六段式 FAQ（zh-CN）** | [中文](foundry-agent-eval-redteam-pyrit-cicd-release-gate-faq.md) | [EN](foundry-agent-eval-redteam-pyrit-cicd-release-gate-faq.en.md) |
| **foundry-eval-ci-vs-apim-shadow-mirroring-vs-appconfig-canary-agent-release-engineering-selection-faq-r1141** | [中文](foundry-eval-ci-vs-apim-shadow-mirroring-vs-appconfig-canary-agent-release-engineering-selection-faq.md) | [EN](foundry-eval-ci-vs-apim-shadow-mirroring-vs-appconfig-canary-agent-release-engineering-selection-faq.en.md) |
| **github-copilot-coding-agent-vs-foundry-swe-agent-vs-ado-pr-review-enterprise-sdlc-agent-selection-faq-r1138** | [中文](github-copilot-coding-agent-vs-foundry-swe-agent-vs-ado-pr-review-enterprise-sdlc-agent-selection-faq.md) | [EN](github-copilot-coding-agent-vs-foundry-swe-agent-vs-ado-pr-review-enterprise-sdlc-agent-selection-faq.en.md) |
| **Round 1128 · Cycle 2533** | [中文](azure-sre-agent-vs-custom-aks-ops-agent-vs-servicenow-aiops-incident-response-selection-faq.md) | [EN](azure-sre-agent-vs-custom-aks-ops-agent-vs-servicenow-aiops-incident-response-selection-faq.en.md) |
| **Azure SRE Agent vs Monitor+Logic Apps Runbook：企业 AIOps 与安全自愈选型 FAQ（Round 1161）** | [中文](azure-sre-agent-vs-monitor-aio-alerts-vs-logic-apps-runbook-autonomous-cloud-ops-selection-faq.md) | [EN](azure-sre-agent-vs-monitor-aio-alerts-vs-logic-apps-runbook-autonomous-cloud-ops-selection-faq.en.md) |
| **Voice Live Realtime vs Speech 级联 vs AKS LiveKit vs 成熟联络中心：企业实时语音 Agent 选型 FAQ** | [中文](voice-live-realtime-vs-speech-cascade-vs-acs-vs-livekit-voice-agent-selection-faq.md) | [EN](voice-live-realtime-vs-speech-cascade-vs-acs-vs-livekit-voice-agent-selection-faq.en.md) |
| **Round 1101 / Cycle 2506 · Azure AI Agent Infra FAQ（zh-CN）** | [中文](acs-aoai-realtime-webrtc-voice-agent-turn-bargein-faq.md) | [EN](acs-aoai-realtime-webrtc-voice-agent-turn-bargein-faq.en.md) |
| **aoai-realtime-webrtc-vs-teams-meeting-bot-vs-acs-vision-vs-live-avatar-copilot-selection-faq-r1143** | [中文](aoai-realtime-webrtc-vs-teams-meeting-bot-vs-acs-vision-vs-live-avatar-copilot-selection-faq.md) | [EN](aoai-realtime-webrtc-vs-teams-meeting-bot-vs-acs-vision-vs-live-avatar-copilot-selection-faq.en.md) |
| **Azure Bot Omnichannel vs D365 Contact Center vs ACS Sidecar Assist：企业全渠道联络中心选型 FAQ（Round 1157）** | [中文](azure-bot-service-omnichannel-d365-contact-center-vs-acs-custom-cc-agent-handoff-selection-faq.md) | [EN](azure-bot-service-omnichannel-d365-contact-center-vs-acs-custom-cc-agent-handoff-selection-faq.en.md) |
| **Azure AI Translator vs AOAI LLM Localization vs Cross-Lingual RAG vs Sovereign Routing：全球多语种智能体选型 FAQ（Round 1147）** | [中文](azure-ai-translator-vs-aoai-llm-localization-vs-glossary-rag-global-multilingual-agent-selection-faq.md) | [EN](azure-ai-translator-vs-aoai-llm-localization-vs-glossary-rag-global-multilingual-agent-selection-faq.en.md) |
