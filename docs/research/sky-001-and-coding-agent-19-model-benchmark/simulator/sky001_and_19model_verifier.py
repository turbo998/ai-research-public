"""Offline verification and simulation suite for:
1. Skyfall AI SKY-001 Engineering World Model (hierarchical composer critical-path scaling & dual-source CAD/BIM benchmark audit)
2. Copilot CLI 19-Model Coding Agent Benchmark (Supplement 5: Claude Haiku 5.5 & Gemini 4 Argon Pareto and tier analysis)
3. Cross-modality comparison between One-Shot LLM CAD/BIM scripting and Multi-Turn CLI Agent software engineering.

All coordinates are sealed from primary source bundles:
- skyfall.ai/assets/index-D5BqB7X_.js (SHA256: 1bc34257c0f2f1db82336d13f95f88c391950c0957655377f752954b4cd7199f)
- skyfall.ai/assets/article-D6mnIEDb.js (SHA256: 8f22592c0d7f0bc1600158903685a5212ddb417499cde1c1e93754de5e6a9830)
- satomic/copilot-benchmark@a191383571a13143685fd6f7787512c4e281a9ba
"""

from __future__ import annotations

import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class AssemblySpec:
    key: str
    name: str
    leaves: int
    nodes: int
    depth: int


@dataclass(frozen=True)
class CriticalPathResult:
    key: str
    name: str
    leaves: int
    nodes: int
    internal_nodes: int
    depth: int
    steps_per_part: int
    parallel_workers: int
    total_model_calls: int
    flat_sequential_steps: int
    hierarchical_batches: int
    hierarchical_sequential_steps: int
    critical_path_speedup: float


@dataclass(frozen=True)
class SkyBenchmarkRow:
    model: str
    iou_pct: float | None
    seconds_per_case: float
    usd_per_case: float
    ours: bool = False


@dataclass(frozen=True)
class CodingModelRecord:
    slug: str
    display_name: str
    cohort: str
    cli_version: str
    effort: str
    atomic_mean: float
    medium_mean: float
    complex_mean: float
    total_mean: float
    hidden_passed: int
    hidden_total: int
    atomic_rounds_mean: float
    medium_rounds_mean: float
    complex_rounds_mean: float
    complex_to_atomic_round_ratio: float
    total_rounds: int
    output_tokens: int
    cost_usd: float
    wall_seconds: float
    inference_seconds: float
    task_scores: dict[str, float]
    task_wall_seconds: dict[str, int]
    task_inference_seconds: dict[str, int]
    task_cost_usd: dict[str, float]
    task_rounds: dict[str, int]
    task_output_tokens: dict[str, int]


SKYFALL_SHOWCASE_ASSEMBLIES: tuple[AssemblySpec, ...] = (
    AssemblySpec("jaguar", "Jaguar E-Type Roadster", leaves=103, nodes=139, depth=5),
    AssemblySpec("jet", "Jet Engine", leaves=70, nodes=96, depth=5),
    AssemblySpec("arcmate", "FANUC ArcMate 100iB Welding Robot", leaves=35, nodes=55, depth=4),
    AssemblySpec("tractor", "Minitractor 4x4", leaves=92, nodes=130, depth=5),
)

SKYFALL_BENCHMARKS: dict[str, dict[str, tuple[SkyBenchmarkRow, ...]]] = {
    "cad": {
        "blog": (
            SkyBenchmarkRow("SKY-001", 79.7, 3.9, 0.005, ours=True),
            SkyBenchmarkRow("GPT-6 Astra", 79.1, 199.0, 0.75),
            SkyBenchmarkRow("Gemini 4", 76.9, 253.0, 0.25),
            SkyBenchmarkRow("Qwen 3.8 Max", 34.4, 764.0, 0.30),
            SkyBenchmarkRow("Kimi K3", 9.5, 439.0, 0.13),
            SkyBenchmarkRow("Grok 4.7", None, 1250.0, 0.59),
        ),
        "landing": (
            SkyBenchmarkRow("SKY-001", 79.7, 3.9, 0.005, ours=True),
            SkyBenchmarkRow("GPT-6 Astra", 79.1, 199.0, 0.75),
            SkyBenchmarkRow("Opus 5.5", 69.4, 110.0, 0.31),
            SkyBenchmarkRow("Gemini 3.8 Flash", 54.7, 112.0, 0.08),
            SkyBenchmarkRow("Qwen 3.8 Max", 34.4, 764.0, 0.30),
            SkyBenchmarkRow("Kimi K3", 9.5, 439.0, 0.13),
            SkyBenchmarkRow("Grok 4.7", None, 1250.0, 0.59),
        ),
    },
    "bim": {
        "blog": (
            SkyBenchmarkRow("SKY-001", 43.6, 1.22, 0.0024, ours=True),
            SkyBenchmarkRow("GPT-6 Astra", 40.6, 144.6, 0.446),
            SkyBenchmarkRow("Gemini 3.8 Flash", 42.3, 346.2, 0.218),
            SkyBenchmarkRow("Qwen 3.8 Max", 28.8, 255.3, 0.111),
            SkyBenchmarkRow("Kimi K3", 33.7, 113.9, 0.270),
            SkyBenchmarkRow("Grok 4.7", 28.2, 592.1, 0.305),
        ),
        "landing": (
            SkyBenchmarkRow("SKY-001", 43.6, 1.22, 0.00237, ours=True),
            SkyBenchmarkRow("GPT-6 Astra", 40.6, 144.4, 0.4465),
            SkyBenchmarkRow("Opus 5.5", 34.4, 113.1, 0.276),
            SkyBenchmarkRow("Gemini 3.8 Flash", 42.3, 345.4, 0.2185),
            SkyBenchmarkRow("Qwen 3.8 Max", 28.8, 254.5, 0.111),
            SkyBenchmarkRow("Kimi K3", 33.7, 114.0, 0.270),
            SkyBenchmarkRow("Grok 4.7", 28.2, 592.3, 0.305),
        ),
    },
}

