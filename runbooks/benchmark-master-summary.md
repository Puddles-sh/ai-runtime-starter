# Benchmark Master Summary

All rounds, all models, all tasks. Timing + Opus quality scores in one place.  
Hardware: GMKtec EVO-X2 — AMD AI Max+ 395, 128GB unified memory  
Scorer: claude-opus-4-8 (adaptive thinking)

---

## Models Tested

| Model | Architecture | Memory | t/s (cold) | Status |
|---|---|---:|---:|---|
| qwen3:8b | Dense 8B | 9.3 GB | 37–39 | **IN STACK** — chat fast lane |
| qwen3:14b | Dense 14B | 13.6 GB | 21–23 | Eliminated — outpaced by gemma4 |
| qwen2.5-coder:32b | Dense 32B | ~20 GB | 10–11 | Eliminated — slowest, wins 1/17 slots |
| deepseek-r1:14b | Dense 14B (CoT) | ~9 GB | 20–22 | Eliminated — CoT doesn't fix grounding |
| phi4:14b | Dense 14B | ~9 GB | 22 | Eliminated — MS heritage didn't help graph |
| qwen3.6:35b | MoE 35B/3.6B active | 22 GB | 51–55 | **IN STACK** — escalation fallback |
| gemma4:26b | MoE 26B/4B active | ~16 GB | 44–51 | **IN STACK** — primary model |

---

## Round 1 — Full Baseline Benchmark
**Date:** 2026-06-25  
**Models:** qwen3:8b, qwen3:14b, qwen2.5-coder:32b, qwen3.6:35b  
**Scored:** opus-scored-20260625-214051.md

### Wall Time — Cold Run (seconds)

| Task | qwen3:8b | qwen3:14b | qwen2.5-coder:32b | qwen3.6:35b |
|---|---:|---:|---:|---:|
| chat-explain | **10.7** | 17.9 | ~45 | 39.3 |
| chat-troubleshoot | **15.8** | 42.6 | ~80 | 39.1 |
| chat-summarize | **7.9** | 12.4 | ~25 | 28.3 |
| clf-intent | **7.5** | 14.0 | ~12 | 27.2 |
| clf-risk | **10.2** | 13.6 | ~12 | 25.2 |
| clf-ambiguous | **7.6** | 24.9 | ~12 | 34.5 |
| ps-graph-device-list | **62.3** | 166.4 | ~180 | 118.1 |
| ps-graph-stale-users | 88.9 | 217.9 | ~200 | **129.1** |
| ps-graph-app-assignment | 106.0 | 195.5 | ~180 | **108.4** |
| runbook-offboard | **56.7** | 68.3 | ~110 | 81.2 |
| runbook-cert-rotation | **58.2** | 112.4 | ~120 | 77.1 |
| script-daily-health | 112.5 | 145.1 | ~160 | **143.3** |
| ga-deprecated-module | 120.7 | 130.0 | ~140 | **110.5** |
| ga-param-names | 87.1 | 111.0 | ~130 | **108.9** |
| ga-pagination | 157.2 | 175.7 | ~180 | **110.3** |
| ga-error-handling | 131.3 | 347.3 | ~350 | **157.0** |
| ctx-short-ps | **26.5** | 71.3 | ~80 | 26.5 |

### Opus Scores — Round 1

| Task | qwen3:8b | qwen3:14b | qwen2.5-coder:32b | qwen3.6:35b | Winner |
|---|:---:|:---:|:---:|:---:|---|
| chat-explain | 9 | **10** | 9 | **10** | tie |
| chat-troubleshoot | 9 | 9 | 8 | **9** | tie |
| chat-summarize | **10** | **10** | **10** | 9 | tie |
| clf-intent | **10** | **10** | **10** | **10** | tie |
| clf-risk | 9 | 8 | 8 | **9** | tie |
| clf-ambiguous | 9 | 9 | 9 | 9 | tie |
| ps-graph-device-list | 4 | 7 | **7** | — | qwen2.5-coder |
| ps-graph-stale-users | 4 | — | — | 4 | tie (all failing) |
| ps-graph-app-assignment | — | **7** | 5 | — | qwen3:14b |
| runbook-offboard | **7** | 6 | 5 | — | qwen3:8b |
| runbook-cert-rotation | — | 5 | — | **8** | qwen3.6 |
| script-daily-health | 6 | **9** | 7 | 9 | tie |
| ga-deprecated-module | 4 | — | — | 6 | qwen3.6 |
| ga-param-names | 7 | **9** | 7 | 8 | qwen3:14b |
| ga-pagination | 6 | 6 | — | **9** | qwen3.6 |
| ga-error-handling | 5 | **5** | — | 5 | tie (all failing) |
| ctx-short-ps | 5 | 9 | 9 | **9** | tie |

