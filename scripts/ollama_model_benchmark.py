#!/usr/bin/env python3
"""Benchmark Ollama models for load time, response speed, loaded size, and output quality.

Intended to run on the EVO or any machine that can reach the Ollama API.
Writes JSON, CSV, Markdown summary, and a response review file so model outputs
can be read and scored manually after a run.

Results are written to disk after each prompt — safe to Ctrl-C and resume from
the saved JSONL file.

Overnight run example:
  python3 ollama_model_benchmark.py \\
    qwen3:8b qwen3:14b deepseek-r1:14b qwen2.5-coder:32b qwen3.6:35b \\
    --host http://evo-x2.local:11434 \\
    --prompt-set all \\
    --prompt-size all \\
    --runs 3 \\
    --thinking \\
    --concurrent 2
"""

from __future__ import annotations

import argparse
import concurrent.futures
import csv
import json
import statistics
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


DEFAULT_PROMPT = (
    "You are being benchmarked for a local AI homelab. "
    "In 6 concise bullets, explain what a local model server does, what Ollama does, "
    "and one operational risk to monitor."
)

# Task prompt sets — three categories matching daily use cases.
# Labels appear in all report output for per-task comparison.
PROMPT_SETS: dict[str, list[tuple[str, str]]] = {
    "chat": [
        (
            "chat-explain",
            "Explain what a homelab is and why someone working in IT operations might want one. "
            "Keep it conversational, under 150 words.",
        ),
        (
            "chat-troubleshoot",
            "A user says their laptop can't connect to the VPN after a Windows update. "
            "Walk through your first three diagnostic steps conversationally, as if talking to a non-technical colleague.",
        ),
        (
            "chat-summarize",
            "Summarize the following in plain language for a manager who doesn't read logs: "
            "'Error: certificate CN=corp-vpn.contoso.com expired 2026-06-01. "
            "Auth failures spiked from 2/hr to 340/hr. Rollback of cert bundle in progress.' "
            "Keep it under 80 words.",
        ),
    ],
    "powershell": [
        (
            "ps-graph-device-list",
            "Write a PowerShell script using Microsoft Graph (via the Microsoft.Graph module) "
            "that lists all Intune-managed Windows devices where the last sync is older than 7 days. "
            "Output: DeviceName, LastSyncDateTime, ComplianceState. Use -Select and -Filter where possible.",
        ),
        (
            "ps-graph-stale-users",
            "Write a PowerShell script using Microsoft Graph that finds all Entra ID user accounts "
            "that have not signed in for 90 days and are still enabled. "
            "Export results to a CSV with columns: UPN, DisplayName, LastSignInDateTime, AccountEnabled.",
        ),
        (
            "ps-graph-app-assignment",
            "Write a PowerShell function using Microsoft Graph that accepts an Intune app display name "
            "and returns the list of groups it is assigned to, with assignment intent (required vs available). "
            "Include error handling for app not found.",
        ),
    ],
    "runbooks": [
        (
            "runbook-offboard",
            "Write a runbook for offboarding an employee from a Microsoft 365 / Intune environment. "
            "Cover: disabling the account, revoking sessions, blocking sign-in, wiping or retiring the device, "
            "and archiving the mailbox. Format as numbered steps with a Done column.",
        ),
        (
            "runbook-cert-rotation",
            "Write a runbook for rotating an expired SCEP certificate profile in Intune. "
            "Include steps to identify affected devices, update the profile, force a sync, and verify. "
            "Note any steps that require change-control approval.",
        ),
        (
            "script-daily-health",
            "Write a repeatable daily health-check script for a homelab running Ollama and Open WebUI on Ubuntu. "
            "Check: service status, disk usage, Ollama API responsiveness, and Docker container state. "
            "Output a one-line PASS/WARN/FAIL summary per check.",
        ),
    ],
    "classify": [
        (
            "clf-intent",
            "Classify the following IT request into exactly one category from this list: "
            "[group-membership, license-assignment, device-management, user-offboard, research-only, unknown]. "
            "Return JSON only with no preamble, no explanation, and no markdown code fences: "
            "{\"category\": \"...\", \"confidence\": 0.0, \"reasoning\": \"one sentence\"}. "
            "Request: 'Can you add Sarah from accounting to the SharePoint-Finance-RW group?'",
        ),
        (
            "clf-risk",
            "Rate the risk of the following IT action. "
            "Return JSON only with no preamble, no explanation, and no markdown code fences: "
            "{\"risk\": \"LOW|MEDIUM|HIGH|CRITICAL\", \"revertable\": true, "
            "\"reasoning\": \"one sentence\"}. "
            "Action: 'Disable MFA for user jsmith@contoso.com temporarily for testing'",
        ),
        (
            "clf-ambiguous",
            "Classify the following IT request. If the request is ambiguous or missing "
            "required information, set category to 'needs-clarification' and explain what "
            "is missing in the reasoning field. "
            "Return JSON only with no preamble, no explanation, and no markdown code fences: "
            "{\"category\": \"...\", \"confidence\": 0.0, \"reasoning\": \"one sentence\", "
            "\"missing_info\": null}. "
            "Request: 'Remove the user from the group please'",
        ),
    ],
    "graph-accuracy": [
        (
            "ga-deprecated-module",
            "Write a PowerShell script that finds all enabled Entra ID users who have not signed in for 60 days "
            "and disables their accounts. "
            "IMPORTANT: Use only the Microsoft.Graph PowerShell module. "
            "Do NOT use the AzureAD module (deprecated) or MSOnline module (retired). "
            "Use Get-MgUser with -Filter and -Property. Include the correct Graph permission scope required.",
        ),
        (
            "ga-param-names",
            "Write a PowerShell script using Microsoft.Graph that adds a user to a group and then immediately "
            "verifies the membership was successful. "
            "Use New-MgGroupMemberByRef (New-MgGroupMember has been removed from MS docs). "
            "Correct call pattern: New-MgGroupMemberByRef -GroupId $groupId -BodyParameter @{'@odata.id' = "
            "'https://graph.microsoft.com/v1.0/directoryObjects/' + $userId}. "
            "Do NOT use New-MgGroupMember, -MemberId, -UserId, or -DirectoryObjectId — those are wrong. "
            "Include error handling that catches the specific Graph API error if the user is already a member.",
        ),
        (
            "ga-pagination",
            "Write a PowerShell script using Microsoft.Graph that retrieves ALL Intune-managed devices "
            "in a tenant, handling pagination correctly. "
            "The Graph API returns a maximum of 1000 records per page with an @odata.nextLink property. "
            "Your script must follow nextLink until exhausted. "
            "Use Get-MgDeviceManagementManagedDevice with -All or implement manual pagination via Invoke-MgGraphRequest. "
            "Output total device count and export to CSV.",
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
    ],
}

# Context size variants — same task at short / medium / long context length.
CONTEXT_PROMPTS: dict[str, list[tuple[str, str]]] = {
    "short": [
        (
            "ctx-short-ps",
            "Write a PowerShell one-liner that lists all disabled Entra ID users.",
        ),
    ],
    "medium": [
        (
            "ctx-medium-ps",
            "Review the following PowerShell script and identify any issues with error handling, "
            "Graph API usage, or output formatting. Suggest fixes.\n\n"
            "```powershell\n"
            "Connect-MgGraph -Scopes 'User.Read.All'\n"
            "$users = Get-MgUser -All\n"
            "foreach ($user in $users) {\n"
            "    if ($user.AccountEnabled -eq $false) {\n"
            "        $lastSign = Get-MgUser -UserId $user.Id -Property SignInActivity\n"
            "        Write-Output \"$($user.DisplayName) - $($lastSign.SignInActivity.LastSignInDateTime)\"\n"
            "    }\n"
            "}\n"
            "```\n\n"
            "Output only the corrected script with inline comments explaining each fix.",
        ),
    ],
    "long": [
        (
            "ctx-long-ps",
            "You are reviewing a complete PowerShell module for Microsoft Graph automation. "
            "Identify issues, suggest improvements, and rewrite the module cleanly.\n\n"
            "```powershell\n"
            "# Module: GraphOps.psm1\n"
            "# Purpose: Common Graph operations for Intune and Entra ID management\n\n"
            "function Connect-GraphSession {\n"
            "    param([string]$TenantId, [string]$ClientId, [string]$ClientSecret)\n"
            "    $body = @{ grant_type='client_credentials'; client_id=$ClientId;\n"
            "               client_secret=$ClientSecret; scope='https://graph.microsoft.com/.default' }\n"
            "    $token = Invoke-RestMethod -Uri \"https://login.microsoftonline.com/$TenantId/oauth2/v2.0/token\" -Method Post -Body $body\n"
            "    $global:GraphToken = $token.access_token\n"
            "}\n\n"
            "function Get-StaleDevices {\n"
            "    $headers = @{ Authorization = \"Bearer $global:GraphToken\" }\n"
            "    $url = 'https://graph.microsoft.com/v1.0/deviceManagement/managedDevices'\n"
            "    $result = Invoke-RestMethod -Uri $url -Headers $headers\n"
            "    $cutoff = (Get-Date).AddDays(-7)\n"
            "    $result.value | Where-Object { [datetime]$_.lastSyncDateTime -lt $cutoff }\n"
            "}\n\n"
            "function Add-UserToGroup {\n"
            "    param([string]$UserId, [string]$GroupId)\n"
            "    $headers = @{ Authorization = \"Bearer $global:GraphToken\"; 'Content-Type'='application/json' }\n"
            "    $body = @{ '@odata.id' = \"https://graph.microsoft.com/v1.0/directoryObjects/$UserId\" } | ConvertTo-Json\n"
            "    Invoke-RestMethod -Uri \"https://graph.microsoft.com/v1.0/groups/$GroupId/members/`$ref\" -Method Post -Headers $headers -Body $body\n"
            "}\n\n"
            "function Remove-UserFromGroup {\n"
            "    param([string]$UserId, [string]$GroupId)\n"
            "    $headers = @{ Authorization = \"Bearer $global:GraphToken\" }\n"
            "    Invoke-RestMethod -Uri \"https://graph.microsoft.com/v1.0/groups/$GroupId/members/$UserId/`$ref\" -Method Delete -Headers $headers\n"
            "}\n\n"
            "function Get-UserLicenses {\n"
            "    param([string]$UPN)\n"
            "    $headers = @{ Authorization = \"Bearer $global:GraphToken\" }\n"
            "    $user = Invoke-RestMethod -Uri \"https://graph.microsoft.com/v1.0/users/$UPN\" -Headers $headers\n"
            "    $licenses = Invoke-RestMethod -Uri \"https://graph.microsoft.com/v1.0/users/$UPN/licenseDetails\" -Headers $headers\n"
            "    $licenses.value | Select-Object skuPartNumber, skuId\n"
            "}\n"
            "```\n\n"
            "Rewrite using the Microsoft.Graph PowerShell SDK instead of raw REST calls. "
            "Add proper error handling, remove the global token variable, and add comment-based help to each function. "
            "Output only the rewritten module.",
        ),
    ],
}

GRAPH_ACCURACY_CHECKLIST = [
    "**Graph Accuracy Checklist** (for ga-* prompts):",
    "- AzureAD or MSOnline module used? → automatic Hallucination: FAIL",
    "- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)",
    "- Correct cmdlet for group membership? (New-MgGroupMemberByRef, NOT New-MgGroupMember — removed from MS docs)",
    "- Correct call pattern? (New-MgGroupMemberByRef -GroupId + -BodyParameter @odata.id, NOT -DirectoryObjectId)",
    "- Pagination handled? (-All flag or manual @odata.nextLink loop)",
    "- Graph permission scope declared and correct?",
    "- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)",
    "- No global variables for tokens?",
    "- Write-Verbose not Write-Host for progress output?",
    "",
]


def ns_to_seconds(value: int | float | None) -> float:
    if not value:
        return 0.0
    return float(value) / 1_000_000_000


def bytes_to_gib(value: int | float | None) -> float:
    if not value:
        return 0.0
    return float(value) / 1024 / 1024 / 1024


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
    try:
        ps = api_json(base_url, "/api/ps")
        loaded = [m.get("name") or m.get("model") for m in ps.get("models", [])]
        if model in loaded:
            print(f"  WARNING: {model} still appears loaded after stop — cold run result may be inaccurate")
    except SystemExit:
        pass


def generate_once(base_url: str, model: str, prompt: str, keep_alive: str, num_ctx: int = 32768) -> dict[str, Any]:
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


def get_model_runtime(base_url: str, model: str) -> dict[str, Any]:
    ps = api_json(base_url, "/api/ps")
    for item in ps.get("models", []):
        if item.get("name") == model or item.get("model") == model:
            return item
    return {}


def flatten_result(
    model: str,
    phase: str,
    response: dict[str, Any],
    runtime: dict[str, Any],
    prompt_label: str = "default",
    run: int = 1,
    thinking: bool = False,
) -> dict[str, Any]:
    eval_count = int(response.get("eval_count") or 0)
    eval_seconds = ns_to_seconds(response.get("eval_duration"))
    prompt_eval_count = int(response.get("prompt_eval_count") or 0)
    prompt_eval_seconds = ns_to_seconds(response.get("prompt_eval_duration"))
    tokens_per_second = eval_count / eval_seconds if eval_seconds else 0.0

    return {
        "model": model,
        "prompt": prompt_label,
        "phase": phase,
        "run": run,
        "thinking": thinking,
        "wall_seconds": round(float(response.get("wall_seconds") or 0.0), 3),
        "total_seconds": round(ns_to_seconds(response.get("total_duration")), 3),
        "load_seconds": round(ns_to_seconds(response.get("load_duration")), 3),
        "prompt_eval_count": prompt_eval_count,
        "prompt_eval_seconds": round(prompt_eval_seconds, 3),
        "eval_count": eval_count,
        "eval_seconds": round(eval_seconds, 3),
        "tokens_per_second": round(tokens_per_second, 2),
        "loaded_size_gib": round(bytes_to_gib(runtime.get("size")), 2),
        "loaded_vram_gib": round(bytes_to_gib(runtime.get("size_vram")), 2),
        "processor": runtime.get("details", {}).get("families", ""),
        "expires_at": runtime.get("expires_at", ""),
    }


def compute_averages(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    from collections import defaultdict

    groups: dict[tuple, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        key = (row["model"], row["prompt"], row["phase"], row["thinking"])
        groups[key].append(row)

    numeric_fields = [
        "wall_seconds", "total_seconds", "load_seconds",
        "prompt_eval_seconds", "eval_seconds", "tokens_per_second",
        "loaded_size_gib", "loaded_vram_gib",
    ]

    averages = []
    for (model, prompt, phase, thinking), group in groups.items():
        if len(group) < 2:
            continue
        avg: dict[str, Any] = {
            "model": model,
            "prompt": prompt,
            "phase": phase,
            "run": "avg",
            "thinking": thinking,
            "eval_count": round(statistics.mean(r["eval_count"] for r in group)),
            "prompt_eval_count": round(statistics.mean(r["prompt_eval_count"] for r in group)),
            "processor": group[0]["processor"],
            "expires_at": "",
        }
        for field in numeric_fields:
            values = [r[field] for r in group]
            avg[field] = round(statistics.mean(values), 3)
            avg[f"{field}_stddev"] = round(statistics.stdev(values), 3) if len(values) > 1 else 0.0
        averages.append(avg)

    return averages


def run_concurrent_test(
    base_url: str,
    model: str,
    prompt: str,
    keep_alive: str,
    n: int,
) -> dict[str, Any]:
    print(f"  Concurrent test: {n} simultaneous requests...")
    started = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor(max_workers=n) as executor:
        futures = [
            executor.submit(generate_once, base_url, model, prompt, keep_alive)
            for _ in range(n)
        ]
        results = [f.result() for f in concurrent.futures.as_completed(futures)]

    total_wall = time.perf_counter() - started
    tok_per_sec_values = []
    for r in results:
        ec = int(r.get("eval_count") or 0)
        es = ns_to_seconds(r.get("eval_duration"))
        if es:
            tok_per_sec_values.append(ec / es)

    return {
        "concurrent_n": n,
        "total_wall_seconds": round(total_wall, 3),
        "avg_tok_per_sec": round(statistics.mean(tok_per_sec_values), 2) if tok_per_sec_values else 0.0,
        "min_tok_per_sec": round(min(tok_per_sec_values), 2) if tok_per_sec_values else 0.0,
        "max_tok_per_sec": round(max(tok_per_sec_values), 2) if tok_per_sec_values else 0.0,
    }


class StreamingWriter:
    """Writes benchmark results to disk after each prompt — no in-memory accumulation."""

    def __init__(self, output_dir: Path, timestamp: str) -> None:
        output_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir = output_dir
        self.timestamp = timestamp

        self.jsonl_path = output_dir / f"ollama-benchmark-{timestamp}.jsonl"
        self.csv_path = output_dir / f"ollama-benchmark-{timestamp}.csv"
        self.responses_path = output_dir / f"ollama-responses-{timestamp}.md"
        self.concurrent_path = output_dir / f"ollama-concurrent-{timestamp}.jsonl"
        self.raw_path = output_dir / f"ollama-raw-{timestamp}.jsonl"

        self._jsonl = self.jsonl_path.open("a", encoding="utf-8")
        self._responses = self.responses_path.open("a", encoding="utf-8")
        self._concurrent = self.concurrent_path.open("a", encoding="utf-8")
        self._csv_handle = self.csv_path.open("a", encoding="utf-8", newline="")
        self._raw_jsonl = self.raw_path.open("a", encoding="utf-8")
        self._csv_writer: csv.DictWriter | None = None
        self._rows_written = 0

        self._responses.write(
            "# Ollama Model Responses\n\n"
            f"Generated: {datetime.now().isoformat(timespec='seconds')}\n\n"
            "Review each response below and score manually using the rubric:\n"
            "| Dimension | Score 1-10 |\n"
            "|---|---|\n"
            "| Accuracy — facts, cmdlets, syntax correct? | |\n"
            "| Completeness — fully answers the request? | |\n"
            "| Format — clean and usable without editing? | |\n"
            "| Hallucination risk — invented cmdlets or endpoints? | |\n"
            "| Consistency — similar quality on repeat runs? | |\n\n"
            "---\n\n"
        )
        self._responses.flush()

    def write_result(
        self,
        row: dict[str, Any],
        model: str,
        prompt_label: str,
        prompt_text: str,
        phase: str,
        run: int,
        thinking: bool,
        response: dict[str, Any],
        runtime: dict[str, Any],
    ) -> None:
        # Write metrics row to JSONL
        self._jsonl.write(json.dumps(row) + "\n")
        self._jsonl.flush()

        # Write full entry to raw JSONL — this is what opus_scorer.py reads
        raw_entry = {
            "model": model,
            "prompt": prompt_label,
            "prompt_text": prompt_text,
            "phase": phase,
            "run": run,
            "thinking": thinking,
            "response": response,
        }
        self._raw_jsonl.write(json.dumps(raw_entry) + "\n")
        self._raw_jsonl.flush()

        # Write metrics row to CSV
        if self._csv_writer is None:
            self._csv_writer = csv.DictWriter(self._csv_handle, fieldnames=list(row.keys()), extrasaction="ignore")
            self._csv_writer.writeheader()
        self._csv_writer.writerow(row)
        self._csv_handle.flush()

        # Write full response to responses file immediately
        resp_text = response.get("response", "").strip()
        thinking_flag = "YES" if thinking else "NO"
        eval_count = int(response.get("eval_count") or 0)
        eval_seconds = ns_to_seconds(response.get("eval_duration"))
        tok_per_sec = eval_count / eval_seconds if eval_seconds else 0.0
        prompt_tokens = int(response.get("prompt_eval_count") or 0)
        wall = float(response.get("wall_seconds") or 0.0)

        lines = [
            f"## {model} | {prompt_label} | {phase} | run {run} | thinking: {thinking_flag}",
            "",
            f"**Tok/sec:** {tok_per_sec:.1f} &nbsp; **Wall sec:** {wall:.2f} &nbsp; "
            f"**Prompt tokens:** {prompt_tokens} &nbsp; **Output tokens:** {eval_count}",
            "",
        ]
        if prompt_label.startswith("ga-"):
            lines += GRAPH_ACCURACY_CHECKLIST
        lines += [
            "**Response:**",
            "",
            resp_text,
            "",
            "**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _",
            "",
            "---",
            "",
        ]
        self._responses.write("\n".join(lines))
        self._responses.flush()

        self._rows_written += 1
        print(f"  -> {phase} | {row['tokens_per_second']} t/s | {row['wall_seconds']}s wall | saved ({self._rows_written} rows total)")

    def write_concurrent(self, result: dict[str, Any]) -> None:
        self._concurrent.write(json.dumps(result) + "\n")
        self._concurrent.flush()

    def close(self) -> None:
        self._jsonl.close()
        self._responses.close()
        self._concurrent.close()
        self._csv_handle.close()
        self._raw_jsonl.close()

    def finalize(self, runs: int) -> None:
        """Read saved JSONL, compute averages, write final markdown summary."""
        rows = []
        with self.jsonl_path.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    rows.append(json.loads(line))

        concurrent_results = []
        if self.concurrent_path.exists():
            with self.concurrent_path.open(encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        concurrent_results.append(json.loads(line))

        avg_rows = compute_averages(rows) if runs > 1 else []

        md_path = self.output_dir / f"ollama-benchmark-{self.timestamp}.md"
        lines = [
            "# Ollama Model Benchmark",
            "",
            f"Generated: {datetime.now().isoformat(timespec='seconds')}",
            "",
            "## Per-Run Results",
            "",
            "| Model | Prompt | Phase | Run | Think | Load sec | Wall sec | Tok/sec | Prompt tokens | Output tokens | Loaded GiB | VRAM GiB |",
            "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
        for row in rows:
            lines.append(
                f"| {row['model']} | {row.get('prompt', 'default')} | {row['phase']} | {row['run']} | "
                f"{'Y' if row.get('thinking') else 'N'} | "
                f"{row['load_seconds']} | {row['wall_seconds']} | {row['tokens_per_second']} | "
                f"{row['prompt_eval_count']} | {row['eval_count']} | "
                f"{row['loaded_size_gib']} | {row['loaded_vram_gib']} |"
            )

        if avg_rows:
            thinking_rows = [r for r in avg_rows if r.get("thinking")]
            standard_rows = [r for r in avg_rows if not r.get("thinking")]
            avg_header = [
                "| Model | Prompt | Phase | Avg Tok/sec | ±Stddev | Avg Wall sec | Avg Output tokens | Loaded GiB |",
                "|---|---|---:|---:|---:|---:|---:|---:|",
            ]

            def avg_row_line(row: dict[str, Any]) -> str:
                return (
                    f"| {row['model']} | {row['prompt']} | {row['phase']} | "
                    f"{row['tokens_per_second']} | {row.get('tokens_per_second_stddev', '-')} | "
                    f"{row['wall_seconds']} | {row.get('eval_count', '-')} | {row['loaded_size_gib']} |"
                )

            if standard_rows:
                lines += ["", "## Averaged Results — Standard Mode", ""] + avg_header
                for row in standard_rows:
                    lines.append(avg_row_line(row))
            if thinking_rows:
                lines += ["", "## Averaged Results — Thinking Mode", ""] + avg_header
                for row in thinking_rows:
                    lines.append(avg_row_line(row))

        if concurrent_results:
            lines += [
                "",
                "## Concurrent Request Results",
                "",
                "| Model | Prompt | Concurrent N | Total Wall sec | Avg Tok/sec | Min Tok/sec | Max Tok/sec |",
                "|---|---|---:|---:|---:|---:|---:|",
            ]
            for r in concurrent_results:
                lines.append(
                    f"| {r['model']} | {r['prompt']} | {r['concurrent_n']} | "
                    f"{r['total_wall_seconds']} | {r['avg_tok_per_sec']} | "
                    f"{r['min_tok_per_sec']} | {r['max_tok_per_sec']} |"
                )

        lines.extend([
            "",
            f"JSONL: `{self.jsonl_path.name}`",
            f"CSV: `{self.csv_path.name}`",
            f"Responses: `{self.responses_path.name}`",
            "",
        ])
        md_path.write_text("\n".join(lines), encoding="utf-8")

        print(f"\nWrote: {md_path}")
        print(f"Wrote: {self.csv_path}")
        print(f"Wrote: {self.jsonl_path}")
        print(f"Wrote: {self.responses_path}")
        print(f"\nTotal rows: {len(rows)}")
        if avg_rows:
            print(f"Averaged summary rows: {len(avg_rows)}")


def build_prompt_list(args: argparse.Namespace) -> list[tuple[str, str]]:
    if args.prompt_file:
        return [("custom", args.prompt_file.read_text(encoding="utf-8"))]

    prompts: list[tuple[str, str]] = []

    if args.prompt_set:
        selected = args.prompt_set
        if selected == ["all"]:
            selected = list(PROMPT_SETS.keys())
        unknown = [s for s in selected if s not in PROMPT_SETS]
        if unknown:
            raise SystemExit(f"Unknown prompt set(s): {unknown}. Available: {list(PROMPT_SETS.keys())}")
        for key in selected:
            prompts.extend(PROMPT_SETS[key])

    if args.prompt_size:
        sizes = args.prompt_size
        if sizes == ["all"]:
            sizes = list(CONTEXT_PROMPTS.keys())
        unknown = [s for s in sizes if s not in CONTEXT_PROMPTS]
        if unknown:
            raise SystemExit(f"Unknown prompt size(s): {unknown}. Available: {list(CONTEXT_PROMPTS.keys())}")
        for key in sizes:
            prompts.extend(CONTEXT_PROMPTS[key])

    if not prompts:
        return [("default", DEFAULT_PROMPT)]

    return prompts


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Benchmark one or more Ollama models.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Overnight run example:
  python3 ollama_model_benchmark.py \\
    qwen3:8b qwen3:14b deepseek-r1:14b qwen2.5-coder:32b qwen3.6:35b \\
    --host http://evo-x2.local:11434 \\
    --prompt-set all --prompt-size all --runs 3 --thinking --concurrent 2
""",
    )
    parser.add_argument("models", nargs="+", help="Ollama model names")
    parser.add_argument("--host", default="http://localhost:11434", help="Ollama API base URL")
    parser.add_argument("--prompt-file", type=Path, help="Single prompt file (overrides all other prompt options)")
    parser.add_argument(
        "--prompt-set", nargs="+", metavar="SET",
        help=f"Task prompt categories, or 'all'. Available: {list(PROMPT_SETS.keys())}",
    )
    parser.add_argument(
        "--prompt-size", nargs="+", metavar="SIZE",
        help=f"Context size variants, or 'all'. Available: {list(CONTEXT_PROMPTS.keys())}",
    )
    parser.add_argument(
        "--runs", type=int, default=1,
        help="Number of times to run each prompt per model (averaged in summary). Default: 1",
    )
    parser.add_argument(
        "--thinking", action="store_true",
        help="Prepend /think to all prompts (for models that support thinking mode e.g. Qwen3)",
    )
    parser.add_argument(
        "--concurrent", type=int, default=0, metavar="N",
        help="Also run a concurrent load test with N simultaneous requests per model (default: skip)",
    )
    parser.add_argument("--keep-alive", default="5m", help="How long Ollama keeps each model loaded")
    parser.add_argument(
        "--output-dir", type=Path,
        default=Path.home() / "benchmark-results",
        help="Directory for output reports (default: ~/benchmark-results)",
    )
    parser.add_argument("--skip-cold", action="store_true", help="Skip cold-start runs")
    parser.add_argument("--skip-warm", action="store_true", help="Skip warm runs")
    args = parser.parse_args()

    prompts = build_prompt_list(args)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    writer = StreamingWriter(args.output_dir, timestamp)

    print(f"Output dir: {args.output_dir}")
    print(f"Models: {args.models}")
    print(f"Prompts: {len(prompts)} | Runs: {args.runs} | Thinking: {args.thinking}")
    print(f"Results streaming to: {writer.jsonl_path.name}\n")

    total_rows = 0
    try:
        for model in args.models:
            for label, base_prompt in prompts:
                prompt = f"/think\n{base_prompt}" if args.thinking else base_prompt

                for run_num in range(1, args.runs + 1):
                    run_label = f"run {run_num}/{args.runs}"
                    print(f"Benchmarking {model} / {label} / {run_label} {'[thinking]' if args.thinking else ''}...")

                    if not args.skip_cold:
                        stop_model(args.host, model)
                        cold = generate_once(args.host, model, prompt, args.keep_alive)
                        runtime = get_model_runtime(args.host, model)
                        row = flatten_result(model, "cold", cold, runtime, label, run_num, args.thinking)
                        writer.write_result(row, model, label, base_prompt, "cold", run_num, args.thinking, cold, runtime)
                        total_rows += 1

                    if not args.skip_warm:
                        warm = generate_once(args.host, model, prompt, args.keep_alive)
                        runtime = get_model_runtime(args.host, model)
                        row = flatten_result(model, "warm", warm, runtime, label, run_num, args.thinking)
                        writer.write_result(row, model, label, base_prompt, "warm", run_num, args.thinking, warm, runtime)
                        total_rows += 1

                if args.concurrent > 0:
                    result = run_concurrent_test(args.host, model, prompt, args.keep_alive, args.concurrent)
                    result["model"] = model
                    result["prompt"] = label
                    writer.write_concurrent(result)

    except KeyboardInterrupt:
        print(f"\nInterrupted — {total_rows} rows already saved to {writer.jsonl_path}")
    finally:
        writer.close()

    if total_rows == 0:
        print("No benchmark rows were generated.", file=sys.stderr)
        return 1

    writer.finalize(args.runs)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