SKYFALL_COMPOSER_LLM_JUDGES: dict[str, dict[str, float]] = {
    "Part decomposition": {"SKY-001": 7.8, "GPT-6 Astra": 6.4},
    "Interior": {"SKY-001": 7.3, "GPT-6 Astra": 6.3},
    "Complexity": {"SKY-001": 8.0, "GPT-6 Astra": 7.3},
    "Match to the input image": {"SKY-001": 8.1, "GPT-6 Astra": 6.7},
    "Exterior realism": {"SKY-001": 7.7, "GPT-6 Astra": 7.4},
}

TASKS: tuple[str, ...] = ("A1", "A2", "A3", "A4", "A5", "M1", "M2", "C1", "C2", "C3", "C4")

NINETEEN_MODELS: tuple[CodingModelRecord, ...] = (
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
        task_wall_seconds={"A1": 69, "A2": 127, "A3": 74, "A4": 76, "A5": 99, "M1": 396, "M2": 228, "C1": 382, "C2": 501, "C3": 788, "C4": 613},
        task_inference_seconds={"A1": 25, "A2": 70, "A3": 27, "A4": 28, "A5": 50, "M1": 197, "M2": 131, "C1": 255, "C2": 255, "C3": 685, "C4": 487},
        task_cost_usd={"A1": 0.42, "A2": 0.43, "A3": 0.27, "A4": 0.28, "A5": 0.35, "M1": 1.07, "M2": 0.86, "C1": 1.54, "C2": 1.83, "C3": 4.34, "C4": 3.06},
        task_rounds={"A1": 3, "A2": 7, "A3": 3, "A4": 4, "A5": 4, "M1": 16, "M2": 10, "C1": 15, "C2": 17, "C3": 35, "C4": 28},
        task_output_tokens={"A1": 1185, "A2": 3303, "A3": 1250, "A4": 1028, "A5": 2482, "M1": 11696, "M2": 8650, "C1": 18735, "C2": 20138, "C3": 52835, "C4": 36552},
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
        task_wall_seconds={"A1": 33, "A2": 39, "A3": 34, "A4": 51, "A5": 98, "M1": 125, "M2": 128, "C1": 156, "C2": 236, "C3": 594, "C4": 415},
        task_inference_seconds={"A1": 17, "A2": 22, "A3": 17, "A4": 29, "A5": 63, "M1": 88, "M2": 106, "C1": 132, "C2": 200, "C3": 546, "C4": 352},
        task_cost_usd={"A1": 0.15, "A2": 0.10, "A3": 0.09, "A4": 0.13, "A5": 0.25, "M1": 0.34, "M2": 0.44, "C1": 0.52, "C2": 0.71, "C3": 1.82, "C4": 1.28},
        task_rounds={"A1": 3, "A2": 3, "A3": 3, "A4": 6, "A5": 9, "M1": 6, "M2": 9, "C1": 8, "C2": 8, "C3": 20, "C4": 17},
        task_output_tokens={"A1": 1775, "A2": 2180, "A3": 1353, "A4": 2441, "A5": 6983, "M1": 9932, "M2": 11524, "C1": 16894, "C2": 21681, "C3": 61611, "C4": 39602},
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
        task_wall_seconds={"A1": 62, "A2": 113, "A3": 48, "A4": 99, "A5": 61, "M1": 216, "M2": 299, "C1": 533, "C2": 613, "C3": 910, "C4": 843},
        task_inference_seconds={"A1": 29, "A2": 74, "A3": 22, "A4": 60, "A5": 33, "M1": 173, "M2": 236, "C1": 450, "C2": 475, "C3": 758, "C4": 732},
        task_cost_usd={"A1": 0.28, "A2": 0.55, "A3": 0.17, "A4": 0.46, "A5": 0.21, "M1": 0.87, "M2": 1.41, "C1": 2.34, "C2": 2.78, "C3": 4.65, "C4": 3.68},
        task_rounds={"A1": 4, "A2": 8, "A3": 3, "A4": 6, "A5": 4, "M1": 11, "M2": 14, "C1": 23, "C2": 33, "C3": 47, "C4": 35},
        task_output_tokens={"A1": 2436, "A2": 6475, "A3": 1359, "A4": 5492, "A5": 2497, "M1": 12217, "M2": 21172, "C1": 37698, "C2": 39188, "C3": 62598, "C4": 58032},
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
        task_wall_seconds={"A1": 23, "A2": 28, "A3": 25, "A4": 31, "A5": 34, "M1": 82, "M2": 84, "C1": 150, "C2": 253, "C3": 1116, "C4": 279},
        task_inference_seconds={"A1": 9, "A2": 17, "A3": 13, "A4": 12, "A5": 18, "M1": 60, "M2": 58, "C1": 117, "C2": 207, "C3": 1089, "C4": 251},
        task_cost_usd={"A1": 0.0048, "A2": 0.0042, "A3": 0.0037, "A4": 0.0033, "A5": 0.0050, "M1": 0.0123, "M2": 0.0137, "C1": 0.0232, "C2": 0.0430, "C3": 0.1693, "C4": 0.0513},
        task_rounds={"A1": 4, "A2": 3, "A3": 4, "A4": 4, "A5": 6, "M1": 7, "M2": 10, "C1": 7, "C2": 11, "C3": 24, "C4": 14},
        task_output_tokens={"A1": 1603, "A2": 3730, "A3": 2509, "A4": 1696, "A5": 3786, "M1": 14002, "M2": 13448, "C1": 29186, "C2": 55248, "C3": 263769, "C4": 64139},
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
        task_wall_seconds={"A1": 394, "A2": 221, "A3": 163, "A4": 53, "A5": 258, "M1": 556, "M2": 238, "C1": 1664, "C2": 1174, "C3": 4686, "C4": 1464},
        task_inference_seconds={"A1": 377, "A2": 200, "A3": 145, "A4": 34, "A5": 236, "M1": 518, "M2": 207, "C1": 1613, "C2": 1084, "C3": 2029, "C4": 1405},
        task_cost_usd={"A1": 0.08, "A2": 0.20, "A3": 0.20, "A4": 0.09, "A5": 0.28, "M1": 0.63, "M2": 0.36, "C1": 1.48, "C2": 2.02, "C3": 5.00, "C4": 1.88},
        task_rounds={"A1": 3, "A2": 6, "A3": 5, "A4": 4, "A5": 7, "M1": 7, "M2": 6, "C1": 16, "C2": 31, "C3": 45, "C4": 13},
        task_output_tokens={"A1": 10544, "A2": 9311, "A3": 6814, "A4": 1372, "A5": 11260, "M1": 28479, "M2": 14084, "C1": 92954, "C2": 73784, "C3": 191967, "C4": 74304},
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
        task_wall_seconds={"A1": 33, "A2": 34, "A3": 34, "A4": 37, "A5": 38, "M1": 82, "M2": 82, "C1": 150, "C2": 155, "C3": 399, "C4": 255},
        task_inference_seconds={"A1": 8, "A2": 17, "A3": 12, "A4": 13, "A5": 14, "M1": 57, "M2": 59, "C1": 112, "C2": 122, "C3": 362, "C4": 220},
        task_cost_usd={"A1": 0.07, "A2": 0.07, "A3": 0.05, "A4": 0.06, "A5": 0.05, "M1": 0.18, "M2": 0.20, "C1": 0.33, "C2": 0.39, "C3": 0.92, "C4": 0.56},
        task_rounds={"A1": 2, "A2": 3, "A3": 3, "A4": 4, "A5": 2, "M1": 5, "M2": 8, "C1": 7, "C2": 9, "C3": 13, "C4": 9},
        task_output_tokens={"A1": 679, "A2": 2409, "A3": 1242, "A4": 1155, "A5": 1795, "M1": 10114, "M2": 9520, "C1": 19577, "C2": 22813, "C3": 56390, "C4": 35442},
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
        task_wall_seconds={"A1": 40, "A2": 50, "A3": 44, "A4": 45, "A5": 64, "M1": 134, "M2": 95, "C1": 198, "C2": 231, "C3": 364, "C4": 379},
        task_inference_seconds={"A1": 16, "A2": 34, "A3": 24, "A4": 22, "A5": 36, "M1": 104, "M2": 77, "C1": 155, "C2": 201, "C3": 341, "C4": 340},
        task_cost_usd={"A1": 0.05, "A2": 0.06, "A3": 0.06, "A4": 0.06, "A5": 0.07, "M1": 0.13, "M2": 0.12, "C1": 0.18, "C2": 0.25, "C3": 0.38, "C4": 0.35},
        task_rounds={"A1": 4, "A2": 4, "A3": 4, "A4": 4, "A5": 6, "M1": 5, "M2": 5, "C1": 4, "C2": 8, "C3": 9, "C4": 7},
        task_output_tokens={"A1": 853, "A2": 1763, "A3": 1285, "A4": 1168, "A5": 2336, "M1": 6732, "M2": 5350, "C1": 10955, "C2": 14742, "C3": 24742, "C4": 22981},
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
        task_wall_seconds={"A1": 44, "A2": 46, "A3": 41, "A4": 51, "A5": 64, "M1": 186, "M2": 125, "C1": 175, "C2": 308, "C3": 482, "C4": 438},
        task_inference_seconds={"A1": 19, "A2": 31, "A3": 25, "A4": 19, "A5": 41, "M1": 160, "M2": 100, "C1": 137, "C2": 254, "C3": 443, "C4": 388},
        task_cost_usd={"A1": 0.30, "A2": 0.35, "A3": 0.34, "A4": 0.32, "A5": 0.37, "M1": 0.89, "M2": 0.72, "C1": 0.99, "C2": 1.46, "C3": 2.08, "C4": 2.09},
        task_rounds={"A1": 4, "A2": 4, "A3": 4, "A4": 4, "A5": 4, "M1": 6, "M2": 5, "C1": 6, "C2": 8, "C3": 8, "C4": 9},
        task_output_tokens={"A1": 885, "A2": 1492, "A3": 1310, "A4": 832, "A5": 1774, "M1": 8963, "M2": 6342, "C1": 10049, "C2": 15975, "C3": 25792, "C4": 24647},
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
        task_wall_seconds={"A1": 50, "A2": 71, "A3": 49, "A4": 41, "A5": 61, "M1": 211, "M2": 150, "C1": 462, "C2": 495, "C3": 921, "C4": 681},
        task_inference_seconds={"A1": 18, "A2": 37, "A3": 22, "A4": 14, "A5": 30, "M1": 146, "M2": 99, "C1": 344, "C2": 334, "C3": 803, "C4": 546},
        task_cost_usd={"A1": 0.10, "A2": 0.11, "A3": 0.09, "A4": 0.07, "A5": 0.10, "M1": 0.31, "M2": 0.24, "C1": 1.33, "C2": 1.18, "C3": 2.81, "C4": 1.53},
        task_rounds={"A1": 3, "A2": 6, "A3": 5, "A4": 4, "A5": 7, "M1": 15, "M2": 10, "C1": 36, "C2": 31, "C3": 34, "C4": 39},
        task_output_tokens={"A1": 1966, "A2": 4120, "A3": 2033, "A4": 1280, "A5": 3145, "M1": 12450, "M2": 9800, "C1": 45120, "C2": 38900, "C3": 68200, "C4": 52136},
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
        task_wall_seconds={"A1": 120, "A2": 109, "A3": 95, "A4": 113, "A5": 162, "M1": 291, "M2": 411, "C1": 589, "C2": 1071, "C3": 5060, "C4": 1008},
        task_inference_seconds={"A1": 57, "A2": 56, "A3": 44, "A4": 37, "A5": 86, "M1": 213, "M2": 318, "C1": 510, "C2": 979, "C3": 1757, "C4": 885},
        task_cost_usd={"A1": 0.12, "A2": 0.12, "A3": 0.11, "A4": 0.11, "A5": 0.17, "M1": 0.26, "M2": 0.41, "C1": 0.59, "C2": 0.97, "C3": 1.81, "C4": 0.93},
        task_rounds={"A1": 6, "A2": 5, "A3": 5, "A4": 6, "A5": 11, "M1": 11, "M2": 22, "C1": 13, "C2": 11, "C3": 29, "C4": 24},
        task_output_tokens={"A1": 1780, "A2": 1961, "A3": 1531, "A4": 879, "A5": 2750, "M1": 6893, "M2": 9197, "C1": 21364, "C2": 38038, "C3": 59463, "C4": 31465},
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
        task_wall_seconds={"A1": 52, "A2": 104, "A3": 51, "A4": 48, "A5": 53, "M1": 231, "M2": 134, "C1": 345, "C2": 288, "C3": 1007, "C4": 397},
        task_inference_seconds={"A1": 32, "A2": 79, "A3": 39, "A4": 26, "A5": 41, "M1": 218, "M2": 122, "C1": 332, "C2": 272, "C3": 984, "C4": 370},
        task_cost_usd={"A1": 0.069, "A2": 0.153, "A3": 0.079, "A4": 0.060, "A5": 0.115, "M1": 0.162, "M2": 0.162, "C1": 0.262, "C2": 0.315, "C3": 0.986, "C4": 0.458},
        task_rounds={"A1": 5, "A2": 11, "A3": 5, "A4": 4, "A5": 5, "M1": 7, "M2": 8, "C1": 7, "C2": 9, "C3": 29, "C4": 16},
        task_output_tokens={"A1": 1214, "A2": 5020, "A3": 1668, "A4": 689, "A5": 2168, "M1": 5963, "M2": 6609, "C1": 10889, "C2": 15002, "C3": 39854, "C4": 27679},
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
        task_wall_seconds={"A1": 103, "A2": 171, "A3": 144, "A4": 116, "A5": 144, "M1": 256, "M2": 224, "C1": 412, "C2": 540, "C3": 1340, "C4": 722},
        task_inference_seconds={"A1": 45, "A2": 111, "A3": 88, "A4": 55, "A5": 85, "M1": 179, "M2": 157, "C1": 335, "C2": 452, "C3": 1179, "C4": 617},
        task_cost_usd={"A1": 0.18, "A2": 0.23, "A3": 0.22, "A4": 0.10, "A5": 0.17, "M1": 0.30, "M2": 0.28, "C1": 0.46, "C2": 0.52, "C3": 1.91, "C4": 0.84},
        task_rounds={"A1": 7, "A2": 9, "A3": 8, "A4": 7, "A5": 9, "M1": 9, "M2": 11, "C1": 10, "C2": 14, "C3": 37, "C4": 17},
        task_output_tokens={"A1": 3100, "A2": 5200, "A3": 4800, "A4": 2100, "A5": 4200, "M1": 12500, "M2": 11800, "C1": 24500, "C2": 28900, "C3": 65110, "C4": 32000},
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
        task_wall_seconds={"A1": 75, "A2": 55, "A3": 52, "A4": 95, "A5": 60, "M1": 120, "M2": 102, "C1": 146, "C2": 199, "C3": 304, "C4": 236},
        task_inference_seconds={"A1": 47, "A2": 29, "A3": 24, "A4": 45, "A5": 27, "M1": 82, "M2": 75, "C1": 97, "C2": 154, "C3": 257, "C4": 198},
        task_cost_usd={"A1": 0.14, "A2": 0.13, "A3": 0.12, "A4": 0.13, "A5": 0.13, "M1": 0.23, "M2": 0.26, "C1": 0.34, "C2": 0.51, "C3": 0.97, "C4": 0.63},
        task_rounds={"A1": 9, "A2": 4, "A3": 4, "A4": 10, "A5": 4, "M1": 11, "M2": 5, "C1": 5, "C2": 8, "C3": 15, "C4": 10},
        task_output_tokens={"A1": 2729, "A2": 1844, "A3": 1349, "A4": 2755, "A5": 1743, "M1": 7060, "M2": 5561, "C1": 8831, "C2": 12869, "C3": 26894, "C4": 17344},
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
        task_wall_seconds={"A1": 70, "A2": 78, "A3": 87, "A4": 72, "A5": 62, "M1": 140, "M2": 155, "C1": 200, "C2": 276, "C3": 1135, "C4": 400},
        task_inference_seconds={"A1": 31, "A2": 47, "A3": 45, "A4": 30, "A5": 32, "M1": 112, "M2": 118, "C1": 149, "C2": 215, "C3": 1011, "C4": 341},
        task_cost_usd={"A1": 0.0033, "A2": 0.0040, "A3": 0.0049, "A4": 0.0034, "A5": 0.0032, "M1": 0.0078, "M2": 0.0107, "C1": 0.0103, "C2": 0.0174, "C3": 0.0839, "C4": 0.0223},
        task_rounds={"A1": 4, "A2": 6, "A3": 6, "A4": 4, "A5": 4, "M1": 6, "M2": 10, "C1": 7, "C2": 13, "C3": 64, "C4": 15},
        task_output_tokens={"A1": 1660, "A2": 2350, "A3": 2992, "A4": 1817, "A5": 1635, "M1": 7583, "M2": 9868, "C1": 10830, "C2": 17956, "C3": 64539, "C4": 24181},
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
        task_wall_seconds={"A1": 233, "A2": 399, "A3": 329, "A4": 234, "A5": 398, "M1": 464, "M2": 576, "C1": 576, "C2": 623, "C3": 722, "C4": 570},
        task_inference_seconds={"A1": 98, "A2": 306, "A3": 215, "A4": 123, "A5": 267, "M1": 346, "M2": 421, "C1": 475, "C2": 453, "C3": 572, "C4": 475},
        task_cost_usd={"A1": 0.09, "A2": 0.16, "A3": 0.11, "A4": 0.08, "A5": 0.21, "M1": 0.18, "M2": 0.30, "C1": 0.33, "C2": 0.38, "C3": 0.67, "C4": 0.32},
        task_rounds={"A1": 12, "A2": 17, "A3": 15, "A4": 14, "A5": 32, "M1": 23, "M2": 34, "C1": 24, "C2": 41, "C3": 39, "C4": 26},
        task_output_tokens={"A1": 2326, "A2": 5302, "A3": 3177, "A4": 1856, "A5": 5119, "M1": 8404, "M2": 14836, "C1": 14218, "C2": 17464, "C3": 27747, "C4": 22540},
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
        task_wall_seconds={"A1": 126, "A2": 169, "A3": 97, "A4": 142, "A5": 128, "M1": 161, "M2": 225, "C1": 381, "C2": 411, "C3": 627, "C4": 594},
        task_inference_seconds={"A1": 35, "A2": 69, "A3": 33, "A4": 41, "A5": 49, "M1": 62, "M2": 95, "C1": 165, "C2": 176, "C3": 339, "C4": 252},
        task_cost_usd={"A1": 0.0111, "A2": 0.0178, "A3": 0.0104, "A4": 0.0140, "A5": 0.0120, "M1": 0.0191, "M2": 0.0250, "C1": 0.0465, "C2": 0.0509, "C3": 0.1062, "C4": 0.0755},
        task_rounds={"A1": 9, "A2": 11, "A3": 6, "A4": 11, "A5": 9, "M1": 10, "M2": 18, "C1": 26, "C2": 30, "C3": 63, "C4": 42},
        task_output_tokens={"A1": 2218, "A2": 5608, "A3": 2518, "A4": 3249, "A5": 2835, "M1": 5191, "M2": 6946, "C1": 14045, "C2": 13691, "C3": 27861, "C4": 22437},
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
        task_wall_seconds={"A1": 116, "A2": 110, "A3": 135, "A4": 117, "A5": 150, "M1": 201, "M2": 196, "C1": 403, "C2": 426, "C3": 812, "C4": 722},
        task_inference_seconds={"A1": 46, "A2": 53, "A3": 81, "A4": 63, "A5": 88, "M1": 131, "M2": 119, "C1": 306, "C2": 328, "C3": 655, "C4": 579},
        task_cost_usd={"A1": 0.0095, "A2": 0.0092, "A3": 0.0109, "A4": 0.0053, "A5": 0.0161, "M1": 0.0239, "M2": 0.0312, "C1": 0.0654, "C2": 0.0679, "C3": 0.1409, "C4": 0.1480},
        task_rounds={"A1": 7, "A2": 4, "A3": 7, "A4": 4, "A5": 8, "M1": 12, "M2": 16, "C1": 19, "C2": 21, "C3": 51, "C4": 43},
        task_output_tokens={"A1": 3100, "A2": 3200, "A3": 4100, "A4": 2200, "A5": 5400, "M1": 11200, "M2": 13900, "C1": 31200, "C2": 33400, "C3": 64200, "C4": 61200},
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
        task_wall_seconds={"A1": 33, "A2": 86, "A3": 80, "A4": 89, "A5": 124, "M1": 174, "M2": 491, "C1": 764, "C2": 1585, "C3": 4563, "C4": 2752},
        task_inference_seconds={"A1": 16, "A2": 64, "A3": 55, "A4": 60, "A5": 85, "M1": 137, "M2": 251, "C1": 383, "C2": 986, "C3": 2278, "C4": 1302},
        task_cost_usd={"A1": 0.01, "A2": 0.01, "A3": 0.02, "A4": 0.02, "A5": 0.03, "M1": 0.02, "M2": 0.08, "C1": 0.12, "C2": 0.22, "C3": 0.82, "C4": 0.60},
        task_rounds={"A1": 3, "A2": 6, "A3": 7, "A4": 8, "A5": 16, "M1": 10, "M2": 34, "C1": 36, "C2": 61, "C3": 145, "C4": 94},
        task_output_tokens={"A1": 1200, "A2": 3400, "A3": 3100, "A4": 2900, "A5": 5800, "M1": 8900, "M2": 21500, "C1": 32400, "C2": 48900, "C3": 98200, "C4": 63800},
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
        task_wall_seconds={"A1": 101, "A2": 214, "A3": 249, "A4": 123, "A5": 530, "M1": 230, "M2": 401, "C1": 826, "C2": 645, "C3": 673, "C4": 856},
        task_inference_seconds={"A1": 52, "A2": 101, "A3": 208, "A4": 61, "A5": 427, "M1": 152, "M2": 209, "C1": 391, "C2": 432, "C3": 463, "C4": 667},
        task_cost_usd={"A1": 0.08, "A2": 0.11, "A3": 0.22, "A4": 0.08, "A5": 0.43, "M1": 0.18, "M2": 0.22, "C1": 0.45, "C2": 0.59, "C3": 0.67, "C4": 0.89},
        task_rounds={"A1": 10, "A2": 14, "A3": 12, "A4": 13, "A5": 20, "M1": 22, "M2": 22, "C1": 43, "C2": 59, "C3": 60, "C4": 66},
        task_output_tokens={"A1": 4100, "A2": 8200, "A3": 12400, "A4": 5100, "A5": 24800, "M1": 15600, "M2": 19200, "C1": 42100, "C2": 48900, "C3": 58400, "C4": 64300},
    ),
)


