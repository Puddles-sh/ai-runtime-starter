# AI Runtime Starter

This repository is the source-controlled starter for the local AI runtime that will eventually run on the EVO.

It should contain source code, templates, runbooks, tests, and Docker Compose files.

It should not contain secrets, raw private data, model files, vector databases, audit databases, or runtime logs.

## Intended Split

```text
GitHub repo:
  source code
  Docker Compose templates
  env examples
  tests
  runbooks
  prompt templates

iCloud AI folder:
  project memory
  runbooks
  prompts
  outputs
  candidate memory

EVO runtime:
  real secrets
  certificates
  token caches
  models
  Docker volumes
  vector DBs
  audit/rollback databases
```

## First Services

Initial services will likely be:

- Ollama
- Open WebUI
- LiteLLM
- homelab scripts
- future NOC/Admin agent prototype

## Local Runtime Target

Recommended EVO runtime layout:

```text
/opt/ai-runtime/
  apps/
  compose/
  config/
  data/
  logs/
  scripts/
  secrets/
```

Secrets stay on the EVO and are never committed.

## First Commands

After the EVO is ready:

```bash
docker compose -f compose/open-webui/docker-compose.yml up -d
```

For now, this repo is a safe starting structure.

