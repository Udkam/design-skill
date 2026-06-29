# Repository Instructions

This is a public Codex skill repository. Keep it reusable by people who clone the repository, copy the skill into another project, install it globally, or package it as a plugin.

## Editing Rules

- Keep `SKILL.md` focused and under control; put detailed playbooks in `references/`.
- Keep public documentation free of personal paths, local account names, emails, private screenshots, internal approval notes, and machine-specific commands.
- Do not commit API keys, tokens, `.env` files, private URLs, local logs, or personal debugging artifacts.
- Use placeholders such as `<repo-root>`, `<skill-dir>`, `$HOME`, and `%USERPROFILE%` in docs.
- If changing docs, release files, scripts, or evals, run the public hygiene check.
- If changing `audit_frontend_design.py`, run Python compile validation and the eval suite.
- Preserve `evals/` as reproducible evidence, not one-off notes.

## Validation

Run from the repository root.

```bash
python -m py_compile .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/landing
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/dashboard
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/mobile-h5
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/mini-program
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/game-ui
python scripts/check_public_hygiene.py .
```

On Windows, `py` may be used instead of `python`.

If a Codex skill validator is available locally, run it against `.agents/skills/craft-frontend-design`. Do not hard-code a private validator path in repository files.

## Git

- Commit related changes in reviewable groups.
- Push completed verified work to `origin/main` unless a publication risk is found.
- Before public releases, ensure the current tree and intended Git history are free of local/private data.
