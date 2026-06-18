# No Secrets Policy

This repository must never contain real secrets.

Do not commit:

- `.env` files
- app client secrets
- certificate private keys
- OAuth tokens
- access tokens
- refresh tokens
- raw audit logs
- raw customer exports
- raw transcripts
- database files
- model files
- vector indexes

Allowed:

- `.env.example`
- config templates
- sanitized sample data
- runbooks
- source code
- tests
- prompt templates

Before every commit, run:

```bash
git status
git diff --cached
```

If unsure, do not commit the file.

