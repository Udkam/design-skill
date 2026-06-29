#!/usr/bin/env python3
"""Create local release archives for the skill and plugin skeleton."""

from __future__ import annotations

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.3.0"
SKILL_SOURCE = ROOT / ".agents" / "skills" / "craft-frontend-design"
PLUGIN_SOURCE = ROOT / "plugins" / "craft-frontend-design"
DIST = ROOT / "dist"

EXCLUDED_PARTS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".codex-log",
    "screenshots",
    "tmp-audit-fixtures",
}
EXCLUDED_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".tmp",
    ".log",
}
EXCLUDED_NAMES = {
    ".DS_Store",
    ".env",
    ".env.local",
    "Thumbs.db",
}


def should_skip(path: Path) -> bool:
    parts = set(path.parts)
    if parts & EXCLUDED_PARTS:
        return True
    if path.name in EXCLUDED_NAMES:
        return True
    if path.suffix in EXCLUDED_SUFFIXES:
        return True
    if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"} and "evals" not in parts:
        return True
    return False


def write_zip(source: Path, archive_root: Path, destination: Path) -> None:
    if not source.is_dir():
        raise FileNotFoundError(f"Missing source directory: {source}")

    with ZipFile(destination, "w", ZIP_DEFLATED) as archive:
        for path in sorted(source.rglob("*")):
            if path.is_dir() or should_skip(path):
                continue
            archive.write(path, path.relative_to(archive_root).as_posix())


def main() -> int:
    DIST.mkdir(exist_ok=True)
    skill_zip = DIST / f"craft-frontend-design-skill-v{VERSION}.zip"
    plugin_zip = DIST / f"craft-frontend-design-plugin-v{VERSION}.zip"

    write_zip(SKILL_SOURCE, ROOT, skill_zip)
    write_zip(PLUGIN_SOURCE, ROOT, plugin_zip)

    print(f"Wrote {skill_zip.relative_to(ROOT).as_posix()}")
    print(f"Wrote {plugin_zip.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
