#!/usr/bin/env python3
"""Generate or verify the repository plugin and skill documentation."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE_PATH = REPOSITORY_ROOT / ".claude-plugin" / "marketplace.json"
DOCS_ROOT = REPOSITORY_ROOT / "docs"
PLUGIN_DOCS_ROOT = DOCS_ROOT / "plugins"
ROOT_INDEX_START = "<!-- BEGIN GENERATED PLUGIN INDEX -->"
ROOT_INDEX_END = "<!-- END GENERATED PLUGIN INDEX -->"


def load_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return value


def load_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML frontmatter")
    try:
        frontmatter = text.split("---\n", 2)[1]
    except IndexError as error:
        raise ValueError(f"{path}: unterminated YAML frontmatter") from error

    values: dict[str, str] = {}
    lines = frontmatter.splitlines()
    index = 0
    while index < len(lines):
        match = re.match(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$", lines[index])
        if not match:
            index += 1
            continue
        key, raw_value = match.groups()
        raw_value = (raw_value or "").strip()
        if raw_value in {">", ">-", "|", "|-"}:
            parts: list[str] = []
            index += 1
            while index < len(lines) and (
                lines[index].startswith(" ") or not lines[index].strip()
            ):
                part = lines[index].strip()
                if part:
                    parts.append(part)
                index += 1
            values[key] = " ".join(parts)
            continue
        values[key] = raw_value.strip("\"'")
        index += 1
    return values


def compact(text: str, limit: int = 220) -> str:
    normalized = " ".join(text.split()).replace("|", "\\|")
    sentence = re.split(r"(?<=[.!?])\s+", normalized, maxsplit=1)[0]
    if len(sentence) <= limit:
        return sentence
    shortened = sentence[: limit - 1].rsplit(" ", 1)[0]
    return f"{shortened}…"


def marketplace_entries() -> list[dict]:
    marketplace = load_json(MARKETPLACE_PATH)
    entries = marketplace.get("plugins")
    if not isinstance(entries, list) or not entries:
        raise ValueError(f"{MARKETPLACE_PATH}: plugins must be a non-empty array")
    return entries


def skill_records(plugin_root: Path) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for skill_path in sorted((plugin_root / "skills").glob("*/SKILL.md")):
        frontmatter = load_frontmatter(skill_path)
        name = frontmatter.get("name") or skill_path.parent.name
        description = frontmatter.get("description")
        if not description:
            raise ValueError(f"{skill_path}: description is required")
        archive = plugin_root / "perplexity" / f"{skill_path.parent.name}.zip"
        records.append(
            {
                "name": name,
                "description": compact(description),
                "path": skill_path,
                "archive": archive if archive.is_file() else None,
            }
        )
    if not records:
        raise ValueError(f"{plugin_root}: no skills found")
    return records


def plugin_records() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for entry in marketplace_entries():
        source = entry.get("source")
        if not isinstance(source, str):
            raise ValueError(f"{MARKETPLACE_PATH}: plugin source must be text")
        plugin_root = (REPOSITORY_ROOT / source).resolve()
        manifest = load_json(plugin_root / ".claude-plugin" / "plugin.json")
        skills = skill_records(plugin_root)
        records.append(
            {
                "name": entry["name"],
                "category": entry["category"],
                "description": entry["description"],
                "summary": compact(entry["description"], 170),
                "version": manifest["version"],
                "root": plugin_root,
                "skills": skills,
                "codex": (plugin_root / ".codex-plugin" / "plugin.json").is_file(),
                "guide": (plugin_root / "GUIDE.md").is_file(),
                "perplexity_count": sum(
                    1 for skill in skills if skill["archive"] is not None
                ),
            }
        )
    return records


def render_catalog_table(records: list[dict[str, object]], *, root: bool) -> str:
    prefix = "docs/plugins" if root else "plugins"
    lines = [
        "| Plugin | Category | Focus | Skills | Codex manifest | Perplexity ZIPs |",
        "|---|---|---|---:|:---:|---:|",
    ]
    for record in records:
        name = str(record["name"])
        lines.append(
            "| "
            f"[`{name}`]({prefix}/{name}.md) | "
            f"{record['category']} | {record['summary']} | "
            f"{len(record['skills'])} | "
            f"{'Yes' if record['codex'] else '—'} | "
            f"{record['perplexity_count'] or '—'} |"
        )
    return "\n".join(lines)


def render_root_index(records: list[dict[str, object]]) -> str:
    return "\n".join(
        [
            "## Plugin index",
            "",
            ROOT_INDEX_START,
            "Every plugin is registered in the Claude marketplace and contains portable "
            "Agent Skills. The manifest and ZIP columns show additional native packaging.",
            "",
            render_catalog_table(records, root=True),
            "",
            f"**{len(records)} plugins, "
            f"{sum(len(record['skills']) for record in records)} skills, and "
            f"{sum(int(record['perplexity_count']) for record in records)} "
            "upload-ready Perplexity packages.**",
            "",
            "Browse the [plugin and skill documentation](docs/README.md) for the "
            "complete per-plugin inventories.",
            ROOT_INDEX_END,
        ]
    )


def render_docs_index(records: list[dict[str, object]]) -> str:
    return "\n".join(
        [
            "# Plugin and skill documentation",
            "",
            "This catalog is generated from the Claude marketplace, plugin manifests, "
            "and each skill's frontmatter. Edit those sources, then run "
            "`python3 scripts/generate_plugin_docs.py`.",
            "",
            render_catalog_table(records, root=False),
            "",
            "## Related documentation",
            "",
            "- [Getting started](../GETTING-STARTED.md)",
            "- [Azure platform-engineering guide](../azure-platform-engineering/GUIDE.md)",
            "- [Platform-engineering source notes](../PLATFORM-ENGINEERING-SOURCE-NOTES.md)",
            "- [Research-division provenance](../RESEARCH-DIVISION-PROVENANCE.md)",
            "- [Prompt-workflow provenance](../prompt-workflows/PROVENANCE.md)",
            "",
        ]
    )


def render_plugin_doc(record: dict[str, object]) -> str:
    name = str(record["name"])
    root = record["root"]
    assert isinstance(root, Path)
    lines = [
        f"# `{name}`",
        "",
        "[← Plugin catalog](../README.md) · [Repository README](../../README.md)",
        "",
        str(record["description"]),
        "",
        f"- Version: `{record['version']}`",
        f"- Category: `{record['category']}`",
        f"- Skills: {len(record['skills'])}",
        "- Claude plugin: yes",
        f"- Codex plugin manifest: {'yes' if record['codex'] else 'no; install the portable skills directly'}",
        f"- Perplexity packages: {record['perplexity_count'] or 'not currently packaged'}",
        "",
        "## Skills",
        "",
        "| Skill | Purpose | Perplexity |",
        "|---|---|:---:|",
    ]
    for skill in record["skills"]:
        assert isinstance(skill, dict)
        skill_path = skill["path"]
        assert isinstance(skill_path, Path)
        source_link = Path("../..") / skill_path.relative_to(REPOSITORY_ROOT)
        archive = skill["archive"]
        if isinstance(archive, Path):
            archive_link = Path("../..") / archive.relative_to(REPOSITORY_ROOT)
            package = f"[ZIP]({archive_link.as_posix()})"
        else:
            package = "—"
        lines.append(
            f"| [`{skill['name']}`]({source_link.as_posix()}) | "
            f"{skill['description']} | {package} |"
        )
    lines.extend(["", "## Plugin files", ""])
    if record["guide"]:
        lines.append(f"- [Usage guide](../../{name}/GUIDE.md)")
    lines.extend(
        [
            f"- [Claude manifest](../../{name}/.claude-plugin/plugin.json)",
            (
                f"- [Codex manifest](../../{name}/.codex-plugin/plugin.json)"
                if record["codex"]
                else "- Codex: install individual skill directories through an Agent "
                "Skills-compatible installer."
            ),
            f"- [Skill source directory](../../{name}/skills/)",
            "",
        ]
    )
    return "\n".join(lines)


def replace_root_index(readme: str, generated: str) -> str:
    if ROOT_INDEX_START in readme and ROOT_INDEX_END in readme:
        start = readme.index("## Plugin index")
        end = readme.index(ROOT_INDEX_END, start) + len(ROOT_INDEX_END)
        return f"{readme[:start]}{generated}{readme[end:]}"

    start = readme.index("## Plugins")
    end = readme.index("## Install", start)
    return f"{readme[:start]}{generated}\n\n{readme[end:]}"


def expected_files(records: list[dict[str, object]]) -> dict[Path, str]:
    files = {DOCS_ROOT / "README.md": render_docs_index(records)}
    for record in records:
        files[PLUGIN_DOCS_ROOT / f"{record['name']}.md"] = render_plugin_doc(record)
    return files


def build() -> int:
    records = plugin_records()
    readme_path = REPOSITORY_ROOT / "README.md"
    updated_readme = replace_root_index(
        readme_path.read_text(encoding="utf-8"), render_root_index(records)
    )
    readme_path.write_text(updated_readme, encoding="utf-8")

    files = expected_files(records)
    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return len(files) + 1


def check() -> int:
    records = plugin_records()
    expected_index = render_root_index(records)
    readme = (REPOSITORY_ROOT / "README.md").read_text(encoding="utf-8")
    if expected_index not in readme:
        raise ValueError("README.md plugin index is missing or stale")

    files = expected_files(records)
    expected_plugin_pages = {
        path for path in files if path.parent == PLUGIN_DOCS_ROOT
    }
    actual_plugin_pages = (
        set(PLUGIN_DOCS_ROOT.glob("*.md")) if PLUGIN_DOCS_ROOT.is_dir() else set()
    )
    unexpected_pages = sorted(actual_plugin_pages - expected_plugin_pages)
    if unexpected_pages:
        rendered = ", ".join(str(path) for path in unexpected_pages)
        raise ValueError(f"unexpected plugin documentation pages: {rendered}")
    for path, expected in files.items():
        if not path.is_file():
            raise ValueError(f"missing generated documentation: {path}")
        if path.read_text(encoding="utf-8") != expected:
            raise ValueError(f"generated documentation is stale: {path}")
    return len(files) + 1


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify generated docs")
    args = parser.parse_args()
    count = check() if args.check else build()
    verb = "Verified" if args.check else "Generated"
    print(f"{verb} the README index and {count - 1} documentation pages")


if __name__ == "__main__":
    main()
