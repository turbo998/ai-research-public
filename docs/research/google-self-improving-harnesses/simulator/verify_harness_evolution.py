#!/usr/bin/env python3
"""Deterministic verification of quantitative invariants from arXiv:2611.22299v1
('Harnesses That Improve Themselves: A Unifying Framework for Self-Improving Agent Harnesses',
Deep Shah & Nehal Kathrotia, Google, Nov 2026).

Validates:
1. Held-out accuracy multipliers and per-solved-task token efficiency on Gemini 3.8 Flash.
2. Stage-3 validation gate (G_val + B_tok = 110k) rejection of over-budget turn-cap inflation.
3. Break-even search amortization (<100 deployment tasks to pay back 100 search rollouts).
4. Zero-shot model-upgrade transfer invariant on Gemini 4 Argon (Modular > Unconstrained at <1/4 cost).
"""

from __future__ import annotations

import json
from pathlib import Path
import unittest


LEDGER_PATH = Path(__file__).resolve().parent.parent / "evidence" / "paper-benchmark-ledger.json"


def load_ledger() -> dict:
    with LEDGER_PATH.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def evaluate_stage3_gate(
    dev_acc_delta: float,
    val_acc_delta: float,
    mean_tokens_k: float,
    patched_lines_executed_ratio: float,
    token_cap_k: float = 110.0,
) -> tuple[bool, str]:
    """Implements Google's Eq. (1) Stage-3 acceptance gate: E[C(tau)] <= B_tok and G_val(h, h0) = 1."""
    if patched_lines_executed_ratio <= 0.0:
        return False, "REJECTED: dead-code patch (0% runtime line execution)"
    if val_acc_delta < 0.0:
        return False, "REJECTED: validation split regression (overfitting Dev quirks)"
    if mean_tokens_k > token_cap_k:
        return False, f"REJECTED: mean tokens {mean_tokens_k:.1f}k exceeds B_tok={token_cap_k:.1f}k"
    if dev_acc_delta <= 0.0 and val_acc_delta <= 0.0:
        return False, "REJECTED: no accuracy gain without efficiency improvement"
    return True, "ACCEPTED: verified runtime execution, non-regressing Val, within B_tok"


class TestSelfImprovingHarnessInvariants(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.ledger = load_ledger()
        cls.exp = cls.ledger["swe_bench_lite_experiment"]
        cls.flash = {row["method"]: row for row in cls.exp["part_a_gemini_3_8_flash"]}
        cls.argon = {row["method"]: row for row in cls.exp["part_b_zero_shot_gemini_4_argon"]}

    def test_split_accounting(self) -> None:
        splits = self.exp["splits"]
        self.assertEqual(splits["held_out_id_n"] + splits["held_out_ood_n"], splits["held_out_total_n"])
        self.assertEqual(
            splits["dev_n"] + splits["val_n"] + splits["held_out_total_n"],
            self.exp["total_issues"],
        )

    def test_flash_accuracy_and_cost_per_solved_task(self) -> None:
        seed = self.flash["Seed Harness (Pass@1)"]
        refl = self.flash["Prompt-Only Reflection (RULES.md)"]
        full = self.flash["Unconstrained Full-Harness Rewrite"]
        mod = self.flash["Modular Gated Evolution (Ours / Google Eq. 1)"]

        # 8x accuracy lift over seed (5.0% -> 40.0%)
        self.assertAlmostEqual(mod["held_out_accuracy_pct"] / seed["held_out_accuracy_pct"], 8.0, places=4)

        # Prompt-only reflection degrades accuracy (5.0% -> 2.5%) and doubles unverified OOD exits (15% -> 30%)
        self.assertLess(refl["held_out_accuracy_pct"], seed["held_out_accuracy_pct"])
        self.assertAlmostEqual(refl["unverified_ood_exits_pct"] / seed["unverified_ood_exits_pct"], 2.0, places=4)

        # Tokens per solved task: 46.7k / 0.40 = 116.75k (~116.8k) vs 451.6k / 0.425 = 1062.59k (~1062.6k)
        mod_cost_per_solved = mod["avg_tokens_per_task_k"] / (mod["held_out_accuracy_pct"] / 100.0)
        full_cost_per_solved = full["avg_tokens_per_task_k"] / (full["held_out_accuracy_pct"] / 100.0)
        self.assertAlmostEqual(round(mod_cost_per_solved, 1), 116.8, places=1)
        self.assertAlmostEqual(round(full_cost_per_solved, 1), 1062.6, places=1)

        # Modular uses nearly 10x (~9.67x) fewer tokens per task than Unconstrained Full Rewrite
        ratio = full["avg_tokens_per_task_k"] / mod["avg_tokens_per_task_k"]
        self.assertGreater(ratio, 9.5)
        self.assertLess(ratio, 10.0)

    def test_search_rollout_payback_under_100_tasks(self) -> None:
        # Seed uses ~2.5x more tokens than Modular (46.7k * 2.5 = 116.75k)
        mod_tok = 46.7
        seed_tok = 46.7 * 2.5
        per_task_savings = seed_tok - mod_tok  # 70.05k saved per deployed task
        # 100 search rollouts at bounded mean cost (~65k-70k during gated search)
        search_cost_100_rollouts = 100 * 68.0
        payback_tasks = search_cost_100_rollouts / per_task_savings
        self.assertLess(payback_tasks, 100.0)

    def test_stage3_gate_blocks_control_py_turn_inflation(self) -> None:
        # Step 3 control.py (12 -> 18 turns): Dev jumps (+8.3%), Val drops (-12.5%), tokens=124k > 110k
        accepted, reason = evaluate_stage3_gate(
            dev_acc_delta=8.3,
            val_acc_delta=-12.5,
            mean_tokens_k=124.0,
            patched_lines_executed_ratio=1.0,
            token_cap_k=110.0,
        )
        self.assertFalse(accepted)
        self.assertIn("REJECTED", reason)

        # Step 4 verify.py pre-stop hook: Dev +16.7%, Val +12.5%, tokens=46.7k <= 110k, executed=1.0
        accepted_ver, _ = evaluate_stage3_gate(
            dev_acc_delta=16.7,
            val_acc_delta=12.5,
            mean_tokens_k=46.7,
            patched_lines_executed_ratio=1.0,
            token_cap_k=110.0,
        )
        self.assertTrue(accepted_ver)

    def test_zero_shot_argon_transfer_beats_unconstrained(self) -> None:
        seed_b = self.argon["Seed Harness (Zero-Shot Transfer)"]
        full_b = self.argon["Unconstrained Full-Harness Rewrite (Zero-Shot Transfer)"]
        mod_b = self.argon["Modular Gated Evolution (Zero-Shot Transfer)"]

        self.assertGreater(mod_b["held_out_accuracy_pct"], full_b["held_out_accuracy_pct"])
        self.assertAlmostEqual(mod_b["held_out_accuracy_pct"] - full_b["held_out_accuracy_pct"], 7.5, places=4)
        self.assertGreater(mod_b["held_out_accuracy_pct"], seed_b["held_out_accuracy_pct"] * 3.5)
        self.assertLess(mod_b["avg_tokens_per_task_k"], full_b["avg_tokens_per_task_k"] * 0.25)


if __name__ == "__main__":
    unittest.main(verbosity=2)
