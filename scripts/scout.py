#!/usr/bin/env python3
"""Scout — Microsoft Graph PowerShell docs crawler.

Fetches cmdlet reference pages from learn.microsoft.com and outputs
clean chunks as JSONL for the Indexer to embed and store.

Targets the specific cmdlets behind the 3 failing benchmark tasks:
  ga-deprecated-module  (best: 4/10) — wrong LastSignInDate property name
  ga-error-handling     (best: 5/10) — hallucinated MFA cmdlet names
  ps-graph-stale-users  (best: 4/10) — wrong LastSignInDate property name

Output format (one JSON object per line):
  {
    "id": "get-mguser-reference",
    "cmdlet": "Get-MgUser",
    "module": "microsoft.graph.users",
    "chunk_type": "reference|examples|permissions",
    "content": "...",
    "source_url": "https://learn.microsoft.com/..."
  }

Usage:
  python3 scout.py
  python3 scout.py --output-dir ~/rag-corpus
  python3 scout.py --output-dir ~/rag-corpus --force
"""

from __future__ import annotations

import argparse
import json
import time
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


BASE_URL = "https://learn.microsoft.com/en-us/powershell/module"
VIEW = "graph-powershell-1.0"

# Cmdlets needed to fix the failing tasks.
# Extend this list to grow the corpus over time.
TARGET_CMDLETS: list[tuple[str, str]] = [
    # ga-deprecated-module / ps-graph-stale-users
    # Root cause: models use LastSignInDate instead of SignInActivity.LastSignInDateTime
    ("Get-MgUser", "microsoft.graph.users"),
    ("Update-MgUser", "microsoft.graph.users"),
    # ga-error-handling
    # Root cause: hallucinated MFA cmdlet names, missing 404/403 differentiation
    # Note: Remove-MgUserAuthenticationMethod is not a real cmdlet — models hallucinate it.
    # Real cmdlets are type-specific. Index them so models learn the correct surface area.
    ("Get-MgUserAuthenticationMethod", "microsoft.graph.identity.signins"),
    ("Remove-MgUserAuthenticationEmailMethod", "microsoft.graph.identity.signins"),
    ("Remove-MgUserAuthenticationMicrosoftAuthenticatorMethod", "microsoft.graph.identity.signins"),
    ("Remove-MgUserAuthenticationPhoneMethod", "microsoft.graph.identity.signins"),
    # ga-param-names — New-MgGroupMemberByRef is the current SDK cmdlet for adding members
    # Correct params: -GroupId and -DirectoryObjectId (not -MemberId or -UserId)
    ("New-MgGroupMemberByRef", "microsoft.graph.groups"),
    ("Get-MgGroupMember", "microsoft.graph.groups"),
    # ga-pagination — device management with nextLink handling
    ("Get-MgDeviceManagementManagedDevice", "microsoft.graph.devicemanagement"),
    # Core auth cmdlets — grounding for Connect-MgGraph scope declarations
    ("Connect-MgGraph", "microsoft.graph.authentication"),
    ("Invoke-MgGraphRequest", "microsoft.graph.authentication"),
]


class SectionParser(HTMLParser):
    """Extract text sections from MS docs HTML by heading boundaries."""

    SKIP_TAGS = {"script", "style", "nav", "header", "footer", "aside"}
    HEADING_TAGS = {"h1", "h2", "h3"}

    def __init__(self) -> None:
        super().__init__()
        self._skip_tag: str | None = None
        self._in_heading = False
        self._current_heading = "Overview"
        self._heading_buf: list[str] = []
        self._text_buf: list[str] = []
        self.sections: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag in self.SKIP_TAGS:
            self._skip_tag = tag
        elif tag in self.HEADING_TAGS and not self._skip_tag:
            self._flush()
            self._in_heading = True
            self._heading_buf = []

    def handle_endtag(self, tag: str) -> None:
        if tag == self._skip_tag:
            self._skip_tag = None
        elif tag in self.HEADING_TAGS and self._in_heading:
            self._in_heading = False
            heading = " ".join(self._heading_buf).strip()
            if heading:
                self._current_heading = heading

    def handle_data(self, data: str) -> None:
        if self._skip_tag:
            return
        text = data.strip()
        if not text:
            return
        if self._in_heading:
            self._heading_buf.append(text)
        else:
            self._text_buf.append(text)

    def _flush(self) -> None:
        text = " ".join(self._text_buf).strip()
        if len(text) > 30:
            self.sections.append((self._current_heading, text))
        self._text_buf = []

    def get_sections(self) -> list[tuple[str, str]]:
        self._flush()
        return self.sections


def fetch_page(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; scout/1.0; ai-runtime-starter RAG crawler)",
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "en-US,en;q=0.9",
    }
    req = Request(url, headers=headers)
    try:
        with urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except HTTPError as exc:
        raise RuntimeError(f"HTTP {exc.code}") from exc
    except URLError as exc:
        raise RuntimeError(f"Network error: {exc.reason}") from exc


