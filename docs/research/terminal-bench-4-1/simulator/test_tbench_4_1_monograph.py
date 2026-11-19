"""Deterministic verification & hygiene suite for Terminal-Bench 4.1 Monograph.

Verifies:
  1. Exact ground-truth metrics in data/tbench_4_1_summary.json & evidence.json
     (65 rows, 52 unique pairs, 7/52 commercial Pareto frontier, #1 Copilot Fusion
     71.21% +5.45pt lead, #2-#8 47.2x cost spread, #11 Kimi K3.1 Pro pass@5=84.85%,
     Overthinking Tax, 7 domain rates, and 4 zero-solve 0/325 Wall tasks).
  2. Strict 7-Card 4:5 HTML compliance (CSP default-src 'none'; style-src 'unsafe-inline',
     zero <script>, #card-1..#card-7, provenance & independently_reproduced=false).
  3. Zero benchmark canary GUIDs across all topic files.
  4. Valid relative links across README.md, README.en.md, and HTML artifacts.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

TOPIC_DIR = Path(__file__).resolve().parent.parent
SUMMARY_PATH = TOPIC_DIR / "data" / "tbench_4_1_summary.json"
EVIDENCE_PATH = TOPIC_DIR / "evidence.json"

UUID_RE = re.compile(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}")
CANARY_PREFIX = "26b5c67b"


def test_ground_truth_leaderboard_pareto_and_tasks() -> None:
    d = json.loads(SUMMARY_PATH.read_text(encoding="utf-8"))
    ev = json.loads(EVIDENCE_PATH.read_text(encoding="utf-8"))

    assert d["benchmark_id"] == "terminal-bench@4.1.0"
    assert d["provenance"] == "anonymized_reported"
    assert d["independently_reproduced"] is False
    assert d["source_bundle_sha256"] == "2f612504302183339b0b6e37938aa7adcb2728279ac839a8d548f052a47959cc"
    assert ev["canary_audit"]["source_bundle_sha256"] == d["source_bundle_sha256"]

    totals = d["totals"]
    assert totals["total_rows"] == 65
    assert totals["unique_model_agent_pairs"] == 52
    assert totals["priced_unique_pairs"] == 51
    assert totals["unpriced_unique_pairs"] == 1
    assert totals["pareto_frontier_count"] == 7
    assert totals["pareto_frontier_share_pct"] == 13.46
    assert totals["total_tasks"] == 66
    assert totals["cpu_only_tasks"] == 63
    assert totals["gpu_tasks_count"] == 3
    assert totals["total_trials"] == 21450
    assert (
        totals["total_passes"] + totals["total_fails"] + totals["total_timeouts"] + totals["total_errors"]
        == 21450
    )

    rows = d["leaderboard_rows"]
    r1, r2a, r2b = rows[0], rows[1], rows[2]
    assert (r1["model"], r1["agent"], r1["accuracy"], r1["ci95"]) == (
        "Copilot Fusion",
        "GitHub Copilot",
        71.21,
        2.88,
    )
    assert round(r1["accuracy"] - r2a["accuracy"], 2) == 5.45
    assert r2a["accuracy"] == r2b["accuracy"] == 65.76

    sol62 = next(r for r in rows if r["model"] == "GPT-6.2 Sol" and r["agent"] == "Codex")
    assert (sol62["rank"], sol62["accuracy"], sol62["cost_usd"], sol62["cost_per_solve"]) == (
        7,
        61.52,
        349.16,
        1.72,
    )
    assert round(r2b["cost_usd"] / sol62["cost_usd"], 1) == 47.2

    kimi = next(r for r in rows if r["model"] == "Kimi K3.1 Pro")
    assert (kimi["accuracy"], kimi["pass_at_5"]) == (59.7, 84.85)
    assert round(kimi["pass_at_5"] - kimi["accuracy"], 2) == 25.15

    # Exact 7-point Pareto frontier order
    pf_models = [p["model"] for p in d["pareto_frontier"]]
    assert pf_models == [
        "Inkling Small",
        "GPT-6 Luna",
        "Muse Ember",
        "DeepSeek V4.1 Flash 1017",
        "GPT-6.2 Sol",
        "Gemini 4 Carbon",
        "Copilot Fusion",
    ]

    # Overthinking Tax verification
    f51_xh = next(r for r in rows if r["model"] == "Fable 5.1" and r["effort"] == "xhigh")
    f51_mx = next(r for r in rows if r["model"] == "Fable 5.1" and r["effort"] == "max")
    assert f51_xh["accuracy"] > f51_mx["accuracy"]
    assert f51_xh["cost_usd"] < f51_mx["cost_usd"]

    op5_xh = next(r for r in rows if r["model"] == "Opus 5" and r["effort"] == "xhigh")
    op5_mx = next(r for r in rows if r["model"] == "Opus 5" and r["effort"] == "max")
    assert op5_xh["accuracy"] > op5_mx["accuracy"]

    # Domain order & 4 zero-solve Wall tasks
    dom = {x["domain"]: x["avg_solve_pct"] for x in d["domain_summary"]}
    assert dom == {
        "Security": 52,
        "ML": 43,
        "Media": 38,
        "Hardware": 37,
        "Software": 35,
        "Science": 34,
        "Operations": 26,
    }

    zero_tasks = sorted(t["task"] for t in d["tasks"] if t["pass_count"] == 0)
    assert zero_tasks == [
        "bun-sourcemap-leak",
        "freight-dispatch-shift",
        "glycan-ms2-elucidation",
        "ontology-kg-querying",
    ]


def test_seven_card_html_csp_and_self_containment() -> None:
    for html_name in ("test-report-cards.en.html", "test-report-cards.zh-CN.html"):
        text = (TOPIC_DIR / html_name).read_text(encoding="utf-8")
        assert "default-src 'none'; style-src 'unsafe-inline'" in text
        assert "<script" not in text.lower()
        for idx in range(1, 8):
            assert f'id="card-{idx}"' in text
            assert f"{idx} / 7" in text
        assert 'id="card-8"' not in text
        assert "anonymized_reported" in text
        assert "independently_reproduced=false" in text
        # Ensure no external http(s) resource fetches in href/src attributes
        ext_refs = re.findall(r'(?:src|href)\s*=\s*["\'](https?://[^"\']+)["\']', text, flags=re.I)
        assert ext_refs == [], f"Unexpected external href/src in {html_name}: {ext_refs}"


def test_zero_canary_guids_and_valid_relative_links() -> None:
    for path in TOPIC_DIR.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".html", ".json", ".svg", ".py"}:
            if path.name == Path(__file__).name:
                continue
            content = path.read_text(encoding="utf-8")
            assert CANARY_PREFIX not in content.lower(), f"Canary prefix found in {path}"
            assert UUID_RE.findall(content) == [], f"UUID string found in {path}"

    assert (TOPIC_DIR / "assets" / "overview.svg").exists()

    link_re = re.compile(r"\]\(([^)#\s]+)")
    for md_name in ("README.md", "README.en.md"):
        md_path = TOPIC_DIR / md_name
        md_text = md_path.read_text(encoding="utf-8")
        assert "https://github.com/turbo998/benchmark-harness-engineering" in md_text
        assert "https://turbo998.github.io/workshops/terminal-bench/index.html" in md_text
        for target in link_re.findall(md_text):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (md_path.parent / target).resolve()
            assert resolved.exists(), f"Broken relative link in {md_name}: {target} -> {resolved}"
