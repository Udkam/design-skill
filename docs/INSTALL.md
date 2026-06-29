# Install Craft Frontend Design

## Prerequisites

- A Codex client that supports agent skills, such as Codex CLI, IDE extension, or Codex app.
- Python 3.10+ to run the optional audit scripts.
- Git if installing from this repository.

## Clone

```bash
git clone https://github.com/Udkam/design-skill.git
cd design-skill
```

## Repo-Scoped Install

Use this when a project should carry the skill with its source code.

macOS/Linux:

```bash
mkdir -p "<target-project>/.agents/skills"
cp -R ".agents/skills/craft-frontend-design" "<target-project>/.agents/skills/"
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "<target-project>\.agents\skills" | Out-Null
Copy-Item -Recurse -Force ".agents\skills\craft-frontend-design" "<target-project>\.agents\skills\"
```

Start or restart Codex from the target project.

## User-Global Install

Use this when the skill should be available across projects for one user.

macOS/Linux:

```bash
mkdir -p "$HOME/.agents/skills"
cp -R ".agents/skills/craft-frontend-design" "$HOME/.agents/skills/"
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.agents\skills" | Out-Null
Copy-Item -Recurse -Force ".agents\skills\craft-frontend-design" "$env:USERPROFILE\.agents\skills\"
```

Restart Codex if the skill does not appear.

## Symlink Install

Symlinks make updates easier during development.

macOS/Linux:

```bash
mkdir -p "$HOME/.agents/skills"
ln -s "$(pwd)/.agents/skills/craft-frontend-design" "$HOME/.agents/skills/craft-frontend-design"
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.agents\skills" | Out-Null
New-Item -ItemType SymbolicLink `
  -Path "$env:USERPROFILE\.agents\skills\craft-frontend-design" `
  -Target (Resolve-Path ".agents\skills\craft-frontend-design")
```

If symlink creation is blocked on Windows, use a normal copy install.

## Confirm Discovery

Try an explicit invocation in a project where the skill is installed:

```text
Use $craft-frontend-design to review this frontend and remove AI-template patterns.
```

If the skill does not appear:

- restart Codex;
- confirm the folder name is `craft-frontend-design`;
- confirm `SKILL.md` is directly inside that folder;
- check whether another skill with the same name is installed in a higher-priority location.

## Run Local Validation

```bash
python -m py_compile .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/landing
python scripts/check_public_hygiene.py .
```

Windows PowerShell can use `py`:

```powershell
py -m py_compile .agents\skills\craft-frontend-design\scripts\audit_frontend_design.py
py .agents\skills\craft-frontend-design\scripts\audit_frontend_design.py evals\cases\landing
py scripts\check_public_hygiene.py .
```

If your Codex installation provides a skill validator, run it against `.agents/skills/craft-frontend-design`. The validator path varies by installation and is optional.

## Troubleshooting

### Skill does not appear

Restart Codex. Confirm the installed folder is exactly:

```text
<skills-root>/craft-frontend-design/SKILL.md
```

### Same-name skill conflict

Codex may see multiple skills named `craft-frontend-design`. Remove or disable older copies, then restart Codex.

### Windows `python` is unavailable

Use `py` instead of `python`.

### Audit script permission denied

Run through Python directly:

```bash
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py <project-path>
```

### Plugin vs skill

A skill is the reusable workflow folder. A plugin is a distribution package that can contain one or more skills plus plugin metadata, assets, tools, or app integrations. This repository currently ships the skill package and documents a plugin-ready layout.
