# Publication Checklist

Run this before making a public release or publishing a plugin package.

## Required

- [ ] `README.md` has public install/use/update/uninstall instructions.
- [ ] `docs/INSTALL.md` uses only generic placeholders.
- [ ] `docs/DISTRIBUTION.md` describes plugin-ready packaging without claiming marketplace availability.
- [ ] `AGENTS.md` contains repo rules only, no private paths.
- [ ] `CHANGELOG.md` is updated.
- [ ] `LICENSE` is present.
- [ ] `SECURITY.md` warns against secrets, local paths, and private screenshots.
- [ ] `.gitignore` ignores local notes, logs, caches, screenshots, temp eval output, and secrets.
- [ ] `python scripts/check_public_hygiene.py .` passes.
- [ ] `python -m py_compile .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py` passes.
- [ ] Eval audits pass for all cases.
- [ ] Optional skill validator passes if available.
- [ ] Git history intended for publication is free of private/local data.

## Eval Commands

```bash
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/landing
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/dashboard
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/mobile-h5
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/mini-program
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/game-ui
```

## Do Not Publish

Do not publish if any current tree or intended public history contains:

- personal user paths;
- emails or account IDs not meant as public contact;
- `.env` values;
- API keys, tokens, passwords, private keys;
- private screenshots or local browser/session notes;
- internal approval chat logs;
- machine-specific validation paths.
