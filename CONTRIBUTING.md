# Contributing

Contributions should keep this repository public-ready and reusable.

## Good Contributions

- Improve `SKILL.md` while keeping it concise.
- Add or refine reference playbooks.
- Add audit rules with low false-positive risk.
- Add eval cases that demonstrate real frontend design risks.
- Improve installation, distribution, or publication docs.

## Reference Changes

When adding a reference:

- make it a playbook, not a long essay;
- include decision steps and acceptance criteria;
- avoid copying proprietary text, images, layouts, or animation sequences;
- cite external sources as links when relevant;
- keep it one level under `references/`.

## Audit Rule Changes

When changing `audit_frontend_design.py`:

```bash
python -m py_compile .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/landing
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/dashboard
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/mobile-h5
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/mini-program
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/game-ui
```

Explain new false-positive risks in the pull request.

## Eval Changes

Each eval case should include:

- `brief.md`;
- representative output fixture;
- `expected-assertions.md`;
- `audit-output.txt`;
- `human-rubric.md`;
- `pass-fail-evidence.md`.

## Public Hygiene

Before submitting:

```bash
python scripts/check_public_hygiene.py .
```

Do not submit local paths, personal account names, private screenshots, API keys, tokens, `.env` values, or private logs.
