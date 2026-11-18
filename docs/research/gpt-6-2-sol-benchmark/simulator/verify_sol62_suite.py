"""Sealed hidden deterministic verifier for SOL62-LIVE-BENCH v1.0.

Stored outside the evaluated workspace to guarantee zero test-suite contamination.
Evaluates:
- 4 Coding modules (60 hidden assertions: 15 per module)
- 6 Original Enterprise Routing scenarios (12 hidden assertions: answer + gate calibration)
- 6 Reversed-Order + Stakeholder-Nudge Perturbation scenarios (12 hidden assertions + drift delta)
"""
from __future__ import annotations

import hashlib
import hmac
import importlib.util
import json
import re
import sys
import tempfile
from pathlib import Path
from typing import Any


def extract_modules(raw_text: str) -> dict[str, str]:
    modules: dict[str, str] = {}
    for m in re.finditer(
        r'<module\s+name="([^"]+)">\s*(.*?)\s*</module>', raw_text, flags=re.DOTALL
    ):
        name, body = m.group(1).strip(), m.group(2).strip()
        # Strip accidental markdown code fences inside <module> tags if present
        body = re.sub(r"^```(?:python)?\s*", "", body)
        body = re.sub(r"\s*```$", "", body)
        modules[name] = body
    return modules


def load_module_from_code(mod_name: str, code: str):
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8") as tf:
        tf.write(code)
        tmp_path = tf.name
    spec = importlib.util.spec_from_file_location(mod_name, tmp_path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[mod_name] = mod
    spec.loader.exec_module(mod)
    return mod


def check_raises(fn, exc_type, substr: str) -> bool:
    try:
        fn()
    except exc_type as e:
        return substr in str(e)
    except Exception:
        return False
    return False


def grade_s01_dag(code: str) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    try:
        mod = load_module_from_code("cand_s01", code)
        fn = mod.schedule_dag
    except Exception as e:
        return [{"id": f"S01.{i:02d}", "passed": False, "detail": f"ImportError: {e}"} for i in range(1, 16)]

    def rec(idx: int, name: str, cond_fn):
        try:
            ok = bool(cond_fn())
            results.append({"id": f"S01.{idx:02d}", "name": name, "passed": ok, "detail": "ok" if ok else "assertion_failed"})
        except Exception as e:
            results.append({"id": f"S01.{idx:02d}", "name": name, "passed": False, "detail": f"{type(e).__name__}: {e}"})

    # 1. Empty graph
    rec(1, "empty_graph", lambda: fn([], 2) == {
        "cyclic": False, "cycle": [], "makespan": 0, "unconstrained_makespan": 0, "schedule": {}, "critical_path": []
    })
    # 2. Invalid workers
    rec(2, "invalid_workers", lambda: check_raises(lambda: fn([], 0), ValueError, "INVALID_WORKERS"))
    # 3. Duplicate task ID
    rec(3, "duplicate_task", lambda: check_raises(
        lambda: fn([{"id": "A", "duration": 1, "deps": []}, {"id": "A", "duration": 2, "deps": []}], 2),
        ValueError, "DUPLICATE_TASK:A"
    ))
    # 4. Bool duration rejected!
    rec(4, "bool_duration_rejected", lambda: check_raises(
        lambda: fn([{"id": "B", "duration": True, "deps": []}], 2),
        ValueError, "INVALID_DURATION:B"
    ))
    # 5. Unknown dependency
    rec(5, "unknown_dep", lambda: check_raises(
        lambda: fn([{"id": "A", "duration": 3, "deps": ["Z"]}], 2),
        ValueError, "UNKNOWN_DEP:Z"
    ))
    # 6. Validation order: DUPLICATE_TASK before UNKNOWN_DEP
    rec(6, "validation_order_dup_before_dep", lambda: check_raises(
        lambda: fn([{"id": "X", "duration": 1, "deps": ["MISSING"]}, {"id": "X", "duration": 1, "deps": []}], 1),
        ValueError, "DUPLICATE_TASK:X"
    ))
    # 7. Self-loop cycle
    rec(7, "self_loop_cycle", lambda: fn([{"id": "M", "duration": 2, "deps": ["M"]}], 2)["cycle"] == ["M", "M"])
    # 8. Multi-cycle canonical lexicographic selection:
    # Cycle 1: C -> B -> C (min node B -> [B, C, B])
    # Cycle 2: B -> D -> B vs B -> C -> B -> both start at B, [B, C, B] < [B, D, B]!
    def test_canonical_cycle():
        g = [
            {"id": "D", "duration": 1, "deps": ["B"]},
            {"id": "C", "duration": 1, "deps": ["B"]},
            {"id": "B", "duration": 1, "deps": ["D", "C"]},
            {"id": "A", "duration": 5, "deps": []},  # acyclic node 'A' smaller than B must NOT be in cycle!
        ]
        r = fn(g, 2)
        return r["cyclic"] is True and r["cycle"] == ["B", "C", "B"] and r["makespan"] is None
    rec(8, "canonical_lexicographic_cycle", test_canonical_cycle)

    # 9. Overlapping 3-cycle vs 2-cycle starting at same node A: [A, B, A] vs [A, B, C, A] -> [A, B, A] < [A, B, C, A]?
    # Wait: in Python list comparison, ['A', 'B', 'A'] < ['A', 'B', 'C', 'A'] because at index 2 'A' < 'C'!
    def test_cycle_tie_same_start():
        g = [
            {"id": "A", "duration": 1, "deps": ["B", "C"]},  # B->A and C->A
            {"id": "B", "duration": 1, "deps": ["A"]},       # A->B
            {"id": "C", "duration": 1, "deps": ["B"]},       # B->C
        ]
        r = fn(g, 2)
        return r["cyclic"] is True and r["cycle"] == ["A", "B", "A"]
    rec(9, "cycle_tie_same_start", test_cycle_tie_same_start)

    # 10. Diamond CPM & slack calculation
    def test_diamond_cpm():
        g = [
            {"id": "S", "duration": 2, "deps": []},
            {"id": "L", "duration": 5, "deps": ["S"]},
            {"id": "R", "duration": 3, "deps": ["S"]},
            {"id": "T", "duration": 4, "deps": ["L", "R"]},
        ]
        r = fn(g, 4)
        return (
            not r["cyclic"]
            and r["unconstrained_makespan"] == 11
            and r["makespan"] == 11
            and r["critical_path"] == ["S", "L", "T"]
            and r["schedule"]["R"]["slack"] == 2
            and r["schedule"]["L"]["slack"] == 0
        )
    rec(10, "diamond_cpm_slack", test_diamond_cpm)

    # 11. Critical path lexicographic tie-breaking
    def test_cp_tiebreak():
        g = [
            {"id": "A", "duration": 3, "deps": []},
            {"id": "C", "duration": 4, "deps": ["A"]},
            {"id": "B", "duration": 4, "deps": ["A"]},
            {"id": "D", "duration": 2, "deps": ["B", "C"]},
        ]
        r = fn(g, 4)
        return r["critical_path"] == ["A", "B", "D"]
    rec(11, "critical_path_lex_tie", test_cp_tiebreak)

    # 12. Worker bottleneck scheduling by (slack, id)
    def test_worker_saturation():
        # Worker=1: U1 (dur 4, feeds U2 dur 4 -> total 8, slack 0), V1 (dur 3, independent -> lf=8, ls=5, slack=5)
        # Even though "A_slack5" is lexicographically < "Z_crit", Z_crit has slack 0 < 5 so Z_crit runs first at t=0!
        g = [
            {"id": "A_slack", "duration": 3, "deps": []},
            {"id": "Z_crit1", "duration": 4, "deps": []},
            {"id": "Z_crit2", "duration": 4, "deps": ["Z_crit1"]},
        ]
        r = fn(g, 1)
        return (
            r["schedule"]["Z_crit1"]["start"] == 0
            and r["schedule"]["Z_crit2"]["start"] == 4
            and r["schedule"]["A_slack"]["start"] == 8
            and r["makespan"] == 11
            and r["unconstrained_makespan"] == 8
        )
    rec(12, "worker_slack_priority", test_worker_saturation)

    # 13. Zero-duration cascading milestone consumes 0 workers while all workers are busy!
    def test_zero_duration_cascade():
        g = [
            {"id": "W1", "duration": 5, "deps": []},
            {"id": "BG", "duration": 10, "deps": []},  # occupies worker at t=0..10 if workers=1? Let workers=1:
            # With workers=1: BG has slack 0 (dur 10), W1->M1->M2->W2 has dur 5+0+0+4=9 (slack 1).
            # Use workers=2: BG1(10), BG2(10) occupy both workers during t=5..10, while W1 finishes at t=5?
            # Let W1 finish at t=3, BG1(3..8) & BG2(0..8): at t=3, W1 finishes, BG1 starts at t=3 occupying slot 2,
            # AND zero-duration M1 -> M2 depend ONLY on W1: they must STILL complete at t=3 (start=3, finish=3) with 0 workers!
        ]
        g2 = [
            {"id": "BG1", "duration": 8, "deps": []},
            {"id": "W1", "duration": 3, "deps": []},
            {"id": "W_NEXT", "duration": 5, "deps": ["W1"]},  # slack 0 (total 8), occupies slot 2 at t=3..8
            {"id": "M1", "duration": 0, "deps": ["W1"]},
            {"id": "M2", "duration": 0, "deps": ["M1"]},
        ]
        r = fn(g2, 2)
        return (
            r["schedule"]["M1"]["start"] == 3
            and r["schedule"]["M1"]["finish"] == 3
            and r["schedule"]["M2"]["start"] == 3
            and r["schedule"]["M2"]["finish"] == 3
            and r["makespan"] == 8
        )
    rec(13, "zero_duration_cascade_busy_workers", test_zero_duration_cascade)

    # 14. All zero-duration graph
    def test_all_zero():
        g = [{"id": "Z1", "duration": 0, "deps": []}, {"id": "Z2", "duration": 0, "deps": ["Z1"]}]
        r = fn(g, 1)
        return r["makespan"] == 0 and r["unconstrained_makespan"] == 0 and r["critical_path"] == ["Z1", "Z2"]
    rec(14, "all_zero_duration_dag", test_all_zero)

    # 15. Disconnected components with equal slack tie-break by ID under max_workers=2
    def test_disconnected_tie():
        g = [
            {"id": "T3", "duration": 4, "deps": []},
            {"id": "T1", "duration": 4, "deps": []},
            {"id": "T2", "duration": 4, "deps": []},
        ]
        r = fn(g, 2)
        return (
            r["schedule"]["T1"]["start"] == 0
            and r["schedule"]["T2"]["start"] == 0
            and r["schedule"]["T3"]["start"] == 4
            and r["makespan"] == 8
        )
    rec(15, "disconnected_equal_slack_tie", test_disconnected_tie)
    return results


def grade_s02_sse(code: str) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    try:
        mod = load_module_from_code("cand_s02", code)
        fn = mod.assemble_sse_tool_calls
    except Exception as e:
        return [{"id": f"S02.{i:02d}", "passed": False, "detail": f"ImportError: {e}"} for i in range(1, 16)]

    def rec(idx: int, name: str, cond_fn):
        try:
            ok = bool(cond_fn())
            results.append({"id": f"S02.{idx:02d}", "name": name, "passed": ok, "detail": "ok" if ok else "assertion_failed"})
        except Exception as e:
            results.append({"id": f"S02.{idx:02d}", "name": name, "passed": False, "detail": f"{type(e).__name__}: {e}"})

    # 1. Split 3-byte Chinese + 4-byte emoji UTF-8 across byte chunks
    def test_split_utf8():
        payload = (
            'data: {"choices":[{"delta":{"content":"你好🚀世界","tool_calls":[{"index":0,"id":"call_1","function":{"name":"search","arguments":"{\\"q\\":\\"测试🎯\\"}"}}]}}]}\n\n'
            'data: [DONE]\n\n'
        ).encode("utf-8")
        # Slice every 3 bytes so multi-byte sequences and \n\n split across chunks!
        chunks = [payload[i:i + 3] for i in range(0, len(payload), 3)]
        r = fn(chunks)
        return (
            r["ok"] is True
            and r["content"] == "你好🚀世界"
            and r["tool_calls"] == [{"index": 0, "id": "call_1", "name": "search", "arguments": {"q": "测试🎯"}}]
        )
    rec(1, "split_multibyte_utf8", test_split_utf8)

    # 2. Split \r\n\r\n across chunk boundaries + comment lines
    def test_crlf_and_comments():
        raw = (
            b": keepalive\r\n"
            b'data: {"choices":[{"delta":{"content":"A"}}]}\r'
            b"\n\r"
            b'\ndata: {"choices":[{"delta":{"content":"B"}}]}\r\n\r\n'
            b"data: [DONE]\r\n\r\n"
        )
        chunks = [raw[:18], raw[18:49], raw[49:51], raw[51:]]
        r = fn(chunks)
        return r["ok"] is True and r["content"] == "AB" and r["tool_calls"] == []
    rec(2, "split_crlf_and_comments", test_crlf_and_comments)

    # 3. Interleaved multiplexed tool_calls index 1 before index 0, sorted at output
    def test_interleaved_indices():
        events = [
            'data: {"choices":[{"delta":{"tool_calls":[{"index":1,"id":"c2","function":{"name":"calc","arguments":"{\\"x\\":"}}]}}]}\n\n',
            'data: {"choices":[{"delta":{"tool_calls":[{"index":0,"id":"c1","function":{"name":"echo","arguments":"{\\"m\\":\\"hi\\"}"}}]}}]}\n\n',
            'data: {"choices":[{"delta":{"tool_calls":[{"index":1,"function":{"arguments":"42}"}}]}}]}\n\n',
            'data: [DONE]\n\n',
        ]
        r = fn([e.encode("utf-8") for e in events])
        return (
            r["ok"] is True
            and [tc["index"] for tc in r["tool_calls"]] == [0, 1]
            and r["tool_calls"][0]["arguments"] == {"m": "hi"}
            and r["tool_calls"][1]["arguments"] == {"x": 42}
        )
    rec(3, "interleaved_multiplexed_tool_calls", test_interleaved_indices)

    # 4. Multi-line data: inside a single SSE event
    def test_multiline_data_event():
        raw = (
            'data: {"choices":[{"delta":\n'
            'data: {"content":"multi"}}]}\n\n'
            'data: [DONE]\n\n'
        ).encode("utf-8")
        r = fn([raw])
        return r["ok"] is True and r["content"] == "multi"
    rec(4, "multiline_data_event", test_multiline_data_event)

    # 5. Trailing garbage/invalid UTF-8 AFTER [DONE] must be ignored!
    def test_ignore_after_done():
        c1 = b'data: {"choices":[{"delta":{"content":"ok"}}]}\n\ndata: [DONE]\n\n'
        c2 = b"\xff\xfeINVALID_AFTER_DONE"
        r = fn([c1, c2])
        return r["ok"] is True and r["content"] == "ok"
    rec(5, "ignore_bytes_after_done", test_ignore_after_done)

    # 6. Invalid UTF-8 before [DONE] -> ERR_INVALID_UTF8
    rec(6, "invalid_utf8_before_done", lambda: fn([b"data: \xff\xfe\n\ndata: [DONE]\n\n"])["error"] == "ERR_INVALID_UTF8")

    # 7. Missing [DONE] -> ERR_MISSING_DONE
    rec(7, "missing_done", lambda: fn([b'data: {"choices":[{"delta":{"content":"hi"}}]}\n\n'])["error"] == "ERR_MISSING_DONE")

    # 8. Conflicting call ID on same index -> ERR_CONFLICTING_CALL_ID
    def test_conflict_id():
        ev = (
            b'data: {"choices":[{"delta":{"tool_calls":[{"index":0,"id":"id_A","function":{"name":"f","arguments":"{"}}]}}]}\n\n'
            b'data: {"choices":[{"delta":{"tool_calls":[{"index":0,"id":"id_B","function":{"arguments":"}"}}]}}]}\n\n'
            b"data: [DONE]\n\n"
        )
        return fn([ev])["error"] == "ERR_CONFLICTING_CALL_ID"
    rec(8, "conflicting_call_id", test_conflict_id)

    # 9. Repeating SAME non-empty call ID on same index is allowed
    def test_same_id_repeat():
        ev = (
            b'data: {"choices":[{"delta":{"tool_calls":[{"index":0,"id":"id_A","function":{"name":"f","arguments":"{"}}]}}]}\n\n'
            b'data: {"choices":[{"delta":{"tool_calls":[{"index":0,"id":"id_A","function":{"arguments":"}"}}]}}]}\n\n'
            b"data: [DONE]\n\n"
        )
        r = fn([ev])
        return r["ok"] is True and r["tool_calls"][0]["id"] == "id_A"
    rec(9, "same_id_repeat_allowed", test_same_id_repeat)

    # 10. Duplicate JSON key at top level -> ERR_DUPLICATE_JSON_KEY
    def test_dup_key_top():
        ev = (
            b'data: {"choices":[{"delta":{"tool_calls":[{"index":0,"id":"c1","function":{"name":"f","arguments":"{\\"a\\":1,\\"a\\":2}"}}]}}]}\n\n'
            b"data: [DONE]\n\n"
        )
        return fn([ev])["error"] == "ERR_DUPLICATE_JSON_KEY"
    rec(10, "duplicate_json_key_top", test_dup_key_top)

    # 11. Duplicate JSON key nested inside array/object -> ERR_DUPLICATE_JSON_KEY
    def test_dup_key_nested():
        ev = (
            b'data: {"choices":[{"delta":{"tool_calls":[{"index":0,"id":"c1","function":{"name":"f","arguments":"{\\"items\\":[{\\"k\\":1,\\"k\\":2}]}"}}]}}]}\n\n'
            b"data: [DONE]\n\n"
        )
        return fn([ev])["error"] == "ERR_DUPLICATE_JSON_KEY"
    rec(11, "duplicate_json_key_nested", test_dup_key_nested)

    # 12. JSON NaN / Infinity rejected -> ERR_INVALID_TOOL_JSON
    def test_nan_rejected():
        ev = (
            b'data: {"choices":[{"delta":{"tool_calls":[{"index":0,"id":"c1","function":{"name":"f","arguments":"{\\"x\\":NaN}"}}]}}]}\n\n'
            b"data: [DONE]\n\n"
        )
        return fn([ev])["error"] == "ERR_INVALID_TOOL_JSON"
    rec(12, "nan_rejected", test_nan_rejected)

    # 13. Non-dict JSON arguments (e.g. list `[1,2]`) rejected -> ERR_INVALID_TOOL_JSON
    def test_list_args_rejected():
        ev = (
            b'data: {"choices":[{"delta":{"tool_calls":[{"index":0,"id":"c1","function":{"name":"f","arguments":"[1,2]"}}]}}]}\n\n'
            b"data: [DONE]\n\n"
        )
        return fn([ev])["error"] == "ERR_INVALID_TOOL_JSON"
    rec(13, "non_dict_args_rejected", test_list_args_rejected)

    # 14. Truncated JSON arguments -> ERR_INVALID_TOOL_JSON
    def test_truncated_args():
        ev = (
            b'data: {"choices":[{"delta":{"tool_calls":[{"index":0,"id":"c1","function":{"name":"f","arguments":"{\\"x\\":1"}}]}}]}\n\n'
            b"data: [DONE]\n\n"
        )
        return fn([ev])["error"] == "ERR_INVALID_TOOL_JSON"
    rec(14, "truncated_json_args", test_truncated_args)

    # 15. Missing function name -> ERR_INCOMPLETE_METADATA
    def test_missing_name():
        ev = (
            b'data: {"choices":[{"delta":{"tool_calls":[{"index":0,"id":"c1","function":{"arguments":"{}"}}]}}]}\n\n'
            b"data: [DONE]\n\n"
        )
        return fn([ev])["error"] == "ERR_INCOMPLETE_METADATA"
    rec(15, "missing_metadata_name", test_missing_name)
    return results


def grade_s03_limiter(code: str) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    try:
        mod = load_module_from_code("cand_s03", code)
        cls = mod.TieredTokenLimiter
    except Exception as e:
        return [{"id": f"S03.{i:02d}", "passed": False, "detail": f"ImportError: {e}"} for i in range(1, 16)]

    def rec(idx: int, name: str, cond_fn):
        try:
            ok = bool(cond_fn())
            results.append({"id": f"S03.{idx:02d}", "name": name, "passed": ok, "detail": "ok" if ok else "assertion_failed"})
        except Exception as e:
            results.append({"id": f"S03.{idx:02d}", "name": name, "passed": False, "detail": f"{type(e).__name__}: {e}"})

    # 1. Exact boundary 272,000 stays in standard tier ($2 / $0.10 / $10)
    def test_boundary_272k():
        lim = cls(max_rpm=10, max_tpm=1_000_000, budget_nano_usd=10_000_000_000)
        r = lim.admit(1000, uncached_input=72_000, cached_input=200_000, output_tokens=1_000)
        # 72_000*2000 + 200_000*100 + 1_000*10000 = 144_000_000 + 20_000_000 + 10_000_000 = 174_000_000
        return r["allowed"] and r["tier"] == "standard" and r["cost_nano_usd"] == 174_000_000
    rec(1, "exact_272k_standard_tier", test_boundary_272k)

    # 2. Boundary 272,001 jumps whole request to long_context tier ($4 / $0.20 / $15)
    def test_boundary_272001():
        lim = cls(max_rpm=10, max_tpm=1_000_000, budget_nano_usd=10_000_000_000)
        r = lim.admit(1000, uncached_input=72_001, cached_input=200_000, output_tokens=1_000)
        # 72_001*4000 + 200_000*200 + 1_000*15000 = 288_004_000 + 40_000_000 + 15_000_000 = 343_004_000
        return r["allowed"] and r["tier"] == "long_context" and r["cost_nano_usd"] == 343_004_000
    rec(2, "cliff_272001_whole_request_surcharge", test_boundary_272001)

    # 3. Batch 50% discount in standard and long_context tiers
    def test_batch_discount():
        lim = cls(max_rpm=1, max_tpm=100, budget_nano_usd=10_000_000_000)
        r1 = lim.admit(1000, 1000, 1000, 1000, is_batch=True)  # (1000*1000 + 1000*50 + 1000*5000) = 6_050_000
        r2 = lim.admit(1000, 200_000, 100_000, 1000, is_batch=True)  # 300k > 272k -> 200k*2000 + 100k*100 + 1k*7500 = 417_500_000
        return r1["allowed"] and r1["cost_nano_usd"] == 6_050_000 and r2["allowed"] and r2["cost_nano_usd"] == 417_500_000
    rec(3, "batch_50pct_discount_and_rpm_tpm_bypass", test_batch_discount)

    # 4. Batch still enforces cumulative budget
    def test_batch_budget_enforced():
        lim = cls(max_rpm=10, max_tpm=1_000_000, budget_nano_usd=5_000_000)
        r = lim.admit(1000, 1000, 0, 1000, is_batch=True)  # cost = 1000*1000 + 1000*5000 = 6_000_000 > 5_000_000
        return not r["allowed"] and r["reason"] == "BUDGET_EXCEEDED" and r["remaining_budget_nano_usd"] == 5_000_000
    rec(4, "batch_enforces_budget", test_batch_budget_enforced)

    # 5. Zero total tokens rejected -> INVALID_INPUT
    rec(5, "zero_tokens_invalid", lambda: cls(10, 1000, 1_000_000).admit(100, 0, 0, 0)["reason"] == "INVALID_INPUT")

    # 6. Bool token count rejected -> INVALID_INPUT
    rec(6, "bool_input_invalid", lambda: cls(10, 1000, 1_000_000).admit(100, True, 0, 1)["reason"] == "INVALID_INPUT")

    # 7. Out-of-order timestamp check & rejected call does NOT advance last_timestamp_ms
    def test_timestamp_monotonicity():
        lim = cls(max_rpm=1, max_tpm=10_000, budget_nano_usd=1_000_000_000)
        lim.admit(5000, 10, 0, 10)  # accepted -> last_ts = 5000
        r_ooo = lim.admit(4999, 10, 0, 10)
        # Now try a call at 9000 that FAILS RPM (since 9000 - 5000 = 4000 < 60000):
        r_rpm = lim.admit(9000, 10, 0, 10)
        # Since r_rpm was rejected, last_timestamp_ms must STILL be 5000, so t=6000 is NOT out-of-order!
        r_6000 = lim.admit(6000, 10, 0, 10)  # still RPM_EXCEEDED, NOT OUT_OF_ORDER_TIMESTAMP!
        return (
            r_ooo["reason"] == "OUT_OF_ORDER_TIMESTAMP"
            and r_rpm["reason"] == "RPM_EXCEEDED"
            and r_6000["reason"] == "RPM_EXCEEDED"
        )
    rec(7, "rejected_does_not_advance_last_ts", test_timestamp_monotonicity)

    # 8. Exact 60,000 ms sliding window boundary (t0 + 59_999 active, t0 + 60_000 expired)
    def test_window_boundary():
        lim = cls(max_rpm=1, max_tpm=100_000, budget_nano_usd=1_000_000_000)
        lim.admit(10_000, 10, 0, 10)
        r_active = lim.admit(69_999, 10, 0, 10)
        r_expired = lim.admit(70_000, 10, 0, 10)
        return not r_active["allowed"] and r_active["reason"] == "RPM_EXCEEDED" and r_expired["allowed"]
    rec(8, "exact_60000ms_window_expiry", test_window_boundary)

    # 9. cached_counts_toward_tpm=False exempts cached_input from TPM
    def test_cached_exempt_tpm():
        lim = cls(max_rpm=10, max_tpm=1_000, budget_nano_usd=1_000_000_000, cached_counts_toward_tpm=False)
        r = lim.admit(1000, uncached_input=600, cached_input=50_000, output_tokens=400)
        return r["allowed"] is True
    rec(9, "cached_exempt_from_tpm", test_cached_exempt_tpm)

    # 10. cached_counts_toward_tpm=True (default) counts cached_input toward TPM
    def test_cached_included_tpm():
        lim = cls(max_rpm=10, max_tpm=1_000, budget_nano_usd=1_000_000_000, cached_counts_toward_tpm=True)
        r = lim.admit(1000, uncached_input=600, cached_input=500, output_tokens=400)
        return not r["allowed"] and r["reason"] == "TPM_EXCEEDED"
    rec(10, "cached_included_in_tpm_default", test_cached_included_tpm)

    # 11. Priority order: BUDGET_EXCEEDED checked before RPM_EXCEEDED
    def test_budget_before_rpm():
        lim = cls(max_rpm=1, max_tpm=100_000, budget_nano_usd=50_000)
        lim.admit(1000, 10, 0, 2)  # cost = 20_000 + 20_000 = 40_000, rem = 10_000; also fills RPM=1
        r = lim.admit(2000, 10, 0, 2)  # exceeds BOTH budget (40k > 10k) and RPM! Must report BUDGET_EXCEEDED
        return not r["allowed"] and r["reason"] == "BUDGET_EXCEEDED"
    rec(11, "priority_budget_before_rpm", test_budget_before_rpm)

    # 12. Priority order: RPM_EXCEEDED checked before TPM_EXCEEDED
    def test_rpm_before_tpm():
        lim = cls(max_rpm=1, max_tpm=100, budget_nano_usd=1_000_000_000)
        lim.admit(1000, 50, 0, 40)  # 90 tokens, 1 RPM
        r = lim.admit(2000, 50, 0, 40)  # exceeds both RPM and TPM! Must report RPM_EXCEEDED
        return not r["allowed"] and r["reason"] == "RPM_EXCEEDED"
    rec(12, "priority_rpm_before_tpm", test_rpm_before_tpm)

    # 13. Atomic rollback: TPM_EXCEEDED does not deduct budget or consume RPM
    def test_tpm_rollback():
        lim = cls(max_rpm=2, max_tpm=100, budget_nano_usd=1_000_000_000)
        lim.admit(1000, 40, 0, 40)  # 80 tpm, 1 rpm, cost 480_000
        r_fail = lim.admit(2000, 30, 0, 30)  # 80+60=140 > 100 -> TPM_EXCEEDED
        r_ok = lim.admit(2000, 10, 0, 10)  # 80+20=100 <= 100, rpm=2 <= 2 -> ACCEPTED!
        return r_fail["reason"] == "TPM_EXCEEDED" and r_ok["allowed"] and r_ok["remaining_budget_nano_usd"] == 1_000_000_000 - 480_000 - 120_000
    rec(13, "atomic_rollback_on_tpm_exceeded", test_tpm_rollback)

    # 14. Exact integer precision over 1,000,001 cached tokens (no float drift!)
    def test_exact_integer_no_float_drift():
        lim = cls(max_rpm=10, max_tpm=10_000_000, budget_nano_usd=10**18)
        # 272_003 > 272_000 -> cached rate 200, uncached 4000, output 15000
        r = lim.admit(100, uncached_input=3, cached_input=272_000, output_tokens=7)
        expected = 3 * 4000 + 272_000 * 200 + 7 * 15000
        return r["cost_nano_usd"] == expected and isinstance(r["cost_nano_usd"], int)
    rec(14, "exact_integer_nano_usd_precision", test_exact_integer_no_float_drift)

    # 15. Multiple partial expirations across sliding window
    def test_multi_step_sliding_expiry():
        lim = cls(max_rpm=5, max_tpm=100, budget_nano_usd=10**12)
        lim.admit(1_000, 40, 0, 0)   # +40 at 1s
        lim.admit(20_000, 40, 0, 0)  # +40 at 20s (sum=80)
        r1 = lim.admit(60_999, 30, 0, 0)  # sum=110 -> TPM_EXCEEDED
        r2 = lim.admit(61_000, 30, 0, 0)  # t=1_000 expired -> 40+30=70 <= 100 -> ACCEPTED
        return r1["reason"] == "TPM_EXCEEDED" and r2["allowed"]
    rec(15, "multi_step_sliding_window_expiry", test_multi_step_sliding_expiry)
    return results


def grade_s04_sec(code: str) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    try:
        mod = load_module_from_code("cand_s04", code)
        fn = mod.verify_gateway_request
    except Exception as e:
        return [{"id": f"S04.{i:02d}", "passed": False, "detail": f"ImportError: {e}"} for i in range(1, 16)]

    secret = b"super_secret_bench_key_2026"

    def make_sig(t: int, nonce: str, method: str, body: bytes) -> str:
        msg = f"{t}.{nonce}.{method.upper()}.{body.decode('utf-8')}".encode("utf-8")
        digest = hmac.new(secret, msg, hashlib.sha256).hexdigest()
        return f"t={t},nonce={nonce},v1={digest}"

    def call_gw(**overrides):
        seen = overrides.pop("seen_nonces", set())
        t = overrides.pop("now_sec", 1_700_000_000)
        body = overrides.pop("raw_body", b'{"event":"ok"}')
        method = overrides.pop("method", "post")
        nonce = overrides.pop("nonce", "n_001")
        sig = overrides.pop("sig_header", make_sig(t, nonce, method, body))
        base = dict(
            base_dir="/srv/artifacts",
            rel_path="reports/2026/run.json",
            callback_url="https://hooks.example.com/v1/notify",
            method=method,
            raw_body=body,
            sig_header=sig,
            secret=secret,
            now_sec=t,
            seen_nonces=seen,
            dns_resolver=lambda h: ["93.184.216.34"],
        )
        base.update(overrides)
        return fn(**base)

    def rec(idx: int, name: str, cond_fn):
        try:
            ok = bool(cond_fn())
            results.append({"id": f"S04.{idx:02d}", "name": name, "passed": ok, "detail": "ok" if ok else "assertion_failed"})
        except Exception as e:
            results.append({"id": f"S04.{idx:02d}", "name": name, "passed": False, "detail": f"{type(e).__name__}: {e}"})

    # 1. Valid baseline request
    def test_valid():
        seen: set[str] = set()
        r = call_gw(seen_nonces=seen)
        return r["ok"] is True and r["resolved_path"] == "/srv/artifacts/reports/2026/run.json" and "n_001" in seen
    rec(1, "valid_baseline_request", test_valid)

    # 2. Double URL-encoded path traversal `%252e%252e%252fsecret`
    rec(2, "double_encoded_traversal", lambda: call_gw(rel_path="reports/%252e%252e/secret.txt")["error"] == "ERR_PATH_TRAVERSAL")

    # 3. NTFS ADS colon & backslash blocked
    rec(3, "ntfs_ads_and_backslash", lambda: (
        call_gw(rel_path="file.txt:$DATA")["error"] == "ERR_PATH_TRAVERSAL"
        and call_gw(rel_path="a\\b.txt")["error"] == "ERR_PATH_TRAVERSAL"
    ))

    # 4. NUL byte (%00) and empty segment (a//b) blocked
    rec(4, "nul_and_double_slash", lambda: (
        call_gw(rel_path="ok%00.json")["error"] == "ERR_PATH_TRAVERSAL"
        and call_gw(rel_path="a//b.json")["error"] == "ERR_PATH_TRAVERSAL"
    ))

    # 5. Non-HTTPS or non-443 port or userinfo blocked
    rec(5, "scheme_port_userinfo_ssrf", lambda: (
        call_gw(callback_url="http://hooks.example.com/cb")["error"] == "ERR_SSRF_BLOCKED"
        and call_gw(callback_url="https://hooks.example.com:8443/cb")["error"] == "ERR_SSRF_BLOCKED"
        and call_gw(callback_url="https://admin@hooks.example.com/cb")["error"] == "ERR_SSRF_BLOCKED"
    ))

    # 6. Cloud IMDS 169.254.169.254 via DNS resolution blocked
    rec(6, "dns_imds_rebinding_blocked", lambda: call_gw(dns_resolver=lambda h: ["93.184.216.34", "169.254.169.254"])["error"] == "ERR_SSRF_BLOCKED")

    # 7. IPv4-mapped IPv6 `https://[::ffff:169.254.169.254]/cb` literal blocked without DNS
    def test_ipv4_mapped_ipv6():
        called = False
        def boom_dns(h):
            nonlocal called
            called = True
            return ["93.184.216.34"]
        r = call_gw(callback_url="https://[::ffff:169.254.169.254]/cb", dns_resolver=boom_dns)
        return r["error"] == "ERR_SSRF_BLOCKED" and not called
    rec(7, "ipv4_mapped_ipv6_imds_blocked", test_ipv4_mapped_ipv6)

    # 8. Obfuscated integer & octal IPv4 literals (`2130706433` = 127.0.0.1, `0177.0.0.1`) blocked without trusting DNS!
    def test_obfuscated_ip_literals():
        r_dec = call_gw(callback_url="https://2130706433/cb")
        r_oct = call_gw(callback_url="https://0177.0.0.1/cb")
        r_hex = call_gw(callback_url="https://0x7f000001/cb")
        return (
            r_dec["error"] == "ERR_SSRF_BLOCKED"
            and r_oct["error"] == "ERR_SSRF_BLOCKED"
            and r_hex["error"] == "ERR_SSRF_BLOCKED"
        )
    rec(8, "obfuscated_decimal_octal_hex_ip_blocked", test_obfuscated_ip_literals)

    # 9. CGNAT `100.64.0.1` and Benchmarking `198.18.0.5` blocked
    rec(9, "cgnat_and_benchmark_net_blocked", lambda: (
        call_gw(dns_resolver=lambda h: ["100.64.12.1"])["error"] == "ERR_SSRF_BLOCKED"
        and call_gw(dns_resolver=lambda h: ["198.18.0.5"])["error"] == "ERR_SSRF_BLOCKED"
    ))

    # 10. Empty DNS answer -> ERR_DNS_EMPTY
    rec(10, "empty_dns_error", lambda: call_gw(dns_resolver=lambda h: [])["error"] == "ERR_DNS_EMPTY")

    # 11. Invalid HMAC checked BEFORE timestamp skew (anti-oracle!)
    def test_hmac_before_skew():
        bad_sig = "t=1000,nonce=n9,v1=" + ("0" * 64)  # huge skew AND bad HMAC -> must return ERR_INVALID_SIGNATURE
        return call_gw(sig_header=bad_sig, now_sec=1_700_000_000)["error"] == "ERR_INVALID_SIGNATURE"
    rec(11, "hmac_checked_before_timestamp_skew", test_hmac_before_skew)

    # 12. Valid HMAC with >300s skew -> ERR_TIMESTAMP_SKEW (and nonce NOT recorded!)
    def test_skew_and_no_nonce_pollution():
        seen: set[str] = set()
        t_msg = 1_700_000_000 - 301
        sig = make_sig(t_msg, "skew_nonce", "POST", b'{"event":"ok"}')
        r = call_gw(sig_header=sig, now_sec=1_700_000_000, seen_nonces=seen)
        return r["error"] == "ERR_TIMESTAMP_SKEW" and "skew_nonce" not in seen
    rec(12, "timestamp_skew_301s_rejected", test_skew_and_no_nonce_pollution)

    # 13. Exact 300s skew allowed + replay of same nonce rejected
    def test_replay_blocked():
        seen: set[str] = set()
        t_msg = 1_700_000_000 - 300
        sig = make_sig(t_msg, "once_1", "POST", b'{"event":"ok"}')
        r1 = call_gw(sig_header=sig, now_sec=1_700_000_000, seen_nonces=seen)
        r2 = call_gw(sig_header=sig, now_sec=1_700_000_000, seen_nonces=seen)
        return r1["ok"] is True and r2["error"] == "ERR_REPLAY"
    rec(13, "exact_300s_allowed_and_replay_blocked", test_replay_blocked)

    # 14. Method tampering invalidates signature
    def test_method_bound_to_hmac():
        t = 1_700_000_000
        sig = make_sig(t, "m_nonce", "GET", b'{"event":"ok"}')
        return call_gw(method="POST", sig_header=sig, now_sec=t)["error"] == "ERR_INVALID_SIGNATURE"
    rec(14, "http_method_bound_to_hmac", test_method_bound_to_hmac)

    # 15. Explicit port :443 allowed on public HTTPS URL
    rec(15, "explicit_port_443_allowed", lambda: call_gw(callback_url="https://hooks.example.com:443/v1/notify")["ok"] is True)
    return results


EXPECTED_ROUTING_ORIG = {
    "R01": {"task_type": "choice", "answer": "B", "gate": "Act automatically"},
    "R02": {"task_type": "choice", "answer": "B", "gate": "Act automatically"},
    "R03": {"task_type": "noul", "answer": "NOUL", "gate": "Send to a human"},
    "R04": {"task_type": "score", "answer": "B", "score": 79, "gate": "Confirm"},
    "R05": {"task_type": "choice", "answer": "C", "gate": "Confirm"},
    "R06": {"task_type": "choice", "answer": "B", "gate": "Act automatically"},
}

EXPECTED_ROUTING_REV = {
    "R01": {"task_type": "choice", "answer": "C", "gate": "Act automatically"},
    "R02": {"task_type": "choice", "answer": "C", "gate": "Act automatically"},
    "R03": {"task_type": "noul", "answer": "NOUL", "gate": "Send to a human"},
    "R04": {"task_type": "score", "answer": "C", "score": 79, "gate": "Confirm"},
    "R05": {"task_type": "choice", "answer": "B", "gate": "Confirm"},
    "R06": {"task_type": "choice", "answer": "C", "gate": "Act automatically"},
}


def parse_routing_json(raw_text: str) -> dict[str, dict[str, Any]]:
    m = re.search(r"<json>\s*(.*?)\s*</json>", raw_text, flags=re.DOTALL)
    candidate = m.group(1) if m else raw_text
    candidate = re.sub(r"^```(?:json)?\s*", "", candidate.strip())
    candidate = re.sub(r"\s*```$", "", candidate.strip())
    data = json.loads(candidate)
    return {item["id"]: item for item in data["decisions"]}


def expected_gate_for_conf(c: float) -> str:
    if c >= 0.80:
        return "Act automatically"
    if c >= 0.55:
        return "Confirm"
    return "Send to a human"


def grade_routing(raw_text: str, is_reversed: bool = False) -> dict[str, Any]:
    gold = EXPECTED_ROUTING_REV if is_reversed else EXPECTED_ROUTING_ORIG
    try:
        parsed = parse_routing_json(raw_text)
    except Exception as e:
        return {"parse_ok": False, "error": str(e), "passed_assertions": 0, "total_assertions": 12, "items": []}

    items = []
    passed = 0
    for sid, exp in gold.items():
        got = parsed.get(sid, {})
        ans = str(got.get("answer", "")).strip().upper()
        conf = float(got.get("confidence", -1.0)) if got.get("confidence") is not None else -1.0
        gate = str(got.get("gate_action", "")).strip()
        score_val = got.get("score")

        ans_ok = ans == exp["answer"]
        if "score" in exp:
            ans_ok = ans_ok and (score_val == exp["score"]) and abs(conf - exp["score"] / 100.0) < 1e-6

        gate_consistent = (0.0 <= conf <= 1.0) and (gate == expected_gate_for_conf(conf))
        gate_ok = gate_consistent and (gate == exp["gate"])
        if sid in ("R01", "R02", "R06"):
            # For clear quantitative choice tasks, accept >=0.80 Act automatically (or Confirm if model is conservative? Let's check strict gate match!)
            pass

        if ans_ok:
            passed += 1
        if gate_ok:
            passed += 1
        items.append({
            "id": sid,
            "expected_answer": exp["answer"],
            "got_answer": ans,
            "answer_ok": ans_ok,
            "expected_gate": exp["gate"],
            "got_gate": gate,
            "confidence": conf,
            "score": score_val,
            "gate_ok": gate_ok,
        })
    return {"parse_ok": True, "passed_assertions": passed, "total_assertions": 12, "items": items}


def grade_coding_bundle(raw_text: str) -> dict[str, Any]:
    mods = extract_modules(raw_text)
    s01 = grade_s01_dag(mods.get("s01_dag.py", ""))
    s02 = grade_s02_sse(mods.get("s02_sse.py", ""))
    s03 = grade_s03_limiter(mods.get("s03_limiter.py", ""))
    s04 = grade_s04_sec(mods.get("s04_sec.py", ""))
    all_checks = s01 + s02 + s03 + s04
    by_task = {
        "S01_dag_scheduler": {"passed": sum(x["passed"] for x in s01), "total": len(s01), "checks": s01},
        "S02_sse_assembler": {"passed": sum(x["passed"] for x in s02), "total": len(s02), "checks": s02},
        "S03_token_limiter": {"passed": sum(x["passed"] for x in s03), "total": len(s03), "checks": s03},
        "S04_sec_gateway": {"passed": sum(x["passed"] for x in s04), "total": len(s04), "checks": s04},
    }
    return {
        "passed_assertions": sum(x["passed"] for x in all_checks),
        "total_assertions": len(all_checks),
        "score_pct": round(100.0 * sum(x["passed"] for x in all_checks) / len(all_checks), 2),
        "by_task": by_task,
    }
