# Model Benchmark Findings

Last updated: 2026-06-25 (Round 3 results added)
Hardware: GMKtec EVO-X2 (AMD AI Max+ 395, 128 GB unified memory)
Scorer: claude-opus-4-8 with adaptive thinking

---

## Round 1 — Overnight Full Benchmark

**Models tested:** qwen3:8b, qwen3:14b, qwen2.5-coder:32b, qwen3.6:35b  
**Prompt sets:** chat, powershell, runbooks, classify, graph-accuracy, context (short)  
**Script:** `scripts/ollama_model_benchmark.py`  
**Scorer:** `scripts/opus_scorer.py`

### Model Averages

| Model | Avg Overall | Avg Accuracy | Avg Hallucination | Tok/sec |
|---|---:|---:|---:|---:|
| qwen3.6:35b | 8.9 | 8.9 | 9.2 | 52.5 |
| qwen2.5-coder:32b | 8.0 | 8.1 | 8.9 | 10.5 |
| qwen3:14b | 7.8 | 7.8 | 8.3 | 22.3 |
| qwen3:8b | 7.5 | 7.6 | 8.4 | 37.7 |

**Notable:** qwen3.6:35b is both the highest quality and fastest model — AMD unified memory bandwidth advantage over discrete VRAM architectures.

**Dropped:** qwen2.5-coder:32b eliminated — slowest at 10.5 t/s, wins only 1 of 17 routing slots.

### Routing Table (Round 1)

| Task | Model | Score |
|---|---|---:|
| chat-explain | qwen3:14b | 10 |
| chat-summarize | qwen3:14b | 10 |
| chat-troubleshoot | qwen3:14b | 9 |
| clf-ambiguous | qwen3:14b | 9 |
| clf-intent | qwen3:14b | 10 |
| clf-risk | qwen3.6:35b | 9 |
| ctx-short-ps | qwen3:14b | 9 |
| ga-param-names | qwen3:14b | 9 |
| ga-pagination | qwen3.6:35b | 9 |
| runbook-cert-rotation | qwen3.6:35b | 8 |
| runbook-offboard | qwen3:8b | 7 |
| script-daily-health | qwen3:14b | 9 |
| ps-graph-app-assignment | qwen3:14b | 7 |
| ps-graph-device-list | qwen2.5-coder:32b | 7 |
| **ga-deprecated-module** | qwen3:8b | **4** |
| **ga-error-handling** | qwen3:14b | **5** |
| **ps-graph-stale-users** | qwen3:8b | **4** |

### Failing Tasks Analysis

Three tasks scored ≤ 5/10 across all models. Root cause is factual grounding, not reasoning capacity:

- **ga-deprecated-module / ps-graph-stale-users:** Models use `LastSignInDate` instead of the correct `SignInActivity.LastSignInDateTime` property. Not a logic error — a training data gap.
- **ga-error-handling:** Requires real MFA cmdlet names (`Get-MgUserAuthenticationMethod`, `Remove-MgUserAuthenticationMethod`), specific 404/403 catch differentiation, pre-action revert logging, and a typed return object — all five simultaneously. Models hallucinate the cmdlet names or collapse error handling.

---

## Round 2 — Graph API Shootout

**Models:** deepseek-r1:14b, phi4:14b, qwen3.6:35b (control)  
**Prompts:** ga-deprecated-module, ga-error-handling, ps-graph-stale-users  
**Script:** `scripts/graph_api_shootout.py`  
**Rationale:**
- deepseek-r1:14b — chain-of-thought reasoning may catch hallucinated cmdlets before committing
- phi4:14b — Microsoft-trained model, strongest prior exposure to Graph API surface area
- qwen3.6:35b — round 1 control; confirms whether challengers actually improve on the baseline

### Round 2 Results

| Model | ga-deprecated-module | ga-error-handling | ps-graph-stale-users | Verdict |
|---|:---:|:---:|:---:|---|
| deepseek-r1:14b | 2-3 | 2-3 | 2-3 | Eliminated — chain-of-thought doesn't help without correct training data |
| phi4:14b | 0-5 | 0-5 | 0-5 | Eliminated — Microsoft heritage didn't translate to Graph API accuracy |
| qwen3.6:35b (control) | 4-6 | 4-6 | 4-6 | Baseline holds — best of the group, still not production ready without grounding |

**Conclusion:** No model cleared the bar. Root cause confirmed as a grounding problem, not a model capacity or reasoning problem. deepseek-r1's chain-of-thought and phi4's Microsoft training both failed to overcome the training data gap in Graph API surface area.

**Next target:** qwen3.6:35b + RAG vs gemma4:26b + RAG.

---

## Round 3 — gemma4:26b Shootout

**Models:** gemma4:26b  
**Prompts:** ga-deprecated-module, ga-error-handling, ps-graph-stale-users  
**Script:** `scripts/graph_api_shootout.py`  
**Rationale:** MoE architecture (4B active), 256K context, 50 t/s — pulled as a wildcard after Round 2 confirmed grounding is the problem, not capacity.

### Round 3 Results

