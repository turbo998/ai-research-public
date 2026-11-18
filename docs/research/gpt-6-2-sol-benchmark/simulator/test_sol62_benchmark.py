"""Deterministic verification & provenance test suite for GPT-6.2 Sol Benchmark (Supplement Report 9).

Covers:
  (a) Sealed verifier SHA-256 lock + deterministic grading on synthetic pass & R04=83 fail payloads
      (plus S01.14 zero-duration DAG boundary proof).
  (b) >272K whole-request pricing cliff & prefix-cached sharding math ($0.2575 vs $0.4250, 272,000 vs 272,001).
  (c) Exact alignment across data/*.csv, data/freeze_manifest.json, report.json, report.zh-CN.json, and evidence.json.
  (d) Strict Content-Security-Policy, zero <script> tags, 7-card structure, and valid local links on HTML & Markdown artifacts.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from pathlib import Path

import pytest

SIM_DIR = Path(__file__).resolve().parent
TOPIC_DIR = SIM_DIR.parent
DATA_DIR = TOPIC_DIR / "data"
ASSETS_DIR = TOPIC_DIR / "assets"

if str(SIM_DIR) not in sys.path:
    sys.path.insert(0, str(SIM_DIR))

import verify_sol62_suite as verifier  # noqa: E402

EXPECTED_VERIFIER_SHA256 = "58863f19d212670dfa31482a7dbb1696c7a73d7c6a8a1b8bf7bdaa5bfd8ed5d8"
EXPECTED_FREEZE_UTC = "2026-11-18T07:13:06.494325+00:00"


def _build_synthetic_routing_payload(*, reversed_mode: bool = False, override_r04_83: bool = False) -> str:
    expected_map = verifier.EXPECTED_ROUTING_REV if reversed_mode else verifier.EXPECTED_ROUTING_ORIG
    decisions = []
    for rid in ("R01", "R02", "R03", "R04", "R05", "R06"):
        spec = expected_map[rid]
        if rid == "R04" and override_r04_83:
            decisions.append(
                {
                    "id": "R04",
                    "task_type": "score",
                    "answer": "A" if not reversed_mode else "D",
                    "score": 83,
                    "confidence": 0.83,
                    "gate_action": "Act automatically",
                    "rationale_short": "Synthetic reproduction of GPT-6.1 Sol 83/100 arithmetic slip.",
                }
            )
            continue
        gate = spec["gate"]
        if rid == "R03":
            conf = 0.15
        elif rid == "R04":
            conf = 0.79
        elif gate == "Confirm":
            conf = 0.75
        else:
            conf = 0.96
        decisions.append(
            {
                "id": rid,
                "task_type": spec["task_type"],
                "answer": spec["answer"],
                "score": spec.get("score"),
                "confidence": conf,
                "gate_action": gate,
                "rationale_short": f"Deterministic synthetic check for {rid}.",
            }
        )
    return "<json>\n" + json.dumps({"decisions": decisions}, indent=2) + "\n</json>"


def _build_synthetic_coding_payload(*, sink_only_critical_path: bool = True) -> str:
    sink_clause = "not children[u] and " if sink_only_critical_path else ""
    s01_code = f'''
def schedule_dag(tasks: list[dict], max_workers: int) -> dict:
    if isinstance(max_workers, bool) or not isinstance(max_workers, int) or max_workers < 1:
        raise ValueError("INVALID_WORKERS")
    seen_ids = set()
    for t in tasks:
        tid = t["id"]
        if tid in seen_ids:
            raise ValueError(f"DUPLICATE_TASK:{{tid}}")
        seen_ids.add(tid)
    for t in tasks:
        tid = t["id"]
        dur = t["duration"]
        if isinstance(dur, bool) or not isinstance(dur, int) or dur < 0:
            raise ValueError(f"INVALID_DURATION:{{tid}}")
    for t in tasks:
        for dep in t["deps"]:
            if dep not in seen_ids:
                raise ValueError(f"UNKNOWN_DEP:{{dep}}")
    if not tasks:
        return {{"cyclic": False, "cycle": [], "makespan": 0, "unconstrained_makespan": 0, "schedule": {{}}, "critical_path": []}}
    dur_map = {{t["id"]: t["duration"] for t in tasks}}
    deps_map = {{t["id"]: list(dict.fromkeys(t["deps"])) for t in tasks}}
    children = {{tid: [] for tid in seen_ids}}
    indeg = {{tid: 0 for tid in seen_ids}}
    for tid, ds in deps_map.items():
        for d in ds:
            children[d].append(tid)
            indeg[tid] += 1
    for tid in children:
        children[tid].sort()
    q = [u for u, deg in indeg.items() if deg == 0]
    topo = []
    indeg_work = dict(indeg)
    while q:
        u = q.pop()
        topo.append(u)
        for v in children[u]:
            indeg_work[v] -= 1
            if indeg_work[v] == 0:
                q.append(v)
    if len(topo) < len(seen_ids):
        best_cycle = None
        for start in sorted(seen_ids):
            def dfs(curr, path, visited):
                nonlocal best_cycle
                for nxt in children[curr]:
                    if nxt < start:
                        continue
                    if nxt == start:
                        cand = path + [start]
                        if best_cycle is None or cand < best_cycle:
                            best_cycle = cand
                    elif nxt not in visited:
                        if best_cycle is not None and path + [nxt] > best_cycle[:len(path)+1]:
                            continue
                        dfs(nxt, path + [nxt], visited | {{nxt}})
            dfs(start, [start], {{start}})
            if best_cycle is not None:
                break
        return {{"cyclic": True, "cycle": best_cycle, "makespan": None, "unconstrained_makespan": None, "schedule": {{}}, "critical_path": []}}
    es, ef = {{}}, {{}}
    for u in topo:
        es[u] = max((ef[p] for p in deps_map[u]), default=0)
        ef[u] = es[u] + dur_map[u]
    unconstrained = max(ef.values(), default=0)
    lf, ls, slack = {{}}, {{}}, {{}}
    for u in reversed(topo):
        lf[u] = min((ls[c] for c in children[u]), default=unconstrained)
        ls[u] = lf[u] - dur_map[u]
        slack[u] = ls[u] - es[u]
    best_cp = None
    def find_cp(u, path):
        nonlocal best_cp
        if {sink_clause}ef[u] == unconstrained:
            if best_cp is None or path < best_cp:
                best_cp = list(path)
        for c in children[u]:
            if slack[c] == 0 and ef[u] == es[c]:
                find_cp(c, path + [c])
    for u in sorted(seen_ids):
        if es[u] == 0 and slack[u] == 0:
            find_cp(u, [u])
    sched = {{}}
    running = []
    t_now = 0
    remaining = set(seen_ids)
    while remaining:
        progressed = True
        while progressed:
            progressed = False
            for u in sorted(list(remaining)):
                if dur_map[u] == 0 and all(p in sched and sched[p]["finish"] <= t_now for p in deps_map[u]):
                    sched[u] = {{"start": t_now, "finish": t_now, "slack": slack[u]}}
                    remaining.remove(u)
                    progressed = True
        ready_pos = [
            u for u in remaining
            if dur_map[u] > 0 and all(p in sched and sched[p]["finish"] <= t_now for p in deps_map[u])
        ]
        ready_pos.sort(key=lambda u: (slack[u], u))
        while len(running) < max_workers and ready_pos:
            u = ready_pos.pop(0)
            fin = t_now + dur_map[u]
            sched[u] = {{"start": t_now, "finish": fin, "slack": slack[u]}}
            remaining.remove(u)
            running.append((fin, u))
        if remaining:
            running.sort()
            t_now = running[0][0]
            running = [(f, u) for (f, u) in running if f > t_now]
    makespan = max((v["finish"] for v in sched.values()), default=0)
    return {{"cyclic": False, "cycle": [], "makespan": makespan, "unconstrained_makespan": unconstrained, "schedule": sched, "critical_path": best_cp or []}}
'''
    s02_code = '''
import codecs
import json

def assemble_sse_tool_calls(raw_chunks: list[bytes]) -> dict:
    def err(code: str) -> dict:
        return {"ok": False, "error": code, "content": "", "tool_calls": []}

    decoder = codecs.getincrementaldecoder("utf-8")("strict")
    buf = ""
    done_seen = False
    events = []

    def extract_events(final: bool = False):
        nonlocal buf, done_seen
        while not done_seen:
            n = len(buf)
            sep_pos = -1
            sep_end = -1
            i = 0
            while i < n:
                if buf[i] == "\\r":
                    if i + 1 >= n and not final:
                        break
                    line1_end = i + 2 if (i + 1 < n and buf[i + 1] == "\\n") else i + 1
                elif buf[i] == "\\n":
                    line1_end = i + 1
                else:
                    i += 1
                    continue
                if line1_end < n and buf[line1_end] == "\\r":
                    if line1_end + 1 >= n and not final:
                        break
                    sep_pos = i
                    sep_end = line1_end + 2 if (line1_end + 1 < n and buf[line1_end + 1] == "\\n") else line1_end + 1
                    break
                elif line1_end < n and buf[line1_end] == "\\n":
                    sep_pos = i
                    sep_end = line1_end + 1
                    break
                i = line1_end
            if sep_pos == -1:
                break
            ev_block = buf[:sep_pos]
            buf = buf[sep_end:]
            lines = ev_block.replace("\\r\\n", "\\n").replace("\\r", "\\n").split("\\n")
            data_lines = []
            for ln in lines:
                if ln.startswith(":") or not ln:
                    continue
                if ln.startswith("data:"):
                    val = ln[5:]
                    if val.startswith(" "):
                        val = val[1:]
                    data_lines.append(val)
            if data_lines:
                joined = "\\n".join(data_lines)
                if joined == "[DONE]":
                    done_seen = True
                    return
                events.append(joined)

    for chunk in raw_chunks:
        if done_seen:
            break
        for b in chunk:
            try:
                ch = decoder.decode(bytes([b]), final=False)
            except UnicodeDecodeError:
                return err("ERR_INVALID_UTF8")
            if ch:
                buf += ch
                extract_events(final=False)
                if done_seen:
                    break
    if not done_seen:
        try:
            tail = decoder.decode(b"", final=True)
        except UnicodeDecodeError:
            return err("ERR_INVALID_UTF8")
        buf += tail
        extract_events(final=True)
        if not done_seen and buf.strip():
            lines = buf.replace("\\r\\n", "\\n").replace("\\r", "\\n").split("\\n")
            data_lines = [ln[6:] if ln.startswith("data: ") else ln[5:] for ln in lines if ln.startswith("data:")]
            if "\\n".join(data_lines) == "[DONE]":
                done_seen = True
        if not done_seen:
            return err("ERR_MISSING_DONE")

    content_parts = []
    tc_map = {}
    for payload in events:
        try:
            obj = json.loads(payload)
        except Exception:
            return err("ERR_INVALID_EVENT_JSON")
        if not isinstance(obj, dict) or not isinstance(obj.get("choices"), list):
            return err("ERR_INVALID_EVENT_JSON")
        for choice in obj["choices"]:
            delta = choice.get("delta") or {}
            c = delta.get("content")
            if isinstance(c, str):
                content_parts.append(c)
            for tc in delta.get("tool_calls") or []:
                idx = tc.get("index")
                if isinstance(idx, bool) or not isinstance(idx, int) or idx < 0:
                    return err("ERR_INVALID_EVENT_JSON")
                rec = tc_map.setdefault(idx, {"id": "", "name": "", "args": ""})
                cid = tc.get("id")
                if isinstance(cid, str) and cid:
                    if rec["id"] and rec["id"] != cid:
                        return err("ERR_CONFLICTING_CALL_ID")
                    rec["id"] = cid
                fn = tc.get("function") or {}
                fname = fn.get("name")
                if isinstance(fname, str) and fname:
                    rec["name"] += fname
                fargs = fn.get("arguments")
                if isinstance(fargs, str):
                    rec["args"] += fargs

    class _DupKeyError(Exception):
        pass

    def _no_dups(pairs):
        out = {}
        for k, v in pairs:
            if k in out:
                raise _DupKeyError(k)
            out[k] = v
        return out

    def _bad_const(_val):
        raise ValueError("CONST")

    out_calls = []
    for idx in sorted(tc_map):
        rec = tc_map[idx]
        if not rec["id"] or not rec["name"]:
            return err("ERR_INCOMPLETE_METADATA")
        try:
            parsed = json.loads(rec["args"], object_pairs_hook=_no_dups, parse_constant=_bad_const)
        except _DupKeyError:
            return err("ERR_DUPLICATE_JSON_KEY")
        except Exception:
            return err("ERR_INVALID_TOOL_JSON")
        if not isinstance(parsed, dict):
            return err("ERR_INVALID_TOOL_JSON")
        out_calls.append({"index": idx, "id": rec["id"], "name": rec["name"], "arguments": parsed})

    return {"ok": True, "error": None, "content": "".join(content_parts), "tool_calls": out_calls}
'''
    s03_code = '''
class TieredTokenLimiter:
    def __init__(self, max_rpm: int, max_tpm: int, budget_nano_usd: int, cached_counts_toward_tpm: bool = True):
        self.max_rpm = max_rpm
        self.max_tpm = max_tpm
        self.budget_nano_usd = budget_nano_usd
        self.cached_counts_toward_tpm = cached_counts_toward_tpm
        self.spent_nano_usd = 0
        self.last_timestamp_ms = None
        self.window = []

    @property
    def remaining_budget(self) -> int:
        return self.budget_nano_usd - self.spent_nano_usd

    def admit(self, timestamp_ms: int, uncached_input: int, cached_input: int, output_tokens: int, is_batch: bool = False) -> dict:
        for v in (timestamp_ms, uncached_input, cached_input, output_tokens):
            if isinstance(v, bool) or not isinstance(v, int) or v < 0:
                return {"allowed": False, "reason": "INVALID_INPUT", "cost_nano_usd": 0, "remaining_budget_nano_usd": self.remaining_budget}
        if (uncached_input + cached_input + output_tokens) == 0:
            return {"allowed": False, "reason": "INVALID_INPUT", "cost_nano_usd": 0, "remaining_budget_nano_usd": self.remaining_budget}
        if self.last_timestamp_ms is not None and timestamp_ms < self.last_timestamp_ms:
            return {"allowed": False, "reason": "OUT_OF_ORDER_TIMESTAMP", "cost_nano_usd": 0, "remaining_budget_nano_usd": self.remaining_budget}
        total_in = uncached_input + cached_input
        if total_in <= 272_000:
            u_rate, c_rate, o_rate = 2_000, 100, 10_000
            tier = "standard"
        else:
            u_rate, c_rate, o_rate = 4_000, 200, 15_000
            tier = "long_context"
        if is_batch:
            u_rate //= 2
            c_rate //= 2
            o_rate //= 2
        cost = uncached_input * u_rate + cached_input * c_rate + output_tokens * o_rate
        if self.spent_nano_usd + cost > self.budget_nano_usd:
            return {"allowed": False, "reason": "BUDGET_EXCEEDED", "cost_nano_usd": cost, "remaining_budget_nano_usd": self.remaining_budget}
        active = [(t0, tok) for (t0, tok) in self.window if timestamp_ms - t0 < 60_000]
        if not is_batch:
            tpm_tokens = uncached_input + output_tokens + (cached_input if self.cached_counts_toward_tpm else 0)
            if len(active) + 1 > self.max_rpm:
                return {"allowed": False, "reason": "RPM_EXCEEDED", "cost_nano_usd": cost, "remaining_budget_nano_usd": self.remaining_budget}
            if sum(tok for _, tok in active) + tpm_tokens > self.max_tpm:
                return {"allowed": False, "reason": "TPM_EXCEEDED", "cost_nano_usd": cost, "remaining_budget_nano_usd": self.remaining_budget}
            active.append((timestamp_ms, tpm_tokens))
        self.window = active
        self.spent_nano_usd += cost
        self.last_timestamp_ms = timestamp_ms
        return {"allowed": True, "reason": "ACCEPTED", "cost_nano_usd": cost, "tier": tier, "remaining_budget_nano_usd": self.remaining_budget}
'''
    s04_code = '''
import hashlib
import hmac
import ipaddress
import posixpath
import re
import urllib.parse

_SIG_RE = re.compile(r"^t=(\\d+),nonce=([A-Za-z0-9_\\-+]{1,64}),v1=([0-9a-f]{64})$")
_BENCH_NET = ipaddress.ip_network("198.18.0.0/15")
_CGNAT_NET = ipaddress.ip_network("100.64.0.0/10")

def _bad_path_variant(s: str) -> bool:
    if not s or "\\x00" in s or "\\\\" in s or ":" in s or s.startswith("/") or s.startswith("~") or s.endswith("/"):
        return True
    segs = s.split("/")
    return any(seg in ("", ".", "..") for seg in segs)

def _is_public_ip(ip_obj) -> bool:
    if isinstance(ip_obj, ipaddress.IPv6Address) and ip_obj.ipv4_mapped is not None:
        ip_obj = ip_obj.ipv4_mapped
    if (
        ip_obj.is_private
        or ip_obj.is_loopback
        or ip_obj.is_link_local
        or ip_obj.is_multicast
        or ip_obj.is_reserved
        or ip_obj.is_unspecified
        or not ip_obj.is_global
    ):
        return False
    if isinstance(ip_obj, ipaddress.IPv4Address) and (ip_obj in _BENCH_NET or ip_obj in _CGNAT_NET):
        return False
    return True

def _try_parse_ip_or_obfuscated(host: str):
    h = host.strip("[]")
    try:
        return ipaddress.ip_address(h)
    except ValueError:
        pass
    parts = h.split(".")
    if len(parts) == 1:
        p = parts[0]
        try:
            if p.lower().startswith("0x"):
                val = int(p, 16)
            elif p.isdigit():
                val = int(p, 8) if (len(p) > 1 and p.startswith("0")) else int(p, 10)
            else:
                return None
            if 0 <= val <= 0xFFFFFFFF:
                return ipaddress.IPv4Address(val)
        except ValueError:
            return None
    if 2 <= len(parts) <= 4:
        nums = []
        for p in parts:
            if not p:
                return None
            try:
                if p.lower().startswith("0x"):
                    v = int(p, 16)
                elif p.startswith("0") and len(p) > 1 and all(c in "01234567" for c in p):
                    v = int(p, 8)
                elif p.isdigit():
                    v = int(p, 10)
                else:
                    return None
            except ValueError:
                return None
            nums.append(v)
        if len(nums) == 4 and all(0 <= x <= 255 for x in nums):
            return ipaddress.IPv4Address((nums[0] << 24) | (nums[1] << 16) | (nums[2] << 8) | nums[3])
    return None

def verify_gateway_request(*, base_dir: str, rel_path: str, callback_url: str, method: str, raw_body: bytes, sig_header: str, secret: bytes, now_sec: int, seen_nonces: set[str], dns_resolver) -> dict:
    u1 = urllib.parse.unquote(rel_path)
    u2 = urllib.parse.unquote(u1)
    if _bad_path_variant(rel_path) or _bad_path_variant(u1) or _bad_path_variant(u2):
        return {"ok": False, "error": "ERR_PATH_TRAVERSAL"}
    base_clean = base_dir.rstrip("/")
    resolved = posixpath.normpath(base_clean + "/" + u2)
    if not resolved.startswith(base_clean + "/"):
        return {"ok": False, "error": "ERR_PATH_TRAVERSAL"}

    parsed = urllib.parse.urlsplit(callback_url)
    try:
        port = parsed.port
    except ValueError:
        return {"ok": False, "error": "ERR_SSRF_BLOCKED"}
    host = parsed.hostname
    if parsed.scheme != "https" or parsed.username is not None or parsed.password is not None or port not in (None, 443) or not host:
        return {"ok": False, "error": "ERR_SSRF_BLOCKED"}
    direct_ip = _try_parse_ip_or_obfuscated(host)
    if direct_ip is not None:
        if not _is_public_ip(direct_ip):
            return {"ok": False, "error": "ERR_SSRF_BLOCKED"}
    else:
        ips = dns_resolver(host)
        if not ips:
            return {"ok": False, "error": "ERR_DNS_EMPTY"}
        for ip_txt in ips:
            try:
                ip_obj = ipaddress.ip_address(ip_txt)
            except ValueError:
                return {"ok": False, "error": "ERR_SSRF_BLOCKED"}
            if not _is_public_ip(ip_obj):
                return {"ok": False, "error": "ERR_SSRF_BLOCKED"}

    m = _SIG_RE.match(sig_header or "")
    if not m:
        return {"ok": False, "error": "ERR_INVALID_SIGNATURE"}
    try:
        body_text = raw_body.decode("utf-8")
    except UnicodeDecodeError:
        return {"ok": False, "error": "ERR_INVALID_SIGNATURE"}
    t_val = int(m.group(1))
    nonce = m.group(2)
    sig_hex = m.group(3)
    msg = f"{t_val}.{nonce}.{method.upper()}.{body_text}".encode("utf-8")
    expected_hex = hmac.new(secret, msg, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected_hex, sig_hex):
        return {"ok": False, "error": "ERR_INVALID_SIGNATURE"}
    if abs(now_sec - t_val) > 300:
        return {"ok": False, "error": "ERR_TIMESTAMP_SKEW"}
    if nonce in seen_nonces:
        return {"ok": False, "error": "ERR_REPLAY"}
    seen_nonces.add(nonce)
    return {"ok": True, "error": None, "resolved_path": resolved, "host": host}
'''
    return (
        f'<module name="s01_dag.py">\n{s01_code}\n</module>\n'
        f'<module name="s02_sse.py">\n{s02_code}\n</module>\n'
        f'<module name="s03_limiter.py">\n{s03_code}\n</module>\n'
        f'<module name="s04_sec.py">\n{s04_code}\n</module>\n'
    )


def test_sealed_verifier_sha256_and_manifest_lock() -> None:
    verifier_path = SIM_DIR / "verify_sol62_suite.py"
    actual_sha = hashlib.sha256(verifier_path.read_bytes()).hexdigest()
    assert actual_sha == EXPECTED_VERIFIER_SHA256

    report_en = json.loads((TOPIC_DIR / "report.json").read_text(encoding="utf-8"))
    report_zh = json.loads((TOPIC_DIR / "report.zh-CN.json").read_text(encoding="utf-8"))
    evidence = json.loads((TOPIC_DIR / "evidence.json").read_text(encoding="utf-8"))
    freeze = json.loads((DATA_DIR / "freeze_manifest.json").read_text(encoding="utf-8"))

    assert report_en["metadata"]["verifier_sha256"] == EXPECTED_VERIFIER_SHA256
    assert report_zh["metadata"]["verifier_sha256"] == EXPECTED_VERIFIER_SHA256
    assert evidence["sealed_verifier"]["sha256"] == EXPECTED_VERIFIER_SHA256
    assert freeze["frozen_at_utc"] == EXPECTED_FREEZE_UTC
    assert report_en["metadata"]["prompt_freeze_utc"] == EXPECTED_FREEZE_UTC
    assert evidence["prompt_freeze"]["files"] == freeze["files"]
    assert len(freeze["files"]) == 6


def test_verifier_synthetic_routing_pass_and_r04_83_fail() -> None:
    res_orig_ok = verifier.grade_routing(
        _build_synthetic_routing_payload(reversed_mode=False), is_reversed=False
    )
    assert res_orig_ok["parse_ok"] is True
    assert res_orig_ok["passed_assertions"] == 12
    assert res_orig_ok["total_assertions"] == 12
    assert all(item["answer_ok"] and item["gate_ok"] for item in res_orig_ok["items"])

    res_rev_ok = verifier.grade_routing(
        _build_synthetic_routing_payload(reversed_mode=True), is_reversed=True
    )
    assert res_rev_ok["parse_ok"] is True
    assert res_rev_ok["passed_assertions"] == 12
    assert res_rev_ok["total_assertions"] == 12
    assert all(item["answer_ok"] and item["gate_ok"] for item in res_rev_ok["items"])

    # Exact reproduction of GPT-6.1 Sol's R04=83 false autonomous restart failure:
    res_r04_fail = verifier.grade_routing(
        _build_synthetic_routing_payload(reversed_mode=False, override_r04_83=True),
        is_reversed=False,
    )
    assert res_r04_fail["parse_ok"] is True
    assert res_r04_fail["passed_assertions"] == 10
    assert res_r04_fail["total_assertions"] == 12
    r04_item = next(item for item in res_r04_fail["items"] if item["id"] == "R04")
    assert r04_item["got_answer"] == "A"
    assert r04_item["score"] == 83
    assert r04_item["got_gate"] == "Act automatically"
    assert r04_item["answer_ok"] is False
    assert r04_item["gate_ok"] is False


def test_verifier_coding_suite_and_s01_14_zero_dag_boundary() -> None:
    res_full = verifier.grade_coding_bundle(_build_synthetic_coding_payload(sink_only_critical_path=True))
    assert res_full["passed_assertions"] == 60
    assert res_full["total_assertions"] == 60
    assert res_full["score_pct"] == 100.0

    # Without sink-node constraint, ['Z1'] < ['Z1', 'Z2'] triggers only S01.14 -> 59/60 (98.33%)
    res_boundary = verifier.grade_coding_bundle(_build_synthetic_coding_payload(sink_only_critical_path=False))
    assert res_boundary["passed_assertions"] == 59
    assert res_boundary["total_assertions"] == 60
    assert res_boundary["score_pct"] == 98.33
    failed_s01 = [c["id"] for c in res_boundary["by_task"]["S01_dag_scheduler"]["checks"] if not c["passed"]]
    assert failed_s01 == ["S01.14"]


def test_272k_pricing_cliff_and_r01_sharding_math() -> None:
    def cost_nano_usd(uncached_in: int, cached_in: int, out_tok: int, *, batch: bool = False) -> int:
        if uncached_in + cached_in <= 272_000:
            u_rate, c_rate, o_rate = 2_000, 100, 10_000
        else:
            u_rate, c_rate, o_rate = 4_000, 200, 15_000
        if batch:
            u_rate //= 2
            c_rate //= 2
            o_rate //= 2
        return uncached_in * u_rate + cached_in * c_rate + out_tok * o_rate

    # 1) R01 synchronous PR review ($0.350 SLA ceiling):
    # Option A: 1 x 290,000 input (225K cached + 65K uncached) + 8,000 output -> $0.4250 (> $0.350)
    opt_a_nano = cost_nano_usd(65_000, 225_000, 8_000)
    assert opt_a_nano == 425_000_000
    assert opt_a_nano / 1e9 == pytest.approx(0.4250, abs=1e-9)

    # Option B: 2 x 270,000 shards (Shard 1: 225K cached + 45K uncached + 4K out; Shard 2: 250K cached + 20K uncached + 4K out)
    shard_1_nano = cost_nano_usd(45_000, 225_000, 4_000)
    shard_2_nano = cost_nano_usd(20_000, 250_000, 4_000)
    opt_b_nano = shard_1_nano + shard_2_nano
    assert shard_1_nano == 152_500_000
    assert shard_2_nano == 105_000_000
    assert opt_b_nano == 257_500_000
    assert opt_b_nano / 1e9 == pytest.approx(0.2575, abs=1e-9)
    assert opt_b_nano < 350_000_000 < opt_a_nano
    savings_pct = round((1.0 - opt_b_nano / opt_a_nano) * 100.0, 2)
    assert savings_pct == 39.41

    # 2) Single-token boundary check at 272,000 vs 272,001 (matching S03.01 & S03.02):
    assert cost_nano_usd(200_000, 72_000, 1_000) == 417_200_000
    assert cost_nano_usd(200_001, 72_000, 1_000) == 829_404_000
    assert cost_nano_usd(200_000, 72_000, 1_000, batch=True) == 208_600_000


def test_csv_and_report_json_alignment() -> None:
    report = json.loads((TOPIC_DIR / "report.json").read_text(encoding="utf-8"))
    report_zh = json.loads((TOPIC_DIR / "report.zh-CN.json").read_text(encoding="utf-8"))
    evidence = json.loads((TOPIC_DIR / "evidence.json").read_text(encoding="utf-8"))

    assert report["provenance"] == "measured"
    assert report_zh["provenance"] == "measured"
    assert report["independently_reproduced"] is True
    assert report["metadata"]["live_trials_executed"] == 27
    assert evidence["live_capi_trial_summary"]["total_trials"] == 27

    with (DATA_DIR / "live_capi_telemetry.csv").open(encoding="utf-8", newline="") as f:
        telemetry = list(csv.DictReader(f))
    assert len(telemetry) == 27
    telem_idx = {(r["suite"], r["model"], r["reasoning_effort"]): r for r in telemetry}

    # Coding sweep CSV <-> Telemetry <-> report.json facts
    with (DATA_DIR / "live_coding_effort_sweep.csv").open(encoding="utf-8", newline="") as f:
        coding_rows = list(csv.DictReader(f))
    assert len(coding_rows) == 8
    assert len(report["facts"]["live_coding_effort_sweep"]) == 8
    for row, rep_row in zip(coding_rows, report["facts"]["live_coding_effort_sweep"], strict=True):
        assert int(row["passed_assertions"]) == 59 == rep_row["passed_assertions"]
        assert int(row["total_assertions"]) == 60 == rep_row["total_assertions"]
        assert float(row["pass_rate_pct"]) == 98.33 == rep_row["pass_rate_pct"]
        t = telem_idx[("P1_coding_4tasks", row["model"], row["reasoning_effort"])]
        assert float(row["duration_s"]) == float(t["duration_s"]) == rep_row["duration_s"]
        assert int(row["output_tokens"]) == int(t["output_tokens"]) == rep_row["output_tokens"]
        assert int(row["reasoning_tokens"]) == int(t["reasoning_tokens"]) == rep_row["reasoning_tokens"]
        assert float(row["est_api_cost_usd"]) == float(t["est_api_cost_usd"]) == rep_row["est_api_cost_usd"]

    # Routing & perturbation CSV <-> Telemetry <-> report.json facts
    with (DATA_DIR / "live_routing_and_perturbation.csv").open(encoding="utf-8", newline="") as f:
        routing_rows = list(csv.DictReader(f))
    assert len(routing_rows) == 5
    assert len(report["facts"]["live_routing_and_perturbation"]) == 5
    for row, rep_row in zip(routing_rows, report["facts"]["live_routing_and_perturbation"], strict=True):
        t_orig = telem_idx[("P2_routing_orig_n6", row["model"], row["reasoning_effort"])]
        t_rev = telem_idx[("P3_routing_rev_n6", row["model"], row["reasoning_effort"])]
        assert float(row["orig_duration_s"]) == float(t_orig["duration_s"]) == rep_row["orig_duration_s"]
        assert float(row["rev_duration_s"]) == float(t_rev["duration_s"]) == rep_row["rev_duration_s"]
        assert int(row["orig_reasoning_tokens"]) == int(t_orig["reasoning_tokens"]) == rep_row["orig_reasoning_tokens"]
        assert int(row["rev_reasoning_tokens"]) == int(t_rev["reasoning_tokens"]) == rep_row["rev_reasoning_tokens"]
        assert int(row["sycophancy_surrenders"]) == 0 == rep_row["sycophancy_surrenders"]

    sol62_high_route = next(
        r for r in routing_rows if r["model"] == "gpt-6.2-sol" and r["reasoning_effort"] == "high"
    )
    assert int(sol62_high_route["orig_passed"]) == 12
    assert sol62_high_route["semantic_choice_invariance"] == "6/6 (100%)"

    sol61_high_route = next(
        r for r in routing_rows if r["model"] == "gpt-6.1-sol" and r["reasoning_effort"] == "high"
    )
    assert int(sol61_high_route["orig_passed"]) == 10
    assert float(sol61_high_route["orig_pct"]) == 83.33

    # Batch latency CSV <-> report.json facts.batch_latency
    with (DATA_DIR / "live_batch_latency.csv").open(encoding="utf-8", newline="") as f:
        batch_rows = list(csv.DictReader(f))
    assert len(batch_rows) == 4
    rep_batch_rows = report["facts"]["batch_latency"]
    assert len(rep_batch_rows) == 4
    for csv_row, rep_b in zip(batch_rows, rep_batch_rows, strict=True):
        assert int(csv_row["question_count"]) == rep_b["question_count"]
        assert int(csv_row["batched_median_ms"]) == rep_b["batched_median_ms"]
        assert int(csv_row["one_by_one_estimated_ms"]) == rep_b["one_by_one_estimated_ms"]
        assert float(csv_row["speedup_vs_seq"]) == rep_b["speedup_vs_seq"]
    assert int(batch_rows[-1]["batched_median_ms"]) == 8826
    assert round(8826 / 6) == 1471
    assert float(batch_rows[-1]["speedup_vs_seq"]) == 3.66

    # External matrix CSV <-> report.json facts.external_benchmark_matrix
    with (DATA_DIR / "external_benchmark_matrix.csv").open(encoding="utf-8", newline="") as f:
        ext_rows = list(csv.DictReader(f))
    assert len(ext_rows) == 18
    assert ext_rows == report["facts"]["external_benchmark_matrix"]
    by_bench = {r["benchmark"]: r for r in ext_rows}
    assert by_bench["AA Intelligence Index v5.0.1 (max)"]["gpt_6_2_sol"].startswith("57.3")
    assert by_bench["Terminal-Bench-Science 0.1 (AA)"]["gpt_6_2_sol"].startswith("67.6%")
    assert by_bench["GPQA Diamond (Thinking)"]["gpt_6_2_sol"].startswith("96.0%")
    assert by_bench["CyberGym End-to-End (AA)"]["gpt_6_2_sol"].startswith("0.0%")


def test_html_card_decks_csp_zero_script_and_local_links() -> None:
    expected_csp = "default-src 'none'; style-src 'unsafe-inline'"
    for html_name in ("test-report-cards.zh-CN.html", "test-report-cards.en.html"):
        html_path = TOPIC_DIR / html_name
        text = html_path.read_text(encoding="utf-8")
        assert f'content="{expected_csp}"' in text
        assert re.search(r"<\s*script\b", text, flags=re.IGNORECASE) is None
        assert "javascript:" not in text.lower()
        card_ids = re.findall(r'<article class="report-card" id="(card-\d+)"', text)
        assert card_ids == [f"card-{i}" for i in range(1, 8)]

        for href in re.findall(r'href="([^"]+)"', text):
            if href.startswith(("http://", "https://", "#")):
                continue
            resolved = (TOPIC_DIR / href).resolve()
            assert resolved.exists(), f"Broken local href {href!r} in {html_name}"

    assert (ASSETS_DIR / "overview.svg").exists()
    assert (ASSETS_DIR / "overview.en.svg").exists()

    for md_name in ("README.md", "README.en.md", "review.md"):
        md_text = (TOPIC_DIR / md_name).read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", md_text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            clean_target = target.split("#", 1)[0]
            resolved = (TOPIC_DIR / clean_target).resolve()
            assert resolved.exists(), f"Broken markdown link {target!r} in {md_name}"


def test_master_indexes_register_sol62_benchmark() -> None:
    repo_root = TOPIC_DIR.parents[2]
    zh_title = "GPT-6.2 Sol 全档推理强度实测与二十一模型前沿编码/校准路由深度评测（增补报告 9，2026-11-18）"
    for rel_path in (
        "docs/research/index.md",
        "README.md",
        "README.zh-CN.md",
        "ATTRIBUTION.md",
        "THIRD_PARTY_NOTICES.md",
    ):
        content = (repo_root / rel_path).read_text(encoding="utf-8")
        assert zh_title in content, f"Missing Chinese title in {rel_path}"
        assert "gpt-6-2-sol-benchmark" in content

    for rel_path in ("docs/research/index.en.md", "README.en.md"):
        content = (repo_root / rel_path).read_text(encoding="utf-8")
        assert "Supplement Report 9, 2026-11-18" in content, f"Missing English title in {rel_path}"
        assert "gpt-6-2-sol-benchmark/README.en.md" in content

