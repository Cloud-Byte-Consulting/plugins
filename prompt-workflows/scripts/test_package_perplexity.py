from __future__ import annotations

import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from package_perplexity import FIXED_ZIP_TIME, check, package_skill


SKILL = """---
name: demo
description: Demonstrate deterministic packaging.
---

# Demo

Line one.
Line two.
"""
BINARY_PAYLOAD = b"\x00opaque-binary\r\npayload"


class PackagePerplexityTests(unittest.TestCase):
    def make_skill(self, root: Path, newline: str) -> Path:
        skill = root / "demo"
        (skill / "agents").mkdir(parents=True)
        (skill / "SKILL.md").write_bytes(SKILL.replace("\n", newline).encode())
        metadata = "interface:\n  display_name: Demo\n"
        (skill / "agents" / "openai.yaml").write_bytes(
            metadata.replace("\n", newline).encode()
        )
        (skill / "asset.bin").write_bytes(BINARY_PAYLOAD)
        return skill

    def test_lf_and_crlf_sources_create_identical_archives(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            lf = package_skill(self.make_skill(root / "lf", "\n"), root / "lf-out")
            crlf = package_skill(
                self.make_skill(root / "crlf", "\r\n"), root / "crlf-out"
            )
            self.assertEqual(lf.read_bytes(), crlf.read_bytes())

            with zipfile.ZipFile(lf) as archive:
                self.assertIn("SKILL.md", archive.namelist())
                self.assertEqual(archive.read("asset.bin"), BINARY_PAYLOAD)
                self.assertTrue(
                    all(info.create_system == 3 for info in archive.infolist())
                )
                self.assertTrue(
                    all(info.date_time == FIXED_ZIP_TIME for info in archive.infolist())
                )

    def test_check_verifies_archive_contents_against_source(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            skill = self.make_skill(root / "skills", "\n")
            output = root / "perplexity"
            package_skill(skill, output)

            self.assertEqual(check(root / "skills", output), 1)

            (skill / "SKILL.md").write_text(SKILL + "\nChanged.\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "outdated.*content"):
                check(root / "skills", output)


if __name__ == "__main__":
    unittest.main()
