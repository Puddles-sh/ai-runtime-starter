#!/usr/bin/env python3
"""Head-to-head benchmark for the 3 Graph API task types that scored lowest
in the main overnight benchmark:
  ga-deprecated-module  (best: 4/10)
  ga-error-handling     (best: 5/10)
  ps-graph-stale-users  (best: 4/10)

Default contestants: deepseek-r1:14b, phi4:14b
Outputs raw JSONL that opus_scorer.py consumes directly.

Usage:
  # Run on EVO with defaults:
  python3 graph_api_shootout.py --host http://evo-x2.local:11434

  # Add a reference model for context:
  python3 graph_api_shootout.py --host http://evo-x2.local:11434 \\
    --models deepseek-r1:14b phi4:14b qwen3:14b

  # Score results:
  python3 opus_scorer.py ~/benchmark-results/graph-shootout-raw-TIMESTAMP.jsonl
"""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


DEFAULT_MODELS = ["deepseek-r1:14b", "phi4:14b"]

# Prompts taken verbatim from ollama_model_benchmark.py so results are comparable.
# These are the 3 tasks where every model scored <= 5/10 in the overnight run.
SHOOTOUT_PROMPTS: list[tuple[str, str]] = [
    (
        "ga-deprecated-module",
        "Write a PowerShell script that finds all enabled Entra ID users who have not signed in for 60 days "
        "and disables their accounts. "
        "IMPORTANT: Use only the Microsoft.Graph PowerShell module. "
        "Do NOT use the AzureAD module (deprecated) or MSOnline module (retired). "
        "Use Get-MgUser with -Filter and -Property. Include the correct Graph permission scope required.",
    ),
    (
        "ga-error-handling",
        "Write a PowerShell function using Microsoft.Graph that resets a user's MFA authentication methods "
        "by removing all registered methods and returns a structured result object. "
        "Include: try/catch around each Graph call, specific handling for 404 (user not found) and "
        "403 (insufficient permissions), a revert log entry written before any destructive action, "
        "and a return object with properties: Success (bool), UserId, MethodsRemoved (int), Error (string). "
        "Do not use Write-Host — use Write-Verbose for progress and return the object.",
    ),
    (
        "ps-graph-stale-users",
        "Write a PowerShell script using Microsoft Graph that finds all Entra ID user accounts "
        "that have not signed in for 90 days and are still enabled. "
        "Export results to a CSV with columns: UPN, DisplayName, LastSignInDateTime, AccountEnabled.",
    ),
]

GRAPH_ACCURACY_CHECKLIST = [
    "**Graph Accuracy Checklist:**",
    "- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL",
    "- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)",
    "- -Filter and -Property used correctly with Get-MgUser?",
    "- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)",
    "- 404 vs 403 error handling distinguished in catch blocks?",
    "- Write-Verbose not Write-Host for progress output?",
    "- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?",
    "",
]


def ns_to_seconds(value: int | float | None) -> float:
    if not value:
        return 0.0
    return float(value) / 1_000_000_000


def api_json(base_url: str, path: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
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
        raise SystemExit(f"Ollama API error {exc.code} for {path}: {detail}") from exc
    except URLError as exc:
        raise SystemExit(f"Could not reach Ollama at {base_url}: {exc.reason}") from exc


def stop_model(base_url: str, model: str) -> None:
    try:
        api_json(base_url, "/api/generate", {"model": model, "keep_alive": 0, "prompt": ""})
    except SystemExit:
        pass
    subprocess.run(["ollama", "stop", model], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)


def generate_once(
    base_url: str,
    model: str,
    prompt: str,
    keep_alive: str = "5m",
    num_ctx: int = 32768,
) -> dict[str, Any]:
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "keep_alive": keep_alive,
        "options": {"num_ctx": num_ctx},
    }
    started = time.perf_counter()
    response = api_json(base_url, "/api/generate", payload)
    response["wall_seconds"] = time.perf_counter() - started
    return response


def calc_tps(response: dict[str, Any]) -> float:
    eval_count = int(response.get("eval_count") or 0)
    eval_secs = ns_to_seconds(response.get("eval_duration"))
    return round(eval_count / eval_secs, 2) if eval_secs else 0.0


def write_response_block(
    fh: Any,
    model: str,
    label: str,
    phase: str,
    run: int,
    thinking: bool,
    response: dict[str, Any],
    tps: float,
) -> None:
    resp_text = response.get("response", "").strip()
    wall = float(response.get("wall_seconds") or 0.0)
    eval_count = int(response.get("eval_count") or 0)
    prompt_tokens = int(response.get("prompt_eval_count") or 0)

    lines = [
        f"## {model} | {label} | {phase} | run {run} | thinking: {'YES' if thinking else 'NO'}",
        "",
        f"**Tok/sec:** {tps:.1f}  **Wall sec:** {wall:.2f}  "
        f"**Prompt tokens:** {prompt_tokens}  **Output tokens:** {eval_count}",
        "",
        *GRAPH_ACCURACY_CHECKLIST,
        "**Response:**",
        "",
        resp_text,
        "",
        "**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _",
        "",
        "---",
        "",
    ]
    fh.write("\n".join(lines))
    fh.flush()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Graph API accuracy shootout — focused head-to-head on the 3 failing task types.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 graph_api_shootout.py --host http://evo-x2.local:11434
  python3 graph_api_shootout.py --host http://evo-x2.local:11434 --runs 2
  python3 graph_api_shootout.py --models deepseek-r1:14b phi4:14b qwen3:14b \\
    --host http://evo-x2.local:11434