### Round 1 Model Averages

| Model | Avg Overall | Avg Accuracy | Avg Hallucination | Avg t/s |
|---|---:|---:|---:|---:|
| qwen3.6:35b | **8.9** | 8.9 | 9.2 | 52.5 |
| qwen2.5-coder:32b | 8.0 | 8.1 | 8.9 | 10.5 |
| qwen3:14b | 7.8 | 7.8 | 8.3 | 22.3 |
| qwen3:8b | 7.5 | 7.6 | 8.4 | 37.7 |

**Key finding:** Three tasks (ga-deprecated-module, ga-error-handling, ps-graph-stale-users) fail across ALL models. Root cause: training data gap on MS Graph property names and MFA cmdlets — not a reasoning failure.

**Eliminated:** qwen2.5-coder:32b (10.5 t/s, wins 1/17 slots).

---

## Round 2 — Graph API Shootout
**Date:** 2026-06-25  
**Models:** deepseek-r1:14b, phi4:14b, qwen3.6:35b (control)  
**Scope:** Failing 3 tasks only  
**Scored:** opus-scored-20260625-230501.md

### Opus Scores — Round 2

| Task | deepseek-r1:14b | phi4:14b | qwen3.6:35b |
|---|:---:|:---:|:---:|
| ga-deprecated-module (cold) | 2 | 4 | **6** |
| ga-deprecated-module (warm) | 3 | 4 | **6** |
| ga-error-handling (cold) | 4 | — | **5** |
| ga-error-handling (warm) | 3 | **5** | 5 |
| ps-graph-stale-users (cold) | 3 | — | **4** |
| ps-graph-stale-users (warm) | 3 | 3 | **4** |

### Round 2 Model Averages

| Model | Avg Overall | Avg t/s |
|---|---:|---:|
| qwen3.6:35b | **5.0** | 51.6 |
| phi4:14b | 4.0 | 22.1 |
| deepseek-r1:14b | 3.0 | 21.7 |

**Eliminated:** deepseek-r1:14b (chain-of-thought doesn't fix a grounding problem), phi4:14b (Microsoft training heritage didn't translate to Graph accuracy). **Conclusion: grounding problem confirmed, not model capacity.**

---

## Round 3 — gemma4:26b Shootout
**Date:** 2026-06-25  
**Models:** gemma4:26b  
**Scope:** Failing 3 tasks only  
**Scored:** opus-scored-20260625-232442.md

### Opus Scores — Round 3

| Task | gemma4:26b cold | gemma4:26b warm | Previous best |
|---|:---:|:---:|:---:|
| ga-deprecated-module | 7 | 8 | 6 (qwen3.6) |
| ga-error-handling | — | 5 | 5 (phi4/qwen3.6) |
| ps-graph-stale-users | 6 | **9** | 4 (qwen3.6) |

**gemma4:26b at ~44 t/s is the new leader on all three failing tasks without RAG.** Warm run on ps-graph-stale-users scoring 9 (hallucination 10) suggests correct property knowledge exists — just not consistent on cold load. RAG identified as the fix.

---

## Round 4 — RAG Benchmark
**Date:** 2026-06-26  
**Models:** gemma4:26b, qwen3.6:35b (+ others for comparison)  
**Scope:** Failing 3 tasks with Qdrant retrieval injected  
**RAG:** Tier 1 (compact summary), top-6 chunks, nomic-embed-text  
**Scored:** opus-scored-20260626-035355.md

### Opus Scores — Round 4 (with RAG)

| Task | gemma4 cold | gemma4 warm | qwen3.6 cold | qwen3.6 warm |
|---|:---:|:---:|:---:|:---:|
| ga-deprecated-module | **7** | 5 | 4 | 4 |
| ga-error-handling | **8** | 4 | 4 | 6 |
| ps-graph-stale-users | **7** | 6 | 5 | **7** |

### Round 4 Model Averages

