#!/usr/bin/env python3
"""Build the local plugin-ready skeleton from the canonical skill folder."""

from __future__ import annotations

import json
import os
import shutil
import stat
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_SOURCE = ROOT / ".agents" / "skills" / "craft-frontend-design"
PLUGIN_ROOT = ROOT / "plugins" / "craft-frontend-design"
PLUGIN_SKILL = PLUGIN_ROOT / "skills" / "craft-frontend-design"
PLUGIN_MANIFEST = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"


PLUGIN_JSON = {
    "name": "craft-frontend-design",
    "version": "0.3.0",
    "description": "Frontend design skill for Codex that improves visual systems, interaction, motion, responsiveness, states, accessibility, and design QA.",
    "author": {
        "name": "Craft Frontend Design contributors",
        "url": "https://github.com/Udkam/codex-design-skill",
    },
    "homepage": "https://github.com/Udkam/codex-design-skill",
    "repository": "https://github.com/Udkam/codex-design-skill",
    "license": "MIT",
    "keywords": [
        "codex",
        "skill",
        "frontend",
        "design",
        "ui",
        "motion",
        "accessibility",
    ],
    "skills": "./skills/",
    "interface": {
        "displayName": "Craft Frontend Design",
        "shortDescription": "Build and review polished frontend experiences.",
        "longDescription": "A Codex skill for frontend visual systems, interaction, motion, responsive behavior, state coverage, accessibility, inspiration sampling, and design QA.",
        "developerName": "Craft Frontend Design contributors",
        "category": "Productivity",
        "capabilities": ["Write", "Review"],
        "websiteURL": "https://github.com/Udkam/codex-design-skill",
        "defaultPrompt": [
            "Use $craft-frontend-design to redesign this dashboard.",
            "Use $craft-frontend-design to remove AI-template UI patterns.",
            "Use $craft-frontend-design to tune motion and responsive states.",
        ],
        "brandColor": "#146B4F",
    },
}


README = """# Craft Frontend Design Plugin Skeleton

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
py scripts\\build_plugin_package.py
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
"""


def copy_skill() -> None:
    if not SKILL_SOURCE.exists():
        raise SystemExit(f"Missing skill source: {SKILL_SOURCE}")
    if PLUGIN_SKILL.exists():
        def clear_readonly(function, path, _excinfo):
            os.chmod(path, stat.S_IWRITE)
            function(path)

        shutil.rmtree(PLUGIN_SKILL, onexc=clear_readonly)
    PLUGIN_SKILL.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(
        SKILL_SOURCE,
        PLUGIN_SKILL,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
    )


def write_manifest() -> None:
    PLUGIN_MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    PLUGIN_MANIFEST.write_text(json.dumps(PLUGIN_JSON, indent=2) + "\n", encoding="utf-8")


def write_readme() -> None:
    PLUGIN_ROOT.mkdir(parents=True, exist_ok=True)
    (PLUGIN_ROOT / "README.md").write_text(README, encoding="utf-8")


def main() -> int:
    copy_skill()
    write_manifest()
    write_readme()
    print(f"Built plugin skeleton at {PLUGIN_ROOT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
