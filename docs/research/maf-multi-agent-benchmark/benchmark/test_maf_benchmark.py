#!/usr/bin/env python3
"""Unit tests for the MAF vs Mainstream Multi-Agent Orchestration Benchmark Suite."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from run_benchmark import (
    A2AAgentCard,
    AgentSession,
    FunctionInvocationContext,
    MAFOrchestrationHarness,
    run_all_benchmarks,
)


class TestMAFMultiAgentBenchmark(unittest.TestCase):
    def setUp(self) -> None:
        self.harness = MAFOrchestrationHarness()
        self.session = AgentSession(session_id="test-sess-01", thread_id="thread-01")

    def test_three_layer_middleware_pii_and_hitl(self) -> None:
        clean_text = self.harness.mw.run_agent_layer(
            self.session, "Fix E-22 [INJECT_IGNORE_RULES] now"
        )
        self.assertIn("[STRIPPED_BY_AGENT_RUN_MW]", clean_text)

        ctx = FunctionInvocationContext(
            function_name="submit_claim",
            arguments={"ssn": "999-00-1111", "device": "X10"},
            requires_approval=False,
        )
        self.harness.mw.run_function_layer(ctx, lambda a: a)
        self.assertEqual(ctx.result["ssn"], "***REDACTED_PII***")
        self.assertIn("ssn", ctx.redacted_fields)

        hitl_ctx = FunctionInvocationContext(
            function_name="delete_prod_index",
            arguments={"index": "kb-main"},
            requires_approval=True,
            approved_by_human=False,
        )
        self.harness.mw.run_function_layer(hitl_ctx, lambda a: a)
        self.assertTrue(hitl_ctx.terminate)
        self.assertEqual(hitl_ctx.result["status"], "paused_for_hitl_approval")

    def test_five_orchestration_modes_and_order_invariance(self) -> None:
        # 1. Sequential
        seq = self.harness.run_sequential(self.session, ["A1", "A2", "A3"], "init")
        self.assertEqual(seq["steps"], 3)

        # 2. Concurrent order invariance
        c1 = self.harness.run_concurrent(self.session, ["DocAgent", "VideoAgent", "WebAgent"], "E-22")
        c2 = self.harness.run_concurrent(self.session, ["WebAgent", "VideoAgent", "DocAgent"], "E-22")
        self.assertEqual(c1["winner"], c2["winner"])
        self.assertEqual(c1["mean_confidence"], c2["mean_confidence"])

        # 3. Handoff order invariance
        reg = [
            ("BillingAgent", {"refund", "invoice"}),
            ("HardwareAgent", {"thermostat", "e22", "wifi"}),
        ]
        h1 = self.harness.run_handoff(self.session, "thermostat e22 wifi", reg)
        h2 = self.harness.run_handoff(self.session, "thermostat e22 wifi", list(reversed(reg)))
        self.assertEqual(h1["selected_agent"], "HardwareAgent")
        self.assertEqual(h1["selected_agent"], h2["selected_agent"])

        # 4. Group Chat
        gc = self.harness.run_group_chat(self.session, ["Exec", "Reviewer"], max_rounds=3, require_hitl_signoff=False)
        self.assertGreaterEqual(gc["consensus_score"], 0.90)
        self.assertEqual(gc["action"], "Act automatically")

        # 5. Magentic Ledger
        mag = self.harness.run_magentic_ledger(
            self.session,
            goal="Diagnose E-22",
            required_facts=["f1", "f2"],
            available_agents={"f1": "DocAgent", "f2": "VideoAgent"},
        )
        self.assertTrue(mag["completed"])
        self.assertEqual(mag["iterations"], 2)

    def test_session_checkpoint_serialization_and_a2a_jws(self) -> None:
        self.harness.run_sequential(self.session, ["S1", "S2"], "payload")
        blob = self.session.serialize()
        restored = AgentSession.deserialize(blob)
        self.assertEqual(restored.superstep, self.session.superstep)
        self.assertEqual(len(restored.history), len(self.session.history))

        card = A2AAgentCard(
            name="TestA2AAgent",
            version="1.0",
            endpoint="https://a2a.local/agent",
            bindings=["HTTP/REST", "JSON-RPC 2.0", "gRPC"],
            skills=["diagnose"],
            auth_schemes=["mTLS"],
        )
        card.sign("secret-key")
        self.assertTrue(card.verify("secret-key"))
        self.assertFalse(card.verify("wrong-key"))

    def test_end_to_end_report_generation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            data = run_all_benchmarks(out)
            self.assertEqual(data["facts"]["decisions_tested"], 12)
            self.assertEqual(data["facts"]["choice_questions_reversal_stable"], 6)
            self.assertTrue((out / "report.json").exists())
            self.assertTrue((out / "evidence" / "test-scenarios.csv").exists())
            self.assertTrue((out / "evidence" / "framework-comparison.csv").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