| Task | Cold | Warm | Notes |
|---|:---:|:---:|---|
| ga-deprecated-module | 7 | 8 | Significant jump from previous best of 4 |
| ga-error-handling | 0 | 5 | Still the hardest task — hallucination risk remains high |
| ps-graph-stale-users | 6 | 9 | Near production-ready on warm run |

**Verdict:** gemma4:26b is the new leader on Graph API tasks without RAG. The warm run on ps-graph-stale-users scoring 9 with hallucination_risk=10 suggests it actually knows the correct property names in some inference paths — just not consistently. RAG should lock that in.

**ga-error-handling remains the outlier** — the cold=0 indicates it's still fabricating cmdlets on first load. This task needs RAG more than any other.

**Key differentiator going forward:** both qwen3.6:35b and gemma4:26b run at ~50 t/s. The RAG round will come down to instruction following under context load — which model stays accurate when the prompt is 10K+ tokens deep with retrieved API reference material. gemma4's 256K window vs qwen3.6's 262K is a wash; behavior under load is what matters.

---

---

## Round 4 — RAG Benchmark (gemma4:26b vs qwen3.6:35b)

**Models:** gemma4:26b, qwen3.6:35b  
**Prompts:** ga-deprecated-module, ga-error-handling, ps-graph-stale-users  
**Script:** `scripts/rag_benchmark.py`  
**Scorer output:** `outputs/opus-scored-20260626-035355.md`  
**RAG corpus:** MS Graph PowerShell docs — Get-MgUser, Update-MgUser, Get-MgUserAuthenticationMethod, Remove-MgUserAuthenticationMicrosoftAuthenticatorMethod, New-MgGroupMemberByRef, Get-MgGroupMember, Get-MgDeviceManagementManagedDevice, Connect-MgGraph, Invoke-MgGraphRequest  
**Retrieval:** Tier 1 (compact summary), top-6 chunks, nomic-embed-text

### Round 4 Results

| Rank | Model | Task | Phase | Overall | Accuracy | Hallucination | t/s |
|---:|---|---|---|---:|---:|---:|---:|
| 1 | gemma4:26b | ga-error-handling | cold | **8** | 8 | 9 | 41.3 |
| 2 | gemma4:26b | ga-deprecated-module | cold | **7** | 7 | 9 | 41.5 |
| 3 | gemma4:26b | ps-graph-stale-users | cold | **7** | 7 | 9 | 40.4 |
| 4 | qwen3.6:35b | ps-graph-stale-users | warm | **7** | 7 | 9 | 48.9 |
| 6 | gemma4:26b | ps-graph-stale-users | warm | **6** | 6 | 9 | 40.2 |
| 7 | qwen3.6:35b | ga-error-handling | warm | **6** | 6 | 5 | 48.9 |
| 10 | qwen3.6:35b | ps-graph-stale-users | cold | **5** | 4 | 6 | 48.6 |
| 15 | qwen3.6:35b | ga-deprecated-module | cold | **4** | 4 | 6 | 47.7 |
| 16 | qwen3.6:35b | ga-deprecated-module | warm | **4** | 3 | 4 | 47.9 |
| 17 | qwen3.6:35b | ga-error-handling | cold | **4** | 4 | 6 | 48.9 |

### Model Averages (RAG round, 6 entries each)

| Model | Avg Overall | Avg Accuracy | Avg Hallucination | Avg t/s |
|---|---:|---:|---:|---:|
| gemma4:26b | **6.2** | 6.2 | 7.8 | 40.9 |
| qwen3.6:35b | **5.0** | 4.7 | 6.0 | 48.5 |

### Key Findings

**gemma4:26b wins all 3 tasks.** RAG fixed ga-error-handling (0 cold → 8 cold) — confirms grounding was the root cause, not model capacity.

**qwen3.6 "one-trick-andy" confirmed.** Even with 94 RAG chunks injected containing `SignInActivity.LastSignInDateTime`, qwen3.6 consistently used `lastSignInDateTime` as a direct property. Training weights overrode retrieved context. This is the definitive disqualifier for Graph API property accuracy tasks.

**gemma4 warm-run degradation explained.** KV cache from cold run anchors warm run to a degraded inference path when the same prompt is reused. Production requests are always unique — not a real-world concern. Warm runs now use a cache-busting prefix in the benchmark.

**Two-model stack locked:** gemma4:26b as primary, qwen3.6:35b as fallback for high-complexity or Scorer escalation. All other models eliminated.

---

## Round 5 — Drift Validation (COMPLETE)

**Models:** gemma4:26b, qwen3.6:35b  
**Prompt sets:** all (classify, chat, powershell, runbook, graph-accuracy, context)  
**Script:** `scripts/ollama_model_benchmark.py`  
**Scorer output:** `outputs/benchmark-results/opus-scored-20260626-161123.md`  
**Runs:** 3 cold runs per task (--skip-warm) — drift measurement  
**Context sizing:** per-task (`TASK_CONTEXT_SIZES` — classify/chat 4-8K, ps/runbook 8-16K, graph-accuracy 32K)  
**Cold eviction:** verified via /api/ps polling loop (not fixed 2s sleep)  
**Rows:** 96 (16 tasks × 2 models × 3 cold runs)

