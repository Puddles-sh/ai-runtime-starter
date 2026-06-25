#!/usr/bin/env python3
"""Score benchmark outputs using Claude Opus as a quality oracle.

Reads the raw JSON produced by ollama_model_benchmark.py, sends each
prompt+response pair to Opus for structured scoring, and writes scored
training data that the local Scorer agent will learn from.

Usage:
  python3 opus_scorer.py path/to/ollama-benchmark-YYYYMMDD-HHMMSS.json

  # Dry run — shows what would be scored without calling the API
  python3 opus_scorer.py path/to/... --dry-run

  # Override output directory
  python3 opus_scorer.py path/to/... --output-dir /custom/path

Output files (written to same dir as input unless --output-dir set):
  opus-scored-YYYYMMDD-HHMMSS.json   — full scored records (training data)
  opus-scored-YYYYMMDD-HHMMSS.md     — ranked model comparison report

Checkpointing:
  Progress is saved to {input-stem}.checkpoint.jsonl after every entry.
  If the script is interrupted (rate limit, timeout, Ctrl-C), re-run the
  same command and it will resume automatically from where it stopped.
  The checkpoint file is deleted on successful completion.
  Use --force to ignore an existing checkpoint and start over.

API key: set ANTHROPIC_API_KEY environment variable before running.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any

import anthropic


SCORE_DIMENSIONS = ["accuracy", "completeness", "format", "hallucination_risk", "overall"]

SCORING_SYSTEM = """\
You are an expert evaluator for local AI model benchmark outputs. Your job is to
score model responses against a rubric used to build routing and training data for
an agentic IT operations system that generates PowerShell/Graph scripts and runbooks.

You must return ONLY a valid JSON object — no explanation, no markdown fences.
The JSON must have exactly these fields:
  accuracy          (int 1-10): Are facts, cmdlets, syntax, and Graph API calls correct?
  completeness      (int 1-10): Does it fully answer what was asked?
  format            (int 1-10): Is output clean and directly usable without editing?
  hallucination_risk (int 1-10): 10 = zero invented cmdlets/endpoints. 1 = heavily fabricated.
  overall           (int 1-10): Overall quality weighting all dimensions.
  issues            (list[str]): Specific problems found. Empty list if none.
  strengths         (list[str]): Specific things done well. At least one if overall >= 6.
  verdict           (str): One sentence summary — what makes this response pass or fail.

Scoring guidance:
- Accuracy: penalize wrong parameter names, incorrect Graph scopes, bad PowerShell syntax.
- Completeness: the response must address the full request, not just part of it.
- Format: PowerShell should be ready to paste. Chat should be clean prose. Runbooks should have steps.
- Hallucination risk: invented Graph beta endpoints, non-existent -Filter operators, or cmdlets that
  don't exist in the Microsoft.Graph module are severe failures (score 1-3).
- A score of 7+ means this response could be used in production with light review.
- A score of 4-6 means usable with significant edits.
- A score of 1-3 means this response should not be used.
"""

SCORING_TEMPLATE = """\
TASK CATEGORY: {category}
PROMPT LABEL: {label}

ORIGINAL PROMPT:
{prompt_text}

MODEL RESPONSE:
{response_text}

