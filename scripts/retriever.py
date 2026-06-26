#!/usr/bin/env python3
"""Retriever — query Qdrant for relevant Graph API context chunks.

Embeds a query using nomic-embed-text, searches the Qdrant collection,
and returns the top-k chunks as formatted context for prompt injection.

Can be used standalone for testing, or imported by rag_benchmark.py.

Usage:
  # Test a query directly:
  python3 retriever.py --query "Get-MgUser sign in activity last sign in"

  # Adjust result count:
  python3 retriever.py --query "MFA authentication method remove" --top-k 5

  # Output raw JSON for piping:
  python3 retriever.py --query "group membership add user" --json
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


EMBED_MODEL = "nomic-embed-text"
DEFAULT_COLLECTION = "graph-ps"
MAX_EMBED_CHARS = 6000
DEFAULT_TOP_K = 3


def ollama_embed(base_url: str, text: str) -> list[float]:
    payload = {"model": EMBED_MODEL, "prompt": text[:MAX_EMBED_CHARS]}
    body = json.dumps(payload).encode("utf-8")
    req = Request(
        f"{base_url.rstrip('/')}/api/embeddings",
        data=body,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data["embedding"]
    except HTTPError as exc:
        raise RuntimeError(f"Ollama embed error {exc.code}") from exc
    except URLError as exc:
        raise RuntimeError(f"Ollama unreachable: {exc.reason}") from exc


def qdrant_search(
    base_url: str,
    collection: str,
    vector: list[float],
    top_k: int,
    tier: int | None = None,
) -> list[dict[str, Any]]:
    payload: dict[str, Any] = {
        "vector": vector,
        "limit": top_k,
        "with_payload": True,
    }
    if tier is not None:
        payload["filter"] = {"must": [{"key": "tier", "match": {"value": tier}}]}
    body = json.dumps(payload).encode("utf-8")
    req = Request(
        f"{base_url.rstrip('/')}/collections/{collection}/points/search",
        data=body,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("result", [])
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Qdrant search error {exc.code}: {detail}") from exc
    except URLError as exc:
        raise RuntimeError(f"Qdrant unreachable: {exc.reason}") from exc


def retrieve(
    query: str,
    ollama_url: str = "http://localhost:11434",
    qdrant_url: str = "http://localhost:6333",
    collection: str = DEFAULT_COLLECTION,
    top_k: int = DEFAULT_TOP_K,
    tier: int = 1,
) -> list[dict[str, Any]]:
    """Embed query and return top-k matching chunks with scores.

    tier=1 (default): compact summary chunks — syntax, required params, permissions.
    tier=2: full reference chunks — pulled on Auditor/Scorer escalation signal.

    Each result dict has: score, cmdlet, chunk_type, tier, content, source_url
    """
    vector = ollama_embed(ollama_url, query)
    results = qdrant_search(qdrant_url, collection, vector, top_k, tier=tier)

    chunks = []
    for r in results:
        payload = r.get("payload", {})
        chunks.append({
            "score": round(r.get("score", 0.0), 4),
            "cmdlet": payload.get("cmdlet", ""),
            "chunk_type": payload.get("chunk_type", ""),
            "tier": payload.get("tier", 2),
            "content": payload.get("content", ""),
            "source_url": payload.get("source_url", ""),
        })
    return chunks


def format_context(chunks: list[dict[str, Any]]) -> str:
    """Format retrieved chunks as a context block for prompt injection."""
    if not chunks:
        return ""

    lines = [
        "## Retrieved Microsoft Graph PowerShell Reference",
        "",
        "The following documentation was retrieved to help answer this request.",
        "Use it to ensure correct cmdlet names, parameter names, and property names.",
        "",
    ]
    for i, chunk in enumerate(chunks, 1):
        lines += [
            f"### Source {i}: {chunk['cmdlet']} ({chunk['chunk_type']}) — score {chunk['score']}",
            "",
            chunk["content"],
            "",
        ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Retriever — search Qdrant for relevant Graph API context.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 retriever.py --query "Get-MgUser sign in activity last sign in"
  python3 retriever.py --query "remove MFA authentication method" --top-k 5
  python3 retriever.py --query "add user to group" --json
""",
    )
    parser.add_argument("--query", required=True, help="Natural language query")
    parser.add_argument("--ollama", default="http://localhost:11434", metavar="URL")
    parser.add_argument("--qdrant", default="http://localhost:6333", metavar="URL")
    parser.add_argument("--collection", default=DEFAULT_COLLECTION)
    parser.add_argument("--top-k", type=int, default=DEFAULT_TOP_K)
    parser.add_argument("--tier", type=int, default=1, choices=[1, 2], help="1=summary (default), 2=full reference")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Output raw JSON instead of formatted context")
    args = parser.parse_args()

    try:
        chunks = retrieve(
            query=args.query,
            ollama_url=args.ollama,
            qdrant_url=args.qdrant,
            collection=args.collection,
            top_k=args.top_k,
            tier=args.tier,
        )
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if not chunks:
        print("No results found.", file=sys.stderr)
        return 1

    if args.as_json:
        print(json.dumps(chunks, indent=2))
    else:
        print(f"Query : {args.query}")
        print(f"Top-{args.top_k} results from '{args.collection}':\n")
        for i, chunk in enumerate(chunks, 1):
            print(f"  [{i}] score={chunk['score']}  {chunk['cmdlet']} / {chunk['chunk_type']}")
            print(f"       {chunk['source_url']}")
        print()
        print(format_context(chunks))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
