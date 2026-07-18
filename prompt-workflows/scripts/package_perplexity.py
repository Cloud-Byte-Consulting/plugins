#!/usr/bin/env python3
"""Build or verify deterministic Perplexity Computer Skill ZIP packages."""

from __future__ import annotations

import argparse
import re
import zipfile
from pathlib import Path


MAX_PACKAGE_BYTES = 10 * 1024 * 1024
FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)
PORTABLE_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TEXT_EXTENSIONS = {
    ".bash",
    ".cfg",
    ".css",
    ".csv",
    ".html",
    ".ini",
    ".js",
    ".json",
    ".jsx",
    ".md",
    ".markdown",
    ".ps1",
    ".py",
    ".sh",
    ".sql",
    ".svg",
    ".toml",
    ".ts",
    ".tsv",
    ".tsx",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
    ".zsh",
}
TEXT_FILENAMES = {"Dockerfile", "Makefile"}


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
    for path in sorted(
        skill_dir.rglob("*"),
        key=lambda candidate: candidate.relative_to(skill_dir).as_posix(),
    ):
        if path.is_symlink():
            raise ValueError(f"{skill_dir}: symlinks are not portable: {path}")
        if path.is_file() and path.name != ".DS_Store":
            files.append(path)
    return files


def stable_file_bytes(path: Path) -> bytes:
    """Normalize UTF-8 text so checkout line endings cannot change archive bytes."""
    payload = path.read_bytes()
    if path.suffix.lower() not in TEXT_EXTENSIONS and path.name not in TEXT_FILENAMES:
        return payload
    try:
        text = payload.decode("utf-8")
    except UnicodeDecodeError:
        return payload
    if "\r" not in text:
        return payload
    return text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


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
                zipped.writestr(info, stable_file_bytes(path), compress_type=zipfile.ZIP_STORED)

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


def verify_archive(skill_dir: Path, archive: Path) -> None:
    """Verify a committed archive's portable contents and relevant metadata."""
    if archive.stat().st_size > MAX_PACKAGE_BYTES:
        raise ValueError(
            f"{archive}: ZIP is {archive.stat().st_size} bytes; "
            f"maximum is {MAX_PACKAGE_BYTES}"
        )

    expected = [
        (path.relative_to(skill_dir).as_posix(), stable_file_bytes(path))
        for path in validate_skill(skill_dir)
    ]

    try:
        with zipfile.ZipFile(archive) as zipped:
            infos = zipped.infolist()
            actual_names = [info.filename for info in infos]
            expected_names = [name for name, _ in expected]
            if actual_names != expected_names:
                raise ValueError(
                    f"outdated Perplexity package entries: {archive}; "
                    f"expected={expected_names}, actual={actual_names}"
                )
            if zipped.comment:
                raise ValueError(f"non-portable ZIP comment in {archive}")

            for info, (name, payload) in zip(infos, expected):
                if info.date_time != FIXED_ZIP_TIME:
                    raise ValueError(f"non-deterministic timestamp for {name} in {archive}")
                if info.create_system != 3:
                    raise ValueError(f"non-portable creator system for {name} in {archive}")
                if info.compress_type != zipfile.ZIP_STORED:
                    raise ValueError(f"unexpected compression for {name} in {archive}")
                if info.external_attr != 0o100644 << 16:
                    raise ValueError(f"non-portable file mode for {name} in {archive}")
                if info.extra or info.comment:
                    raise ValueError(f"unexpected ZIP metadata for {name} in {archive}")
                if zipped.read(info) != payload:
                    raise ValueError(f"outdated Perplexity package content: {archive}")
    except zipfile.BadZipFile as error:
        raise ValueError(f"invalid Perplexity package: {archive}") from error


def check(skills_dir: Path, output_dir: Path) -> int:
    skill_dirs = sorted(
        (
            path
            for path in skills_dir.iterdir()
            if path.is_dir() and (path / "SKILL.md").is_file()
        ),
        key=lambda path: path.name,
    )
    if not skill_dirs:
        raise ValueError(f"no skills found under {skills_dir}")

    expected_names = {f"{skill_dir.name}.zip" for skill_dir in skill_dirs}
    actual_names = {path.name for path in output_dir.glob("*.zip")}
    if actual_names != expected_names:
        missing = sorted(expected_names - actual_names)
        stale = sorted(actual_names - expected_names)
        raise ValueError(f"Perplexity packages differ: missing={missing}, stale={stale}")

    for skill_dir in skill_dirs:
        verify_archive(skill_dir, output_dir / f"{skill_dir.name}.zip")
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
