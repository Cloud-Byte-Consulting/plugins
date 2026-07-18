#!/usr/bin/env python3
"""Build or verify deterministic Perplexity Computer Skill ZIP packages."""

from __future__ import annotations

import argparse
import re
import tempfile
import zipfile
from pathlib import Path


MAX_PACKAGE_BYTES = 10 * 1024 * 1024
FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)
PORTABLE_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def frontmatter_value(text: str, key: str) -> str:
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---", 4)
    if end < 0:
        return ""
    match = re.search(rf"(?m)^{re.escape(key)}:\s*([^\n]*)$", text[4:end])
    if not match:
        return ""
    return match.group(1).strip().strip("\"'")


def validate_skill(skill_dir: Path) -> list[Path]:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        raise ValueError(f"{skill_dir}: missing SKILL.md")

    text = skill_file.read_text(encoding="utf-8")
    name = frontmatter_value(text, "name")
    if name != skill_dir.name:
        raise ValueError(
            f"{skill_dir}: frontmatter name {name!r} must match the directory name"
        )
    if len(name) > 64 or not PORTABLE_NAME.fullmatch(name):
        raise ValueError(f"{skill_dir}: name is not portable: {name!r}")
    if not frontmatter_value(text, "description"):
        raise ValueError(f"{skill_dir}: missing description frontmatter")

    files: list[Path] = []
    for path in sorted(skill_dir.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"{skill_dir}: symlinks are not portable: {path}")
        if path.is_file() and path.name != ".DS_Store":
            files.append(path)
    return files


def package_skill(skill_dir: Path, output_dir: Path) -> Path:
    files = validate_skill(skill_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    archive = output_dir / f"{skill_dir.name}.zip"
    temporary = archive.with_suffix(".zip.tmp")

    try:
        with zipfile.ZipFile(
            temporary, "w", compression=zipfile.ZIP_STORED
        ) as zipped:
            for path in files:
                relative = path.relative_to(skill_dir).as_posix()
                info = zipfile.ZipInfo(relative, FIXED_ZIP_TIME)
                info.create_system = 3
                info.compress_type = zipfile.ZIP_STORED
                info.external_attr = 0o100644 << 16
                zipped.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_STORED)

        size = temporary.stat().st_size
        if size > MAX_PACKAGE_BYTES:
            raise ValueError(
                f"{skill_dir.name}: ZIP is {size} bytes; maximum is {MAX_PACKAGE_BYTES}"
            )
        temporary.replace(archive)
    finally:
        temporary.unlink(missing_ok=True)
    return archive


def build(skills_dir: Path, output_dir: Path) -> list[Path]:
    skill_dirs = sorted(
        path for path in skills_dir.iterdir() if path.is_dir() and (path / "SKILL.md").is_file()
    )
    if not skill_dirs:
        raise ValueError(f"no skills found under {skills_dir}")

    archives = [package_skill(skill_dir, output_dir) for skill_dir in skill_dirs]
    desired = {archive.name for archive in archives}
    for stale in output_dir.glob("*.zip"):
        if stale.name not in desired:
            stale.unlink()
    return archives


def check(skills_dir: Path, output_dir: Path) -> int:
    with tempfile.TemporaryDirectory(prefix="perplexity-skills-") as temp:
        generated = build(skills_dir, Path(temp))
        expected_names = {path.name for path in generated}
        actual_names = {path.name for path in output_dir.glob("*.zip")}
        if actual_names != expected_names:
            missing = sorted(expected_names - actual_names)
            stale = sorted(actual_names - expected_names)
            raise ValueError(f"Perplexity packages differ: missing={missing}, stale={stale}")
        for archive in generated:
            committed = output_dir / archive.name
            if archive.read_bytes() != committed.read_bytes():
                raise ValueError(f"outdated Perplexity package: {committed}")
    return len(expected_names)


def main() -> None:
    plugin_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills-dir", type=Path, default=plugin_root / "skills")
    parser.add_argument("--out", type=Path, default=plugin_root / "perplexity")
    parser.add_argument("--check", action="store_true", help="verify committed ZIPs")
    args = parser.parse_args()

    count = check(args.skills_dir, args.out) if args.check else len(build(args.skills_dir, args.out))
    verb = "Verified" if args.check else "Built"
    print(f"{verb} {count} Perplexity skill packages in {args.out}")


if __name__ == "__main__":
    main()
