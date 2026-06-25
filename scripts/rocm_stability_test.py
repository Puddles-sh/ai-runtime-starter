#!/usr/bin/env python3
"""ROCm stability test — confirms XNACK is the crash culprit, not OLLAMA_MAX_LOADED_MODELS.

Runs two models concurrently with long-generation prompts that previously triggered
the 'ROCm error: unspecified launch failure'. If this completes without error,
XNACK was the fix and MAX_LOADED_MODELS=1 is not required for stability.

Usage:
  python3 rocm_stability_test.py
  python3 rocm_stability_test.py --models qwen3:8b qwen3:14b
  python3 rocm_stability_test.py --host http://evo-x2.local:11434
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

# Prompt that previously caused the ROCm launch failure (long generation output)
STRESS_PROMPT = (
    "Write a PowerShell script using Microsoft.Graph that retrieves ALL Intune-managed devices "
    "in a tenant, handling pagination correctly. "
    "The Graph API returns a maximum of 1000 records per page with an @odata.nextLink property. "
    "Your script must follow nextLink until exhausted. "
    "Use Get-MgDeviceManagementManagedDevice with -All or implement manual pagination via Invoke-MgGraphRequest. "
    "Output total device count and export to CSV."
)


def api_json(base_url: str, path: str, payload: dict | None = None) -> dict:
    body = None
    headers = {"Content-Type": "application/json"}
    if payload is not None:
        body = json.dumps(payload).encode("utf-8")
    request = Request(f"{base_url.rstrip('/')}{path}", data=body, headers=headers)
    try:
        with urlopen(request, timeout=600) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"API error {exc.code}: {detail}") from exc
    except URLError as exc:
        raise RuntimeError(f"Could not reach Ollama: {exc.reason}") from exc


def run_inference(base_url: str, model: str, label: str) -> dict:
    print(f"  [{label}] Starting inference on {model}...")
    started = time.perf_counter()
    try:
        response = api_json(base_url, "/api/generate", {
            "model": model,
            "prompt": STRESS_PROMPT,
            "stream": False,
            "keep_alive": "2m",
            "options": {"num_ctx": 8192},
        })
        elapsed = time.perf_counter() - started
        eval_count = int(response.get("eval_count") or 0)
        eval_ns = float(response.get("eval_duration") or 0)
        tps = eval_count / (eval_ns / 1e9) if eval_ns else 0
        print(f"  [{label}] PASS — {tps:.1f} t/s | {elapsed:.1f}s wall | {eval_count} tokens")
        return {"model": model, "label": label, "status": "pass", "tps": round(tps, 2), "wall": round(elapsed, 1)}
    except RuntimeError as exc:
        elapsed = time.perf_counter() - started
        print(f"  [{label}] FAIL — {exc}")
        return {"model": model, "label": label, "status": "fail", "error": str(exc), "wall": round(elapsed, 1)}


def check_ollama_ps(base_url: str) -> list[str]:
    try:
        ps = api_json(base_url, "/api/ps")
        return [m.get("name") or m.get("model", "") for m in ps.get("models", [])]
    except RuntimeError:
        return []


def main() -> int:
    parser = argparse.ArgumentParser(description="ROCm stability / concurrent model test")
    parser.add_argument("--host", default="http://localhost:11434")
    parser.add_argument("--models", nargs=2, default=["qwen3:8b", "qwen3:14b"],
                        metavar="MODEL", help="Two models to load concurrently")
    args = parser.parse_args()

    m1, m2 = args.models
    print(f"ROCm Stability Test")
    print(f"Models: {m1}  +  {m2}")
    print(f"Host:   {args.host}")
    print()

    # Phase 1 — sequential long-generation (baseline, should always pass)
    print("Phase 1 — Sequential long-generation (baseline)")
    print("-" * 50)
    for model, label in [(m1, "seq-1"), (m2, "seq-2")]:
        result = run_inference(args.host, model, label)
        if result["status"] == "fail":
            print(f"\nFAIL: Sequential test failed on {model} — ROCm issue exists even without concurrency.")
            return 1
    print()

    # Phase 2 — concurrent inference (both models loaded simultaneously)
    print("Phase 2 — Concurrent inference (both models loaded at once)")
    print("-" * 50)
    loaded_before = check_ollama_ps(args.host)
    print(f"  Models loaded before test: {loaded_before or 'none'}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        f1 = executor.submit(run_inference, args.host, m1, "concurrent-1")
        f2 = executor.submit(run_inference, args.host, m2, "concurrent-2")
        results = [f1.result(), f2.result()]

    loaded_after = check_ollama_ps(args.host)
    print(f"  Models loaded after test:  {loaded_after or 'none'}")
    print()

    # Phase 3 — long generation while second model is still hot in memory
    print("Phase 3 — Long generation with both models warm")
    print("-" * 50)
    result = run_inference(args.host, m1, "warm-stress")
    results.append(result)
    print()

    # Summary
    passed = sum(1 for r in results if r["status"] == "pass")
    failed = sum(1 for r in results if r["status"] == "fail")

    print("=" * 50)
    print(f"Results: {passed} passed / {failed} failed")
    print()

    if failed == 0:
        print("PASS — ROCm stable with concurrent models loaded.")
        print("XNACK was the crash culprit. OLLAMA_MAX_LOADED_MODELS=1 is not required for stability.")
        print("(It still saves memory — keep it if you want tighter VRAM control.)")
    else:
        print("FAIL — ROCm still crashing under concurrent load.")
        print("Keep OLLAMA_MAX_LOADED_MODELS=1 in the service override.")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
