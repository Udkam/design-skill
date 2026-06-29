# Public Eval Suite

These evals are small, reproducible fixtures used to verify that the skill and audit script catch public frontend design quality signals.

Run from the repository root:

```bash
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/landing
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/dashboard
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/mobile-h5
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/mini-program
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/game-ui
```

Each case contains:

- `brief.md`: task prompt and expected skill routing;
- representative output fixture;
- `expected-assertions.md`: machine/human assertions;
- `audit-output.txt`: expected audit result;
- `human-rubric.md`: scoring rubric;
- `pass-fail-evidence.md`: evidence that the case reduces template smell, covers states, uses suitable motion, and adapts to platform.

These fixtures are not full production apps. They are representative evidence for public regression checks.
