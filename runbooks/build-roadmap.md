# Homelab Build Roadmap

## Philosophy

Each phase must prove itself before the next adds complexity.
No automation without a working manual version first.
Security and isolation built in from the start, not retrofitted.

---

## Phase 1 — Hardware and OS Foundation

**Goal:** EVO is online, stable, and reachable.

- [ ] Ubuntu 24.04 LTS installed
- [ ] ROCm drivers installed, GPU verified
- [ ] Docker installed
- [ ] Ollama installed natively
- [ ] Static IP / reserved DHCP lease confirmed
- [ ] EVO reachable from MacBook by hostname

Runbook: `evo-first-boot.md`

---

## Phase 2 — Model Installation and Benchmarking

**Goal:** Know which model is best for which task before building anything on top of them.

- [ ] All models pulled (see first-boot runbook for pull order)
- [ ] Benchmark script run across all models with `--prompt-set all`
- [ ] Baseline performance results saved to outputs folder
- [ ] Routing table drafted based on results

Runbook: `model-benchmarking.md`

---

## Phase 3 — Git and Backup Standards

**Goal:** Everything built from this point forward is version controlled from day one.

- [ ] Git installed on EVO
- [ ] SSH key generated, added to GitHub
- [ ] `ai-runtime-starter` repo cloned to `/opt/ai-runtime`
- [ ] Commit and push workflow confirmed working
- [ ] `.gitignore` covers secrets, model files, logs, and volumes

---

## Phase 4 — First Support Agent (Manual Output Mode)

**Goal:** Agent parses requests and produces PowerShell scripts for manual review and execution.
No automation yet. Human runs every script. Build trust in output quality first.

### Azure Key Vault Setup
- [ ] App registration created in client tenant (read-only Graph API permissions)
- [ ] Key Vault created in client tenant
- [ ] Service principal credentials stored in Key Vault
- [ ] PowerShell auth pattern tested — secret pulled from vault into memory, never logged

### Script Library (Starting Set)
- [ ] Add user to Azure AD / Entra group
- [ ] Remove user from group
- [ ] List group members
- [ ] Check user license assignment
- [ ] Create task from screenshot (vision model parses → structured output)
- [ ] Each script has a corresponding revert script

### Agent Behavior
- [ ] Parser receives request (manual input to start)
- [ ] Scout pulls relevant script template and memory
- [ ] Auditor confirms Graph cmdlets are current (flags if RAG needed)
- [ ] Scorer rates confidence and risk
- [ ] Planner outputs a PowerShell script for manual execution
- [ ] Output saved to project outputs folder with timestamp and request ID

---

## Phase 5 — Training Review

**Goal:** Audit every Phase 4 interaction before expanding scope.

- [ ] Review all Planner outputs for accuracy and quality
- [ ] Score against rubric (accuracy, completeness, format, hallucination risk)
- [ ] Identify which models performed best per task type
- [ ] Update routing table with validated assignments
- [ ] Promote strong patterns to approved memory
- [ ] Archive or discard weak patterns

---

## Phase 6 — Comms and Access Layer

**Goal:** Remote access and notification pipeline working before any automation is added.
Telegram is the primary human interface — low friction keeps the human in the loop naturally.
If checking in requires a laptop, the gate gets bypassed. If it's a phone tap, it doesn't.

### Access
- [ ] Tailscale installed on EVO and MacBook
- [ ] EVO reachable via Tailscale from anywhere
- [ ] Open WebUI deployed via Docker, reachable on LAN and via Tailscale
- [ ] Enchanted app configured on MacBook and iPhone pointing to EVO via Tailscale

### Telegram Bot
- [ ] Bot created via BotFather, webhook configured to EVO
- [ ] Bot locked to your Telegram user ID — no other user can interact with it
- [ ] Inbound message parser built — accepts plain language problem descriptions
- [ ] Message routed to correct agent based on content (research vs. approval vs. status)

### Message Formats

**Inbound — you to bot (examples):**
```
"T-Mobile iPhones, Warp enabled, Apple services dead on cellular"
"Approve request #1042"
"Status on last run"
"What scripts ran today"
```

**Outbound — bot to you:**

