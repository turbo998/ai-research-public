"""Unit tests for gemini4_carbon_20model_verifier.py."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from gemini4_carbon_20model_verifier import (
    CWE_BENCH_LEADERBOARD,
    EXPLOITGYM_LEADERBOARD,
    GEMINI_4_CARBON_RELEASE_METADATA,
    GRAY_SWAN_IPI_LEADERBOARD,
    NINETEEN_CLI_MODELS,
    OFFICIAL_CARBON_BENCHMARKS,
    SEC_BENCH_PRO_LEADERBOARD,
    TWENTY_MODELS,
    audit_carbon_official_benchmarks,
    audit_cybersecurity_and_safety,
    classify_coding_model_action,
    compute_pareto_frontier,
    export_summary_json,
)


def test_twenty_model_roster_and_zero_cli_drift() -> None:
    assert len(TWENTY_MODELS) == 20
    assert len(NINETEEN_CLI_MODELS) == 19
    by_slug = {m.slug: m for m in TWENTY_MODELS}

    carbon = by_slug["gemini-4-carbon"]
    assert carbon.capi_status == "Fairwind Preview (Pending Public CLI)"
    assert carbon.total_mean is None
    assert classify_coding_model_action(carbon) == "Confirm"

    fable = by_slug["claude-fable-5.1"]
    assert fable.total_mean == 99.77
    assert fable.hidden_passed == 1310

    opus55 = by_slug["claude-opus-5.5"]
    assert opus55.total_mean == 99.68
    assert opus55.hidden_passed == 1310

    haiku55 = by_slug["claude-haiku-5.5"]
    assert haiku55.total_mean == 99.24
    assert haiku55.cost_usd == 0.33
    assert haiku55.hidden_passed == 1308

    argon = by_slug["gemini-4-argon"]
    assert argon.total_mean == 98.59
    assert argon.cost_usd == 2.82
    assert argon.hidden_passed == 1310

    actions = [classify_coding_model_action(m) for m in NINETEEN_CLI_MODELS]
    assert actions.count("Act automatically") == 9
    assert actions.count("Confirm") == 8
    assert actions.count("Send to a human") == 2

    pareto = compute_pareto_frontier()
    for model_name in ("Fable 5.1", "Opus 5.5", "Haiku 5.5", "Sonnet 5.5", "GPT-6.1 Sol", "GPT-6 Luna"):
        assert model_name in pareto


def test_gemini_4_carbon_pricing_and_release_metadata() -> None:
    assert GEMINI_4_CARBON_RELEASE_METADATA["release_date"] == "2026-10-28"
    pricing = GEMINI_4_CARBON_RELEASE_METADATA["pricing_per_1m_usd"]
    assert pricing["input_usd"] == 2.00
    assert pricing["output_usd"] == 10.00
    assert pricing["cached_input_usd"] == 0.10
    assert pricing["cached_input_discount_pct"] == 95.0
    assert pricing["cache_write_usd"] == 0.00
    assert pricing["same_as_gemini_4_argon"] is True

    webdev = GEMINI_4_CARBON_RELEASE_METADATA["webdev_arena"]
    assert webdev["carbon_elo"] == 1768
    assert webdev["argon_elo"] == 1679
    assert webdev["delta_elo"] == 89
    assert webdev["overall_rank"] == 4


def test_official_17_benchmarks_and_deltas_vs_argon() -> None:
    audit = audit_carbon_official_benchmarks()
    assert audit["total_benchmarks_audited"] == 17
    # Carbon ranks #1 on 15 of the 17 benchmarks (#2 on OSWorld-2.1 behind Opus 5.5 at 87.2%, #3 on FrontierSWE 2 behind Astra 65.5% and Opus 5.5 62.3%)
    assert audit["rank_1_count"] == 15
    assert audit["non_rank_1_benchmarks"] == {"FrontierSWE 2": 3, "OSWorld-2.1": 2}
    assert audit["swe_sweep_delta_pts"] == 5.3
    assert audit["swe_sweep_ratio_x"] == 2.23
    assert audit["vending_bench_2_delta_usd"] == 2766
    assert audit["vending_bench_2_gain_pct"] == 20.2
    assert audit["graphwalks_delta_pts"] == 12.0
    assert audit["terminal_bench_4_delta_pts"] == 8.1
    assert audit["agents_last_exam_delta_pts"] == 8.4
    assert audit["exploitgym_10h_delta_pts"] == 12.8
    assert audit["exploitgym_6h_delta_pts"] == 14.0
    assert audit["sec_bench_pro_delta_pts"] == 4.8
    assert audit["cwe_bench_delta_pts"] == 3.0
    assert audit["webdev_arena_delta_elo"] == 89

    by_name = {b.benchmark: b for b in OFFICIAL_CARBON_BENCHMARKS}
    assert by_name["AA Index v5.0"].carbon == 59.0
    assert by_name["AA Index v5.0"].argon == 50.0
    assert by_name["Vals Index v2.2"].carbon == 70.4
    assert by_name["Terminal-Bench-Science 0.1 (AA)"].delta_vs_argon == 11.9


def test_cybersecurity_defense_lifecycle_leaderboards() -> None:
    cyber = audit_cybersecurity_and_safety()
    assert cyber["sec_bench_pro"]["leader"] == "Gemini 4 Carbon"
    assert cyber["sec_bench_pro"]["leader_score_pct"] == 88.2
    assert cyber["sec_bench_pro"]["lead_vs_astra_pts"] == 2.8
    assert cyber["sec_bench_pro"]["lead_vs_argon_pts"] == 4.8
    assert len(SEC_BENCH_PRO_LEADERBOARD) == 8

    assert cyber["exploitgym"]["leader_10h_pct"] == 54.8
    assert cyber["exploitgym"]["leader_6h_pct"] == 53.5
    assert cyber["exploitgym"]["astra_no_cap_pct"] == 42.4
    assert cyber["exploitgym"]["carbon_6h_lead_vs_astra_no_cap_pts"] == 11.1
    assert cyber["exploitgym"]["carbon_10h_lead_vs_astra_no_cap_pts"] == 12.4
    assert cyber["exploitgym"]["carbon_6h_lead_vs_opus_5_5_6h_pts"] == 19.0
    assert len(EXPLOITGYM_LEADERBOARD) == 10

    assert cyber["cwe_bench"]["leader"] == "Gemini 4 Carbon"
    assert cyber["cwe_bench"]["leader_score_pct"] == 71.0
    assert cyber["cwe_bench"]["tied_second_models_at_68_pct"] == ["Grok 4.7", "Gemini 4 Argon", "GPT-6 Astra"]
    assert cyber["cwe_bench"]["lead_vs_second_pts"] == 3.0
    assert len(CWE_BENCH_LEADERBOARD) == 11


def test_gray_swan_ipi_and_alignment_bounds() -> None:
    cyber = audit_cybersecurity_and_safety()
    assert cyber["gray_swan_ipi"]["zero_asr_pct" if "zero_asr_pct" in cyber["gray_swan_ipi"] else "carbon_asr_pct"] == 0.0
    assert cyber["gray_swan_ipi"]["zero_asr_models"] == ["Gemini 4 Carbon"]
    assert cyber["gray_swan_ipi"]["argon_asr_pct"] == 0.7
    assert cyber["gray_swan_ipi"]["opus_5_5_asr_pct"] == 1.0
    assert cyber["gray_swan_ipi"]["fable_5_1_asr_pct"] == 1.0
    assert cyber["gray_swan_ipi"]["gpt6_astra_asr_pct"] == 8.5
    assert cyber["gray_swan_ipi"]["gpt6_1_sol_asr_pct"] == 8.6
    assert cyber["gray_swan_ipi"]["kimi_k3_asr_pct"] == 52.7
    assert len(GRAY_SWAN_IPI_LEADERBOARD) == 13

    safety = GEMINI_4_CARBON_RELEASE_METADATA["alignment_and_safety"]
    assert safety["terminal_bench_4_successful_cheating_pct"] == 0.0
    assert safety["terminal_bench_4_cheating_attempt_pct"] == 0.4
    assert safety["live_coding_high_severity_misalignment_delta_pct"] == -80.0
    assert safety["unsupported_claims_delta_pct"] == -50.0
    assert safety["overreach_delta_pct"] == -26.0
    assert safety["under_service_delta_pct"] == -29.0
    assert safety["secure_code_generation_multiplier_vs_argon_min_x"] == 2.0
    assert safety["chrome_patch_quality_multiplier_vs_competing_frontier_min_x"] == 10.0


def test_summary_json_export() -> None:
    with tempfile.TemporaryDirectory() as td:
        out_path = Path(td) / "verifier-summary.json"
        payload = export_summary_json(out_path)
        assert out_path.exists()
        assert payload["total_models_in_roster"] == 20
        assert payload["cli_evaluated_models_count"] == 19
        assert payload["cli_evaluated_total_runs"] == 209
        assert payload["cli_prior_model_score_drifts"] == 0


class VerifierTestCase(unittest.TestCase):
    def test_all(self) -> None:
        test_twenty_model_roster_and_zero_cli_drift()
        test_gemini_4_carbon_pricing_and_release_metadata()
        test_official_17_benchmarks_and_deltas_vs_argon()
        test_cybersecurity_defense_lifecycle_leaderboards()
        test_gray_swan_ipi_and_alignment_bounds()
        test_summary_json_export()


if __name__ == "__main__":
    unittest.main(verbosity=2)
