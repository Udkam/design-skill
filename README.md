# Craft Frontend Design

Craft Frontend Design is a Codex frontend design skill that helps Codex reduce template-heavy UI, obvious AI visual patterns, and stiff animation when building or reviewing websites, web apps, dashboards, mobile H5 flows, mini-program-style interfaces, and interactive UI.

This repository is a public-ready skill package. It can be copied into a project, installed globally for a user, or used as the source for a future Codex plugin package.

## Use Cases

Use this skill for:

- building new frontend experiences;
- refactoring UI and interaction design;
- reviewing landing pages and product sites for AI-template patterns;
- improving motion, interaction feedback, and responsive behavior;
- checking state coverage, accessibility, and design QA;
- dashboards, tools, workspaces, portfolios, ecommerce/content sites, mobile H5, WeChat mini-program-style flows, and game/interactive toy UI.

Do not use this skill for:

- logos, posters, or standalone brand strategy;
- pure Figma-only work with no frontend implementation;
- backend-only tasks;
- unauthorized copying of competitor sites;
- broad "all design" tasks unrelated to frontend visual and interaction implementation.

## Installation

### A. Repo-Scoped Install

Copy the skill folder into the target project's skill directory:

```text
<target-project>/.agents/skills/craft-frontend-design/
```

Then start or restart Codex from that target project.

### B. User-Global Install

Install the skill for all projects used by the current user.

macOS/Linux:

```bash
mkdir -p "$HOME/.agents/skills"
cp -R .agents/skills/craft-frontend-design "$HOME/.agents/skills/"
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.agents\skills" | Out-Null
Copy-Item -Recurse -Force ".agents\skills\craft-frontend-design" "$env:USERPROFILE\.agents\skills\"
```

Restart Codex if the skill does not appear immediately.

### C. Plugin-Ready Install

This repository is structured so the skill can later be packaged as a Codex plugin. If a plugin package exists, install it through your local marketplace setup or the Codex plugin marketplace available to your environment.

Current status: this repository is a skill package, not a guarantee that the skill is published in an official plugin marketplace.

## Usage

Example prompts:

```text
Use $craft-frontend-design to redesign this dashboard.
Use $craft-frontend-design to review this landing page and remove AI-template patterns.
Use $craft-frontend-design to implement a mobile-first mini program style flow.
Use $craft-frontend-design to tune the motion and responsive states for this web app.
```

## Validation

Run from the repository root.

```bash
python -m py_compile .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/landing
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/dashboard
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/mobile-h5
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/mini-program
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/game-ui
python .agents/skills/craft-frontend-design/scripts/audit_frontend_design.py evals/cases/personal-site-interactive
python scripts/check_public_hygiene.py .
```

On Windows, use `py` instead of `python` if `python` is not available:

```powershell
py -m py_compile .agents\skills\craft-frontend-design\scripts\audit_frontend_design.py
py scripts\check_public_hygiene.py .
```

If your Codex installation includes a skill validator, you can also run it against:

```text
.agents/skills/craft-frontend-design
```

The validator is optional because its path varies by Codex installation.

## Update

For a repo-scoped install:

```bash
git pull
cp -R .agents/skills/craft-frontend-design <target-project>/.agents/skills/
```

For a user-global install, copy or symlink the updated skill folder into the global skills directory again, then restart Codex if needed.

## Uninstall

Delete the installed skill directory:

```text
<target-project>/.agents/skills/craft-frontend-design
$HOME/.agents/skills/craft-frontend-design
%USERPROFILE%\.agents\skills\craft-frontend-design
```

Restart Codex if the old skill still appears.

## Repository Layout

```text
.agents/skills/craft-frontend-design/   # Skill package
docs/                                   # Install, distribution, and publication docs
evals/                                  # Reproducible public eval suite
plugins/                                # Generated local/plugin-ready skeleton
scripts/                                # Repository-level validation scripts
```

## License

MIT. See `LICENSE`.
