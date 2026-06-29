# Negative Eval Suite

These fixtures intentionally contain bad frontend design patterns. They verify that the audit script catches common regressions instead of only passing positive examples.

Run from the repository root:

```bash
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/negative/cases/purple-blue-saas-hero
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/negative/cases/missing-alt-and-focus
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/negative/cases/motion-without-reduced-motion
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/negative/cases/desktop-style-mini-program
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/negative/cases/dashboard-as-marketing-page
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/negative/cases/personal-site-as-saas-hero
```

Expected result: each command should produce findings. Cases with error-level findings return a non-zero exit code; warning-only cases may return zero.
