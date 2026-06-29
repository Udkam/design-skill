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

This repository includes that local/plugin-ready skeleton under `plugins/craft-frontend-design/`.
It is a package skeleton only; it does not mean the plugin has been published to an official Codex marketplace.

## Generate Or Refresh The Skeleton

The plugin skill copy is generated from the canonical repo-scoped skill:

```text
.agents/skills/craft-frontend-design/
```

Regenerate it from the repository root:

```bash
python scripts/build_plugin_package.py
```

On Windows, use `py` if needed:

```powershell
py scripts\build_plugin_package.py
```

The script refreshes:

```text
plugins/craft-frontend-design/.codex-plugin/plugin.json
plugins/craft-frontend-design/skills/craft-frontend-design/
plugins/craft-frontend-design/README.md
```

Do not hand-edit the generated skill copy unless you also update the canonical skill and rerun the script.

## Local Checks

Run the normal public checks:

```bash
python scripts/check_public_hygiene.py .
python -m py_compile .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py
python -m py_compile scripts/build_plugin_package.py
python -m py_compile scripts/package_release.py
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/landing
```

If your Codex installation includes a plugin validator, run it against:

```text
plugins/craft-frontend-design
```

The validator path varies by installation, so this repository does not hard-code it.

## Delete Generated Skeleton

If you want to remove the generated plugin package while keeping the source skill:

```bash
rm -rf plugins/craft-frontend-design
```

Windows PowerShell:

```powershell
Remove-Item -Recurse -Force plugins\craft-frontend-design
```

Regenerate later with `python scripts/build_plugin_package.py`.

## Example `plugin.json`

```json
{
  "name": "craft-frontend-design",
  "version": "0.3.0",
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
      "version": "0.3.0",
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
python -m py_compile scripts/build_plugin_package.py
python -m py_compile scripts/package_release.py
```

4. Run eval audits:

```bash
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/landing
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/dashboard
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/mobile-h5
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/mini-program
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/game-ui
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/personal-site-interactive
```

5. Run negative eval audits and confirm they produce the expected findings:

```bash
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/negative/cases/purple-blue-saas-hero
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/negative/cases/missing-alt-and-focus
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/negative/cases/motion-without-reduced-motion
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/negative/cases/desktop-style-mini-program
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/negative/cases/dashboard-as-marketing-page
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/negative/cases/personal-site-as-saas-hero
```

6. Regenerate the plugin skeleton:

```bash
python scripts/build_plugin_package.py
```

7. Generate local release archives:

```bash
python scripts/package_release.py
```

Expected local outputs:

```text
dist/craft-frontend-design-skill-v0.3.0.zip
dist/craft-frontend-design-plugin-v0.3.0.zip
```

These archives are local release artifacts. They are ignored by Git unless a future release policy explicitly chooses to track them.

8. Run Codex skill/plugin validators if available locally.
9. Update `CHANGELOG.md`.
10. Create release notes.
11. Tag the release:

```bash
git tag v0.3.0
git push origin v0.3.0
```

12. Package or publish through the plugin process available to your environment.

## Public History Warning

Before publishing a public repository, verify the current tree and intended Git history do not contain local paths, secrets, private screenshots, account identifiers, or internal approval notes.