def compute_critical_path(
    assembly: AssemblySpec,
    steps_per_part: int = 100,
    parallel_workers: int = 128,
) -> CriticalPathResult:
    """Compute sequential model calls for a flat autoregressive chain vs SKY-001's hierarchical part tree."""
    if steps_per_part <= 0:
        raise ValueError("steps_per_part must be positive")
    if parallel_workers <= 0:
        raise ValueError("parallel_workers must be positive")
    internal = assembly.nodes - assembly.leaves
    total_calls = internal + assembly.leaves * steps_per_part
    flat_steps = total_calls
    batches = math.ceil(assembly.leaves / parallel_workers)
    hier_steps = assembly.depth + batches * steps_per_part
    speedup = round(flat_steps / hier_steps, 2)
    return CriticalPathResult(
        key=assembly.key,
        name=assembly.name,
        leaves=assembly.leaves,
        nodes=assembly.nodes,
        internal_nodes=internal,
        depth=assembly.depth,
        steps_per_part=steps_per_part,
        parallel_workers=parallel_workers,
        total_model_calls=total_calls,
        flat_sequential_steps=flat_steps,
        hierarchical_batches=batches,
        hierarchical_sequential_steps=hier_steps,
        critical_path_speedup=speedup,
    )


def audit_sky001_benchmarks() -> dict[str, Any]:
    """Audit SKY-001 CAD and BIM benchmark tables across the blog and landing page JS bundles."""
    cad_blog = {r.model: r for r in SKYFALL_BENCHMARKS["cad"]["blog"]}
    cad_landing = {r.model: r for r in SKYFALL_BENCHMARKS["cad"]["landing"]}
    bim_blog = {r.model: r for r in SKYFALL_BENCHMARKS["bim"]["blog"]}
    bim_landing = {r.model: r for r in SKYFALL_BENCHMARKS["bim"]["landing"]}

    sky_cad = cad_blog["SKY-001"]
    astra_cad = cad_blog["GPT-6 Astra"]
    cad_speed_ratio = round(astra_cad.seconds_per_case / sky_cad.seconds_per_case, 1)
    cad_cost_ratio = round(astra_cad.usd_per_case / sky_cad.usd_per_case, 1)
    cad_iou_lead_vs_astra = round((sky_cad.iou_pct or 0.0) - (astra_cad.iou_pct or 0.0), 1)

    sky_bim_b = bim_blog["SKY-001"]
    astra_bim_b = bim_blog["GPT-6 Astra"]
    flash_bim_b = bim_blog["Gemini 3.8 Flash"]
    bim_speed_ratio_blog = round(astra_bim_b.seconds_per_case / sky_bim_b.seconds_per_case, 1)
    bim_cost_ratio_blog = round(astra_bim_b.usd_per_case / sky_bim_b.usd_per_case, 1)

    sky_bim_l = bim_landing["SKY-001"]
    astra_bim_l = bim_landing["GPT-6 Astra"]
    bim_speed_ratio_landing = round(astra_bim_l.seconds_per_case / sky_bim_l.seconds_per_case, 1)
    bim_cost_ratio_landing = round(astra_bim_l.usd_per_case / sky_bim_l.usd_per_case, 1)

    cad_only_in_blog = sorted(set(cad_blog) - set(cad_landing))
    cad_only_in_landing = sorted(set(cad_landing) - set(cad_blog))
    bim_only_in_landing = sorted(set(bim_landing) - set(bim_blog))

    return {
        "cad": {
            "sky001_iou_pct": sky_cad.iou_pct,
            "astra_iou_pct": astra_cad.iou_pct,
            "iou_lead_vs_astra_pts": cad_iou_lead_vs_astra,
            "speedup_vs_astra_x": cad_speed_ratio,
            "cost_ratio_vs_astra_x": cad_cost_ratio,
            "models_only_in_blog": cad_only_in_blog,
            "models_only_in_landing": cad_only_in_landing,
            "grok_4_7_completed_cases": 0,
        },
        "bim": {
            "sky001_iou_pct": sky_bim_b.iou_pct,
            "next_best_model": "Gemini 3.8 Flash",
            "next_best_iou_pct": flash_bim_b.iou_pct,
            "iou_lead_vs_next_best_pts": round((sky_bim_b.iou_pct or 0.0) - (flash_bim_b.iou_pct or 0.0), 1),
            "iou_lead_vs_astra_pts": round((sky_bim_b.iou_pct or 0.0) - (astra_bim_b.iou_pct or 0.0), 1),
            "speedup_vs_astra_blog_x": bim_speed_ratio_blog,
            "cost_ratio_vs_astra_blog_x": bim_cost_ratio_blog,
            "speedup_vs_astra_landing_x": bim_speed_ratio_landing,
            "cost_ratio_vs_astra_landing_x": bim_cost_ratio_landing,
            "models_only_in_landing": bim_only_in_landing,
        },
    }