### Round 5 Model Averages

| Model | Avg Overall | Avg Accuracy | Avg Hallucination | Avg t/s |
|---|---:|---:|---:|---:|
| gemma4:26b | **8.3** | 8.3 | 9.1 | 47.3 |
| qwen3.6:35b | 7.9 | 7.7 | 8.2 | 53.0 |

### Drift Summary — Score Variance Across 3 Cold Runs

| Task | gemma4 drift | qwen3.6 drift | RAG required |
|---|:---:|:---:|---|
| chat-explain | ±1 | 0 | No |
| chat-troubleshoot | 0 | ±1 | No |
| chat-summarize | ±1 | 0 | No |
| clf-intent | 0 | 0 | No |
| clf-risk | 0 | ±1 | No |
| clf-ambiguous | ±1 | ±2 | No |
| runbook-offboard | 0 | 0 | No |
| runbook-cert-rotation | ±2 | ±2 | Monitor |
| script-daily-health | ±1 | 0 | No |
| ps-graph-device-list | ±2 | ±1 | Yes |
| ps-graph-app-assignment | **±4** | ±2 | **Yes — mandatory** |
| ga-param-names | ±2 | ±2 | Yes |
| ga-pagination | ±3 | ±2 | Yes |
| ctx-short-ps | ±1 | **±5** | No (gemma4 only) |
| ctx-medium-ps | ±1 | ±2 | No |
| ctx-long-ps | ±1 | 0 | Both low — RAG helps |

### Final Routing Table (Three-Model Stack)

| Task Type | Model | Rationale |
|---|---|---|
| Interactive chat | qwen3:8b | 8-16s wall time vs 40-120s for gemma4 |
| Quality chat | gemma4:26b | 10/10 quality, verbose — async use |
| Vision / screenshot parsing | gemma4:26b | Multimodal intake for support tickets |
| clf-intent, clf-ambiguous | gemma4:26b | Perfect score, stable |
| clf-risk | qwen3.6:35b | Wins this task, 10/10 |
| PowerShell + Graph API | gemma4:26b + RAG | ±2-4 drift without RAG |
| Runbooks | gemma4:26b | 9/10, stable |
| script-daily-health | qwen3.6:35b | Wins this task, 9/10 zero drift |
| Graph accuracy tasks | gemma4:26b + RAG + curated corpus | Dedicated RAG mandatory |
| Escalation fallback | qwen3.6:35b | When Scorer confidence < threshold |

**Disqualifier confirmed:** qwen3.6 ctx-short-ps ±5 variance disqualifies it from context tasks. Route to gemma4.

---

## RAG Architecture — Implemented

### Two-Tier Corpus

| Tier | Content | When Used |
|---|---|---|
| Tier 1 | Syntax + required params + permissions (compact) | Default — injected on every request |
| Tier 2 | Full reference + examples + all params | Escalation — Auditor/Scorer signal below threshold |

### Corpus Sources

| Source | Script | Content |
|---|---|---|
| Scraped | `scripts/scout.py` | MS docs HTML for each target cmdlet |
| Curated | `scripts/curate.py` | Hand-authored entries for confirmed failure modes |

### Current Curated Entries

| ID | Fixes |
|---|---|
| `signinactivity-property-access-t1/t2` | `$user.LastSignInDateTime` doesn't exist — must use `$user.SignInActivity.LastSignInDateTime` with `-Property "signInActivity"` |
| `mfa-auth-methods-uris-t1/t2` | Correct REST paths (`/users/{id}/authentication/methods`), type-specific cmdlet switch pattern, removes hallucinated `Remove-MgUserAuthenticationMethod` |

### Escalation Signals (Tier 1 → Tier 2) — Designed, Not Yet Wired

- Scorer confidence < threshold
- Auditor parameter mismatch
- Parser complexity flag
- Historical hallucination risk for task type

---

## Next Steps — Phase 4

- [x] Score Round 2 results with `opus_scorer.py`
- [x] Score Round 3 results (gemma4:26b)
- [x] Build Scout agent (MS Graph docs crawler)
- [x] Build Indexer agent (chunk, embed, store in Qdrant)
- [x] Build Retriever (tier-filtered vector search)
- [x] Build two-tier RAG corpus (Tier 1 summary + Tier 2 full reference)
- [x] Build curated corpus entries for confirmed failure modes
- [x] Re-run failing tasks: gemma4:26b + RAG vs qwen3.6:35b + RAG
- [x] Two-model stack locked: gemma4:26b primary, qwen3.6:35b fallback
- [x] Round 5 drift validation complete — routing table finalized
- [x] Three-model stack confirmed: qwen3:8b chat fast lane added
- [ ] Fix scout tier-1 summary generation (HTML parser misses Syntax headings on most cmdlets)
- [ ] Implement Tier 2 escalation logic in pipeline (retriever supports it, pipeline doesn't yet)
- [ ] Task-specific system prompts (Phase 4)
- [ ] Build Parser agent — intent classification and task routing (Phase 5)
