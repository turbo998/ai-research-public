"""Unit tests for E2B Sandbox Resilience & Nomad Heartbeat Verifier."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2b_nomad_heartbeat_verifier import (
    BASELINE_REPLACEMENTS,
    EXPERIMENT_REGIMES,
    NOMAD_SMALL_CLUSTER_HEARTBEAT,
    OBSERVED_LOG_TIMELINE_SECONDS,
    PINNED_COMMITS,
    YAMUX_KEEPALIVE_DEFAULTS,
    compute_blast_radius_metrics,
    export_verifier_summary,
    simulate_heartbeat_timeline,
)


class TestE2BNomadHeartbeatVerifier(unittest.TestCase):
    def test_pinned_upstream_commits_and_baseline_replacements(self) -> None:
        self.assertEqual(
            PINNED_COMMITS["hashicorp/nomad"],
            "bf24b0dd97430d3b364b68b1f7375e85e585778f",
        )
        self.assertEqual(PINNED_COMMITS["hashicorp/yamux"], "v0.1.2")
        self.assertEqual(
            PINNED_COMMITS["e2b-dev/runtime"],
            "afaaeaef96aae86f65ce60bf38fe083e7638a28e",
        )
        by_name = {item.task_name: item for item in BASELINE_REPLACEMENTS}
        self.assertEqual(by_name["Orchestrator"].replaced_allocations, 7)
        self.assertEqual(by_name["Orchestrator"].total_allocations, 20)
        self.assertEqual(by_name["Orchestrator"].replaced_pct, 35.0)
        self.assertEqual(by_name["session-proxy"].replaced_allocations, 7)
        self.assertEqual(by_name["session-proxy"].total_allocations, 20)
        self.assertEqual(by_name["client-proxy"].replaced_allocations, 2)
        self.assertEqual(by_name["client-proxy"].total_allocations, 3)
        self.assertEqual(by_name["client-proxy"].replaced_pct, 66.67)

    def test_observed_log_timeline_and_yamux_race(self) -> None:
        self.assertEqual(OBSERVED_LOG_TIMELINE_SECONDS["client_healthy_server_heartbeat_captured_s"], 21)
        self.assertEqual(OBSERVED_LOG_TIMELINE_SECONDS["original_task_killing_started_s"], 39)
        self.assertEqual(OBSERVED_LOG_TIMELINE_SECONDS["original_stream_closed_s"], 44)
        self.assertLess(
            OBSERVED_LOG_TIMELINE_SECONDS["client_healthy_server_heartbeat_captured_s"],
            OBSERVED_LOG_TIMELINE_SECONDS["original_task_killing_started_s"],
        )
        # Default Leader budget (20-30s) is narrower than yamux silent failure detection max (40s)
        default_budget_max = (
            NOMAD_SMALL_CLUSTER_HEARTBEAT["dynamic_ttl_max_s"]
            + NOMAD_SMALL_CLUSTER_HEARTBEAT["default_heartbeat_grace_s"]
        )
        self.assertEqual(default_budget_max, 30)
        self.assertLess(default_budget_max, YAMUX_KEEPALIVE_DEFAULTS["silent_drop_detection_max_s"])

    def test_three_illustrative_sequence_diagrams(self) -> None:
        # 1. Baseline: TTL=15s, grace=10s -> expires at 25s; reconnect at 40s kills original task
        base = simulate_heartbeat_timeline(
            ttl_s=15.0,
            heartbeat_grace_s=10.0,
            server_fail_at_s=5.0,
            client_recover_at_s=40.0,
            disconnect_lost_after_s=0.0,
            replace_on_disconnect=True,
        )
        self.assertEqual(base["leader_expire_at_s"], 25.0)
        self.assertTrue(base["heartbeat_expired"])
        self.assertTrue(base["original_task_killed_on_reconnect"])
        self.assertFalse(base["eligible_for_new_sandboxes_throughout"])

        # 2. Solution 1 (disconnect): TTL=15s, grace=10s, lost_after=50s -> unknown at 25s, expires at 75s
        disc = simulate_heartbeat_timeline(
            ttl_s=15.0,
            heartbeat_grace_s=10.0,
            server_fail_at_s=5.0,
            client_recover_at_s=40.0,
            disconnect_lost_after_s=50.0,
            replace_on_disconnect=False,
        )
        self.assertEqual(disc["leader_expire_at_s"], 25.0)
        self.assertEqual(disc["disconnect_expiry_at_s"], 75.0)
        self.assertEqual(disc["node_status_during_fault"], "disconnected")
        self.assertEqual(disc["alloc_status_during_fault"], "unknown")
        self.assertFalse(disc["original_task_killed_on_reconnect"])
        self.assertFalse(disc["eligible_for_new_sandboxes_throughout"])

        # 3. Solution 2 (heartbeat_grace=50s): TTL=15s, grace=50s -> expires at 65s; reconnect at 40s avoids disconnect
        grace = simulate_heartbeat_timeline(
            ttl_s=15.0,
            heartbeat_grace_s=50.0,
            server_fail_at_s=5.0,
            client_recover_at_s=40.0,
            disconnect_lost_after_s=0.0,
            replace_on_disconnect=True,
        )
        self.assertEqual(grace["leader_expire_at_s"], 65.0)
        self.assertFalse(grace["heartbeat_expired"])
        self.assertEqual(grace["node_status_during_fault"], "ready")
        self.assertFalse(grace["original_task_killed_on_reconnect"])
        self.assertTrue(grace["eligible_for_new_sandboxes_throughout"])

    def test_experiment_regimes_validation_metrics(self) -> None:
        regimes = {r.regime_id: r for r in EXPERIMENT_REGIMES}
        sol1 = regimes["solution_1_disconnect_50s"]
        self.assertEqual(sol1.orchestrator_replaced, 0)
        self.assertEqual(sol1.session_proxy_replaced, 0)
        self.assertEqual(sol1.client_proxy_replaced, 0)
        self.assertEqual(sol1.sandboxes_preserved, 10)
        self.assertEqual(sol1.ndjson_streams_preserved, 23)
        self.assertEqual(sol1.short_requests_succeeded, 12581)
        self.assertEqual(sol1.short_request_errors, 0)
        self.assertAlmostEqual(sol1.observed_unknown_min_s, 1.7)
        self.assertAlmostEqual(sol1.observed_unknown_max_s, 31.6)

        sol2 = regimes["solution_2_heartbeat_grace_50s"]
        self.assertEqual(sol2.clients_entering_disconnected, 0)
        self.assertEqual(sol2.eligible_creation_nodes_during_fault, 20)
        self.assertEqual(sol2.real_host_crash_nomad_detect_max_s, 70)

    def test_blast_radius_capacity_math(self) -> None:
        br = compute_blast_radius_metrics(total_nodes=20, affected_nodes=7)
        self.assertEqual(br["remaining_ready_nodes"], 13)
        self.assertEqual(br["capacity_retained_pct"], 65.0)
        self.assertEqual(br["capacity_lost_pct"], 35.0)
        self.assertAlmostEqual(br["per_node_overload_pct"], 53.85)

    def test_export_verifier_summary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            out_path = Path(tmp_dir) / "verifier-summary.json"
            summary = export_verifier_summary(out_path)
            self.assertTrue(out_path.exists())
            self.assertEqual(summary["topic"], "e2b-nomad-heartbeat-resilience")


if __name__ == "__main__":
    unittest.main()