Research result (high confidence):
```
🔍 Research complete — HIGH confidence (85%)

Root cause: T-Mobile IPv6 CGNAT + Warp DNS intercept

Fix:
1. Add local DNS fallback for push.apple.com
2. Add gateway.icloud.com to split tunnel exclusions
3. Test on cellular before pushing MDM policy

Sources:
• r/sysadmin (412 upvotes, 28 confirmed) [link]
• Cloudflare Warp known issues — staff reply [link]
• Apple MDM whitepaper p.14 [link]

[Forward to tech] [Send me more detail] [Archive]
```

Approval request:
```
⚠️ Approval required — Request #1042

Task: Remove user jsmith@contoso.com from group IT-Admins
Risk: MEDIUM — group membership change, revert available
Requested: 2026-07-15 14:32
Script: view-script-1042.ps1

[Approve] [Reject] [Hold] [Show script]
```

Status update:
```
✅ Request #1042 complete
Executed: Remove-MgGroupMember
Duration: 4.2s
Revert available: revert-1042.ps1
Trace: saved to outputs/traces/1042.json
```

Error / low confidence:
```
⚠️ Low confidence result (34%)

Could not find a high-confidence resolution.
Top partial match: DNS caching issue (r/sysadmin, 12 upvotes)

Recommend: Manual investigation
Trace saved for review.

[Search again with more detail] [Escalate] [Dismiss]
```

### Reply Parsing
- [ ] [Approve] / [Reject] / [Hold] inline keyboard buttons confirmed working
- [ ] Plain text replies also parsed ("approve", "reject", "yes", "no")
- [ ] Unknown replies prompt clarification rather than silently failing
- [ ] All interactions logged with timestamp and your Telegram user ID

### Done Criteria
- [ ] You can send a plain language problem from your phone and get a research result back
- [ ] You can approve or reject a pending action from your phone in one tap
- [ ] Bot ignores messages from any user ID that isn't yours
- [ ] All Telegram interactions logged to trace file

---

## Phase 7 — Foundation Complete

**Goal:** Solid, proven base to expand from. Everything working, documented, and version controlled.

- [ ] All Phase 1-6 criteria met
- [ ] Runbooks up to date
- [ ] Git history clean with meaningful commit messages
- [ ] Benchmark results archived
- [ ] Memory candidates reviewed, approved set clean

---

## Phase 8 — Memory Librarian

**Goal:** Memory governance that scales. Replace manual candidate review with an agent-assisted curation process.

- [ ] Curator agent built and integrated into pipeline
- [ ] Memory scoring and rating system defined
- [ ] Stale memory detection implemented
- [ ] Candidate → approved → archive promotion flow working
- [ ] Evaluate readiness to migrate from markdown to vector DB (Qdrant)

---

## Phase 9 — Automated Execution with Human Confirmation

**Goal:** Agent executes scripts automatically after Telegram approval. Revert available on every action.

- [ ] Dispatcher agent built
- [ ] Pre-action state snapshot stored before every execution
- [ ] Revert function confirmed working for each script in library
- [ ] Telegram approval gate integrated into pipeline
- [ ] Full trace logging on every run
- [ ] Audit trail readable and exportable

---

## Phase 10 — Expand Scope

**Goal:** Grow the script library, improve routing, onboard additional clients or use cases.

- [ ] Zendesk email ingestion working
- [ ] Teams screenshot → task pipeline working end to end
- [ ] Per-client Key Vault isolation confirmed
- [ ] ZTNA via Cloudflare Warp + Azure AD verified
- [ ] LiteLLM routing layer deployed for multi-model management

---

## Phase 11 — Live RAG Pipeline (MS Graph Source of Truth)

**Goal:** Give the Auditor agent a live, versioned index of Microsoft Graph API docs and
changelogs so it can verify cmdlets are current before any script reaches the Planner.
Eliminates hallucinated Graph endpoints and deprecated cmdlet usage.

### Architecture

```
Nightly crawler → MS Graph changelog + API docs
               → chunk and embed via nomic-embed-text
                 → store in Qdrant vector DB
                   → Auditor queries index on every PowerShell task
                     → flags deprecated or unrecognized cmdlets
                       → Planner gets verified context
```

