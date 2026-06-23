# Local AI Platform Runbook

## Purpose

Operate the local AI environment from the MacBook while keeping project memory, outputs, and model routing controlled.

## Primary Services

- EVO-X2: always-on Ollama/Open WebUI/LiteLLM host
- Gaming PC: RTX 4080 coding-agent and CUDA experimentation host
- MacBook: daily client machine and script runner

## Preflight

Check the EVO host:

```bash
ping evo-x2.local
```

Check Ollama:

```bash
curl http://evo-x2.local:11434/api/tags
```

Check Open WebUI:

```bash
open http://evo-x2.local:3000
```

## Operating Rules

- Local-only project data does not route to cloud models.
- Approved memory is injected into prompts.
- Candidate memory requires review before approval.
- Raw files in `inbox/` are temporary.
- Outputs should be written under the selected project.

## Troubleshooting

If Ollama does not respond:

```bash
ssh charles@evo-x2.local
systemctl status ollama
```

Restart:

```bash
sudo systemctl restart ollama
```

