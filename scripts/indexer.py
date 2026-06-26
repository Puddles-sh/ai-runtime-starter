#!/usr/bin/env python3
"""Indexer — embed Scout corpus chunks and store in Qdrant.

Reads the JSONL produced by scout.py, embeds each chunk using
nomic-embed-text via Ollama, and upserts into a Qdrant collection.

Qdrant runs in Docker — start it before indexing:
  docker run -d --name qdrant --restart always \
    -p 6333:6333 -p 6334:6334 \
    -v qdrant_storage:/qdrant/storage \
    qdrant/qdrant

Usage:
  python3 indexer.py ~/rag-corpus/graph-ps-corpus-TIMESTAMP.jsonl
  python3 indexer.py ~/rag-corpus/graph-ps-corpus-TIMESTAMP.jsonl --force
  python3 indexer.py ~/rag-corpus/graph-ps-corpus-TIMESTAMP.jsonl \\
    --ollama http://localhost:11434 \\
    --qdrant http://localhost:6333 \\
    --collection graph-ps

Dependencies:
  pip install qdrant-client
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


EMBED_MODEL = "nomic-embed-text"
DEFAULT_COLLECTION = "graph-ps"
VECTOR_SIZE = 768  # nomic-embed-text output dimension


MAX_EMBED_CHARS = 6000  # nomic-embed-text context limit ~8192 tokens; 6000 chars is safe


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


def qdrant_request(
    base_url: str,
    method: str,
    path: str,
    payload: dict[str, Any] | None = None,
) -> dict[str, Any]:
    body = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = Request(
        f"{base_url.rstrip('/')}{path}",
        data=body,
        method=method,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Qdrant {method} {path} → {exc.code}: {detail}") from exc
    except URLError as exc:
        raise RuntimeError(f"Qdrant unreachable: {exc.reason}") from exc


def ensure_collection(qdrant_url: str, collection: str, force: bool) -> None:
    try:
        result = qdrant_request(qdrant_url, "GET", f"/collections/{collection}")
        exists = result.get("result") is not None
    except RuntimeError:
        exists = False

    if exists and force:
        print(f"  --force: deleting existing collection '{collection}'...")
        qdrant_request(qdrant_url, "DELETE", f"/collections/{collection}")
        exists = False

    if not exists:
        print(f"  Creating collection '{collection}' (dim={VECTOR_SIZE}, cosine)...")
        qdrant_request(qdrant_url, "PUT", f"/collections/{collection}", {
            "vectors": {
                "size": VECTOR_SIZE,
                "distance": "Cosine",
            }
        })
    else:
        print(f"  Collection '{collection}' exists — upserting into it.")


def upsert_point(
    qdrant_url: str,
    collection: str,
    point_id: int,
    vector: list[float],
    payload: dict[str, Any],
) -> None:
    qdrant_request(qdrant_url, "PUT", f"/collections/{collection}/points", {
        "points": [{
            "id": point_id,
            "vector": vector,
            "payload": payload,
        }]
    })


def stable_id(chunk_id: str) -> int:
    """Deterministic int ID from chunk string id — Qdrant requires int or UUID."""
    return abs(hash(chunk_id)) % (2 ** 53)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Indexer — embed Scout chunks into Qdrant.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Start Qdrant first:
  docker run -d --name qdrant --restart always \\
    -p 6333:6333 -p 6334:6334 \\
    -v qdrant_storage:/qdrant/storage \\
    qdrant/qdrant

Then index:
  python3 indexer.py ~/rag-corpus/graph-ps-corpus-TIMESTAMP.jsonl
""",
    )
    parser.add_argument("input", type=Path, help="JSONL corpus file from scout.py")
    parser.add_argument("--ollama", default="http://localhost:11434", metavar="URL")
    parser.add_argument("--qdrant", default="http://localhost:6333", metavar="URL")
    parser.add_argument("--collection", default=DEFAULT_COLLECTION)
    parser.add_argument("--force", action="store_true", help="Drop and recreate collection before indexing")
    parser.add_argument("--delay", type=float, default=0.1, help="Seconds between embed calls (default: 0.1)")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"ERROR: file not found: {args.input}", file=sys.stderr)
        return 1

    chunks = []
    with args.input.open(encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                chunks.append(json.loads(line))
            except json.JSONDecodeError as exc:
                print(f"WARNING: skipping malformed line {lineno}: {exc}", file=sys.stderr)

    if not chunks:
        print("ERROR: no chunks found in input file.", file=sys.stderr)
        return 1

    print(f"Indexer — MS Graph PowerShell RAG Corpus")
    print(f"  Input     : {args.input} ({len(chunks)} chunks)")
    print(f"  Embed     : {EMBED_MODEL} @ {args.ollama}")
    print(f"  Qdrant    : {args.qdrant}")
    print(f"  Collection: {args.collection}\n")

    ensure_collection(args.qdrant, args.collection, args.force)
    print()

    errors = 0
    for i, chunk in enumerate(chunks, 1):
        chunk_id = chunk.get("id", f"chunk-{i}")
        cmdlet = chunk.get("cmdlet", "unknown")
        chunk_type = chunk.get("chunk_type", "unknown")
        content = chunk.get("content", "")

        print(f"  [{i}/{len(chunks)}] {cmdlet} / {chunk_type}...", end=" ", flush=True)

        try:
            vector = ollama_embed(args.ollama, content)
            point_id = stable_id(chunk_id)
            upsert_point(args.qdrant, args.collection, point_id, vector, {
                "id": chunk_id,
                "cmdlet": cmdlet,
                "module": chunk.get("module", ""),
                "chunk_type": chunk_type,
                "tier": chunk.get("tier", 2),
                "content": content,
                "source_url": chunk.get("source_url", ""),
            })
            print(f"OK (id={point_id})")
        except RuntimeError as exc:
            print(f"ERROR: {exc}")
            errors += 1

        if i < len(chunks):
            time.sleep(args.delay)

    print(f"\nDone. {len(chunks) - errors}/{len(chunks)} chunks indexed into '{args.collection}'.")
    if errors:
        print(f"  {errors} errors — re-run without --force to retry failed chunks.")

    print(f"\nNext step:")
    print(f"  python3 retriever.py --query 'Get-MgUser sign in activity' --collection {args.collection}")

    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