### Crawler
- [ ] Scheduled crawler built (Python, runs nightly via cron)
- [ ] Targets: MS Graph changelog, Graph API reference, Microsoft.Graph PowerShell module docs
- [ ] Content chunked and cleaned before embedding
- [ ] Delta updates only — re-embed changed pages, not the full corpus every night
- [ ] Crawl log written with timestamp and pages updated

### Embedding and Storage
- [ ] Qdrant deployed via Docker on EVO
- [ ] `nomic-embed-text` used for all embeddings (already in model stack)
- [ ] Collection schema: chunk text, source URL, crawl date, doc version
- [ ] Similarity search confirmed working with test queries

### Auditor Integration
- [ ] Auditor queries Qdrant before every PowerShell/Graph generation task
- [ ] Returns: cmdlet found / not found / deprecated with source URL and date
- [ ] Flagged results passed to Planner as context warnings
- [ ] Audit log records which docs were consulted for each request

### Done Criteria
- [ ] Qdrant running and reachable on EVO
- [ ] Crawler runs nightly, delta updates confirmed
- [ ] Auditor successfully flags a known deprecated cmdlet in test
- [ ] Source URLs logged for every consulted doc

---

## Phase 12 — Self-Extending Script Library (Nightly Suggestion Agent)

**Goal:** An agent that runs nightly, analyzes completed task history, identifies gaps in
the script library, and surfaces suggestions for new scripts. The system grows its own
capabilities based on what it's actually being asked to do.

### How It Works

```
Nightly cron → Librarian agent reads completed task traces (last 30 days)
             → clusters task types by category and frequency
               → compares against existing script library index
                 → identifies: high-frequency tasks with no script
                               script gaps causing manual fallback
                               new task types not seen before
                   → generates suggested script specs (not the scripts themselves)
                     → sends suggestion digest to Telegram for review
                       → approved suggestions added to script library backlog
```

### Key Design Decisions
- Agent suggests specs, not finished scripts — human approves before anything is built
- Frequency threshold configurable — only suggest if a task type appears 3+ times
- Suggestions include: task description, example requests that triggered it, estimated complexity
- Backlog lives in a markdown file, promoted to script library after human review

### Implementation
- [ ] Task trace log schema defined — every completed request stored with category and outcome
- [ ] Librarian agent built — reads traces, clusters by type, diffs against script index
- [ ] Suggestion format defined — structured markdown spec per suggested script
- [ ] Telegram digest working — nightly summary with approve/defer/dismiss per suggestion
- [ ] Backlog file managed — approved specs queued for build, dismissed ones archived
- [ ] First real suggestion validated — agent surfaces something genuinely useful

---

### GitHub Candidate Scout (Graceful Fallback)

When the Scout finds no match in the validated library and no nightly suggestion covers
the gap, it searches GitHub for community scripts rather than returning a hard failure.
The user gets a candidate for review, not a dead end.

#### Flow

```
Request → Scout searches validated library
        → no match
          → Scout searches GitHub (Microsoft.Graph, PowerShell, Intune keywords)
            → ranks candidates by: stars, last commit date, license, module usage
              → filters out: AzureAD/MSOnline module usage, hardcoded credentials,
                             no error handling, GPL/restrictive licenses
                → Telegram notification:

"⚠️ No validated script for this task.

Task: Export all conditional access policies to CSV
Match: github.com/user/repo — ConditionalAccess-Export.ps1
Stars: 312 | Last commit: 2026-04-12 | License: MIT

Confidence: HIGH — Microsoft.Graph module, error handling present,
no hardcoded credentials detected.

[View script] [Add to review queue] [Dismiss]"

→ approved candidate enters manual review
  → validated, templatized to standard header, revert script added
    → promoted to validated library
```

#### Candidate Quality Filters (auto-disqualify if any true)
- Uses AzureAD or MSOnline module
- Hardcoded tenant ID, client ID, or credential strings detected
- Last commit older than 18 months
- No error handling present
- Restrictive license (GPL, no-commercial-use)
- No revert path identifiable

