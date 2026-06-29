#!/usr/bin/env python3
"""Scan a repository tree for public-release hygiene risks."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


TEXT_EXTENSIONS = {
    ".css",
    ".html",
    ".js",
    ".json",
    ".jsx",
    ".md",
    ".mjs",
    ".py",
    ".scss",
    ".ts",
    ".tsx",
    ".txt",
    ".vue",
    ".wxml",
    ".wxss",
    ".yaml",
    ".yml",
}

SKIP_DIRS = {
    ".git",
    ".next",
    ".nuxt",
    ".pytest_cache",
    "__pycache__",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "out",
}


@dataclass
class Finding:
    severity: str
    check: str
    message: str
    file: str
    line: int
    evidence: str


def iter_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS:
            yield path


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def clean(value: str) -> str:
    return " ".join(value.split())[:180]


def rules() -> list[tuple[str, str, re.Pattern[str], str]]:
    cloud_drive_name = "One" + "Drive"
    return [
        (
            "windows-user-path",
            "error",
            re.compile(r"\b[A-Za-z]:\\(?:Users|Documents and Settings)\\[^\\\s\"'<>]+(?:\\[^\s\"'<>]*)?", re.I),
            "Windows user absolute path detected.",
        ),
        (
            "cloud-drive-path",
            "error",
            re.compile(r"\b[A-Za-z]:\\[^\\\n\"'<>]*" + re.escape(cloud_drive_name) + r"[^\\\n\"'<>]*(?:\\[^\s\"'<>]*)?", re.I),
            "Personal cloud-drive absolute path detected.",
        ),
        (
            "unix-user-path",
            "error",
            re.compile(r"\b/(?:Users|home)/[A-Za-z0-9._-]+/[^\s\"'<>]+"),
            "Unix/macOS user absolute path detected.",
        ),
        (
            "codex-system-path",
            "error",
            re.compile(r"\.codex[\\/]+skills[\\/]+\.system", re.I),
            "Local Codex system skill path detected.",
        ),
        (
            "email-address",
            "warn",
            re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
            "Email address detected; confirm it is intended for public contact.",
        ),
        (
            "secret-assignment",
            "error",
            re.compile(r"\b(?:api[_-]?key|access[_-]?token|auth[_-]?token|secret|private[_-]?key|password)\s*[:=]\s*[\"'][^\"']{8,}[\"']", re.I),
            "Possible secret assignment detected.",
        ),
        (
            "private-key-block",
            "error",
            re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA |)?PRIVATE KEY-----", re.I),
            "Private key block detected.",
        ),
        (
            "local-log-file",
            "warn",
            re.compile(r"\b(?:codex\.local\.md|\.codex-log|debug\.log|trace\.log)\b", re.I),
            "Local/debug log reference detected.",
        ),
        (
            "tool-cache",
            "warn",
            re.compile(r"\b(?:AppData|Library/Caches|\.cache|Temp[\\/]|tmp[\\/])", re.I),
            "Tool cache or temp path reference detected.",
        ),
    ]


def scan(root: Path) -> tuple[list[Finding], dict[str, int]]:
    findings: list[Finding] = []
    for path in iter_files(root):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for check, severity, pattern, message in rules():
            if path.name == "check_public_hygiene.py" and check == "tool-cache":
                continue
            for match in pattern.finditer(text):
                findings.append(
                    Finding(
                        severity=severity,
                        check=check,
                        message=message,
                        file=str(path.relative_to(root)),
                        line=line_number(text, match.start()),
                        evidence=clean(match.group(0)),
                    )
                )
    summary = {
        "files_scanned": sum(1 for _ in iter_files(root)),
        "errors": sum(1 for item in findings if item.severity == "error"),
        "warnings": sum(1 for item in findings if item.severity == "warn"),
        "findings": len(findings),
    }
    return findings, summary


def format_report(findings: list[Finding], summary: dict[str, int]) -> str:
    lines = [
        "Public hygiene check",
        f"Files scanned: {summary['files_scanned']}",
        f"Findings: {summary['findings']} (errors: {summary['errors']}, warnings: {summary['warnings']})",
        "",
    ]
    if not findings:
        lines.append("No public hygiene findings.")
        return "\n".join(lines)
    for item in findings:
        lines.append(f"[{item.severity.upper()}] {item.check} ({item.file}:{item.line}): {item.message}")
        lines.append(f"  evidence: {item.evidence}")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Scan publishable files for local/private data.")
    parser.add_argument("path", nargs="?", default=".", help="Repository or directory to scan.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    args = parser.parse_args(argv)

    root = Path(args.path).resolve()
    if not root.exists():
        print(f"Path does not exist: {root}", file=sys.stderr)
        return 2
    if not root.is_dir():
        print(f"Path is not a directory: {root}", file=sys.stderr)
        return 2

    findings, summary = scan(root)
    if args.json:
        print(json.dumps({"summary": summary, "findings": [asdict(item) for item in findings]}, indent=2))
    else:
        print(format_report(findings, summary))
    return 1 if summary["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
