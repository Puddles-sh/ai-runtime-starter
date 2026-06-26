# Scripts

Runtime scripts for benchmarking, RAG corpus management, and model evaluation.

---

## Corpus Pipeline

### `scout.py`
Crawls MS Graph PowerShell docs from learn.microsoft.com and outputs clean JSONL chunks.
Produces Tier 1 (compact summary) and Tier 2 (full reference) chunks per cmdlet.

```bash
python3 scripts/scout.py --output-dir ~/rag-corpus
python3 scripts/scout.py --output-dir ~/rag-corpus --force  # re-crawl everything
```

### `curate.py`
Hand-authored corpus entries for confirmed model failure modes. Use when scraped docs
exist but models still hallucinate — typically property access patterns and REST URI paths
that training weights override.

```bash
python3 scripts/curate.py --output-dir ~/rag-corpus
```

### `indexer.py`
Embeds corpus chunks with nomic-embed-text and upserts into Qdrant. Stores `tier` field
in payload so retriever can filter by tier. Safe to re-run — upserts by stable ID.

```bash
python3 scripts/indexer.py ~/rag-corpus/curated-corpus-<timestamp>.jsonl
python3 scripts/indexer.py ~/rag-corpus/graph-ps-corpus-<timestamp>.jsonl
# Latest file shortcut:
python3 scripts/indexer.py $(ls -t ~/rag-corpus/graph-ps-corpus-*.jsonl | head -1)
```

### `retriever.py`
Queries Qdrant for relevant chunks. Defaults to Tier 1 (compact). Use `--tier 2` for
full reference or when Tier 1 returns no results.

```bash
python3 scripts/retriever.py --query "Get-MgUser sign in activity"
python3 scripts/retriever.py --query "MFA authentication method remove" --tier 2 --top-k 5
python3 scripts/retriever.py --query "add user to group" --json
```

---

## Benchmarking

### `ollama_model_benchmark.py`
Full prompt suite benchmark — no RAG. Measures speed, quality, and cold/warm behavior
across all task types. Uses per-task context sizing (`TASK_CONTEXT_SIZES`).

```bash
# Drift measurement — 3 cold runs, no warm
python3 scripts/ollama_model_benchmark.py gemma4:26b qwen3.6:35b \
  --prompt-set all --prompt-size all --runs 3 --skip-warm

# Production simulation — 1 cold + 1 warm
python3 scripts/ollama_model_benchmark.py gemma4:26b qwen3.6:35b \
  --prompt-set all --prompt-size all
```

### `rag_benchmark.py`
Same 3 failing tasks as the shootout but with Qdrant retrieval injected. Use to measure
RAG delta vs baseline and validate curated corpus entries.

```bash
python3 scripts/rag_benchmark.py --models gemma4:26b qwen3.6:35b \
  --host http://localhost:11434
```

### `opus_scorer.py`
Scores benchmark JSONL output using Claude Opus. Produces ranked markdown report and
JSON for training data.

```bash
python3 scripts/opus_scorer.py ~/benchmark-results/model-benchmark-raw-<timestamp>.jsonl
python3 scripts/opus_scorer.py ~/benchmark-results/rag-benchmark-raw-<timestamp>.jsonl
```

---

## Context Sizing

Tasks are allocated context windows sized to what they actually need:

| Task type | num_ctx | Labels |
|---|---:|---|
| Classify | 4096 | clf-intent, clf-risk, clf-ambiguous |
| Chat / summarize | 4096–8192 | chat-* |
| PowerShell / runbook | 8192–16384 | ps-*, runbook-*, script-* |
| Graph accuracy | 32768 | ga-* |
| Context tests | 4096–32768 | ctx-short/medium/long |

---

## Known Issues

- **Tier 1 scraping yield is low**: `scout.py` generates Tier 1 summaries only when it
  finds headings matching "syntax", required parameters, or permissions in the MS docs HTML.
  Many cmdlet pages don't match — their Tier 1 chunk is skipped. Curated entries fill
  the gap for known failure modes. Long-term fix: relax heading matching in `build_tier1_summary()`.

- **Tier 2 escalation not yet wired**: The retriever supports `--tier 2` and the
  Auditor/Scorer escalation signals are designed, but the pipeline doesn't yet automatically
  escalate. Manual `--tier 2` flag works for testing.
