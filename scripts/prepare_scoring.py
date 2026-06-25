#!/usr/bin/env python3
"""Convert a responses markdown file + metrics JSONL into a scorable raw JSONL.

The streaming benchmark writes response text to an ollama-responses-*.md file
and timing metrics to ollama-benchmark-*.jsonl. The opus_scorer.py needs both
together in a single ollama-raw-*.jsonl file.

This script merges them for benchmark runs completed before the benchmark was
updated to write ollama-raw-*.jsonl automatically.

Usage:
  python3 prepare_scoring.py --responses ollama-responses-*.md \\
                              --metrics   ollama-benchmark-*.jsonl \\
                              --output    ollama-raw-for-scoring.jsonl

  # Omit --metrics to produce entries with timing estimated from the markdown
  python3 prepare_scoring.py --responses ollama-responses-*.md
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


# Prompt texts from the benchmark script — keyed by prompt label.
# These are the exact texts sent to the models so Opus can score them in context.
PROMPT_TEXTS: dict[str, str] = {
    "clf-intent": (
        "A user says: 'I can't log into my Outlook and my Teams keeps crashing. "
        "Also our shared drive is not mounting on my Mac.' "
        "Categorize each issue into exactly one of: Account, Application, Network, Hardware. "
        "Return a JSON array: [{\"issue\": \"...\", \"category\": \"...\"}]. No explanation."
    ),
    "runbook-pw-reset": (
        "Write a 5-step runbook for an IT help desk technician to reset a user's Azure AD password "
        "and force MFA re-enrollment. The technician has read-only Graph API access and must escalate "
        "to a licensed admin for the actual reset. Include verification steps."
    ),
    "ps-inactive-users": (
        "Write a PowerShell script using Microsoft.Graph that lists all users in a tenant "
        "who have not signed in for 90 or more days. Use Get-MgUser with the SignInActivity property. "
        "Output: UPN, DisplayName, LastSignInDateTime. Export to CSV at C:\\Reports\\InactiveUsers.csv. "
        "Handle pagination — the Graph API may return results across multiple pages."
    ),
    "chat-explain-mfa": (
        "Explain to a non-technical small business owner why their company needs multi-factor "
        "authentication. Use plain language, no jargon. Keep it under 150 words."
    ),
    "ps-bitlocker-report": (
        "Write a PowerShell script that queries Microsoft Intune via the Graph API to report on "
        "BitLocker encryption status for all Windows devices in a tenant. "
        "Use Get-MgDeviceManagementManagedDevice. For each device, retrieve: DeviceName, "
        "SerialNumber, OperatingSystem, ComplianceState, and EncryptionState. "
        "Export to CSV. Handle devices that don't report encryption status gracefully."
    ),
    "ga-pagination": (
        "Write a PowerShell function using Microsoft.Graph that retrieves ALL Intune-managed "
        "devices in a tenant. The Graph API returns a maximum of 1000 records per page with an "
        "@odata.nextLink property in the response. Your function must follow nextLink until "
        "exhausted. Use Get-MgDeviceManagementManagedDevice with -All, or implement manual "
        "pagination via Invoke-MgGraphRequest. The function must handle API errors (401, 429, 503) "
        "with appropriate error messages. Output total device count to console and return the device "
        "collection to the pipeline."
    ),
    "ga-group-membership": (
        "Write a PowerShell script using Microsoft.Graph that adds a list of users (provided as an "
        "array of UPNs) to an Azure AD security group. Use New-MgGroupMember. The script must: "
        "1) skip users already in the group without erroring, "
        "2) handle users that don't exist in the tenant, "
        "3) log each action (added / already member / not found) to a transcript file, "
        "4) accept GroupId and UPNs as parameters. "
        "Declare the minimum required Graph permission scope in a comment."
    ),
    "context-migration": (
        "You are reviewing a PowerShell module that uses the deprecated AzureAD module. "
        "The module has these functions:\n\n"
        "```powershell\n"
        "function Connect-TenantServices {\n"
        "    Connect-AzureAD\n"
        "    $global:GraphToken = (Get-AzureADMSApplication -ObjectId $AppId).AppRoles\n"
        "}\n\n"
        "function Get-InactiveUsers {\n"
        "    Get-AzureADUser -All $true | Where-Object { $_.AccountEnabled -eq $true } | "
        "ForEach-Object {\n"
        "        $lastSignIn = $_.ExtensionProperty['signInSessionsValidFromDateTime']\n"
        "        [pscustomobject]@{ UPN = $_.UserPrincipalName; LastSignIn = $lastSignIn }\n"
        "    }\n"
        "}\n\n"
        "function Add-UserToGroup {\n"
        "    param([string]$UserId, [string]$GroupId)\n"
        "    Add-AzureADGroupMember -ObjectId $GroupId -RefObjectId $UserId\n"
        "}\n\n"
        "function Remove-UserFromGroup {\n"
        "    param([string]$UserId, [string]$GroupId)\n"
        "    Remove-AzureADGroupMember -ObjectId $GroupId -MemberId $UserId\n"
        "}\n\n"
        "function Get-UserLicenses {\n"
        "    param([string]$UPN)\n"
        "    $user = Get-AzureADUser -ObjectId $UPN\n"
        "    Get-AzureADUserLicenseDetail -ObjectId $user.ObjectId\n"
        "}\n"
        "```\n\n"
        "Rewrite using the Microsoft.Graph PowerShell SDK instead of raw REST calls. "
        "Add proper error handling, remove the global token variable, and add comment-based help to each function. "
        "Output only the rewritten module."
    ),
}


def parse_responses_md(path: Path) -> list[dict]:
    """Parse an ollama-responses-*.md file into a list of raw entries."""
    text = path.read_text(encoding="utf-8")

    # Split on the section separator; each section starts with '## '
    sections = re.split(r"\n---\n", text)

    entries = []
    for section in sections:
        section = section.strip()
        if not section.startswith("## "):
            continue

        # Parse header: ## model | prompt | phase | run N | thinking: YES/NO
        header_match = re.match(
            r"^## (.+?) \| (.+?) \| (cold|warm) \| run (\d+) \| thinking: (YES|NO)",
            section,
        )
        if not header_match:
            continue

        model = header_match.group(1).strip()
        prompt_label = header_match.group(2).strip()
        phase = header_match.group(3).strip()
        run = int(header_match.group(4))
        thinking = header_match.group(5) == "YES"

        # Parse stats line: **Tok/sec:** X  **Wall sec:** Y  **Prompt tokens:** Z  **Output tokens:** N
        stats_match = re.search(
            r"\*\*Tok/sec:\*\* ([\d.]+).*?\*\*Wall sec:\*\* ([\d.]+).*?"
            r"\*\*Prompt tokens:\*\* (\d+).*?\*\*Output tokens:\*\* (\d+)",
            section,
        )
        tok_per_sec = float(stats_match.group(1)) if stats_match else 0.0
        wall_seconds = float(stats_match.group(2)) if stats_match else 0.0
        prompt_tokens = int(stats_match.group(3)) if stats_match else 0
        eval_count = int(stats_match.group(4)) if stats_match else 0

        # Extract response text (between **Response:** and **Score:**)
        resp_match = re.search(
            r"\*\*Response:\*\*\n\n(.*?)\n\n\*\*Score:\*\*",
            section,
            re.DOTALL,
        )
        response_text = resp_match.group(1).strip() if resp_match else ""

        eval_duration_ns = int((eval_count / tok_per_sec) * 1e9) if tok_per_sec else 0

        entries.append({
            "model": model,
            "prompt": prompt_label,
            "prompt_text": PROMPT_TEXTS.get(prompt_label, ""),
            "phase": phase,
            "run": run,
            "thinking": thinking,
            "response": {
                "response": response_text,
                "eval_count": eval_count,
                "eval_duration": eval_duration_ns,
                "prompt_eval_count": prompt_tokens,
                "wall_seconds": wall_seconds,
            },
        })

    return entries


def merge_metrics(entries: list[dict], metrics_path: Path) -> None:
    """Patch entries with exact timing from the metrics JSONL if available."""
    metrics_index: dict[tuple, dict] = {}
    with metrics_path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
                key = (row.get("model"), row.get("prompt"), row.get("phase"), row.get("run"))
                metrics_index[key] = row
            except json.JSONDecodeError:
                pass

    for entry in entries:
        key = (entry["model"], entry["prompt"], entry["phase"], entry["run"])
        row = metrics_index.get(key)
        if row:
            entry["response"]["eval_count"] = int(row.get("eval_count") or entry["response"]["eval_count"])
            eval_secs = float(row.get("eval_seconds") or 0)
            if eval_secs:
                entry["response"]["eval_duration"] = int(eval_secs * 1e9)
            entry["response"]["wall_seconds"] = float(row.get("wall_seconds") or entry["response"]["wall_seconds"])


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert responses markdown to scorable raw JSONL")
    parser.add_argument("--responses", type=Path, required=True, help="ollama-responses-*.md file")
    parser.add_argument("--metrics", type=Path, help="ollama-benchmark-*.jsonl (optional, for exact timing)")
    parser.add_argument("--output", type=Path, help="Output path (default: ollama-raw-<stem>.jsonl)")
    args = parser.parse_args()

    if not args.responses.exists():
        print(f"ERROR: responses file not found: {args.responses}", file=sys.stderr)
        return 1

    print(f"Parsing {args.responses}...")
    entries = parse_responses_md(args.responses)
    print(f"  Found {len(entries)} entries")

    if args.metrics:
        if not args.metrics.exists():
            print(f"WARNING: metrics file not found: {args.metrics}, skipping merge", file=sys.stderr)
        else:
            print(f"Merging timing from {args.metrics}...")
            merge_metrics(entries, args.metrics)

    missing_prompts = {e["prompt"] for e in entries if not e["prompt_text"]}
    if missing_prompts:
        print(f"WARNING: no prompt text found for labels: {missing_prompts}", file=sys.stderr)
        print("  Scoring will still run but Opus won't have the original prompt for context.", file=sys.stderr)

    empty_responses = [e for e in entries if not e["response"]["response"]]
    if empty_responses:
        print(f"WARNING: {len(empty_responses)} entries have empty response text — they will be skipped by the scorer.")

    output = args.output or args.responses.parent / f"ollama-raw-{args.responses.stem.replace('ollama-responses-', '')}.jsonl"
    with output.open("w", encoding="utf-8") as fh:
        for entry in entries:
            fh.write(json.dumps(entry) + "\n")

    print(f"Wrote {len(entries)} entries to {output}")
    print(f"\nNext step:")
    print(f"  python3 opus_scorer.py {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
