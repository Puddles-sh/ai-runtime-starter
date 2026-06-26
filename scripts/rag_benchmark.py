#!/usr/bin/env python3
"""RAG Benchmark — test all models on failing Graph API tasks with retrieved context.

Retrieves relevant MS Graph PowerShell docs from Qdrant, injects them into
each task prompt, runs all models, and outputs raw JSONL for opus_scorer.py.

The delta between these scores and the baseline shootout scores (no RAG)
identifies which models can actually incorporate retrieved context vs which
ignore it — separating capable models from one-trick performers.

Baseline scores (no RAG) for reference:
  ga-deprecated-module : deepseek-r1:14b 2-3 | phi4:14b 0-5 | qwen3.6:35b 4-6 | gemma4:26b 7-8
  ga-error-handling    : deepseek-r1:14b 2-3 | phi4:14b 0-5 | qwen3.6:35b 4-6 | gemma4:26b 0-5
  ps-graph-stale-users : deepseek-r1:14b 2-3 | phi4:14b 0-5 | qwen3.6:35b 4-6 | gemma4:26b 6-9

Usage:
  python3 rag_benchmark.py --host http://localhost:11434

  # Subset of models:
  python3 rag_benchmark.py --models gemma4:26b qwen3.6:35b --host http://localhost:11434

  # Score afterward:
  python3 opus_scorer.py ~/benchmark-results/rag-benchmark-raw-TIMESTAMP.jsonl
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


# All models benchmarked so far — full field gives the most informative delta table.
DEFAULT_MODELS = [
    "gemma4:26b",
    "qwen3.6:35b",
    "qwen3:14b",
    "qwen3:8b",
    "deepseek-r1:14b",
    "phi4:14b",
]

EMBED_MODEL = "nomic-embed-text"
DEFAULT_COLLECTION = "graph-ps"
MAX_EMBED_CHARS = 6000
TOP_K = 4  # retrieve top-4 chunks per task

# The 3 failing tasks — identical to graph_api_shootout.py for direct comparison.
FAILING_TASKS: list[tuple[str, str]] = [
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

# Baseline scores from non-RAG runs for delta reporting.
BASELINE: dict[str, dict[str, str]] = {
    "ga-deprecated-module": {
        "gemma4:26b": "7-8", "qwen3.6:35b": "4-6", "qwen3:14b": "4",
        "qwen3:8b": "4", "deepseek-r1:14b": "2-3", "phi4:14b": "0-5",
    },
    "ga-error-handling": {
        "gemma4:26b": "0-5", "qwen3.6:35b": "4-6", "qwen3:14b": "5",
        "qwen3:8b": "5", "deepseek-r1:14b": "2-3", "phi4:14b": "0-5",
    },
    "ps-graph-stale-users": {
        "gemma4:26b": "6-9", "qwen3.6:35b": "4-6", "qwen3:14b": "4",
        "qwen3:8b": "4", "deepseek-r1:14b": "2-3", "phi4:14b": "0-5",
    },
}

RAG_SYSTEM = (
    "You are a Microsoft 365 and Intune automation expert writing production PowerShell scripts.\n\n"
    "IMPORTANT: The following Microsoft Graph PowerShell documentation has been retrieved for this task.\n"
    "Use ONLY the cmdlets, parameter names, and property names shown in this documentation.\n"
    "Do not use cmdlets, parameters, or property names that are not listed in the reference below.\n\n"
    "{context}\n\n"
    "---\n\n"
    "Now complete the following task using the documentation above as your authoritative reference:\n\n"
    "{task}"
)


# --- HTTP helpers (no external deps) ---

def _post(url: str, payload: dict[str, Any], timeout: int = 60) -> dict[str, Any]:
    body = json.dumps(payload).encode("utf-8")
    req = Request(url, data=body, headers={"Content-Type": "application/json"})
    try:
        with urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {detail}") from exc
    except URLError as exc:
        raise RuntimeError(f"Network error: {exc.reason}") from exc


def _get(url: str, timeout: int = 30) -> dict[str, Any]:
    req = Request(url, headers={"Content-Type": "application/json"})
    try:
        with urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as exc:
        raise RuntimeError(f"HTTP {exc.code}") from exc
    except URLError as exc:
        raise RuntimeError(f"Network error: {exc.reason}") from exc


# --- Retrieval ---

def embed(ollama_url: str, text: str) -> list[float]:
    data = _post(f"{ollama_url}/api/embeddings", {"model": EMBED_MODEL, "prompt": text[:MAX_EMBED_CHARS]})
    return data["embedding"]


def search(qdrant_url: str, collection: str, vector: list[float], top_k: int) -> list[dict[str, Any]]:
    data = _post(
        f"{qdrant_url}/collections/{collection}/points/search",
        {"vector": vector, "limit": top_k, "with_payload": True},
    )
    return data.get("result", [])


def retrieve_context(query: str, ollama_url: str, qdrant_url: str, collection: str) -> str:
    vector = embed(ollama_url, query)
    results = search(qdrant_url, collection, vector, TOP_K)
    if not results:
        return ""
    lines = ["## Microsoft Graph PowerShell Reference\n"]
    for r in results:
        p = r.get("payload", {})
        lines.append(f"### {p.get('cmdlet', '')} ({p.get('chunk_type', '')})\n")
        lines.append(p.get("content", ""))
        lines.append("")
    return "\n".join(lines)


# --- Ollama generation ---

def stop_model(ollama_url: str, model: str) -> None:
    try:
        _post(f"{ollama_url}/api/generate", {"model": model, "keep_alive": 0, "prompt": ""})
    except RuntimeError:
        pass
    subprocess.run(["ollama", "stop", model], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)


def generate(ollama_url: str, model: str, prompt: str, keep_alive: str = "5m") -> dict[str, Any]:
    started = time.perf_counter()
    resp = _post(
        f"{ollama_url}/api/generate",
        {"model": model, "prompt": prompt, "stream": False, "keep_alive": keep_alive, "options": {"num_ctx": 32768}},
        timeout=600,
    )
    resp["wall_seconds"] = time.perf_counter() - started
    return resp


def tok_per_sec(resp: dict[str, Any]) -> float:
    ec = int(resp.get("eval_count") or 0)
    ed = float(resp.get("eval_duration") or 0)
    return round(ec / (ed / 1e9), 2) if ed else 0.0


# --- Main ---

def main() -> int:
    parser = argparse.ArgumentParser(
        description="RAG benchmark — all models on failing Graph API tasks with retrieved context.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 rag_benchmark.py --host http://localhost:11434
  python3 rag_benchmark.py --models gemma4:26b qwen3.6:35b --host http://localhost:11434

Score results:
  python3 opus_scorer.py ~/benchmark-results/rag-benchmark-raw-TIMESTAMP.jsonl
""",
    )
    parser.add_argument("--models", nargs="+", default=DEFAULT_MODELS)
    parser.add_argument("--host", default="http://localhost:11434")
    parser.add_argument("--qdrant", default="http://localhost:6333")
    parser.add_argument("--collection", default=DEFAULT_COLLECTION)
    parser.add_argument("--output-dir", type=Path, default=Path.home() / "benchmark-results")
    parser.add_argument("--skip-cold", action="store_true")
    parser.add_argument("--skip-warm", action="store_true")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    raw_path = args.output_dir / f"rag-benchmark-raw-{timestamp}.jsonl"
    responses_path = args.output_dir / f"rag-benchmark-responses-{timestamp}.md"

    print("RAG Benchmark — Graph API Failing Tasks")
    print(f"  Models     : {args.models}")
    print(f"  Tasks      : {[t for t, _ in FAILING_TASKS]}")
    print(f"  Ollama     : {args.host}")
    print(f"  Qdrant     : {args.qdrant} / {args.collection}")
    print(f"  Output     : {args.output_dir}\n")

    # Pre-retrieve context for each task once — same context for all models.
    print("Retrieving context from Qdrant...")
    task_contexts: dict[str, str] = {}
    for label, task_prompt in FAILING_TASKS:
        try:
            context = retrieve_context(task_prompt[:500], args.host, args.qdrant, args.collection)
            task_contexts[label] = context
            chunk_count = context.count("###")
            print(f"  {label}: {chunk_count} chunks retrieved")
        except RuntimeError as exc:
            print(f"  {label}: retrieval FAILED — {exc}")
            task_contexts[label] = ""
    print()

    raw_fh = raw_path.open("w", encoding="utf-8")
    resp_fh = responses_path.open("w", encoding="utf-8")
    resp_fh.write(
        "# RAG Benchmark — Model Responses\n\n"
        f"Generated: {datetime.now().isoformat(timespec='seconds')}\n\n"
        "Baseline scores (no RAG) shown per entry for delta comparison.\n\n---\n\n"
    )

    total_rows = 0
    speed_rows: list[dict[str, Any]] = []

    try:
        for model in args.models:
            for label, task_prompt in FAILING_TASKS:
                context = task_contexts.get(label, "")
                augmented_prompt = RAG_SYSTEM.format(context=context, task=task_prompt)
                baseline = BASELINE.get(label, {}).get(model, "N/A")

                print(f"{model} / {label} (baseline: {baseline})...")

                if not args.skip_cold:
                    stop_model(args.host, model)
                    cold = generate(args.host, model, augmented_prompt)
                    tps = tok_per_sec(cold)
                    raw_entry = {
                        "model": model,
                        "prompt": label,
                        "prompt_text": task_prompt,
                        "phase": "cold",
                        "run": 1,
                        "thinking": False,
                        "rag": True,
                        "baseline_score": baseline,
                        "response": cold,
                    }
                    raw_fh.write(json.dumps(raw_entry) + "\n")
                    raw_fh.flush()
                    _write_response(resp_fh, model, label, "cold", cold, tps, baseline, context)
                    speed_rows.append({"model": model, "prompt": label, "phase": "cold", "tps": tps, "baseline": baseline})
                    total_rows += 1
                    print(f"  cold  {tps:.1f} t/s  {cold.get('wall_seconds', 0):.1f}s")

                if not args.skip_warm:
                    warm = generate(args.host, model, augmented_prompt)
                    tps = tok_per_sec(warm)
                    raw_entry = {
                        "model": model,
                        "prompt": label,
                        "prompt_text": task_prompt,
                        "phase": "warm",
                        "run": 1,
                        "thinking": False,
                        "rag": True,
                        "baseline_score": baseline,
                        "response": warm,
                    }
                    raw_fh.write(json.dumps(raw_entry) + "\n")
                    raw_fh.flush()
                    _write_response(resp_fh, model, label, "warm", warm, tps, baseline, context)
                    speed_rows.append({"model": model, "prompt": label, "phase": "warm", "tps": tps, "baseline": baseline})
                    total_rows += 1
                    print(f"  warm  {tps:.1f} t/s  {warm.get('wall_seconds', 0):.1f}s")

    except KeyboardInterrupt:
        print(f"\nInterrupted — {total_rows} rows saved to {raw_path}")
    finally:
        raw_fh.close()
        resp_fh.close()

    if total_rows == 0:
        return 1

    # Speed summary
    print(f"\n{'='*65}")
    print("Speed summary (warm runs):")
    print(f"  {'Model':<25} {'Task':<28} {'t/s':>5}  Baseline")
    print(f"  {'-'*25} {'-'*28} {'-'*5}  {'-'*8}")
    for r in speed_rows:
        if r["phase"] == "warm":
            print(f"  {r['model']:<25} {r['prompt']:<28} {r['tps']:>5.1f}  {r['baseline']}")

    print(f"\nRaw JSONL  : {raw_path}")
    print(f"Responses  : {responses_path}")
    print(f"\nScore with Opus:")
    print(f"  python3 opus_scorer.py {raw_path}")

    return 0


def _write_response(
    fh: Any,
    model: str,
    label: str,
    phase: str,
    response: dict[str, Any],
    tps: float,
    baseline: str,
    context: str,
) -> None:
    resp_text = response.get("response", "").strip()
    wall = float(response.get("wall_seconds") or 0.0)
    eval_count = int(response.get("eval_count") or 0)
    prompt_tokens = int(response.get("prompt_eval_count") or 0)
    context_chunks = context.count("###")

    lines = [
        f"## {model} | {label} | {phase} | RAG=YES",
        "",
        f"**Baseline (no RAG):** {baseline} &nbsp; **RAG chunks injected:** {context_chunks}",
        f"**Tok/sec:** {tps:.1f} &nbsp; **Wall sec:** {wall:.2f} &nbsp; "
        f"**Prompt tokens:** {prompt_tokens} &nbsp; **Output tokens:** {eval_count}",
        "",
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


if __name__ == "__main__":
    raise SystemExit(main())