Score this response using the rubric. Return only the JSON object.
"""


def detect_category(label: str) -> str:
    """Map prompt label to a human-readable task category for context."""
    if label.startswith("ps-") or label.startswith("powershell"):
        return "PowerShell / Microsoft Graph scripting"
    if label.startswith("runbook") or label.startswith("rb-"):
        return "Runbook / repeatable operations documentation"
    if label.startswith("chat"):
        return "Conversational IT support"
    if label.startswith("context-"):
        return "Long context comprehension"
    return "General"


def score_entry(
    client: anthropic.Anthropic,
    entry: dict[str, Any],
    index: int,
    total: int,
) -> dict[str, Any]:
    """Call Opus to score a single benchmark entry. Returns entry + scores."""
    model = entry.get("model", "unknown")
    label = entry.get("prompt", "unknown")
    phase = entry.get("phase", "unknown")
    run = entry.get("run", 1)
    prompt_text = entry.get("prompt_text", "")
    response_obj = entry.get("response", {})
    response_text = response_obj.get("response", "").strip()

    print(f"  [{index}/{total}] {model} | {label} | {phase} | run {run}")

    if not response_text:
        print("    WARNING: empty response text, skipping")
        return {**entry, "scores": None, "score_error": "empty response"}

    user_msg = SCORING_TEMPLATE.format(
        category=detect_category(label),
        label=label,
        prompt_text=prompt_text or "(prompt text not available)",
        response_text=response_text,
    )

    scored = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1024,
        thinking={"type": "adaptive"},
        system=SCORING_SYSTEM,
        messages=[{"role": "user", "content": user_msg}],
    )

    # Find the text block explicitly — adaptive thinking may prepend a thinking block.
    raw_text = ""
    for block in scored.content:
        if getattr(block, "type", None) == "text":
            raw_text = block.text.strip()
            break

    if not raw_text:
        print(f"    ERROR: no text block in response (blocks: {[getattr(b, 'type', '?') for b in scored.content]})")
        return {**entry, "scores": None, "score_error": "empty text block"}

    # Strip markdown fences if Opus wrapped the JSON despite instructions.
    if raw_text.startswith("```"):
        raw_text = "\n".join(
            line for line in raw_text.splitlines()
            if not line.startswith("```")
        ).strip()

    try:
        scores = json.loads(raw_text)
        overall = scores.get("overall", 0)
        print(f"    overall={overall} accuracy={scores.get('accuracy')} "
              f"completeness={scores.get('completeness')} "
              f"hallucination_risk={scores.get('hallucination_risk')}")
    except json.JSONDecodeError as exc:
        print(f"    ERROR parsing score JSON: {exc}")
        print(f"    Raw response: {raw_text[:200]}")
        scores = {"parse_error": str(exc), "raw": raw_text}

    tok_per_sec = 0.0
    eval_count = response_obj.get("eval_count", 0)
    eval_duration_ns = response_obj.get("eval_duration", 0)
    if eval_duration_ns:
        tok_per_sec = round(eval_count / (eval_duration_ns / 1e9), 2)

    return {
        "model": model,
        "prompt": label,
        "prompt_text": prompt_text,
        "phase": phase,
        "run": run,
        "thinking": entry.get("thinking", False),
        "response_text": response_text,
        "tokens_per_second": tok_per_sec,
        "wall_seconds": response_obj.get("wall_seconds", 0),
        "eval_count": eval_count,
        "scores": scores,
    }


def build_report(scored: list[dict[str, Any]]) -> str:
    """Generate a ranked markdown comparison from scored results."""
    valid = [s for s in scored if s.get("scores") and isinstance(s["scores"], dict) and "overall" in s["scores"]]
    if not valid:
        return "# Opus Scoring Report\n\nNo valid scores to report.\n"

    lines = [
        "# Opus Scoring Report",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        f"Scored entries: {len(scored)} total, {len(valid)} with valid scores",
        "",
        "---",
        "",
        "## Ranked Results",
        "",
        "| Rank | Model | Prompt | Phase | Overall | Accuracy | Completeness | Format | Hallucination | Tok/sec |",
        "|---:|---|---|---|---:|---:|---:|---:|---:|---:|",
    ]

    ranked = sorted(valid, key=lambda x: x["scores"].get("overall", 0), reverse=True)
    for i, entry in enumerate(ranked, 1):
        s = entry["scores"]
        lines.append(
            f"| {i} | {entry['model']} | {entry['prompt']} | {entry['phase']} | "
            f"**{s.get('overall', '-')}** | {s.get('accuracy', '-')} | "
            f"{s.get('completeness', '-')} | {s.get('format', '-')} | "
            f"{s.get('hallucination_risk', '-')} | {entry.get('tokens_per_second', '-')} |"
        )

    # Per-model summary
    model_groups: dict[str, list[dict[str, Any]]] = {}
    for entry in valid:
        model_groups.setdefault(entry["model"], []).append(entry)

    lines += [
        "",
        "---",
        "",
        "## Model Averages (all prompts)",
        "",
        "| Model | Avg Overall | Avg Accuracy | Avg Completeness | Avg Hallucination | Avg Tok/sec | Entries |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]

    model_avgs = []
    for model, entries in model_groups.items():
        def avg(key: str) -> float:
            vals = [e["scores"].get(key, 0) for e in entries if isinstance(e["scores"].get(key), (int, float))]
            return round(sum(vals) / len(vals), 1) if vals else 0.0

        model_avgs.append((
            model,
            avg("overall"),
            avg("accuracy"),
            avg("completeness"),
            avg("hallucination_risk"),
            round(sum(e.get("tokens_per_second", 0) for e in entries) / len(entries), 1),
            len(entries),
        ))

    for row in sorted(model_avgs, key=lambda x: x[1], reverse=True):
        lines.append(f"| {row[0]} | **{row[1]}** | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} |")

    # Per-task-category routing recommendation
    task_groups: dict[str, list[dict[str, Any]]] = {}
    for entry in valid:
        task_groups.setdefault(entry["prompt"], []).append(entry)

    lines += [
        "",
        "---",
        "",
        "## Routing Recommendation (best model per task)",
        "",
        "| Task | Best Model | Overall | Accuracy | Notes |",
        "|---|---|---:|---:|---|",
    ]

    for task, entries in sorted(task_groups.items()):
        best = max(entries, key=lambda x: x["scores"].get("overall", 0))
        s = best["scores"]
        verdict = s.get("verdict", "")
        lines.append(
            f"| {task} | {best['model']} | {s.get('overall', '-')} | "
            f"{s.get('accuracy', '-')} | {verdict[:80] + '...' if len(verdict) > 80 else verdict} |"
        )

    lines += ["", "---", ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Score Ollama benchmark outputs with Claude Opus")
    parser.add_argument("input", type=Path, help="ollama-benchmark-*.json file from benchmark script")
    parser.add_argument("--output-dir", type=Path, help="Override output directory (default: same as input)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be scored without calling API")
    parser.add_argument("--delay", type=float, default=1.0, help="Seconds to sleep between API calls (default: 1.0)")
    parser.add_argument("--force", action="store_true", help="Ignore existing checkpoint and start over")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"ERROR: file not found: {args.input}", file=sys.stderr)
        return 1

    # Accept both JSONL (new streaming format) and JSON (old in-memory format).
    if args.input.suffix == ".jsonl":
        raw_entries = []
        with args.input.open(encoding="utf-8") as fh:
            for lineno, line in enumerate(fh, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    raw_entries.append(json.loads(line))
                except json.JSONDecodeError as exc:
                    print(f"WARNING: skipping malformed line {lineno}: {exc}", file=sys.stderr)
    else:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        raw_entries = data.get("raw", [])

    if not raw_entries:
        print("ERROR: no scorable entries found in input file.", file=sys.stderr)
        print("  For JSONL: use ollama-raw-*.jsonl (produced by the updated benchmark script).", file=sys.stderr)
        print("  For JSON:  file must contain a 'raw' key with response data.", file=sys.stderr)
        return 1

    print(f"Input: {args.input}")
    print(f"Raw entries to score: {len(raw_entries)}")

    if args.dry_run:
        print("\nDry run — entries that would be scored:")
        for i, entry in enumerate(raw_entries, 1):
            print(f"  {i}. {entry.get('model')} | {entry.get('prompt')} | {entry.get('phase')} | run {entry.get('run')}")
        return 0

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set", file=sys.stderr)
        return 1

    client = anthropic.Anthropic(api_key=api_key)

    output_dir = args.output_dir or args.input.parent
    output_dir.mkdir(parents=True, exist_ok=True)

    # Checkpoint file is named after the input — same run, same checkpoint.
    checkpoint_path = output_dir / f"{args.input.stem}.checkpoint.jsonl"

    # Load any existing progress unless --force was passed.
    already_scored: dict[tuple, dict[str, Any]] = {}
    if checkpoint_path.exists() and not args.force:
        with checkpoint_path.open(encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    record = json.loads(line)
                    key = (record.get("model"), record.get("prompt"), record.get("phase"), record.get("run"))
                    already_scored[key] = record
        print(f"Resuming from checkpoint: {len(already_scored)} entries already scored.")
    elif checkpoint_path.exists() and args.force:
        checkpoint_path.unlink()
        print("--force: ignoring existing checkpoint, starting over.")

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    json_out = output_dir / f"opus-scored-{timestamp}.json"
    md_out = output_dir / f"opus-scored-{timestamp}.md"

    print(f"\nScoring with claude-opus-4-8...\n")
    scored: list[dict[str, Any]] = list(already_scored.values())
    total = len(raw_entries)
    skipped = 0

    checkpoint_fh = checkpoint_path.open("a", encoding="utf-8")
    try:
        for i, entry in enumerate(raw_entries, 1):
            key = (entry.get("model"), entry.get("prompt"), entry.get("phase"), entry.get("run"))
            if key in already_scored:
                skipped += 1
                continue

            result = score_entry(client, entry, i, total)
            scored.append(result)

            # Flush one line to checkpoint immediately so progress survives any crash.
            checkpoint_fh.write(json.dumps(result) + "\n")
            checkpoint_fh.flush()

            remaining = total - i
            if remaining > 0:
                time.sleep(args.delay)
    except KeyboardInterrupt:
        print(f"\nInterrupted. Progress saved to {checkpoint_path}. Re-run to resume.")
        checkpoint_fh.close()
        return 1
    finally:
        checkpoint_fh.close()

    json_out.write_text(
        json.dumps({"scored": scored, "source": str(args.input), "timestamp": timestamp}, indent=2),
        encoding="utf-8",
    )

    report = build_report(scored)
    md_out.write_text(report, encoding="utf-8")

    # Only delete checkpoint on clean completion.
    if checkpoint_path.exists():
        checkpoint_path.unlink()

    valid_count = sum(1 for s in scored if isinstance(s.get("scores"), dict) and "overall" in s.get("scores", {}))
    new_count = len(scored) - skipped
    print(f"\nDone. {valid_count}/{total} entries scored ({new_count} new, {skipped} resumed from checkpoint).")
    print(f"Training data: {json_out}")
    print(f"Report:        {md_out}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