def classify_section(heading: str) -> str:
    h = heading.lower()
    if any(k in h for k in ("synopsis", "description", "overview", "syntax")):
        return "reference"
    if "parameter" in h:
        return "reference"
    if "example" in h:
        return "examples"
    if any(k in h for k in ("permission", "scope", "privilege", "role")):
        return "permissions"
    return "reference"


def build_chunks(
    cmdlet: str,
    module: str,
    sections: list[tuple[str, str]],
    source_url: str,
) -> list[dict]:
    reference: list[str] = []
    examples: list[str] = []
    permissions: list[str] = []

    for heading, text in sections:
        bucket = classify_section(heading)
        content = f"### {heading}\n{text}"
        if bucket == "examples":
            examples.append(content)
        elif bucket == "permissions":
            permissions.append(content)
        else:
            reference.append(content)

    chunks = []
    base = cmdlet.lower()

    if reference:
        chunks.append({
            "id": f"{base}-reference",
            "cmdlet": cmdlet,
            "module": module,
            "chunk_type": "reference",
            "content": f"# {cmdlet} ({module})\n\n" + "\n\n".join(reference),
            "source_url": source_url,
        })
    if examples:
        chunks.append({
            "id": f"{base}-examples",
            "cmdlet": cmdlet,
            "module": module,
            "chunk_type": "examples",
            "content": f"# {cmdlet} — Examples\n\n" + "\n\n".join(examples),
            "source_url": source_url,
        })
    if permissions:
        chunks.append({
            "id": f"{base}-permissions",
            "cmdlet": cmdlet,
            "module": module,
            "chunk_type": "permissions",
            "content": f"# {cmdlet} — Required Permissions\n\n" + "\n\n".join(permissions),
            "source_url": source_url,
        })

    return chunks


def crawl_cmdlet(cmdlet: str, module: str) -> tuple[list[dict], str]:
    url = f"{BASE_URL}/{module}/{cmdlet.lower()}?view={VIEW}"
    html = fetch_page(url)
    parser = SectionParser()
    parser.feed(html)
    sections = parser.get_sections()
    chunks = build_chunks(cmdlet, module, sections, url)
    return chunks, url


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scout — crawl MS Graph PowerShell docs for RAG grounding.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 scout.py
  python3 scout.py --output-dir ~/rag-corpus
  python3 scout.py --force   # ignore checkpoint, re-crawl everything
""",
    )
    parser.add_argument("--output-dir", type=Path, default=Path.home() / "rag-corpus")
    parser.add_argument("--delay", type=float, default=1.5, help="Seconds between requests (default: 1.5)")
    parser.add_argument("--force", action="store_true", help="Re-crawl even if checkpoint exists")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_path = args.output_dir / f"graph-ps-corpus-{timestamp}.jsonl"
    checkpoint_path = args.output_dir / "scout.checkpoint.json"

    crawled: set[str] = set()
    if checkpoint_path.exists() and not args.force:
        try:
            crawled = set(json.loads(checkpoint_path.read_text())["crawled"])
            print(f"Resuming from checkpoint: {len(crawled)} cmdlets already done.")
        except (json.JSONDecodeError, KeyError):
            pass
    elif checkpoint_path.exists() and args.force:
        checkpoint_path.unlink()
        print("--force: ignoring checkpoint, starting fresh.")

    print("Scout — MS Graph PowerShell Docs Crawler")
    print(f"  Targets : {len(TARGET_CMDLETS)} cmdlets")
    print(f"  Output  : {output_path}")
    print(f"  Delay   : {args.delay}s per request\n")

    total_chunks = 0
    errors: list[str] = []
    out_fh = output_path.open("w", encoding="utf-8")

    try:
        for i, (cmdlet, module) in enumerate(TARGET_CMDLETS, 1):
            if cmdlet in crawled:
                print(f"  [{i}/{len(TARGET_CMDLETS)}] {cmdlet} — skipped (checkpoint)")
                continue

            print(f"  [{i}/{len(TARGET_CMDLETS)}] {cmdlet}...")
            try:
                chunks, url = crawl_cmdlet(cmdlet, module)
                for chunk in chunks:
                    out_fh.write(json.dumps(chunk) + "\n")
                out_fh.flush()
                total_chunks += len(chunks)
                crawled.add(cmdlet)
                checkpoint_path.write_text(json.dumps({"crawled": list(crawled)}))
                print(f"    {len(chunks)} chunks | {url}")
            except RuntimeError as exc:
                print(f"    ERROR: {exc} — skipping")
                errors.append(f"{cmdlet}: {exc}")

            if i < len(TARGET_CMDLETS):
                time.sleep(args.delay)

    except KeyboardInterrupt:
        print(f"\nInterrupted — {total_chunks} chunks saved to {output_path}")
    finally:
        out_fh.close()

    print(f"\nDone. {total_chunks} chunks | {len(errors)} errors")
    if errors:
        print("Errors:")
        for e in errors:
            print(f"  {e}")

    if total_chunks > 0 and len(crawled) == len(TARGET_CMDLETS):
        checkpoint_path.unlink(missing_ok=True)

    print(f"\nNext step:")
    print(f"  python3 indexer.py {output_path}")

    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
