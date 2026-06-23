# Model Benchmarking and Selection Runbook

## Purpose

Build a scored index of model strengths across task types so the agent pipeline
can route requests to the right model automatically rather than guessing.

## Script

```text
AI/scripts/ollama_model_benchmark.py
AI-Repos/ai-runtime-starter/scripts/ollama_model_benchmark.py  (source of truth)
```

## Prompt Sets

| Set | Flag | What It Tests |
|---|---|---|
| `chat` | `--prompt-set chat` | Conversational explanation, troubleshooting, summarization |
| `powershell` | `--prompt-set powershell` | Graph API scripting, device lists, stale users, app assignments |
| `runbooks` | `--prompt-set runbooks` | Employee offboarding, cert rotation, daily health checks |
| `graph-accuracy` | `--prompt-set graph-accuracy` | Deprecated module detection, correct param names, pagination, error handling |
| `all` | `--prompt-set all` | All of the above |

### graph-accuracy Prompt Set (Detail)

This set is specifically designed to catch the failure modes that matter most for
production PowerShell/Graph automation. A model that scores well on general powershell
prompts but poorly here should NOT be used for Graph scripting tasks.

| Prompt | What It Catches |
|---|---|
| `ga-deprecated-module` | Does the model use deprecated AzureAD / MSOnline modules instead of Microsoft.Graph? |
| `ga-param-names` | Does it use correct parameter names? (`-DirectoryObjectId` not `-UserId` on New-MgGroupMember) |
| `ga-pagination` | Does it handle `@odata.nextLink` pagination or silently truncate at 1000 records? |
| `ga-error-handling` | Does it produce structured error handling with 404/403 specificity and revert logging? |

A hallucination score below 7 on any `graph-accuracy` prompt is a disqualifier for
routing PowerShell tasks to that model.

---

## Phase 1 — Baseline Performance (Day One)

Run immediately after first boot across all installed models.
Captures cold/warm load times, tokens/sec, and memory footprint per task category.

```bash
# Run from EVO
python3 /opt/ai-runtime/scripts/ollama_model_benchmark.py \
  qwen3:8b qwen3:14b \
  deepseek-r1:8b deepseek-r1:14b \
  qwen2.5-coder:7b qwen2.5-coder:14b qwen2.5-coder:32b \
  qwen3.6:35b \
  --host http://localhost:11434 \
  --prompt-set all

# Run from MacBook against EVO
python3 "$HOME/Library/Mobile Documents/com~apple~CloudDocs/AI/scripts/ollama_model_benchmark.py" \
  qwen3:8b qwen3:14b \
  deepseek-r1:8b deepseek-r1:14b \
  qwen2.5-coder:7b qwen2.5-coder:14b qwen2.5-coder:32b \
  qwen3.6:35b \
  --host http://evo-x2.local:11434 \
  --prompt-set all
```

Reports written to: `AI/projects/homelab/outputs/model-benchmarks/`

Each run produces: Markdown summary, CSV table, JSON raw details, response review file.

## What To Compare

| Metric | What It Tells You |
|---|---|
| `load_seconds` | Time to load model from disk into memory |
| `wall_seconds` | Real elapsed request time end to end |
| `tokens_per_second` | Output generation speed |
| `loaded_size_gib` | Total memory footprint |
| `loaded_vram_gib` | GPU memory usage (unified pool on AI Max+ 395) |

Note: on the AI Max+ 395, VRAM and RAM are the same pool. `loaded_vram_gib`
reflects unified memory in use, not a separate VRAM budget.

---

## Phase 2 — Output Quality Scoring (Opus-Assisted)

Speed tells you half the story. Quality tells you the other half.

Run the Opus scorer against the benchmark JSON output:

```bash
python3 /opt/ai-runtime/scripts/opus_scorer.py \
  projects/homelab/outputs/model-benchmarks/ollama-benchmark-*.json
```

The scorer calls Claude Opus 4.8 for each prompt+response pair and scores:

### Scoring Rubric

| Dimension | What to Check |
|---|---|
| Accuracy | Are facts, cmdlets, and syntax correct? |
| Completeness | Does it fully answer the request? |
| Format | Is output clean and usable without editing? |
| Hallucination risk | Did it invent cmdlets, parameters, or Graph endpoints? |
| Consistency | Does it produce similar quality on repeat runs? |

Scored output written to: `opus-scored-TIMESTAMP.json` (training data) and `opus-scored-TIMESTAMP.md` (ranked report).

---

## Phase 3 — Routing Index

Once enough scored examples exist, the Scorer agent uses this index to route
incoming requests to the best model for that task type automatically.

Target routing table (to be validated by benchmark results):

| Task Type | Candidates to Benchmark | Expected Winner |
|---|---|---|
| Daily chat | qwen3:8b, qwen3:14b | qwen3:14b |
| PowerShell / Graph scripting | qwen2.5-coder:32b, qwen3.6:35b | TBD — graph-accuracy score decides |
| Runbook generation | qwen2.5-coder:32b, qwen3.6:35b, qwen3:14b | TBD — benchmark decides |
| Complex reasoning / debugging | deepseek-r1:8b, deepseek-r1:14b | deepseek-r1:14b |
| Request classification (fast) | qwen3:8b | qwen3:8b |
| Embeddings | nomic-embed-text | nomic-embed-text |
| Screenshot / vision parsing | llama3.2-vision:11b, qwen3.6:35b | TBD — qwen3.6 has native vision |

**Note:** For PowerShell/Graph routing, the `graph-accuracy` prompt set scores are the
deciding factor — not overall benchmark scores. A fast model that hallucinates cmdlets
is worse than a slower model that gets it right.

---

## Phase 4 — Continuous Improvement

Every completed production request becomes a scored example.
Every revert event becomes a labeled failure.
Curator surfaces these as memory candidates after each run.
Routing index improves automatically over time without manual intervention.

---

## Notes

- Cold runs stop the model first, then send the request — simulates real first load
- Warm runs send a second request while the model is still loaded
- Large models may fit in memory but still feel slow — tok/sec is the honest measure
- Keep benchmark results as memory candidates first before promoting into approved memory
- Any model scoring hallucination_risk < 7 on graph-accuracy prompts is disqualified
  from PowerShell routing regardless of other scores

---

## Done Criteria for Phase 1

- [ ] Benchmark run completed across all models including qwen3.6:35b
- [ ] graph-accuracy prompt set run on all PowerShell candidate models
- [ ] JSON/CSV/Markdown results saved to outputs folder
- [ ] Opus scorer run, training data written
- [ ] At least one clear winner identified per task category
- [ ] Routing table updated with validated model assignments
- [ ] Any model with hallucination_risk < 7 on graph-accuracy flagged and excluded
