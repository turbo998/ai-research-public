"""Generate report.json, evidence.json, and test-report-cards.html for:
sky-001-and-coding-agent-19-model-benchmark.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

HARNESS_SRC = Path(r"C:\Users\qichen2\benchmark-harness-engineering\src")
sys.path.insert(0, str(HARNESS_SRC))

from benchmark_harness.cards import render_card_deck  # noqa: E402
from sky001_and_19model_verifier import (  # noqa: E402
    NINETEEN_MODELS,
    SKYFALL_BENCHMARKS,
    SKYFALL_COMPOSER_LLM_JUDGES,
    SKYFALL_SHOWCASE_ASSEMBLIES,
    TASKS,
    audit_sky001_benchmarks,
    build_cross_modality_matrix,
    classify_coding_model_action,
    compute_critical_path,
    compute_pareto_frontier,
)


def build_report_json() -> dict:
    crit_paths = [compute_critical_path(a) for a in SKYFALL_SHOWCASE_ASSEMBLIES]
    sky_audit = audit_sky001_benchmarks()
    pareto = compute_pareto_frontier()
    cross_matrix = build_cross_modality_matrix()

    scorecard_rows = []
    for m in NINETEEN_MODELS:
        act_full = classify_coding_model_action(m)
        act_short = "Auto" if act_full == "Act automatically" else ("Human" if act_full == "Send to a human" else "Confirm")
        wall_m = round(m.wall_seconds / 60.0, 1)
        out_w = round(m.output_tokens / 10000.0, 1)
        new_tag = " [NEW]" if m.slug in ("claude-haiku-5.5", "gemini-4-argon") else ""
        if m.total_mean >= 99.50:
            tier_label = "Tier 1 · Flagship Ceiling"
        elif m.slug in ("claude-haiku-5.5", "claude-sonnet-5.5", "gpt-6.1-sol", "hydrafusion"):
            tier_label = "Tier 2 · High-ROI Pareto"
        elif m.total_mean >= 98.50:
            tier_label = "Tier 3 · High-Score Specialist"
        else:
            tier_label = "Tier 4 · Low-Cost & Lightweight"
        hidden_note = (
            "1310/1310 hidden"
            if m.hidden_passed == m.hidden_total
            else f"{m.hidden_passed}/{m.hidden_total} (-{m.hidden_total - m.hidden_passed} hidden)"
        )
        scorecard_rows.append(
            {
                "scenario": tier_label,
                "question": f"{m.display_name}{new_tag} ({m.total_rounds} rounds · {wall_m}m wall · ${m.cost_usd:.2f} · {out_w}w out)",
                "decider_answer": f"{m.total_mean:.2f} mean | Complex {m.complex_mean:.2f} | {hidden_note}",
                "reported_probability_pct": round(m.total_mean),
                "pointed_right_way": m.hidden_passed == m.hidden_total,
                "action": act_short,
            }
        )

    scorecard_rows.extend(
        [
            {
                "scenario": "Track B · SKY-001 CAD (1k cases)",
                "question": "SKY-001 vs GPT-6 Astra (3.9s / $0.005 vs 199s / $0.75 per part)",
                "decider_answer": "79.7% vs 79.1% IoU (+0.6 pt tie; 51.0x faster, 150.0x cheaper)",
                "reported_probability_pct": 80,
                "pointed_right_way": True,
                "action": "Confirm",
            },
            {
                "scenario": "Track B · SKY-001 BIM (1k plans)",
                "question": "SKY-001 vs Gemini 3.8 Flash & Astra (1.22s / $0.0024 vs 346.2s & 144.6s)",
                "decider_answer": "43.6% vs 42.3% Flash & 40.6% Astra (118.5x faster, 185.8x cheaper)",
                "reported_probability_pct": 44,
                "pointed_right_way": False,
                "action": "Confirm",
            },
        ]
    )

    robustness_rows = [
        {
            "scenario": "Haiku 5.5 · Generational Leap vs Haiku 4.5 (11-Task Mean & Complex)",
            "selected_option": "Complex mean 89.64% -> 99.22% (+9.58 pts); Hidden 1239 -> 1308/1310; Cost $3.93 -> $0.33 (-91.6%)",
            "original_pct": 94.0,
            "reversed_pct": 99.2,
            "change_pts": 5.2,
            "answer_held": True,
        },
        {
            "scenario": "Gemini 4 Argon · Generational Leap vs Gemini 3.8 Flash (11-Task Mean)",
            "selected_option": "Hidden assertions 1276/1310 (97.4%) -> 1310/1310 (100.0%); Rounds 277 -> 106 (-61.7%)",
            "original_pct": 98.0,
            "reversed_pct": 98.6,
            "change_pts": 0.6,
            "answer_held": True,
        },
        {
            "scenario": "Grok 4.7 ·Modality Shift: One-Shot CAD Script vs Multi-Turn CLI Agent",
            "selected_option": "SKY-001 CAD benchmark: 0.0% IoU (null output at 1,250s) -> Copilot CLI: 99.21% (#5 of 19)",
            "original_pct": 0.0,
            "reversed_pct": 99.2,
            "change_pts": 99.2,
            "answer_held": False,
        },
        {
            "scenario": "Kimi K3 · Modality Shift: One-Shot CAD Script vs Multi-Turn CLI Agent",
            "selected_option": "SKY-001 CAD benchmark: 9.5% IoU (439s, $0.13) -> Copilot CLI: 98.68% (1,305/1,310 hidden)",
            "original_pct": 9.5,
            "reversed_pct": 98.7,
            "change_pts": 89.2,
            "answer_held": False,
        },
        {
            "scenario": "GPT-6 Astra · Modality Shift: One-Shot CAD Script vs Multi-Turn CLI Agent",
            "selected_option": "SKY-001 CAD: 79.1% IoU (-0.6 pt vs SKY-001) -> Copilot CLI: 98.82% (Complex #1 at 99.75%)",
            "original_pct": 79.1,
            "reversed_pct": 98.8,
            "change_pts": 19.7,
            "answer_held": True,
        },
        {
            "scenario": "Opus 5.5 · Modality Shift: One-Shot CAD Script vs Multi-Turn CLI Agent",
            "selected_option": "SKY-001 CAD landing: 69.4% IoU (omitted in blog) -> Copilot CLI: 99.68% (#2 overall, 1310/1310)",
            "original_pct": 69.4,
            "reversed_pct": 99.7,
            "change_pts": 30.3,
            "answer_held": True,
        },
        {
            "scenario": "Gemini 4 / Argon · Modality Shift: One-Shot CAD vs Multi-Turn CLI Agent",
            "selected_option": "SKY-001 CAD blog: 76.9% IoU (omitted on landing page) -> Copilot CLI: 98.59% (1310/1310 hidden)",
            "original_pct": 76.9,
            "reversed_pct": 98.6,
            "change_pts": 21.7,
            "answer_held": True,
        },
    ]

    latency_rows = [
        {"question_count": 1, "batched_median_ms": 995, "one_by_one_estimated_ms": 1301, "runs": 11},
        {"question_count": 2, "batched_median_ms": 1034, "one_by_one_estimated_ms": 1444, "runs": 11},
        {"question_count": 3, "batched_median_ms": 1348, "one_by_one_estimated_ms": 1645, "runs": 11},
        {"question_count": 4, "batched_median_ms": 1570, "one_by_one_estimated_ms": 1909, "runs": 11},
        {"question_count": 5, "batched_median_ms": 1617, "one_by_one_estimated_ms": 1960, "runs": 11},
        {"question_count": 6, "batched_median_ms": 1852, "one_by_one_estimated_ms": 2104, "runs": 11},
        {"question_count": 7, "batched_median_ms": 2512, "one_by_one_estimated_ms": 2710, "runs": 11},
        {"question_count": 8, "batched_median_ms": 2210, "one_by_one_estimated_ms": 3355, "runs": 11},
    ]

    tables = [
        {
            "name": "scores_by_difficulty_19_models",
            "columns": ["Rank", "Model", "Cohort", "CLI", "Atomic (5)", "Medium (2)", "Complex (4)", "Total Mean", "Hidden Pass"],
            "rows": [
                [
                    str(idx),
                    m.display_name,
                    m.cohort,
                    m.cli_version,
                    f"{m.atomic_mean:.2f}",
                    f"{m.medium_mean:.2f}",
                    f"{m.complex_mean:.2f}",
                    f"{m.total_mean:.2f}",
                    f"{m.hidden_passed}/{m.hidden_total}",
                ]
                for idx, m in enumerate(NINETEEN_MODELS, start=1)
            ],
            "unit": "score_points_0_to_100",
        },
        {
            "name": "usage_and_efficiency_19_models",
            "columns": ["Model", "Atomic Rds", "Medium Rds", "Complex Rds", "C/A Ratio", "Total Rds", "Output Tokens", "Cost ($)", "Wall (s)", "Inference (s)"],
            "rows": [
                [
                    m.display_name,
                    f"{m.atomic_rounds_mean:.1f}",
                    f"{m.medium_rounds_mean:.1f}",
                    f"{m.complex_rounds_mean:.1f}",
                    f"{m.complex_to_atomic_round_ratio:.1f}x",
                    str(m.total_rounds),
                    str(m.output_tokens),
                    f"{m.cost_usd:.2f}",
                    str(int(m.wall_seconds)),
                    str(int(m.inference_seconds)),
                ]
                for m in NINETEEN_MODELS
            ],
            "unit": "mixed_usage_metrics",
        },
        {
            "name": "task_scores_19_models",
            "columns": ["Model", *TASKS, "Sum"],
            "rows": [
                [
                    m.display_name,
                    *[f"{m.task_scores[t]:.2f}" for t in TASKS],
                    f"{sum(m.task_scores[t] for t in TASKS):.2f}",
                ]
                for m in NINETEEN_MODELS
            ],
            "unit": "score_points_0_to_100",
        },
        {
            "name": "sky001_critical_path_scaling",
            "columns": ["Assembly", "Leaves (L)", "Total Nodes (N)", "Internal (N-L)", "Tree Depth (D)", "Flat Sequential Calls", "Hierarchical Sequential Calls", "Critical Path Speedup"],
            "rows": [
                [
                    cp.name,
                    str(cp.leaves),
                    str(cp.nodes),
                    str(cp.internal_nodes),
                    str(cp.depth),
                    str(cp.flat_sequential_steps),
                    str(cp.hierarchical_sequential_steps),
                    f"{cp.critical_path_speedup:.2f}x",
                ]
                for cp in crit_paths
            ],
            "unit": "sequential_model_evaluations_at_S100_W128",
        },
    ]

    return {
        "schema_version": 1,
        "report_id": "sky-001-and-coding-agent-19-model-benchmark",
        "deck_title": "SKY-001 World Model & Coding Agent 19-Model Benchmark (Supplement 5: Haiku 5.5 & Gemini 4 Argon)",
        "provenance": "anonymized_reported",
        "independently_reproduced": False,
        "source_binding": {
            "upstream_coding_repo": "satomic/copilot-benchmark",
            "pinned_commit": "a191383571a13143685fd6f7787512c4e281a9ba",
            "previous_commit": "aa1e0dc31661ff6343433f06fe3bea1e015b8525",
            "skyfall_landing_bundle": "https://skyfall.ai/assets/index-D5BqB7X_.js",
            "skyfall_landing_sha256": "1bc34257c0f2f1db82336d13f95f88c391950c0957655377f752954b4cd7199f",
            "skyfall_article_bundle": "https://skyfall.ai/assets/article-D6mnIEDb.js",
            "skyfall_article_sha256": "8f22592c0d7f0bc1600158903685a5212ddb417499cde1c1e93754de5e6a9830",
            "models_evaluated_coding": 19,
            "tasks_evaluated_coding": 11,
            "scored_non_reference_runs": 209,
            "reference_bundles": 11,
            "hidden_assertions_per_model": 1310,
            "new_models_in_supplement_5": ["Claude Haiku 5.5", "Gemini 4 Argon"],
            "supplement_5_date": "2026-10-15",
            "supplement_5_cli": "1.0.98",
            "sky001_launch_date": "2026-10-19",
        },
        "cards": [
            {
                "kind": "overview",
                "eyebrow": "HANDS-ON · ENGINEERING WORLD MODEL & 19-MODEL CODING BENCHMARK",
                "headline_prefix": "Haiku 5.5 (#4 at $0.33), Gemini 4 Argon (100% hidden) & ",
                "headline_Gradient": "SKY-001 98.4x Critical-Path Scaling",
                "subtitle": (
                    "Supplement 5 expands Copilot CLI to 19 models (209 runs, CLI 1.0.98): Haiku 5.5 jumps to 99.24 (#4) "
                    "for $0.33 and Gemini 4 Argon passes 1,310/1,310 hidden tests (98.59). Cross-auditing Skyfall AI's SKY-001 "
                    "shows why hierarchical 3D state decomposition beats one-shot LLM CAD scripts by 51x–118.5x in speed."
                ),
                "workbench": {
                    "title": "Dual-Track Engineering Benchmark Workbench (19 Coding Agents + SKY-001 CAD/BIM)",
                    "status_pill": "CLI 1.0.84-3..1.0.98 (209 runs) + SKY-001 JS Audit · anonymized_reported",
                    "scenarios": [
                        "Track A · Coding Agent (19 models × 11 stdlib tasks = 209 runs, 1,310 hidden tests)",
                        "Supplement 5 (2026-10-15 · CLI 1.0.98): Claude Haiku 5.5 & Gemini 4 Argon (+22 runs)",
                        "Track B · SKY-001 Stage 1: Hierarchical Composer (Coarse 3D -> Split Tree -> Leaf Refiner)",
                        "Track B · SKY-001 Stage 2: Construction World Model (3D State Subgoals + 2D Inverse Sketches)",
                        "SKY-001 CAD Benchmark (1,000 parts, ~100 steps/part, 3D IoU + latency + cost)",
                        "SKY-001 BIM Benchmark (1,000 floor plans: 350 IFC + 650 apartments, ~70 steps/plan)",
                        "Cross-Modality Audit: 6 overlapping frontier families (Astra, Opus 5.5, Gemini 4, Flash, Kimi K3, Grok 4.7)",
                    ],
                    "bands_note": (
                        "Coding Agent gating: Act automatically if 1,310/1,310 hidden pass & mean >= 98.45 (9 models); "
                        "Confirm if <1,310 hidden or mean 97.50–98.44 (8 models); Send to a human if hidden < 1,260 (2 models)."
                    ),
                    "metrics": [
                        "Haiku 5.5: 99.24 (#4) · $0.33 · 35.1m",
                        "Gemini 4 Argon: 98.59 (#10) · 1310/1310 · $2.82",
                        "SKY-001 CAD: 79.7% IoU · 3.9s · $0.005",
                        "SKY-001 BIM: 43.6% IoU · 1.22s · $0.0024",
                    ],
                    "decisions": [
                        {
                            "field": "supplement_5_coding_breakthrough",
                            "question_type": "choice",
                            "question": "How do Claude Haiku 5.5 and Gemini 4 Argon reshape the 19-model Coding Agent Pareto frontier?",
                            "selected_answer": "Haiku 5.5 hits 99.24 (#4, $0.33) · Gemini 4 Argon hits 98.59 (1,310/1,310 hidden, $2.82)",
                            "closest_label": "Haiku 5.5 beats Sonnet 5.5 (99.00) & GPT-6.1 Sol (98.86) at 88.6% lower cost; Argon is 9th 100%-hidden model",
                            "confidence": 0.992,
                            "action": "Act automatically",
                            "distribution_pct": {
                                "Haiku 5.5 overall mean (99.24/100 · $0.33)": 99.2,
                                "Sonnet 5.5 overall mean (99.00/100 · $2.89)": 99.0,
                                "Gemini 4 Argon overall mean (98.59/100 · $2.82)": 98.6,
                            },
                        },
                        {
                            "field": "sky_001_world_model_advantage",
                            "question_type": "score",
                            "question": "Does SKY-001 beat frontier LLMs via single-part IoU accuracy or parallel hierarchical critical-path compression?",
                            "selected_answer": "51x–118.5x faster & 150x–188.4x cheaper (IoU +0.6 pt CAD tie vs Astra; +1.3 pt BIM vs Flash)",
                            "closest_label": "Jaguar E-Type (103 leaves, depth 5): 10,336 flat steps compressed to 105 sequential steps (98.44x speedup)",
                            "confidence": 0.797,
                            "action": "Confirm",
                            "distribution_pct": {
                                "SKY-001 CAD IoU (3.9s · $0.005)": 79.7,
                                "GPT-6 Astra CAD IoU (199s · $0.75)": 79.1,
                                "Gemini 4 CAD IoU (253s · $0.25 · blog)": 76.9,
                            },
                        },
                        {
                            "field": "executable_cad_vs_visual_rollout",
                            "question_type": "noul",
                            "question": "Does SKY-001 currently output an editable parametric CAD feature tree (B-Rep/STEP) ready for manufacturing?",
                            "selected_answer": "No (outputs visual 3D state + 2D sketch rollouts; executable feature history is roadmap)",
                            "closest_label": "Waitlist-only closed preview; BIM mean IoU is 43.6% across 1,000 floor plans",
                            "confidence": 0.436,
                            "action": "Confirm",
                            "distribution_pct": {
                                "SKY-001 BIM 1,000-plan IoU (1.22s · $0.0024)": 43.6,
                                "Gemini 3.8 Flash BIM IoU (346.2s · $0.218)": 42.3,
                                "GPT-6 Astra BIM IoU (144.6s · $0.446)": 40.6,
                            },
                        },
                    ],
                },
                "callouts": [
                    {
                        "lead": "Two complementary engineering paradigms audited from primary artifacts (anonymized_reported, independently_reproduced=false).",
                        "body": (
                            "In code space with a CLI test loop, lightweight Haiku 5.5 ($0.33) and Gemini 4 Argon ($2.82, 0$ cache-write) "
                            "match flagship agents; in 3D geometry space without a visual state-feedback loop, one-shot LLM scripts collapse or stall."
                        ),
                    }
                ],
            },
            {
                "kind": "deep_dive",
                "eyebrow": "SCENARIO: HAIKU 5.5, GEMINI 4 ARGON & SKY-001 DUAL-SOURCE AUDIT",
                "headline": "Haiku 5.5 leaps +5.28 pts to 99.24 ($0.33); Argon hits 1,310/1,310; SKY-001 cuts critical path 98.4x.",
                "quote": (
                    "Supplement 5 commit a1913835 (2026-10-15, CLI 1.0.98) adds 22 runs for claude-haiku-5.5 and gemini-4-argon "
                    "while verifying zero score changes across all 17 prior models. Skyfall AI's production JS bundles "
                    "(index-D5BqB7X_.js & article-D6mnIEDb.js) expose exact CAD/BIM metrics and tree node counts."
                ),
                "decisions": [
                    {
                        "field": "claude_haiku_5_5_deep_dive",
                        "question_type": "score",
                        "question": "Claude Haiku 5.5 vs Haiku 4.5 & Sonnet 5.5 across A1–C4 (CLI 1.0.98, effort=medium)",
                        "selected_answer": "99.24 / 100 (Rank 4 of 19 · 1,308/1,310 hidden · $0.33 · 94 rounds · 45.3w out)",
                        "closest_label": "+5.28 pts & -91.6% cost vs Haiku 4.5 ($3.93); only 2 hidden misses in C4-microvm test_parse_errors",
                        "confidence": 0.992,
                        "action": "Confirm",
                        "distribution_pct": {
                            "Medium M1-M2 mean (99.50/100)": 99.5,
                            "Complex C1-C4 mean (99.22/100)": 99.2,
                            "Atomic A1-A5 mean (99.15/100)": 99.2,
                        },
                    },
                    {
                        "field": "gemini_4_argon_deep_dive",
                        "question_type": "score",
                        "question": "Gemini 4 Argon vs Gemini 3.8 Flash & GPT-6.1 Sol (1.05M context, $0/M cache_write)",
                        "selected_answer": "98.59 / 100 (Rank 10 of 19 · 1,310/1,310 hidden · $2.82 · 106 rounds · 11.7w out)",
                        "closest_label": "Eliminates all 34 hidden test failures of Gemini 3.8 Flash; 61.7% fewer API rounds (106 vs 277)",
                        "confidence": 0.986,
                        "action": "Act automatically",
                        "distribution_pct": {
                            "Hidden test pass rate (1310/1310)": 100.0,
                            "Atomic A1-A5 mean (99.00/100)": 99.0,
                            "Complex C1-C4 mean (98.06/100)": 98.1,
                        },
                    },
                    {
                        "field": "sky_001_bundle_discrepancy_audit",
                        "question_type": "choice",
                        "question": "What did cross-auditing Skyfall AI's blog bundle (article-D6mnIEDb.js) vs landing bundle (index-D5BqB7X_.js) reveal?",
                        "selected_answer": "Blog includes Gemini 4 (76.9% CAD IoU); Landing swaps in Opus 5.5 (69.4%) & Flash (54.7%)",
                        "closest_label": "In BIM, Gemini 3.8 Flash (42.3% IoU) beats GPT-6 Astra (40.6% IoU) and trails SKY-001 (43.6%) by 1.3 pts",
                        "confidence": 0.95,
                        "action": "Confirm",
                        "distribution_pct": {
                            "Jaguar critical-path compression (105 vs 10,336)": 99.0,
                            "SKY-001 Composer LLM-judge win rate (5/5 axes)": 100.0,
                            "Astra Composer asset completion rate (82%)": 82.0,
                        },
                    },
                ],
                "callouts": [
                    {
                        "lead": "Haiku 5.5 achieves 100.0 on A1, A4, M1, C2, C3 and 99.61 on C4 — missing Auto gating solely due to 2/296 parser error tests in C4-microvm.",
                        "body": (
                            "Meanwhile, Gemini 4 Argon passes 100% of hidden tests (1,310/1,310) with zero cache-write billing, "
                            "losing points only on subjective/structural deductions in A3 (97.0), M2 (97.25), C3 (96.0), and C4 (98.0)."
                        ),
                    }
                ],
            },
            {
                "kind": "scorecard",
                "eyebrow": "WHAT I TESTED",
                "headline": "19 coding models (209 runs) + SKY-001 2,000-case CAD/BIM matrix",
                "rows": scorecard_rows,
                "callouts": [
                    {
                        "lead": "9 of 19 coding models pass all 1,310 / 1,310 hidden assertions and clear the Auto bar (>= 98.45 mean).",
                        "body": (
                            "Auto-eligible cohort: Fable 5.1, Opus 5.5, Opus 5, Sonnet 5.5, GPT-6.1 Sol, GPT-6 Astra, "
                            "Sonnet 5, Gemini 4 Argon [NEW], and HydraFusion."
                        ),
                    },
                    {
                        "lead": "The near-miss champion (✕): Claude Haiku 5.5 ranks #4 overall (99.24) at $0.33 with 1,308/1,310 hidden pass.",
                        "body": (
                            "Haiku 5.5 outscores Sonnet 5.5 (99.00) and GPT-6.1 Sol (98.86) at 1/9th to 1/5th the cost, "
                            "requiring only a lightweight AST/parser guard on C4 to reach full automation."
                        ),
                    },
                ],
            },
            {
                "kind": "protocol",
                "eyebrow": "UNDER THE HOOD",
                "headline": "Copilot CLI 70/15/15 verifier vs SKY-001 Two-Pass World Model",
                "top_code": json.dumps(
                    {
                        "track_A_copilot_cli_supplement_5": {
                            "commit": "a191383571a13143685fd6f7787512c4e281a9ba",
                            "cli_version": "1.0.98",
                            "haiku_5_5_C4_microvm": {
                                "wall_s": 278.8,
                                "api_s": 250.5,
                                "rounds": 14,
                                "ai_credits": 5.13,
                                "hidden_tests": "294/296 (2 test_parse_errors misses -> 69.61/70)",
                                "total_score": 99.61,
                            },
                            "gemini_4_argon_C3_microdb": {
                                "wall_s": 1007.4,
                                "api_s": 983.9,
                                "rounds": 29,
                                "ai_credits": 98.58,
                                "cache_write_price_per_m": 0.0,
                                "hidden_tests": "377/377 (58/58 + 12/12 self_test = 70/70)",
                                "total_score": 96.0,
                            },
                        }
                    },
                    indent=2,
                ),
                "transition": "↓ vs SKY-001 Hierarchical Part Tree + Matryoshka Two-Pass Construction Rollout",
                "bottom_code": (
                    "<sky_001_execution_graph steps_per_part=\"100\" parallel_workers=\"128\">\n"
                    "  Stage 1 (Hierarchical Composer): Coarse 3D DiT -> Parallel Tree Split (depth D) -> Leaf Refiner DiT\n"
                    "    Jaguar E-Type: L=103 leaves, N=139 nodes (36 splits), D=5\n"
                    "    Flat chain:   (N - L) + L * S = 36 + 103 * 100 = 10,336 sequential steps\n"
                    "    Tree rollout: D + ceil(L / W) * S = 5 + 1 * 100 = 105 sequential steps (98.44x shorter!)\n"
                    "  Stage 2 (Construction World Model):\n"
                    "    Pass 1: Roll out intermediate 3D solid states + 2D inverse sketches in leading Matryoshka latents\n"
                    "    Pass 2: Parallel full-resolution Refiner restores sharp edges, corners & vertices\n"
                    "</sky_001_execution_graph>\n"
                    "<answer>"
                ),
                "callouts": [
                    {
                        "lead": "Why Haiku 5.5 generated 453k output tokens for only $0.33 while Argon cost $2.82 for 117k tokens:",
                        "body": (
                            "In C3-microdb, Haiku 5.5 emitted 263,769 output tokens ($0.50/M output, $0.01/M cache read = 16.93 credits), "
                            "whereas Argon billed $2.00/M input, $0.10/M cache read, $0.00/M cache write, and $10.00/M output (98.58 credits)."
                        ),
                    }
                ],
            },
            {
                "kind": "robustness",
                "eyebrow": "ROBUSTNESS CHECK",
                "headline": "Generational leaps & cross-modality sensitivity (Code vs 3D CAD)",
                "subtitle": (
                    "Comparing Supplement 5 models against their predecessors on the 11-task CLI suite, and contrasting "
                    "6 frontier families across multi-turn CLI coding vs Skyfall's one-shot 3D CAD scripting benchmark."
                ),
                "rows": robustness_rows,
                "callouts": [
                    {
                        "lead": "Modality & harness inversion: Grok 4.7 (0% -> 99.21%) and Kimi K3 (9.5% -> 98.68%).",
                        "body": (
                            "Frontier LLMs fail when forced to emit a 100-step 3D CAD/Blender script in a single blind shot without "
                            "spatial state feedback, yet excel when paired with an iterative CLI test/compiler loop."
                        ),
                    }
                ],
            },
            {
                "kind": "latency",
                "eyebrow": "LATENCY",
                "headline": "11-task API inference vs wall time across top 8 models (seconds)",
                "subtitle": (
                    "Blue bars ('Batched' slot) show pure API inference seconds; gray bars ('One by one*' slot) show total "
                    "11-task wall-clock seconds across #1 Sonnet 5.5 (995/1301s), #2 HydraFusion (1034/1444s), #3 GPT-6.1 Sol "
                    "(1348/1645s), #4 Opus 5.5 (1570/1909s), #5 Astra (1617/1960s), #6 Haiku 5.5 (1852/2104s), #7 Argon (2512/2710s), #8 Fable 5.1 (2210/3355s)."
                ),
                "rows": latency_rows,
                "callouts": [
                    {
                        "lead": "Haiku 5.5 ranks #6 in total wall time (2,104s = 35.1m) because 53% of its time was spent in C3-microdb (1,116s).",
                        "body": (
                            "On Atomic tasks (A1–A5), Haiku 5.5 is the fastest model in the entire 19-model cohort (141.5s total = 28.3s/task). "
                            "Meanwhile, in 3D CAD, SKY-001 finishes a 100-step part in 3.9s vs Astra's 199s (51.0x faster)."
                        ),
                    }
                ],
            },
            {
                "kind": "takeaways",
                "eyebrow": "MY TAKE",
                "headline": "Where Haiku 5.5, Gemini 4 Argon & SKY-001 fit in production",
                "good_fit": [
                    "Claude Haiku 5.5 ($0.33, 99.24): Default high-throughput Coding Agent for atomic/medium tasks and CI auto-repair with a final pytest gate",
                    "Gemini 4 Argon ($2.82, 1310/1310 hidden): Long-context (1.05M) multi-file refactoring where $0/M cache-write slashes prompt-warmed cost",
                    "Sonnet 5.5 ($2.89, 21.7m) & GPT-6.1 Sol ($1.71, 60 rds): Primary unattended daily drivers clearing 1,310/1,310 hidden tests",
                    "SKY-001 Architecture: Coarse-to-fine 3D concept exploration, hierarchical assembly decomposition, and visual construction planning",
                ],
                "not_for": [
                    "Treating SKY-001's current visual state+sketch rollouts as manufacturing-ready parametric B-Rep/STEP feature histories",
                    "Benchmarking general LLMs on 3D CAD via single-request blind scripts without a geometric solver or visual feedback loop",
                    "Running Haiku 5.5 unguarded on complex parser/VM edge cases without unit-test assertions (2/296 misses on C4)",
                    "Over-interpreting <1.0 pt single-run (repeat=1) rank gaps across CLI versions 1.0.84-3..1.0.98",
                ],
                "dark_box": {
                    "lead": "Provenance: anonymized_reported (independently_reproduced=false) + Offline Verifier Suite (6/6 unit tests passing).",
                    "repo": "Sources: satomic/copilot-benchmark@a1913835 · skyfall.ai JS bundles · benchmark-harness-engineering 7-Card v1",
                },
            },
        ],
        "tables": tables,
        "sky001_audit": sky_audit,
        "sky001_composer_llm_judges": SKYFALL_COMPOSER_LLM_JUDGES,
        "pareto_frontier_19_models": pareto,
        "cross_modality_matrix": cross_matrix,
    }


def build_evidence_json() -> dict:
    return {
        "schema_version": 1,
        "topic": "sky-001-and-coding-agent-19-model-benchmark",
        "generated_at": "2026-10-23",
        "provenance": "anonymized_reported",
        "independently_reproduced": False,
        "upstream_repositories": [
            {
                "repo": "satomic/copilot-benchmark",
                "url": "https://github.com/satomic/copilot-benchmark",
                "pinned_commit": "a191383571a13143685fd6f7787512c4e281a9ba",
                "commit_date": "2026-10-15T08:28:58Z",
                "commit_message": "add haiku 5.5 and gemini 5 argon",
                "commit_url": "https://github.com/satomic/copilot-benchmark/commit/a191383571a13143685fd6f7787512c4e281a9ba",
                "previous_commit": "aa1e0dc31661ff6343433f06fe3bea1e015b8525",
                "license": None,
                "license_note": "No SPDX LICENSE file present at commit a191383571a13143685fd6f7787512c4e281a9ba; only factual benchmark statistics and schema metadata are cited.",
                "verified_counts": {
                    "tasks": 11,
                    "models": 19,
                    "non_reference_report_bundles": 209,
                    "reference_report_bundles": 11,
                    "hidden_assertions_per_model": 1310,
                    "new_bundles_in_supplement_5": 22,
                    "prior_model_score_drifts_in_commit": 0,
                },
            },
            {
                "repo": "skyfall.ai (Public Production Bundles)",
                "url": "https://skyfall.ai/blog/introducing-sky-001",
                "artifacts": [
                    {
                        "url": "https://skyfall.ai/assets/index-D5BqB7X_.js",
                        "bytes": 494518,
                        "sha256": "1bc34257c0f2f1db82336d13f95f88c391950c0957655377f752954b4cd7199f",
                    },
                    {
                        "url": "https://skyfall.ai/assets/article-D6mnIEDb.js",
                        "bytes": 77103,
                        "sha256": "8f22592c0d7f0bc1600158903685a5212ddb417499cde1c1e93754de5e6a9830",
                    },
                ],
                "launch_date": "2026-10-19",
                "access_status": "Waitlist-only closed preview (no public weights, API, or raw 1,000-case geometry files released)",
            },
        ],
        "verified_supplement_5_bundles": {
            "claude-haiku-5.5": {
                "cli_version": "1.0.98",
                "effort": "medium",
                "capi_pricing_per_1m": {
                    "input_usd": 0.10,
                    "cache_read_usd": 0.01,
                    "cache_write_usd": 0.125,
                    "output_usd": 0.50,
                    "long_context_threshold_tokens": 100000,
                },
                "totals": {
                    "score_sum": 1091.61,
                    "score_mean": 99.24,
                    "atomic_mean": 99.15,
                    "medium_mean": 99.50,
                    "complex_mean": 99.22,
                    "hidden_passed": 1308,
                    "hidden_total": 1310,
                    "failed_hidden_tests": [
                        "_verify.test_c4::test_parse_errors[if true { }]",
                        "_verify.test_c4::test_parse_errors[while true { }]",
                    ],
                    "wall_clock_s": 2103.62,
                    "api_time_s": 1851.85,
                    "premium_requests": 94,
                    "ai_credits": 33.38,
                    "cost_usd": 0.3338,
                    "output_tokens": 453116,
                },
            },
            "gemini-4-argon": {
                "cli_version": "1.0.98",
                "effort": "medium",
                "commit_message_note": "Commit a1913835 message wrote 'gemini 5 argon', but run.json model id and CAPI catalog entry are 'gemini-4-argon' ('Gemini 4 Argon').",
                "capi_pricing_per_1m": {
                    "input_usd": 2.00,
                    "cache_read_usd": 0.10,
                    "cache_write_usd": 0.00,
                    "output_usd": 10.00,
                    "max_context_window_tokens": 1048576,
                },
                "totals": {
                    "score_sum": 1084.50,
                    "score_mean": 98.59,
                    "atomic_mean": 99.00,
                    "medium_mean": 98.62,
                    "complex_mean": 98.06,
                    "hidden_passed": 1310,
                    "hidden_total": 1310,
                    "failed_hidden_tests": [],
                    "wall_clock_s": 2709.84,
                    "api_time_s": 2512.30,
                    "premium_requests": 106,
                    "ai_credits": 282.09,
                    "cost_usd": 2.8209,
                    "output_tokens": 116755,
                },
            },
        },
        "sky001_verified_bundle_arrays": {
            "cad_blog_article_D6mnIEDb_js": [asdict_row(r) for r in SKYFALL_BENCHMARKS["cad"]["blog"]],
            "cad_landing_index_D5BqB7X_js": [asdict_row(r) for r in SKYFALL_BENCHMARKS["cad"]["landing"]],
            "bim_blog_article_D6mnIEDb_js": [asdict_row(r) for r in SKYFALL_BENCHMARKS["bim"]["blog"]],
            "bim_landing_index_D5BqB7X_js": [asdict_row(r) for r in SKYFALL_BENCHMARKS["bim"]["landing"]],
            "composer_llm_judges": SKYFALL_COMPOSER_LLM_JUDGES,
        },
    }


def asdict_row(r) -> dict:
    return {
        "model": r.model,
        "iou_pct": r.iou_pct,
        "seconds_per_case": r.seconds_per_case,
        "usd_per_case": r.usd_per_case,
        "ours": r.ours,
    }


def main() -> None:
    out_dir = Path(__file__).resolve().parent.parent
    report_data = build_report_json()
    evidence_data = build_evidence_json()

    report_path = out_dir / "report.json"
    evidence_path = out_dir / "evidence.json"
    cards_html_path = out_dir / "test-report-cards.html"

    report_path.write_text(json.dumps(report_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    evidence_path.write_text(json.dumps(evidence_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    cards_html_path.write_text(render_card_deck(report_data), encoding="utf-8", newline="\n")

    print(f"Wrote {report_path} ({report_path.stat().st_size} bytes)")
    print(f"Wrote {evidence_path} ({evidence_path.stat().st_size} bytes)")
    print(f"Wrote {cards_html_path} ({cards_html_path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
