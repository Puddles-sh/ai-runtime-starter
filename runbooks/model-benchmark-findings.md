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

## Decision Tree — Resolved

```
Round 2 scores > 7/10?
├── YES → Build task-specific system prompts (N/A — no model cleared bar)
└── NO  → Round 3: gemma4:26b shootout → new leader confirmed
          → Build Scout + Indexer agents to crawl MS Graph PowerShell docs  ← WE ARE HERE
          → RAG retrieval layer injects correct API surface before generation
          → Re-run: gemma4:26b + RAG vs qwen3.6:35b + RAG
          → Differentiator: instruction following under heavy context load
          → If still failing → model problem, not grounding problem
```

---

## Next Steps

- [x] Score Round 2 results with `opus_scorer.py`
- [x] Score Round 3 results (gemma4:26b)
- [ ] Build Scout agent (MS Graph docs crawler)
- [ ] Build Indexer agent (chunk, embed, store)
- [ ] Re-run failing tasks: gemma4:26b + RAG vs qwen3.6:35b + RAG
- [ ] Benchmark instruction following under heavy context load (minimal vs full retrieval chunks)
- [ ] Lock routing table and build task-specific system prompts
