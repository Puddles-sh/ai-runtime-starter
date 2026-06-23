# Memory Governance Runbook

## Purpose

Keep local AI memory useful, project-scoped, reviewable, and safe.

## Memory Rule

Raw data is not memory.

Memory should be small, durable, useful, sourced, and approved.

## Memory States

- `candidate`: proposed memory awaiting review
- `approved`: active memory allowed into prompts
- `archived`: old or superseded memory kept for audit/rollback
- `rejected`: memory candidate that should not be used

## Review Flow

```text
workflow output
  -> memory candidate
  -> review queue
  -> approve, edit, reject, or archive
```

## What To Approve

- Durable classification rules
- Project aliases
- Writing preferences
- Source quality notes
- Exclusion rules
- Safety and routing policies

## What Not To Approve

- Full raw emails or transcripts
- Secrets, keys, tokens, passwords
- One-time meeting details
- Guesses about ownership or commitments
- Sensitive personal context outside the correct project

## Agent Permissions

Agents may suggest:

- duplicates
- stale memories
- merge proposals
- sensitive-data warnings
- candidate ranking

Agents should not automatically approve, delete, or merge approved memory until the workflow has mature rollback controls.

