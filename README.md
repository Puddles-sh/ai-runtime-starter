# AI Runtime Starter

Local AI inference stack running on a GMKtec EVO-X2 (AMD AI Max+ 395, 128GB unified memory).
Built for a DevOps/AI consultancy — compliance-first, human-in-the-loop, local inference with no cloud data dependency.

## Current State

Phase 3 complete. Three-model stack validated across 5 benchmark rounds (96+ scored runs, Opus-evaluated).

| Model | Role | t/s |
|---|---|---:|
| gemma4:26b | Primary — PowerShell, Graph API, runbooks, vision | ~47 |
| qwen3.6:35b | Escalation fallback — Scorer confidence threshold | ~53 |
| qwen3:8b | Chat fast lane — interactive latency | ~38 |

RAG pipeline operational: Scout → Indexer → Qdrant → Retriever → Tier 1/2 delivery.

## What's In This Repo

```text
scripts/          — Corpus pipeline and benchmarking tools
runbooks/         — Architecture decisions, benchmark findings, operational guides
outputs/          — All benchmark results and Opus scoring reports
config/           — Configuration templates
tests/            — Test stubs
```

## Quick Reference — Corpus Pipeline

```bash
# Crawl MS docs
python3 scripts/scout.py --output-dir ~/rag-corpus

# Hand-authored entries for confirmed failure modes
python3 scripts/curate.py --output-dir ~/rag-corpus

# Embed and store in Qdrant
python3 scripts/indexer.py $(ls -t ~/rag-corpus/curated-corpus-*.jsonl | head -1)
python3 scripts/indexer.py $(ls -t ~/rag-corpus/graph-ps-corpus-*.jsonl | head -1)

# Test retrieval
python3 scripts/retriever.py --query "Get-MgUser sign in activity"
```

## Quick Reference — Benchmarking

```bash
# Drift measurement — 3 cold runs, no RAG
python3 scripts/ollama_model_benchmark.py gemma4:26b qwen3.6:35b \
  --prompt-set all --prompt-size all --runs 3 --skip-warm

# RAG benchmark — failing tasks with retrieval
python3 scripts/rag_benchmark.py --models gemma4:26b qwen3.6:35b

# Score results
python3 scripts/opus_scorer.py ~/benchmark-results/ollama-raw-<timestamp>.jsonl
```

## Key Docs

| Doc | What It Contains |
|---|---|
| [runbooks/benchmark-master-summary.md](runbooks/benchmark-master-summary.md) | All 5 rounds, all models, timing + scores in one place |
| [runbooks/model-benchmark-findings.md](runbooks/model-benchmark-findings.md) | Round-by-round narrative, architecture decisions |
| [runbooks/model-benchmarking.md](runbooks/model-benchmarking.md) | How to run benchmarks, final routing table |
| [scripts/README.md](scripts/README.md) | Every script with usage examples |
| [runbooks/no-secrets-policy.md](runbooks/no-secrets-policy.md) | What never gets committed |

## What Never Goes In This Repo

Secrets, API keys, certificates, model files, vector databases, audit logs, runtime data.
See [runbooks/no-secrets-policy.md](runbooks/no-secrets-policy.md).

## Phase Roadmap

- [x] Phase 1 — Hardware, OS, ROCm drivers, GPU memory unlock
- [x] Phase 2 — Model benchmarking, Opus scoring, routing table
- [x] Phase 3 — RAG pipeline: Scout, Indexer, Qdrant, Retriever, two-tier corpus
- [ ] Phase 4 — Model routing locked, task-specific system prompts
- [ ] Phase 5 — Parser agent — intent classification and task routing
- [ ] Phase 6 — Azure Key Vault integration, credential isolation
- [ ] Phase 7 — Telegram approval gate, Tailscale remote access
- [ ] Phase 8 — Planner + Dispatcher agents, human-in-the-loop execution
- [ ] Phase 9 — Foundation complete — all 7 agents operational
