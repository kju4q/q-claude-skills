#!/usr/bin/env python3
"""Tests for skill-stats: validate the generated markdown report.

Runs the script against a fixture skills tree, then asserts properties of the
report file. Also validates the real ./skill-stats-report.md if present.
Stdlib only — invoke with `python3 scripts/test_skill_stats.py`.
"""

from __future__ import annotations

import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "skill-stats.py"
REAL_REPORT = REPO_ROOT / "skill-stats-report.md"


def run_script(skills_dir: Path, output: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--skills-dir",
            str(skills_dir),
            "--output",
            str(output),
        ],
        capture_output=True,
        text=True,
        check=False,
    )


def make_skill(parent: Path, folder: str, body: str) -> None:
    d = parent / folder
    d.mkdir(parents=True, exist_ok=True)
    (d / "SKILL.md").write_text(body, encoding="utf-8")


class FixtureReportTests(unittest.TestCase):
    """Generate a report from a fixture tree, then validate it."""

    @classmethod
    def setUpClass(cls) -> None:
        cls._tmp = tempfile.TemporaryDirectory()
        root = Path(cls._tmp.name)
        skills = root / "skills"
        skills.mkdir()

        make_skill(
            skills,
            "alpha",
            "---\nname: alpha-skill\ndescription: A complete skill for testing.\n---\n\n# Alpha\n",
        )
        make_skill(
            skills,
            "beta",
            "---\nname: beta-skill\n---\n\n# Beta missing description\n",
        )
        make_skill(skills, "gamma", "")  # totally empty -- no frontmatter

        cls.report = root / "report.md"
        cls.proc = run_script(skills, cls.report)
        cls.text = cls.report.read_text(encoding="utf-8") if cls.report.exists() else ""

    @classmethod
    def tearDownClass(cls) -> None:
        cls._tmp.cleanup()

    def test_script_exits_zero(self) -> None:
        self.assertEqual(
            self.proc.returncode,
            0,
            msg=f"stderr: {self.proc.stderr}\nstdout: {self.proc.stdout}",
        )

    def test_report_file_created(self) -> None:
        self.assertTrue(self.report.exists(), "report file was not created")
        self.assertGreater(len(self.text), 0, "report is empty")

    def test_has_title_and_metadata(self) -> None:
        self.assertIn("# Skill Stats Report", self.text)
        self.assertIn("Skills scanned: 3", self.text)
        self.assertIn("Flagged: 2", self.text)

    def test_markdown_table_well_formed(self) -> None:
        # Header + separator + one row per skill folder.
        table_lines = [ln for ln in self.text.splitlines() if ln.startswith("|")]
        self.assertGreaterEqual(len(table_lines), 2 + 3)
        header = table_lines[0]
        separator = table_lines[1]
        self.assertIn("Folder", header)
        self.assertIn("Name", header)
        self.assertIn("Description", header)
        self.assertIn("Last Modified", header)
        self.assertIn("Missing Fields", header)
        self.assertRegex(separator, r"^\|\s*-+\s*(\|\s*-+\s*){4}\|$")
        # Every data row must have the same column count as the header.
        expected_cols = header.count("|")
        for row in table_lines[2:]:
            self.assertEqual(row.count("|"), expected_cols, msg=f"bad row: {row}")

    def test_complete_skill_not_flagged(self) -> None:
        row = self._row_for("alpha")
        self.assertIn("alpha-skill", row)
        self.assertIn("A complete skill for testing.", row)
        self.assertNotIn(":warning:", row)
        self.assertIn("| - |", row)

    def test_missing_description_flagged(self) -> None:
        row = self._row_for("beta")
        self.assertIn(":warning:", row)
        self.assertIn("description", row)
        self.assertNotIn(" name,", row)  # `name` was present, shouldn't be listed

    def test_empty_skill_flagged_for_both(self) -> None:
        row = self._row_for("gamma")
        self.assertIn(":warning:", row)
        self.assertIn("name", row)
        self.assertIn("description", row)

    def test_last_modified_is_iso_date(self) -> None:
        for folder in ("alpha", "beta", "gamma"):
            row = self._row_for(folder)
            self.assertRegex(row, r"\b\d{4}-\d{2}-\d{2}\b", msg=row)

    def _row_for(self, folder: str) -> str:
        for line in self.text.splitlines():
            if line.startswith(f"| {folder} "):
                return line
        self.fail(f"no row found for folder {folder!r}")


class RealReportTests(unittest.TestCase):
    """Sanity-check the committed ./skill-stats-report.md if it exists."""

    def setUp(self) -> None:
        if not REAL_REPORT.exists():
            self.skipTest("skill-stats-report.md not generated yet")
        self.text = REAL_REPORT.read_text(encoding="utf-8")

    def test_has_title(self) -> None:
        self.assertTrue(self.text.startswith("# Skill Stats Report"))

    def test_mentions_required_fields(self) -> None:
        self.assertIn("name", self.text)
        self.assertIn("description", self.text)

    def test_contains_table(self) -> None:
        self.assertRegex(self.text, r"\n\| Folder \| Name \|")

    def test_scanned_count_matches_table_rows(self) -> None:
        m = re.search(r"Skills scanned: (\d+)", self.text)
        self.assertIsNotNone(m, "missing 'Skills scanned' line")
        scanned = int(m.group(1))
        data_rows = [
            ln
            for ln in self.text.splitlines()
            if ln.startswith("|")
            and not ln.startswith("| Folder")
            and not re.match(r"^\|\s*-+", ln)
        ]
        self.assertEqual(len(data_rows), scanned)


if __name__ == "__main__":
    unittest.main(verbosity=2)