#### Implementation
- [ ] GitHub search API integrated into Scout fallback path
- [ ] Quality filter logic built — auto-disqualifies low-quality candidates
- [ ] Candidate scoring: stars + recency + module correctness + license
- [ ] Telegram notification format for candidate found vs no candidate found
- [ ] Review queue file managed — candidates staged for human validation
- [ ] Promotion flow: reviewed → templatized → revert added → library index updated
- [ ] First real candidate promoted end to end

### Done Criteria
- [ ] Librarian runs nightly without manual trigger
- [ ] At least one useful script suggestion generated from real task history
- [ ] Telegram digest readable and actionable
- [ ] Approved suggestion successfully built into a working script
- [ ] Unknown task type triggers GitHub scout, candidate delivered to Telegram
- [ ] At least one GitHub candidate successfully promoted to validated library

---

## Phase 13 — Support Research Bot (Multi-Source Intelligence)

**Goal:** An agent that takes a real-world IT problem as input, searches a curated set of
trusted community and vendor sources simultaneously, and returns a ranked list of relevant
findings with sources — cutting days of manual research down to minutes. Human still
evaluates and decides. The bot researches, not fixes.

### The Problem It Solves

Some issues have no official documentation. The solution exists scattered across a Reddit
thread, a vendor community post, and a carrier whitepaper. This bot connects those dots
automatically while you keep working.

**Example:** T-Mobile iPhones + Cloudflare Warp + Apple services failing on cellular.
Root cause: IPv6 DNS routing issue. Solution: local DNS fallback on Apple domains.
The answer existed in the community — finding it took 3 days manually. This bot does
it in one prompt.

### Sources (Curated, Expandable)

| Source | Type | Signal |
|---|---|---|
| r/sysadmin | Community | Upvote count + comment confirmation |
| r/PowerShell | Community | Upvote count + solution flair |
| r/Intune | Community | Upvote count |
| r/azuread | Community | Upvote count |
| r/tmobile / r/ATT / r/verizon | Community | Carrier-specific issues |
| Cloudflare Community | Vendor forum | Staff replies weighted higher |
| Microsoft Tech Community | Vendor forum | Verified answer flag |
| Apple MDM whitepapers | Vendor docs | Official, version-tagged |
| CISA advisories | Security | Threat intel and known vulnerabilities |

### Architecture

```
Problem prompt → Research agent fans out to all sources simultaneously
               → Reddit API for community threads (ranked by upvotes)
               → Qdrant semantic search across indexed whitepapers and vendor docs
               → Web search for recent vendor community posts
                 → results ranked by: source trust tier + recency + upvote signal
                   → top findings summarized with source URL and confidence
                     → suggested investigation path generated
                       → delivered via Telegram or Open WebUI
```

### Key Design Decisions
- **Research only** — bot surfaces findings, never executes a fix
- **Source transparency** — every finding includes URL, date, and why it was ranked
- **Confidence scoring** — community solutions with 100+ upvotes and confirming comments
  scored higher than a single uncorroborated post
- **Expandable source list** — new subreddits or doc sources added via config, not code
- **Problem stays local** — client-specific details never leave the EVO

### Implementation
- [ ] Reddit API credentials configured (free tier sufficient for nightly + on-demand)
- [ ] Source trust tier config defined (vendor docs > verified community > general threads)
- [ ] Research agent built — fan-out queries, result aggregation, ranking logic
- [ ] Qdrant index extended to include whitepapers and vendor docs (extends Phase 11)
- [ ] Summary format defined — findings, sources, confidence, investigation path
- [ ] Delivery working — Telegram message or Open WebUI response
- [ ] Test case validated — T-Mobile/Warp/IPv6 DNS scenario returns correct findings

### Done Criteria
- [ ] Bot takes a plain-language problem description as input
- [ ] Returns ranked findings with sources in under 2 minutes
- [ ] At least one real-world problem solved faster than manual search
- [ ] Source list documented and expandable without code changes

---

## Guiding Rules

1. Manual before automated — prove the output is correct before the agent runs it unsupervised
2. Every action has a revert
3. Secrets never leave the vault, never touch a log
4. Every interaction is traced and stored
5. Memory is curated, not accumulated
6. Git from day one — if it isn't committed it doesn't exist