def classify_coding_model_action(rec: CodingModelRecord) -> str:
    """Apply threshold gating consistent with the 19-model benchmark report."""
    if rec.hidden_passed == rec.hidden_total and rec.total_mean >= 98.45:
        return "Act automatically"
    if rec.hidden_passed < 1260 or rec.complex_mean < 96.0:
        return "Send to a human"
    return "Confirm"


def compute_pareto_frontier(models: tuple[CodingModelRecord, ...] = NINETEEN_MODELS) -> list[str]:
    """Identify models that are Pareto-optimal on (total_mean DESC, cost_usd ASC, wall_seconds ASC)."""
    frontier: list[str] = []
    for candidate in models:
        dominated = False
        for other in models:
            if other.slug == candidate.slug:
                continue
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


def build_cross_modality_matrix() -> list[dict[str, Any]]:
    """Map shared frontier model families across SKY-001 (One-Shot CAD/BIM) and Copilot CLI (Multi-Turn Coding Agent)."""
    by_name = {m.display_name: m for m in NINETEEN_MODELS}
    cad_landing = {r.model: r for r in SKYFALL_BENCHMARKS["cad"]["landing"]}
    cad_blog = {r.model: r for r in SKYFALL_BENCHMARKS["cad"]["blog"]}
    bim_landing = {r.model: r for r in SKYFALL_BENCHMARKS["bim"]["landing"]}

    pairs = [
        ("GPT-6 Astra", "GPT-6 Astra", "GPT-6 Astra"),
        ("Opus 5.5", "Opus 5.5", "Opus 5.5"),
        ("Gemini 4 Argon", "Gemini 4", None),
        ("Gemini 3.8 Flash", "Gemini 3.8 Flash", "Gemini 3.8 Flash"),
        ("Kimi K3", "Kimi K3", "Kimi K3"),
        ("Grok 4.7", "Grok 4.7", "Grok 4.7"),
    ]
    rows: list[dict[str, Any]] = []
    for coding_name, cad_name, bim_name in pairs:
        cm = by_name[coding_name]
        cad_row = cad_landing.get(cad_name) or cad_blog.get(cad_name)
        bim_row = bim_landing.get(bim_name) if bim_name else None
        rows.append(
            {
                "coding_model": coding_name,
                "coding_mean_score": cm.total_mean,
                "coding_complex_mean": cm.complex_mean,
                "coding_hidden_pass": f"{cm.hidden_passed}/{cm.hidden_total}",
                "coding_11task_cost_usd": cm.cost_usd,
                "coding_11task_wall_min": round(cm.wall_seconds / 60.0, 1),
                "sky_cad_model_label": cad_name,
                "sky_cad_iou_pct": cad_row.iou_pct if cad_row else None,
                "sky_cad_seconds_per_case": cad_row.seconds_per_case if cad_row else None,
                "sky_cad_usd_per_case": cad_row.usd_per_case if cad_row else None,
                "sky_bim_iou_pct": bim_row.iou_pct if bim_row else None,
                "sky_bim_seconds_per_case": bim_row.seconds_per_case if bim_row else None,
                "sky_bim_usd_per_case": bim_row.usd_per_case if bim_row else None,
            }
        )
    return rows


