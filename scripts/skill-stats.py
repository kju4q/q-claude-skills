#!/usr/bin/env python3
"""skill-stats: scan SKILL.md frontmatter and emit a markdown report.

Reads every `skills/<name>/SKILL.md`, parses the YAML-ish frontmatter block
between `---` fences, and writes a markdown table with each skill's name,
description, last-modified date, and a flag for missing required fields.

Stdlib only.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import os
import sys
from pathlib import Path

REQUIRED_FIELDS = ("name", "description")
REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
DEFAULT_OUTPUT = REPO_ROOT / "skill-stats-report.md"


def parse_frontmatter(text: str) -> dict[str, str]:
    """Parse a leading `---` ... `---` block into a dict.

    Only handles flat `key: value` lines — enough for SKILL.md frontmatter.
    Returns {} if no frontmatter block is found.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields


def md_escape(value: str) -> str:
    """Escape characters that would break a markdown table cell."""
    return value.replace("|", "\\|").replace("\n", " ").strip()


def collect_skills(skills_dir: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for child in sorted(skills_dir.iterdir()):
        if not child.is_dir():
            continue
        skill_md = child / "SKILL.md"
        if not skill_md.exists():
            rows.append(
                {
                    "folder": child.name,
                    "name": "",
                    "description": "",
                    "modified": "",
                    "missing": list(REQUIRED_FIELDS) + ["SKILL.md"],
                }
            )
            continue
        text = skill_md.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        missing = [f for f in REQUIRED_FIELDS if not fm.get(f)]
        mtime = _dt.datetime.fromtimestamp(skill_md.stat().st_mtime)
        rows.append(
            {
                "folder": child.name,
                "name": fm.get("name", ""),
                "description": fm.get("description", ""),
                "modified": mtime.strftime("%Y-%m-%d"),
                "missing": missing,
            }
        )
    return rows


def render_report(rows: list[dict[str, object]], skills_dir: Path) -> str:
    generated = _dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    total = len(rows)
    flagged = sum(1 for r in rows if r["missing"])
    rel_dir = os.path.relpath(skills_dir, REPO_ROOT)

    out: list[str] = []
    out.append("# Skill Stats Report")
    out.append("")
    out.append(f"Generated: {generated}")
    out.append(f"Source: `{rel_dir}/`")
    out.append(f"Skills scanned: {total}  |  Flagged: {flagged}")
    out.append("")
    out.append("| Folder | Name | Description | Last Modified | Missing Fields |")
    out.append("| --- | --- | --- | --- | --- |")
    for r in rows:
        missing_cell = ", ".join(r["missing"]) if r["missing"] else "-"
        flag = " :warning:" if r["missing"] else ""
        out.append(
            "| {folder} | {name} | {desc} | {mod} | {miss}{flag} |".format(
                folder=md_escape(str(r["folder"])),
                name=md_escape(str(r["name"])) or "_(missing)_",
                desc=md_escape(str(r["description"])) or "_(missing)_",
                mod=str(r["modified"]) or "_(n/a)_",
                miss=md_escape(missing_cell),
                flag=flag,
            )
        )
    out.append("")
    out.append(f"Required frontmatter fields: {', '.join(REQUIRED_FIELDS)}.")
    out.append("")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--skills-dir",
        type=Path,
        default=SKILLS_DIR,
        help="Directory containing skill subfolders (default: ./skills)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Output markdown file (default: ./skill-stats-report.md)",
    )
    args = parser.parse_args(argv)

    if not args.skills_dir.is_dir():
        print(f"error: skills directory not found: {args.skills_dir}", file=sys.stderr)
        return 1

    rows = collect_skills(args.skills_dir)
    report = render_report(rows, args.skills_dir)
    args.output.write_text(report, encoding="utf-8")
    print(f"wrote {args.output} ({len(rows)} skills, {sum(1 for r in rows if r['missing'])} flagged)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
