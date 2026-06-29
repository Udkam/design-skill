# Craft Frontend Design Plugin Skeleton

This directory is a local/plugin-ready package skeleton for `craft-frontend-design`.

It is generated from the canonical skill at:

```text
.agents/skills/craft-frontend-design/
```

This skeleton does not mean the plugin has been published to an official Codex marketplace.

## Regenerate

From the repository root:

```bash
python scripts/build_plugin_package.py
```

On Windows, use `py` if `python` is unavailable:

```powershell
py scripts\build_plugin_package.py
```

## Contents

- `.codex-plugin/plugin.json`: local plugin manifest.
- `skills/craft-frontend-design/`: synchronized skill copy.

## Local Checking

Run repository validation from the root:

```bash
python scripts/check_public_hygiene.py .
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/landing
```

If your Codex installation provides a plugin validator, run it against this directory.