| Model | Avg Overall | Avg Accuracy | Avg Hallucination | Avg t/s |
|---|---:|---:|---:|---:|
| gemma4:26b | **6.2** | 6.2 | 7.8 | 40.9 |
| qwen3.6:35b | 5.0 | 4.7 | 6.0 | 48.5 |

**Key findings:**
- gemma4 ga-error-handling: 0 (no RAG) → **8** (with RAG) — grounding was the entire problem
- qwen3.6 "one-trick-andy" confirmed: even with 94 RAG chunks injected, qwen3.6 still uses `lastSignInDateTime` as a direct property. Training weights override retrieved context. Disqualified from Graph property accuracy tasks as primary.
- **Two-model stack locked:** gemma4:26b primary, qwen3.6:35b escalation fallback.

---

## Round 5 — Drift Validation
**Date:** 2026-06-26  
**Models:** gemma4:26b, qwen3.6:35b  
**Scope:** All task types (16 tasks), 3 cold runs each, no warm, no RAG  
**Purpose:** Measure MoE consistency variance at temperature 0  
**Rows:** 96 (16 tasks × 2 models × 3 runs)  
**Scored:** opus-scored-20260626-161123.md

### Wall Time — Cold Run (seconds, gemma4:26b, Round 5)

| Task | Run 1 | Run 2 | Run 3 | Avg |
|---|---:|---:|---:|---:|
| chat-explain | 48.0 | 69.9 | 80.0 | 66.0 |
| chat-troubleshoot | 115.9 | 145.3 | 101.2 | 120.8 |
| chat-summarize | 114.5 | 112.8 | 98.9 | 108.7 |
| clf-intent | ~5 | ~5 | ~5 | ~5 |
| clf-risk | ~12 | ~12 | ~12 | ~12 |
| clf-ambiguous | ~15 | ~15 | ~15 | ~15 |

*Note: ctx-long-ps, ps-graph-*, ga-* timing on EVO — full CSV pending push to repo*

### Drift Analysis — Score Variance Across 3 Cold Runs

| Task | gemma4 scores | gemma4 drift | qwen3.6 scores | qwen3.6 drift |
|---|---|:---:|---|:---:|
| chat-explain | 10, 10, 9 | ±1 | 10, 10, 10 | **0** |
| chat-troubleshoot | 9, 9, 9 | **0** | 9, 9, 8 | ±1 |
| chat-summarize | 10, 10, 9 | ±1 | 9, 9, 9 | **0** |
| clf-intent | 10, 10, 10 | **0** | 10, 10, 10 | **0** |
| clf-risk | 9, 9, 9 | **0** | 10, 9, 9 | ±1 |
| clf-ambiguous | 10, 10, 9 | ±1 | 10, 8, 8 | ±2 |
| runbook-offboard | 9, 9, 9 | **0** | 8, 8, 8 | **0** |
| runbook-cert-rotation | 9, 9, 7 | ±2 | 8, 7, 6 | ±2 |
| script-daily-health | 8, 7, 7 | ±1 | 9, 9, 9 | **0** |
| ps-graph-device-list | 8, 7, 6 | ±2 | 6, 5, 5 | ±1 |
| ps-graph-app-assignment | **8, 6, 4** | **±4** | 8, 7, 6 | ±2 |
| ga-param-names | 9, 8, 7 | ±2 | 8, 7, 6 | ±2 |
| ga-pagination | 8, 8, 5 | ±3 | 8, 7, 6 | ±2 |
| ctx-short-ps | 10, 10, 9 | ±1 | **10, 6, 5** | **±5** |
| ctx-medium-ps | 9, 8, 8 | ±1 | 8, 7, 6 | ±2 |
| ctx-long-ps | 6, 5, 5 | ±1 | 6, 6, 6 | **0** |

### Round 5 Model Averages

| Model | Avg Overall | Avg Accuracy | Avg Hallucination | Avg t/s |
|---|---:|---:|---:|---:|
| gemma4:26b | **8.3** | 8.3 | 9.1 | 47.3 |
| qwen3.6:35b | 7.9 | 7.7 | 8.2 | 53.0 |

### Round 5 Routing Recommendation (best model per task, no RAG)

