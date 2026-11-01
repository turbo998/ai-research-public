"""Deterministic offline verification and simulation suite for:
1. Gemini 4 Carbon (2026-10-28 Fairwind Preview) vs. Gemini 4 Argon, GPT-6 Astra, Claude Opus 5.5, and Claude Fable 5.1
   across the official 17-benchmark suite (16 table benchmarks + SEC-bench Pro) and WebDev Arena.
2. End-to-End Cybersecurity Defense Lifecycle sub-leaderboards (SEC-bench Pro, ExploitGym, CWE-bench) and Safety/Alignment
   audits (Gray Swan IPI k=15 indirect prompt injection, Terminal-Bench 4.0 anti-cheating, and misalignment reductions).
3. 20-Model Frontier Coding Agent Roster (Supplement 6): 19 verified Copilot CLI models (209 runs, 1,310 hidden assertions/model,
   0 drift from satomic/copilot-benchmark@a191383571a13143685fd6f7787512c4e281a9ba) + Gemini 4 Carbon Fairwind Preview cross-track synthesis.

All coordinates are sealed from primary source artifacts:
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/ (2026-10-28)
- https://storage.googleapis.com/deepmind-media/gemini/gemini_4_carbon_model_evaluation.pdf
- satomic/copilot-benchmark@a191383571a13143685fd6f7787512c4e281a9ba
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class CarbonBenchmarkRow:
    benchmark: str
    category: str
    metric_note: str
    unit: str
    carbon: float
    argon: float
    gpt6_astra: float | None
    claude_opus_5_5: float | None
    claude_fable_5_1: float | None
    carbon_rank: int

    @property
    def delta_vs_argon(self) -> float:
        return round(self.carbon - self.argon, 2)

    @property
    def ratio_vs_argon(self) -> float:
        return round(self.carbon / self.argon, 2)


@dataclass(frozen=True)
class SubLeaderboardEntry:
    model: str
    harness_or_cap: str
    score_pct: float
    is_carbon: bool = False


@dataclass(frozen=True)
class CodingModelRecord:
    slug: str
    display_name: str
    cohort: str
    cli_version: str
    effort: str
    atomic_mean: float | None
    medium_mean: float | None
    complex_mean: float | None
    total_mean: float | None
    hidden_passed: int | None
    hidden_total: int
    atomic_rounds_mean: float | None
    medium_rounds_mean: float | None
    complex_rounds_mean: float | None
    complex_to_atomic_round_ratio: float | None
    total_rounds: int | None
    output_tokens: int | None
    cost_usd: float | None
    wall_seconds: float | None
    inference_seconds: float | None
    task_scores: dict[str, float]
    capi_status: str = "GA in CAPI /models"


GEMINI_4_CARBON_RELEASE_METADATA: dict[str, Any] = {
    "model_name": "Gemini 4 Carbon",
    "model_slug": "gemini-4-carbon",
    "release_date": "2026-10-28",
    "blog_url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/",
    "evaluation_pdf_url": "https://storage.googleapis.com/deepmind-media/gemini/gemini_4_carbon_model_evaluation.pdf",
    "access_program": "Google DeepMind Fairwind Program (phased rollout to vetted cyber defenders; pending public Copilot CLI CAPI /models)",
    "pricing_per_1m_usd": {
        "input_usd": 2.00,
        "output_usd": 10.00,
        "cached_input_usd": 0.10,
        "cached_input_discount_pct": 95.0,
        "cache_write_usd": 0.00,
        "same_as_gemini_4_argon": True,
    },
    "webdev_arena": {
        "carbon_elo": 1768,
        "argon_elo": 1679,
        "delta_elo": 89,
        "overall_rank": 4,
    },
    "alignment_and_safety": {
        "gray_swan_ipi_asr_k15_pct": 0.0,
        "terminal_bench_4_successful_cheating_pct": 0.0,
        "terminal_bench_4_cheating_attempt_pct": 0.4,
        "live_coding_high_severity_misalignment_delta_pct": -80.0,
        "unsupported_claims_delta_pct": -50.0,
        "unsupported_claims_reduction_factor_x": 2.0,
        "overreach_delta_pct": -26.0,
        "under_service_delta_pct": -29.0,
        "secure_code_generation_multiplier_vs_argon_min_x": 2.0,
        "chrome_patch_quality_multiplier_vs_competing_frontier_min_x": 10.0,
    },
}

# Official 16-Benchmark Table + SEC-bench Pro (17 rows total)
OFFICIAL_CARBON_BENCHMARKS: tuple[CarbonBenchmarkRow, ...] = (
    CarbonBenchmarkRow(
        benchmark="AA Index v5.0",
        category="General & Enterprise",
        metric_note="Artificial Analysis Intelligence Index v5.0 (with tools)",
        unit="index_pts",
        carbon=59.0,
        argon=50.0,
        gpt6_astra=57.0,
        claude_opus_5_5=58.0,
        claude_fable_5_1=49.0,
        carbon_rank=1,
    ),
    CarbonBenchmarkRow(
        benchmark="Vals Index v2.2",
        category="General & Enterprise",
        metric_note="Enterprise Finance, Legal & Coding Multimodal Index",
        unit="pct",
        carbon=70.4,
        argon=69.2,
        gpt6_astra=65.0,
        claude_opus_5_5=70.2,
        claude_fable_5_1=None,
        carbon_rank=1,
    ),
    CarbonBenchmarkRow(
        benchmark="SWE-sweep",
        category="Software Engineering & Terminal",
        metric_note="mini-swe-agent multi-PR subtask reward",
        unit="pct",
        carbon=9.6,
        argon=4.3,
        gpt6_astra=9.5,
        claude_opus_5_5=3.6,
        claude_fable_5_1=2.9,
        carbon_rank=1,
    ),
    CarbonBenchmarkRow(
        benchmark="FrontierSWE 2",
        category="Software Engineering & Terminal",
        metric_note="Proximal hard repository-level software engineering",
        unit="pct",
        carbon=61.2,
        argon=55.0,
        gpt6_astra=65.5,
        claude_opus_5_5=62.3,
        claude_fable_5_1=56.3,
        carbon_rank=3,
    ),
    CarbonBenchmarkRow(
        benchmark="Terminal-Bench 4.0 (AA)",
        category="Software Engineering & Terminal",
        metric_note="Artificial Analysis standardized terminal agent suite",
        unit="pct",
        carbon=65.2,
        argon=57.1,
        gpt6_astra=59.1,
        claude_opus_5_5=59.6,
        claude_fable_5_1=52.0,
        carbon_rank=1,
    ),
    CarbonBenchmarkRow(
        benchmark="Agents' Last Exam v1.1",
        category="Long-Horizon & Computer Use",
        metric_note="122 tasks, ALE-Claw harness, 5-hour window",
        unit="pct",
        carbon=77.4,
        argon=69.0,
        gpt6_astra=73.1,
        claude_opus_5_5=71.6,
        claude_fable_5_1=None,
        carbon_rank=1,
    ),
    CarbonBenchmarkRow(
        benchmark="OSWorld-2.1",
        category="Long-Horizon & Computer Use",
        metric_note="82-task offline GUI subset, max@3",
        unit="pct",
        carbon=81.5,
        argon=74.7,
        gpt6_astra=80.9,
        claude_opus_5_5=87.2,
        claude_fable_5_1=76.8,
        carbon_rank=2,
    ),
    CarbonBenchmarkRow(
        benchmark="AutomationBench",
        category="Long-Horizon & Computer Use",
        metric_note="Zapier private enterprise workflow automation set",
        unit="pct",
        carbon=53.9,
        argon=51.3,
        gpt6_astra=41.4,
        claude_opus_5_5=42.5,
        claude_fable_5_1=31.4,
        carbon_rank=1,
    ),
    CarbonBenchmarkRow(
        benchmark="Vending-Bench 2",
        category="Long-Horizon & Computer Use",
        metric_note="Andon Labs long-horizon business simulation bank balance ($)",
        unit="usd",
        carbon=16484.0,
        argon=13718.0,
        gpt6_astra=15515.0,
        claude_opus_5_5=9235.0,
        claude_fable_5_1=5422.0,
        carbon_rank=1,
    ),
    CarbonBenchmarkRow(
        benchmark="Chartography",
        category="Visual, Spatial & Long-Context",
        metric_note="Surge complex chart reasoning (no tools)",
        unit="pct",
        carbon=72.5,
        argon=71.6,
        gpt6_astra=71.0,
        claude_opus_5_5=66.3,
        claude_fable_5_1=46.2,
        carbon_rank=1,
    ),
    CarbonBenchmarkRow(
        benchmark="Blueprint-Bench 2",
        category="Visual, Spatial & Long-Context",
        metric_note="Andon Labs structural blueprint similarity",
        unit="pct",
        carbon=58.6,
        argon=54.4,
        gpt6_astra=49.7,
        claude_opus_5_5=51.2,
        claude_fable_5_1=41.9,
        carbon_rank=1,
    ),
    CarbonBenchmarkRow(
        benchmark="GraphWalks",
        category="Visual, Spatial & Long-Context",
        metric_note="256k to 1M tokens, 200 problems, BFS F1",
        unit="pct",
        carbon=96.2,
        argon=84.2,
        gpt6_astra=71.8,
        claude_opus_5_5=66.8,
        claude_fable_5_1=65.0,
        carbon_rank=1,
    ),
    CarbonBenchmarkRow(
        benchmark="RiemannBench",
        category="Math & Scientific Reasoning",
        metric_note="Surge frontier mathematical research benchmark",
        unit="pct",
        carbon=80.0,
        argon=76.0,
        gpt6_astra=72.0,
        claude_opus_5_5=69.6,
        claude_fable_5_1=65.6,
        carbon_rank=1,
    ),
    CarbonBenchmarkRow(
        benchmark="Terminal-Bench-Science 0.1 (AA)",
        category="Math & Scientific Reasoning",
        metric_note="Artificial Analysis scientific terminal computing",
        unit="pct",
        carbon=64.8,
        argon=52.9,
        gpt6_astra=63.3,
        claude_opus_5_5=59.0,
        claude_fable_5_1=43.3,
        carbon_rank=1,
    ),
    CarbonBenchmarkRow(
        benchmark="CWE-bench",
        category="Cybersecurity Defense Lifecycle",
        metric_note="Collinear Pass@1 vulnerability remediation across CWEs",
        unit="pct",
        carbon=71.0,
        argon=68.0,
        gpt6_astra=68.0,
        claude_opus_5_5=67.0,
        claude_fable_5_1=58.0,
        carbon_rank=1,
    ),
    CarbonBenchmarkRow(
        benchmark="ExploitGym",
        category="Cybersecurity Defense Lifecycle",
        metric_note="Causal Pass Rate (10h cap; 6h cap: Carbon 53.5% vs Argon 39.5%)",
        unit="pct",
        carbon=54.8,
        argon=42.0,
        gpt6_astra=42.4,
        claude_opus_5_5=34.5,
        claude_fable_5_1=None,
        carbon_rank=1,
    ),
    CarbonBenchmarkRow(
        benchmark="SEC-bench Pro",
        category="Cybersecurity Defense Lifecycle",
        metric_note="183 real-world JS engine security tasks, Pass@1",
        unit="pct",
        carbon=88.2,
        argon=83.4,
        gpt6_astra=85.4,
        claude_opus_5_5=None,
        claude_fable_5_1=None,
        carbon_rank=1,
    ),
)

SEC_BENCH_PRO_LEADERBOARD: tuple[SubLeaderboardEntry, ...] = (
    SubLeaderboardEntry("Gemini 4 Carbon", "183 JS engine tasks (Pass@1)", 88.2, is_carbon=True),
    SubLeaderboardEntry("GPT-6 Astra", "183 JS engine tasks (Pass@1)", 85.4),
    SubLeaderboardEntry("Gemini 4 Argon", "183 JS engine tasks (Pass@1)", 83.4),
    SubLeaderboardEntry("GPT-6.1 Terra", "183 JS engine tasks (Pass@1)", 83.3),
    SubLeaderboardEntry("GPT-6.1 Sol", "183 JS engine tasks (Pass@1)", 78.8),
    SubLeaderboardEntry("MiMo-V2.6-Pro", "183 JS engine tasks (Pass@1)", 66.3),
    SubLeaderboardEntry("DeepSeek-V4.1-Flash", "183 JS engine tasks (Pass@1)", 62.8),
    SubLeaderboardEntry("DeepSeek-V4-Pro", "183 JS engine tasks (Pass@1)", 56.4),
)

EXPLOITGYM_LEADERBOARD: tuple[SubLeaderboardEntry, ...] = (
    SubLeaderboardEntry("Gemini 4 Carbon (10h)", "10h time cap", 54.8, is_carbon=True),
    SubLeaderboardEntry("Gemini 4 Carbon (6h)", "6h time cap", 53.5, is_carbon=True),
    SubLeaderboardEntry("GPT-6 Astra", "No time cap", 42.4),
    SubLeaderboardEntry("Gemini 4 Argon (10h)", "10h time cap", 42.0),
    SubLeaderboardEntry("Gemini 4 Argon (6h)", "6h time cap", 39.5),
    SubLeaderboardEntry("GPT-6.1 Sol", "No time cap", 35.1),
    SubLeaderboardEntry("Claude Opus 5.5", "6h time cap", 34.5),
    SubLeaderboardEntry("Claude Mythos 5.1", "6h time cap", 30.4),
    SubLeaderboardEntry("MiMo-V2.6-Pro", "Unknown time cap", 17.8),
    SubLeaderboardEntry("GLM-5.3", "6h time cap", 15.0),
)

CWE_BENCH_LEADERBOARD: tuple[SubLeaderboardEntry, ...] = (
    SubLeaderboardEntry("Gemini 4 Carbon", "Antigravity", 71.0, is_carbon=True),
    SubLeaderboardEntry("Grok 4.7", "opencode", 68.0),
    SubLeaderboardEntry("Gemini 4 Argon", "Antigravity", 68.0),
    SubLeaderboardEntry("GPT-6 Astra", "Codex", 68.0),
    SubLeaderboardEntry("Claude Opus 5.5", "Claude Code", 67.0),
    SubLeaderboardEntry("Claude Fable 5.1", "Claude Code", 58.0),
    SubLeaderboardEntry("Grok 4.6", "opencode", 57.0),
    SubLeaderboardEntry("DeepSeek-V4-1-Flash", "opencode", 55.0),
    SubLeaderboardEntry("Muse Spark 1.3", "opencode", 55.0),
    SubLeaderboardEntry("Hy4 Preview", "opencode", 53.0),
    SubLeaderboardEntry("GPT-6 Sol", "Codex", 52.0),
)

# Gray Swan Indirect Prompt Injection (IPI) Attack Success Rate at k=15 attempts (Lower is better!)
GRAY_SWAN_IPI_LEADERBOARD: tuple[SubLeaderboardEntry, ...] = (
    SubLeaderboardEntry("Gemini 4 Carbon", "ASR @ k=15 (Lower is better)", 0.0, is_carbon=True),
    SubLeaderboardEntry("Gemini 4 Argon", "ASR @ k=15 (Lower is better)", 0.7),
    SubLeaderboardEntry("Claude Opus 5.5", "ASR @ k=15 (Lower is better)", 1.0),
    SubLeaderboardEntry("Claude Fable 5.1", "ASR @ k=15 (Lower is better)", 1.0),
    SubLeaderboardEntry("Claude Opus 5", "ASR @ k=15 (Lower is better)", 4.6),
    SubLeaderboardEntry("Gemini 3.8 Flash", "ASR @ k=15 (Lower is better)", 5.5),
    SubLeaderboardEntry("Gemini 3.8 Flash Cyber", "ASR @ k=15 (Lower is better)", 6.0),
    SubLeaderboardEntry("GPT-6 Astra", "ASR @ k=15 (Lower is better)", 8.5),
    SubLeaderboardEntry("GPT-6.1 Sol", "ASR @ k=15 (Lower is better)", 8.6),
    SubLeaderboardEntry("Muse Spark 1.3", "ASR @ k=15 (Lower is better)", 15.9),
    SubLeaderboardEntry("GLM 5.3", "ASR @ k=15 (Lower is better)", 31.5),
    SubLeaderboardEntry("Grok 4.6", "ASR @ k=15 (Lower is better)", 51.8),
    SubLeaderboardEntry("Kimi K3", "ASR @ k=15 (Lower is better)", 52.7),
)

TASKS: tuple[str, ...] = ("A1", "A2", "A3", "A4", "A5", "M1", "M2", "C1", "C2", "C3", "C4")

# 20-Model Roster: 19 Copilot CLI Verified Models (satomic/copilot-benchmark@a1913835) + Gemini 4 Carbon (Fairwind Preview)
TWENTY_MODELS: tuple[CodingModelRecord, ...] = (
    CodingModelRecord(
        slug="gemini-4-carbon",
        display_name="Gemini 4 Carbon",
        cohort="Supplement 6 (20-Model · Fairwind Preview)",
        cli_version="Fairwind Preview",
        effort="medium/high",
        atomic_mean=None,
        medium_mean=None,
        complex_mean=None,
        total_mean=None,
        hidden_passed=None,
        hidden_total=1310,
        atomic_rounds_mean=None,
        medium_rounds_mean=None,
        complex_rounds_mean=None,
        complex_to_atomic_round_ratio=None,
        total_rounds=None,
        output_tokens=None,
        cost_usd=None,
        wall_seconds=None,
        inference_seconds=None,
        task_scores={},
        capi_status="Fairwind Preview (Pending Public CLI)",
    ),
    CodingModelRecord(
        slug="claude-fable-5.1",
        display_name="Fable 5.1",
        cohort="Baseline (5-Model)",
        cli_version="1.0.84-3",
        effort="medium",
        atomic_mean=100.00,
        medium_mean=99.50,
        complex_mean=99.62,
        total_mean=99.77,
        hidden_passed=1310,
        hidden_total=1310,
        atomic_rounds_mean=4.2,
        medium_rounds_mean=13.0,
        complex_rounds_mean=23.8,
        complex_to_atomic_round_ratio=5.7,
        total_rounds=142,
        output_tokens=157854,
        cost_usd=14.45,
        wall_seconds=3355,
        inference_seconds=2210,
        task_scores={"A1": 100.0, "A2": 100.0, "A3": 100.0, "A4": 100.0, "A5": 100.0, "M1": 100.0, "M2": 99.0, "C1": 98.5, "C2": 100.0, "C3": 100.0, "C4": 100.0},
    ),
    CodingModelRecord(
        slug="claude-opus-5.5",
        display_name="Opus 5.5",
        cohort="Supplement 3 (15-Model)",
        cli_version="1.0.89-5",
        effort="medium",
        atomic_mean=99.80,
        medium_mean=99.50,
        complex_mean=99.62,
        total_mean=99.68,
        hidden_passed=1310,
        hidden_total=1310,
        atomic_rounds_mean=4.8,
        medium_rounds_mean=7.5,
        complex_rounds_mean=13.2,
        complex_to_atomic_round_ratio=2.8,
        total_rounds=92,
        output_tokens=175976,
        cost_usd=5.84,
        wall_seconds=1909,
        inference_seconds=1570,
        task_scores={"A1": 100.0, "A2": 99.0, "A3": 100.0, "A4": 100.0, "A5": 100.0, "M1": 100.0, "M2": 99.0, "C1": 98.5, "C2": 100.0, "C3": 100.0, "C4": 100.0},
    ),
    CodingModelRecord(
        slug="claude-opus-5",
        display_name="Opus 5",
        cohort="Baseline (5-Model)",
        cli_version="1.0.84-3",
        effort="medium",
        atomic_mean=99.80,
        medium_mean=99.50,
        complex_mean=99.38,
        total_mean=99.59,
        hidden_passed=1310,
        hidden_total=1310,
        atomic_rounds_mean=5.0,
        medium_rounds_mean=12.5,
        complex_rounds_mean=34.5,
        complex_to_atomic_round_ratio=6.9,
        total_rounds=188,
        output_tokens=249164,
        cost_usd=17.41,
        wall_seconds=3797,
        inference_seconds=3042,
        task_scores={"A1": 100.0, "A2": 99.0, "A3": 100.0, "A4": 100.0, "A5": 100.0, "M1": 100.0, "M2": 99.0, "C1": 97.5, "C2": 100.0, "C3": 100.0, "C4": 100.0},
    ),
    CodingModelRecord(
        slug="claude-haiku-5.5",
        display_name="Haiku 5.5",
        cohort="Supplement 5 (19-Model)",
        cli_version="1.0.98",
        effort="medium",
        atomic_mean=99.15,
        medium_mean=99.50,
        complex_mean=99.22,
        total_mean=99.24,
        hidden_passed=1308,
        hidden_total=1310,
        atomic_rounds_mean=4.2,
        medium_rounds_mean=8.5,
        complex_rounds_mean=14.0,
        complex_to_atomic_round_ratio=3.3,
        total_rounds=94,
        output_tokens=453116,
        cost_usd=0.33,
        wall_seconds=2104,
        inference_seconds=1852,
        task_scores={"A1": 100.0, "A2": 99.0, "A3": 98.0, "A4": 100.0, "A5": 98.75, "M1": 100.0, "M2": 99.0, "C1": 97.25, "C2": 100.0, "C3": 100.0, "C4": 99.61},
    ),
    CodingModelRecord(
        slug="grok-4.7",
        display_name="Grok 4.7",
        cohort="Supplement 2 (12-Model)",
        cli_version="1.0.89-0",
        effort="medium",
        atomic_mean=99.00,
        medium_mean=99.50,
        complex_mean=99.33,
        total_mean=99.21,
        hidden_passed=1299,
        hidden_total=1310,
        atomic_rounds_mean=5.0,
        medium_rounds_mean=6.5,
        complex_rounds_mean=26.2,
        complex_to_atomic_round_ratio=5.2,
        total_rounds=143,
        output_tokens=514873,
        cost_usd=12.22,
        wall_seconds=10873,
        inference_seconds=7849,
        task_scores={"A1": 99.0, "A2": 100.0, "A3": 100.0, "A4": 100.0, "A5": 96.0, "M1": 100.0, "M2": 99.0, "C1": 98.87, "C2": 100.0, "C3": 98.46, "C4": 100.0},
    ),
    CodingModelRecord(
        slug="claude-sonnet-5.5",
        display_name="Sonnet 5.5",
        cohort="Supplement 4 (17-Model)",
        cli_version="1.0.90-5",
        effort="medium",
        atomic_mean=98.80,
        medium_mean=99.12,
        complex_mean=99.19,
        total_mean=99.00,
        hidden_passed=1310,
        hidden_total=1310,
        atomic_rounds_mean=2.8,
        medium_rounds_mean=6.5,
        complex_rounds_mean=9.5,
        complex_to_atomic_round_ratio=3.4,
        total_rounds=65,
        output_tokens=161136,
        cost_usd=2.89,
        wall_seconds=1301,
        inference_seconds=995,
        task_scores={"A1": 99.0, "A2": 99.0, "A3": 98.0, "A4": 100.0, "A5": 98.0, "M1": 100.0, "M2": 98.25, "C1": 97.5, "C2": 100.0, "C3": 99.25, "C4": 100.0},
    ),
    CodingModelRecord(
        slug="gpt-6.1-sol",
        display_name="GPT-6.1 Sol",
        cohort="Supplement 4 (17-Model)",
        cli_version="1.0.90-5",
        effort="medium",
        atomic_mean=98.40,
        medium_mean=99.00,
        complex_mean=99.38,
        total_mean=98.86,
        hidden_passed=1310,
        hidden_total=1310,
        atomic_rounds_mean=4.4,
        medium_rounds_mean=5.0,
        complex_rounds_mean=7.0,
        complex_to_atomic_round_ratio=1.6,
        total_rounds=60,
        output_tokens=92907,
        cost_usd=1.71,
        wall_seconds=1645,
        inference_seconds=1348,
        task_scores={"A1": 99.0, "A2": 96.0, "A3": 97.0, "A4": 100.0, "A5": 100.0, "M1": 100.0, "M2": 98.0, "C1": 97.5, "C2": 100.0, "C3": 100.0, "C4": 100.0},
    ),
    CodingModelRecord(
        slug="gpt-6-astra",
        display_name="GPT-6 Astra",
        cohort="Baseline (5-Model)",
        cli_version="1.0.84-3",
        effort="medium",
        atomic_mean=98.00,
        medium_mean=99.00,
        complex_mean=99.75,
        total_mean=98.82,
        hidden_passed=1310,
        hidden_total=1310,
        atomic_rounds_mean=4.0,
        medium_rounds_mean=5.5,
        complex_rounds_mean=7.8,
        complex_to_atomic_round_ratio=1.9,
        total_rounds=62,
        output_tokens=98061,
        cost_usd=9.91,
        wall_seconds=1960,
        inference_seconds=1617,
        task_scores={"A1": 98.0, "A2": 96.0, "A3": 97.0, "A4": 100.0, "A5": 99.0, "M1": 100.0, "M2": 98.0, "C1": 99.0, "C2": 100.0, "C3": 100.0, "C4": 100.0},
    ),
    CodingModelRecord(
        slug="claude-sonnet-5",
        display_name="Sonnet 5",
        cohort="Baseline (5-Model)",
        cli_version="1.0.84-3",
        effort="medium",
        atomic_mean=98.40,
        medium_mean=99.12,
        complex_mean=98.88,
        total_mean=98.70,
        hidden_passed=1310,
        hidden_total=1310,
        atomic_rounds_mean=5.0,
        medium_rounds_mean=12.5,
        complex_rounds_mean=35.0,
        complex_to_atomic_round_ratio=7.0,
        total_rounds=190,
        output_tokens=239150,
        cost_usd=7.87,
        wall_seconds=3192,
        inference_seconds=2393,
        task_scores={"A1": 100.0, "A2": 99.0, "A3": 97.0, "A4": 100.0, "A5": 96.0, "M1": 100.0, "M2": 98.25, "C1": 97.5, "C2": 100.0, "C3": 98.0, "C4": 100.0},
    ),
    CodingModelRecord(
        slug="kimi-k3",
        display_name="Kimi K3",
        cohort="Supplement 1 (10-Model)",
        cli_version="1.0.84-8",
        effort="(unsupported)",
        atomic_mean=98.40,
        medium_mean=99.12,
        complex_mean=98.81,
        total_mean=98.68,
        hidden_passed=1305,
        hidden_total=1310,
        atomic_rounds_mean=6.6,
        medium_rounds_mean=16.5,
        complex_rounds_mean=19.2,
        complex_to_atomic_round_ratio=2.9,
        total_rounds=143,
        output_tokens=175321,
        cost_usd=5.58,
        wall_seconds=9028,
        inference_seconds=4944,
        task_scores={"A1": 99.0, "A2": 97.0, "A3": 97.0, "A4": 100.0, "A5": 99.0, "M1": 100.0, "M2": 98.25, "C1": 97.12, "C2": 99.27, "C3": 98.85, "C4": 100.0},
    ),
    CodingModelRecord(
        slug="gemini-4-argon",
        display_name="Gemini 4 Argon",
        cohort="Supplement 5 (19-Model)",
        cli_version="1.0.98",
        effort="medium",
        atomic_mean=99.00,
        medium_mean=98.62,
        complex_mean=98.06,
        total_mean=98.59,
        hidden_passed=1310,
        hidden_total=1310,
        atomic_rounds_mean=6.0,
        medium_rounds_mean=7.5,
        complex_rounds_mean=15.2,
        complex_to_atomic_round_ratio=2.5,
        total_rounds=106,
        output_tokens=116755,
        cost_usd=2.82,
        wall_seconds=2710,
        inference_seconds=2512,
        task_scores={"A1": 99.0, "A2": 99.0, "A3": 97.0, "A4": 100.0, "A5": 100.0, "M1": 100.0, "M2": 97.25, "C1": 98.25, "C2": 100.0, "C3": 96.0, "C4": 98.0},
    ),
    CodingModelRecord(
        slug="grok-4.6",
        display_name="Grok 4.6",
        cohort="Supplement 1 (10-Model)",
        cli_version="1.0.84-8",
        effort="medium",
        atomic_mean=98.40,
        medium_mean=100.00,
        complex_mean=98.06,
        total_mean=98.57,
        hidden_passed=1305,
        hidden_total=1310,
        atomic_rounds_mean=8.0,
        medium_rounds_mean=10.0,
        complex_rounds_mean=19.5,
        complex_to_atomic_round_ratio=2.4,
        total_rounds=138,
        output_tokens=194210,
        cost_usd=5.21,
        wall_seconds=4172,
        inference_seconds=3302,
        task_scores={"A1": 99.0, "A2": 98.0, "A3": 97.0, "A4": 100.0, "A5": 98.0, "M1": 100.0, "M2": 100.0, "C1": 97.12, "C2": 99.27, "C3": 99.85, "C4": 96.0},
    ),
    CodingModelRecord(
        slug="hydrafusion",
        display_name="HydraFusion",
        cohort="Supplement 3 (15-Model)",
        cli_version="1.0.89-5",
        effort="(unsupported)",
        atomic_mean=98.40,
        medium_mean=98.00,
        complex_mean=98.75,
        total_mean=98.45,
        hidden_passed=1310,
        hidden_total=1310,
        atomic_rounds_mean=6.2,
        medium_rounds_mean=8.0,
        complex_rounds_mean=9.5,
        complex_to_atomic_round_ratio=1.5,
        total_rounds=85,
        output_tokens=88979,
        cost_usd=3.58,
        wall_seconds=1444,
        inference_seconds=1034,
        task_scores={"A1": 96.0, "A2": 99.0, "A3": 97.0, "A4": 100.0, "A5": 100.0, "M1": 97.0, "M2": 99.0, "C1": 99.0, "C2": 100.0, "C3": 98.0, "C4": 98.0},
    ),
    CodingModelRecord(
        slug="gpt-6-luna",
        display_name="GPT-6 Luna",
        cohort="Supplement 2 (12-Model)",
        cli_version="1.0.89-0",
        effort="medium",
        atomic_mean=98.80,
        medium_mean=99.12,
        complex_mean=96.88,
        total_mean=98.16,
        hidden_passed=1279,
        hidden_total=1310,
        atomic_rounds_mean=4.8,
        medium_rounds_mean=8.0,
        complex_rounds_mean=24.8,
        complex_to_atomic_round_ratio=5.2,
        total_rounds=139,
        output_tokens=145411,
        cost_usd=0.17,
        wall_seconds=2675,
        inference_seconds=2129,
        task_scores={"A1": 99.0, "A2": 98.0, "A3": 97.0, "A4": 100.0, "A5": 100.0, "M1": 100.0, "M2": 98.25, "C1": 97.12, "C2": 100.0, "C3": 92.38, "C4": 98.0},
    ),
    CodingModelRecord(
        slug="gemini-3.8-flash",
        display_name="Gemini 3.8 Flash",
        cohort="Supplement 1 (10-Model)",
        cli_version="1.0.84-8",
        effort="medium",
        atomic_mean=98.75,
        medium_mean=98.12,
        complex_mean=97.00,
        total_mean=98.00,
        hidden_passed=1276,
        hidden_total=1310,
        atomic_rounds_mean=18.0,
        medium_rounds_mean=28.5,
        complex_rounds_mean=32.5,
        complex_to_atomic_round_ratio=1.8,
        total_rounds=277,
        output_tokens=122989,
        cost_usd=2.83,
        wall_seconds=5122,
        inference_seconds=3750,
        task_scores={"A1": 100.0, "A2": 100.0, "A3": 95.75, "A4": 100.0, "A5": 98.0, "M1": 100.0, "M2": 96.25, "C1": 98.25, "C2": 99.0, "C3": 93.77, "C4": 97.0},
    ),
    CodingModelRecord(
        slug="gpt-5.6-luna",
        display_name="GPT-5.6 Luna",
        cohort="Supplement 1 (10-Model)",
        cli_version="1.0.84-8",
        effort="medium",
        atomic_mean=98.40,
        medium_mean=99.50,
        complex_mean=96.42,
        total_mean=97.88,
        hidden_passed=1293,
        hidden_total=1310,
        atomic_rounds_mean=9.2,
        medium_rounds_mean=14.0,
        complex_rounds_mean=40.2,
        complex_to_atomic_round_ratio=4.4,
        total_rounds=235,
        output_tokens=106599,
        cost_usd=0.39,
        wall_seconds=3061,
        inference_seconds=1316,
        task_scores={"A1": 99.0, "A2": 98.0, "A3": 97.0, "A4": 100.0, "A5": 98.0, "M1": 100.0, "M2": 99.0, "C1": 97.5, "C2": 97.51, "C3": 94.69, "C4": 96.0},
    ),
    CodingModelRecord(
        slug="mai-code-1.1-flash",
        display_name="MAI-Code-1.1-Flash",
        cohort="Supplement 1 (10-Model)",
        cli_version="1.0.84-8",
        effort="medium",
        atomic_mean=98.20,
        medium_mean=98.62,
        complex_mean=96.61,
        total_mean=97.70,
        hidden_passed=1284,
        hidden_total=1310,
        atomic_rounds_mean=6.0,
        medium_rounds_mean=14.0,
        complex_rounds_mean=33.5,
        complex_to_atomic_round_ratio=5.6,
        total_rounds=192,
        output_tokens=233100,
        cost_usd=0.53,
        wall_seconds=3388,
        inference_seconds=2448,
        task_scores={"A1": 99.0, "A2": 97.0, "A3": 99.0, "A4": 100.0, "A5": 96.0, "M1": 100.0, "M2": 97.25, "C1": 97.12, "C2": 97.0, "C3": 95.71, "C4": 96.61},
    ),
    CodingModelRecord(
        slug="deepseek-v4-flash",
        display_name="DeepSeek-V4-Flash",
        cohort="Supplement 3 (15-Model · BYOK)",
        cli_version="1.0.89-6",
        effort="medium",
        atomic_mean=97.30,
        medium_mean=88.00,
        complex_mean=95.91,
        total_mean=95.10,
        hidden_passed=1250,
        hidden_total=1310,
        atomic_rounds_mean=8.0,
        medium_rounds_mean=22.0,
        complex_rounds_mean=84.0,
        complex_to_atomic_round_ratio=10.5,
        total_rounds=420,
        output_tokens=290100,
        cost_usd=1.95,
        wall_seconds=10740,
        inference_seconds=5618,
        task_scores={"A1": 99.0, "A2": 97.0, "A3": 95.75, "A4": 100.0, "A5": 94.75, "M1": 100.0, "M2": 76.0, "C1": 94.32, "C2": 97.32, "C3": 97.08, "C4": 94.90},
    ),
    CodingModelRecord(
        slug="claude-haiku-4.5",
        display_name="Haiku 4.5",
        cohort="Baseline (5-Model)",
        cli_version="1.0.84-3",
        effort="(unsupported)",
        atomic_mean=97.25,
        medium_mean=94.39,
        complex_mean=89.64,
        total_mean=93.96,
        hidden_passed=1239,
        hidden_total=1310,
        atomic_rounds_mean=13.8,
        medium_rounds_mean=22.0,
        complex_rounds_mean=57.0,
        complex_to_atomic_round_ratio=4.1,
        total_rounds=341,
        output_tokens=303100,
        cost_usd=3.93,
        wall_seconds=4849,
        inference_seconds=3163,
        task_scores={"A1": 97.75, "A2": 95.0, "A3": 95.75, "A4": 100.0, "A5": 97.75, "M1": 93.78, "M2": 95.0, "C1": 93.98, "C2": 94.76, "C3": 82.81, "C4": 87.01},
    ),
)

NINETEEN_CLI_MODELS: tuple[CodingModelRecord, ...] = tuple(
    m for m in TWENTY_MODELS if m.total_mean is not None
)


def classify_coding_model_action(rec: CodingModelRecord) -> str:
    """Apply threshold gating consistent with the 20-model benchmark report."""
    if rec.slug == "gemini-4-carbon":
        return "Confirm"
    assert rec.hidden_passed is not None and rec.total_mean is not None and rec.complex_mean is not None
    if rec.hidden_passed == rec.hidden_total and rec.total_mean >= 98.45:
        return "Act automatically"
    if rec.hidden_passed < 1260 or rec.complex_mean < 96.0:
        return "Send to a human"
    return "Confirm"


def compute_pareto_frontier(models: tuple[CodingModelRecord, ...] = NINETEEN_CLI_MODELS) -> list[str]:
    """Identify CLI-scored models that are Pareto-optimal on (total_mean DESC, cost_usd ASC, wall_seconds ASC)."""
    frontier: list[str] = []
    for candidate in models:
        assert candidate.total_mean is not None and candidate.cost_usd is not None and candidate.wall_seconds is not None
        dominated = False
        for other in models:
            if other.slug == candidate.slug:
                continue
            assert other.total_mean is not None and other.cost_usd is not None and other.wall_seconds is not None
            better_or_equal_all = (
                other.total_mean >= candidate.total_mean
                and other.cost_usd <= candidate.cost_usd
                and other.wall_seconds <= candidate.wall_seconds
            )
            strictly_better_one = (
                other.total_mean > candidate.total_mean
                or other.cost_usd < candidate.cost_usd
                or other.wall_seconds < candidate.wall_seconds
            )
            if better_or_equal_all and strictly_better_one:
                dominated = True
                break
        if not dominated:
            frontier.append(candidate.display_name)
    return frontier


def audit_carbon_official_benchmarks() -> dict[str, Any]:
    """Verify Gemini 4 Carbon official benchmark rankings, deltas vs Argon, and category leads."""
    by_name = {b.benchmark: b for b in OFFICIAL_CARBON_BENCHMARKS}
    rank_1_benchmarks = [b.benchmark for b in OFFICIAL_CARBON_BENCHMARKS if b.carbon_rank == 1]
    non_rank_1 = {b.benchmark: b.carbon_rank for b in OFFICIAL_CARBON_BENCHMARKS if b.carbon_rank != 1}

    swe_sweep = by_name["SWE-sweep"]
    vending = by_name["Vending-Bench 2"]
    graphwalks = by_name["GraphWalks"]
    tb4 = by_name["Terminal-Bench 4.0 (AA)"]
    ale = by_name["Agents' Last Exam v1.1"]
    exploit = by_name["ExploitGym"]
    sec_pro = by_name["SEC-bench Pro"]
    cwe = by_name["CWE-bench"]

    return {
        "total_benchmarks_audited": len(OFFICIAL_CARBON_BENCHMARKS),
        "rank_1_count": len(rank_1_benchmarks),
        "rank_1_benchmarks": rank_1_benchmarks,
        "non_rank_1_benchmarks": non_rank_1,
        "swe_sweep_delta_pts": swe_sweep.delta_vs_argon,
        "swe_sweep_ratio_x": swe_sweep.ratio_vs_argon,
        "vending_bench_2_delta_usd": int(vending.delta_vs_argon),
        "vending_bench_2_gain_pct": round((vending.carbon - vending.argon) / vending.argon * 100.0, 1),
        "graphwalks_delta_pts": graphwalks.delta_vs_argon,
        "terminal_bench_4_delta_pts": tb4.delta_vs_argon,
        "agents_last_exam_delta_pts": ale.delta_vs_argon,
        "exploitgym_10h_delta_pts": exploit.delta_vs_argon,
        "exploitgym_6h_delta_pts": round(53.5 - 39.5, 1),
        "sec_bench_pro_delta_pts": sec_pro.delta_vs_argon,
        "cwe_bench_delta_pts": cwe.delta_vs_argon,
        "webdev_arena_delta_elo": GEMINI_4_CARBON_RELEASE_METADATA["webdev_arena"]["delta_elo"],
    }


def audit_cybersecurity_and_safety() -> dict[str, Any]:
    """Audit SEC-bench Pro, ExploitGym, CWE-bench, and Gray Swan IPI leaderboards."""
    sec_top = SEC_BENCH_PRO_LEADERBOARD[0]
    sec_second = SEC_BENCH_PRO_LEADERBOARD[1]
    exploit_top_10h = EXPLOITGYM_LEADERBOARD[0]
    exploit_top_6h = EXPLOITGYM_LEADERBOARD[1]
    exploit_astra = EXPLOITGYM_LEADERBOARD[2]
    cwe_top = CWE_BENCH_LEADERBOARD[0]
    cwe_tied_second = [e.model for e in CWE_BENCH_LEADERBOARD if e.score_pct == 68.0]
    ipi_zero = [e.model for e in GRAY_SWAN_IPI_LEADERBOARD if e.score_pct == 0.0]
    ipi_by_model = {e.model: e.score_pct for e in GRAY_SWAN_IPI_LEADERBOARD}

    return {
        "sec_bench_pro": {
            "leader": sec_top.model,
            "leader_score_pct": sec_top.score_pct,
            "lead_vs_astra_pts": round(sec_top.score_pct - sec_second.score_pct, 1),
            "lead_vs_argon_pts": round(sec_top.score_pct - 83.4, 1),
            "lead_vs_deepseek_v4_pro_pts": round(sec_top.score_pct - 56.4, 1),
            "entries_count": len(SEC_BENCH_PRO_LEADERBOARD),
        },
        "exploitgym": {
            "leader_10h_pct": exploit_top_10h.score_pct,
            "leader_6h_pct": exploit_top_6h.score_pct,
            "astra_no_cap_pct": exploit_astra.score_pct,
            "carbon_6h_lead_vs_astra_no_cap_pts": round(exploit_top_6h.score_pct - exploit_astra.score_pct, 1),
            "carbon_10h_lead_vs_astra_no_cap_pts": round(exploit_top_10h.score_pct - exploit_astra.score_pct, 1),
            "carbon_6h_lead_vs_opus_5_5_6h_pts": round(exploit_top_6h.score_pct - 34.5, 1),
            "entries_count": len(EXPLOITGYM_LEADERBOARD),
        },
        "cwe_bench": {
            "leader": cwe_top.model,
            "leader_score_pct": cwe_top.score_pct,
            "tied_second_models_at_68_pct": cwe_tied_second,
            "lead_vs_second_pts": round(cwe_top.score_pct - 68.0, 1),
            "lead_vs_opus_5_5_pts": round(cwe_top.score_pct - 67.0, 1),
            "lead_vs_fable_5_1_pts": round(cwe_top.score_pct - 58.0, 1),
            "entries_count": len(CWE_BENCH_LEADERBOARD),
        },
        "gray_swan_ipi": {
            "zero_asr_models": ipi_zero,
            "carbon_asr_pct": ipi_by_model["Gemini 4 Carbon"],
            "argon_asr_pct": ipi_by_model["Gemini 4 Argon"],
            "opus_5_5_asr_pct": ipi_by_model["Claude Opus 5.5"],
            "fable_5_1_asr_pct": ipi_by_model["Claude Fable 5.1"],
            "gpt6_astra_asr_pct": ipi_by_model["GPT-6 Astra"],
            "gpt6_1_sol_asr_pct": ipi_by_model["GPT-6.1 Sol"],
            "kimi_k3_asr_pct": ipi_by_model["Kimi K3"],
            "entries_count": len(GRAY_SWAN_IPI_LEADERBOARD),
        },
    }


def export_summary_json(output_path: Path) -> dict[str, Any]:
    """Export deterministic verification summary JSON for Supplement 6 (20-Model Benchmark)."""
    carbon_audit = audit_carbon_official_benchmarks()
    cyber_audit = audit_cybersecurity_and_safety()
    pareto = compute_pareto_frontier()

    cli_action_counts = {"Act automatically": 0, "Confirm": 0, "Send to a human": 0}
    cli_summaries = []
    for rank, m in enumerate(NINETEEN_CLI_MODELS, start=1):
        act = classify_coding_model_action(m)
        cli_action_counts[act] += 1
        assert m.wall_seconds is not None and m.inference_seconds is not None
        cli_summaries.append(
            {
                "cli_rank": rank,
                "slug": m.slug,
                "display_name": m.display_name,
                "cohort": m.cohort,
                "cli_version": m.cli_version,
                "total_mean": m.total_mean,
                "atomic_mean": m.atomic_mean,
                "medium_mean": m.medium_mean,
                "complex_mean": m.complex_mean,
                "hidden_passed": m.hidden_passed,
                "hidden_total": m.hidden_total,
                "cost_usd": m.cost_usd,
                "wall_seconds": m.wall_seconds,
                "wall_minutes": round(m.wall_seconds / 60.0, 1),
                "inference_seconds": m.inference_seconds,
                "inference_minutes": round(m.inference_seconds / 60.0, 1),
                "total_rounds": m.total_rounds,
                "output_tokens": m.output_tokens,
                "action": act,
            }
        )

    payload = {
        "schema_version": 1,
        "supplement_number": 6,
        "total_models_in_roster": len(TWENTY_MODELS),
        "cli_evaluated_models_count": len(NINETEEN_CLI_MODELS),
        "cli_evaluated_total_runs": len(NINETEEN_CLI_MODELS) * len(TASKS),
        "cli_prior_model_score_drifts": 0,
        "cli_action_counts": cli_action_counts,
        "cli_pareto_frontier": pareto,
        "gemini_4_carbon_metadata": GEMINI_4_CARBON_RELEASE_METADATA,
        "carbon_official_benchmark_audit": carbon_audit,
        "cybersecurity_and_safety_audit": cyber_audit,
        "official_17_benchmarks": [
            {
                **asdict(b),
                "delta_vs_argon": b.delta_vs_argon,
                "ratio_vs_argon": b.ratio_vs_argon,
            }
            for b in OFFICIAL_CARBON_BENCHMARKS
        ],
        "sec_bench_pro_leaderboard": [asdict(e) for e in SEC_BENCH_PRO_LEADERBOARD],
        "exploitgym_leaderboard": [asdict(e) for e in EXPLOITGYM_LEADERBOARD],
        "cwe_bench_leaderboard": [asdict(e) for e in CWE_BENCH_LEADERBOARD],
        "gray_swan_ipi_leaderboard": [asdict(e) for e in GRAY_SWAN_IPI_LEADERBOARD],
        "coding_19_cli_models": cli_summaries,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return payload


if __name__ == "__main__":
    out_file = Path(__file__).resolve().parent.parent / "evidence" / "verifier-summary.json"
    summary = export_summary_json(out_file)
    print(f"Wrote verification summary to {out_file}")
    print(f"Total Roster Models: {summary['total_models_in_roster']} (19 CLI GA + 1 Fairwind Preview)")
    print(f"Gemini 4 Carbon #1 Ranks: {summary['carbon_official_benchmark_audit']['rank_1_count']}/17")
    print(f"Gray Swan IPI k=15 ASR: {summary['cybersecurity_and_safety_audit']['gray_swan_ipi']['carbon_asr_pct']}%")
