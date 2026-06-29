# Distribution Guide

This document is for maintainers who want to package `craft-frontend-design` for broader distribution.

## Skill Source

The canonical skill source is:

```text
.agents/skills/craft-frontend-design/
```

Keep the skill usable as a plain folder before packaging it as a plugin.

## Suggested Plugin Layout

```text
plugins/craft-frontend-design/
  .codex-plugin/
    plugin.json
  skills/
    craft-frontend-design/
      SKILL.md
      agents/
        openai.yaml
      references/
      scripts/
      assets/
  assets/
```

## Example `plugin.json`

```json
{
  "name": "craft-frontend-design",
  "version": "0.2.0",
  "display_name": "Craft Frontend Design",
  "description": "Frontend design skill for Codex that improves visual systems, interaction, motion, responsiveness, states, accessibility, and design QA.",
  "author": "Community",
  "license": "MIT",
  "skills": [
    "skills/craft-frontend-design"
  ]
}
```

Adjust fields to match the plugin format required by your Codex distribution environment.

## Local Marketplace Example

A local marketplace entry can point at the plugin directory or packaged archive used by your environment:

```json
{
  "plugins": [
    {
      "id": "craft-frontend-design",
      "name": "Craft Frontend Design",
      "version": "0.2.0",
      "path": "plugins/craft-frontend-design"
    }
  ]
}
```

The exact marketplace format depends on your Codex plugin setup. Do not publish this example unchanged unless it matches your tooling.

## Release Process

1. Update the version in release notes and plugin metadata if a plugin package exists.
2. Run public hygiene:

```bash
python scripts/check_public_hygiene.py .
```

3. Run script validation:

```bash
python -m py_compile .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py
python -m py_compile scripts/check_public_hygiene.py
```

4. Run eval audits:

```bash
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/landing
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/dashboard
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/mobile-h5
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/mini-program
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/game-ui
```

5. Run a Codex skill validator if available locally.
6. Update `CHANGELOG.md`.
7. Create release notes.
8. Tag the release:

```bash
git tag v0.2.0
git push origin v0.2.0
```

9. Package or publish through the plugin process available to your environment.

## Public History Warning

Before publishing a public repository, verify the current tree and intended Git history do not contain local paths, secrets, private screenshots, account identifiers, or internal approval notes.