| Task | Winner | Score |
|---|---|:---:|
| chat-explain | gemma4:26b | 10 |
| chat-summarize | gemma4:26b | 10 |
| chat-troubleshoot | gemma4:26b | 9 |
| clf-intent | gemma4:26b | 10 |
| clf-ambiguous | gemma4:26b | 10 |
| clf-risk | qwen3.6:35b | 10 |
| ctx-short-ps | gemma4:26b | 10 |
| ctx-medium-ps | gemma4:26b | 9 |
| ctx-long-ps | gemma4:26b | 6 |
| ga-param-names | gemma4:26b | 9 |
| ga-pagination | gemma4:26b | 8 |
| ps-graph-device-list | gemma4:26b | 8 |
| ps-graph-app-assignment | gemma4:26b | 8 |
| runbook-offboard | gemma4:26b | 9 |
| runbook-cert-rotation | gemma4:26b | 9 |
| script-daily-health | qwen3.6:35b | 9 |

**gemma4:26b wins 14 of 16 tasks.** qwen3.6 wins clf-risk and script-daily-health.

---

## Cumulative Model Score History

| Model | R1 Avg | R2 Avg | R3 Avg | R4 Avg (RAG) | R5 Avg | Final Status |
|---|:---:|:---:|:---:|:---:|:---:|---|
| gemma4:26b | — | — | 7.0 | 6.2 | **8.3** | ✅ PRIMARY |
| qwen3.6:35b | 8.9 | 5.0 | — | 5.0 | 7.9 | ✅ ESCALATION |
| qwen3:8b | 7.5 | — | — | — | — | ✅ CHAT FAST LANE |
| qwen3:14b | 7.8 | — | — | — | — | ❌ Eliminated |
| qwen2.5-coder:32b | 8.0 | — | — | — | — | ❌ Eliminated (10.5 t/s) |
| deepseek-r1:14b | — | 3.0 | — | — | — | ❌ Eliminated |
| phi4:14b | — | 4.0 | — | — | — | ❌ Eliminated |

---

## Final Routing Table — Locked

| Task Type | Model | Rationale |
|---|---|---|
| **chat-explain, chat-troubleshoot, chat-summarize** | qwen3:8b (latency) / gemma4:26b (quality) | qwen3:8b ~10s, gemma4 ~66-120s. Route by latency budget. |
| **clf-intent, clf-ambiguous** | gemma4:26b | Perfect score, ~5-15s |
| **clf-risk** | qwen3.6:35b | Wins this task specifically, 10/10 |
| **ps-graph-device-list, ps-graph-app-assignment** | gemma4:26b + RAG | Without RAG: ±2-4 drift. RAG mandatory. |
| **runbook-offboard, runbook-cert-rotation** | gemma4:26b | 9/10, stable |
| **script-daily-health** | qwen3.6:35b | Wins cleanly, 9/10 with zero drift |
| **ga-param-names, ga-pagination** | gemma4:26b + RAG | ±2-3 drift without RAG, needs grounding |
| **ga-deprecated-module, ga-error-handling, ps-graph-stale-users** | gemma4:26b + RAG + curated corpus | Dedicated RAG tasks — curated chunks address known failure modes |
| **ctx-short-ps, ctx-medium-ps** | gemma4:26b | 9-10/10, stable |
| **ctx-long-ps** | Either | Both score 5-6, complex context tasks need RAG regardless |
| **Escalation / high-confidence threshold missed** | qwen3.6:35b | Fallback when Scorer < threshold |

### Disqualifier Rules

- Hallucination score < 7 on any graph-accuracy task → disqualified from PowerShell routing
- qwen3.6 borderline on Graph property tasks — primary for clf-risk and script-daily-health only; fallback otherwise
- qwen3:8b for chat where wall time matters — gemma4 quality is 10 but latency is 1-2 minutes

---

## Key Architecture Decisions

| Decision | Rationale |
|---|---|
| Two-tier RAG (Tier 1 summary / Tier 2 full reference) | Tier 1 keeps prompt tokens low; Tier 2 only on escalation |
| Curated corpus alongside scraped corpus | qwen3.6 training weights override scraped docs — curated chunks win by specificity |
| Per-task context sizing (4K-32K) | Classify/chat don't need 32K; over-allocation wastes inference time |
| Cold eviction via polling loop | 2s fixed sleep was insufficient for large model eviction (can take 10-15s) |
| Cache-bust prefix on warm runs | Identical prompt prefix = KV cache anchoring = degraded warm results |
| MoE-only stack risk accepted | Consistency risk is real but manageable — RAG grounding + Scorer escalation are the mitigation |