def export_summary_json(output_path: Path) -> dict[str, Any]:
    """Generate a deterministic verification summary artifact."""
    critical_paths = [asdict(compute_critical_path(a)) for a in SKYFALL_SHOWCASE_ASSEMBLIES]
    sky_audit = audit_sky001_benchmarks()
    pareto = compute_pareto_frontier()
    action_counts = {"Act automatically": 0, "Confirm": 0, "Send to a human": 0}
    model_summaries = []
    for rank, m in enumerate(NINETEEN_MODELS, start=1):
        act = classify_coding_model_action(m)
        action_counts[act] += 1
        model_summaries.append(
            {
                "rank": rank,
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
        "sky001_critical_paths": critical_paths,
        "sky001_benchmark_audit": sky_audit,
        "sky001_composer_llm_judges": SKYFALL_COMPOSER_LLM_JUDGES,
        "coding_19_models_count": len(NINETEEN_MODELS),
        "coding_19_total_runs": len(NINETEEN_MODELS) * len(TASKS),
        "coding_19_action_counts": action_counts,
        "coding_19_pareto_frontier": pareto,
        "coding_19_models": model_summaries,
        "cross_modality_matrix": build_cross_modality_matrix(),
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return payload


if __name__ == "__main__":
    out_file = Path(__file__).resolve().parent.parent / "evidence" / "verifier-summary.json"
    summary = export_summary_json(out_file)
    print(f"Wrote verification summary to {out_file}")
    print(f"19-Model Pareto Frontier: {summary['coding_19_pareto_frontier']}")
    print(f"Action Gating Counts: {summary['coding_19_action_counts']}")
    print(f"SKY-001 Jaguar Critical Path Speedup: {summary['sky001_critical_paths'][0]['critical_path_speedup']}x")