""",
    )
    parser.add_argument("--models", nargs="+", default=DEFAULT_MODELS, metavar="MODEL")
    parser.add_argument("--host", default="http://localhost:11434")
    parser.add_argument("--runs", type=int, default=1, help="Runs per prompt per model (default: 1)")
    parser.add_argument(
        "--thinking", action="store_true",
        help="Prepend /think to prompts (Qwen3-style). deepseek-r1 thinks natively; omit for it.",
    )
    parser.add_argument("--keep-alive", default="5m")
    parser.add_argument("--output-dir", type=Path, default=Path.home() / "benchmark-results")
    parser.add_argument("--skip-cold", action="store_true")
    parser.add_argument("--skip-warm", action="store_true")
    args = parser.parse_args()

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    raw_path = args.output_dir / f"graph-shootout-raw-{timestamp}.jsonl"
    responses_path = args.output_dir / f"graph-shootout-responses-{timestamp}.md"
    prompt_labels = [label for label, _ in SHOOTOUT_PROMPTS]

    print("Graph API Shootout")
    print(f"  Models : {args.models}")
    print(f"  Prompts: {prompt_labels}")
    print(f"  Runs   : {args.runs}  Thinking: {args.thinking}")
    print(f"  Output : {args.output_dir}\n")

    raw_fh = raw_path.open("w", encoding="utf-8")
    resp_fh = responses_path.open("w", encoding="utf-8")
    resp_fh.write(
        "# Graph API Shootout -- Responses\n\n"
        f"Generated: {datetime.now().isoformat(timespec='seconds')}\n\n"
        "Failing tasks from overnight benchmark: "
        "ga-deprecated-module (4/10), ga-error-handling (5/10), ps-graph-stale-users (4/10)\n\n"
        "---\n\n"
    )
    resp_fh.flush()

    speed_rows: list[dict[str, Any]] = []
    total_rows = 0

    try:
        for model in args.models:
            for label, base_prompt in SHOOTOUT_PROMPTS:
                prompt = f"/think\n{base_prompt}" if args.thinking else base_prompt

                for run_num in range(1, args.runs + 1):
                    print(f"{model} / {label} / run {run_num}...")

                    if not args.skip_cold:
                        stop_model(args.host, model)
                        cold = generate_once(args.host, model, prompt, args.keep_alive)
                        tps = calc_tps(cold)

                        raw_fh.write(json.dumps({
                            "model": model,
                            "prompt": label,
                            "prompt_text": base_prompt,
                            "phase": "cold",
                            "run": run_num,
                            "thinking": args.thinking,
                            "response": cold,
                        }) + "\n")
                        raw_fh.flush()
                        write_response_block(resp_fh, model, label, "cold", run_num, args.thinking, cold, tps)
                        speed_rows.append({"model": model, "prompt": label, "phase": "cold", "tps": tps, "wall": cold.get("wall_seconds", 0)})
                        total_rows += 1
                        print(f"  cold  {tps:.1f} t/s  {cold.get('wall_seconds', 0):.1f}s wall")

                    if not args.skip_warm:
                        warm = generate_once(args.host, model, prompt, args.keep_alive)
                        tps = calc_tps(warm)

                        raw_fh.write(json.dumps({
                            "model": model,
                            "prompt": label,
                            "prompt_text": base_prompt,
                            "phase": "warm",
                            "run": run_num,
                            "thinking": args.thinking,
                            "response": warm,
                        }) + "\n")
                        raw_fh.flush()
                        write_response_block(resp_fh, model, label, "warm", run_num, args.thinking, warm, tps)
                        speed_rows.append({"model": model, "prompt": label, "phase": "warm", "tps": tps, "wall": warm.get("wall_seconds", 0)})
                        total_rows += 1
                        print(f"  warm  {tps:.1f} t/s  {warm.get('wall_seconds', 0):.1f}s wall")

    except KeyboardInterrupt:
        print(f"\nInterrupted -- {total_rows} rows saved to {raw_path}")
    finally:
        raw_fh.close()
        resp_fh.close()

    if total_rows == 0:
        return 1

    print(f"\n{'='*62}")
    print("Speed summary (warm runs):")
    print(f"  {'Model':<25} {'Prompt':<28} {'t/s':>5}")
    print(f"  {'-'*25} {'-'*28} {'-'*5}")
    for r in speed_rows:
        if r["phase"] == "warm":
            print(f"  {r['model']:<25} {r['prompt']:<28} {r['tps']:>5.1f}")

    print(f"\nRaw JSONL : {raw_path}")
    print(f"Responses : {responses_path}")
    print(f"\nScore with Opus:")
    print(f"  python3 opus_scorer.py {raw_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
