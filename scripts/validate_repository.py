#!/usr/bin/env python3
"""Validate marketplace and plugin relationships without external dependencies."""

from __future__ import annotations

import json
import re
from pathlib import Path


SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")
REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
CROSS_TOOL_PLUGINS = (
    "platform-assessment",
    "prompt-workflows",
    "gpu-research-platform",
    "model-training-ops",
    "inference-testing",
    "research-data-platform",
    "adp-enablement",
)


def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"invalid JSON at {path}: {error}") from error
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return value


def require_text(value: dict, field: str, context: Path) -> str:
    result = value.get(field)
    if not isinstance(result, str) or not result.strip():
        raise ValueError(f"{context}: {field} must be a non-empty string")
    return result


def validate_plugin_manifest(path: Path, expected_name: str) -> dict:
    manifest = load_json(path)
    name = require_text(manifest, "name", path)
    if name != expected_name:
        raise ValueError(f"{path}: plugin name {name!r} must be {expected_name!r}")
    version = require_text(manifest, "version", path)
    if not SEMVER.fullmatch(version):
        raise ValueError(f"{path}: version is not semantic: {version!r}")
    require_text(manifest, "description", path)
    author = manifest.get("author")
    if not isinstance(author, dict):
        raise ValueError(f"{path}: author must be an object")
    require_text(author, "name", path)
    return manifest


def validate_marketplace() -> None:
    path = REPOSITORY_ROOT / ".claude-plugin" / "marketplace.json"
    marketplace = load_json(path)
    require_text(marketplace, "name", path)
    metadata = marketplace.get("metadata")
    if not isinstance(metadata, dict) or not SEMVER.fullmatch(str(metadata.get("version", ""))):
        raise ValueError(f"{path}: metadata.version must be semantic")
    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        raise ValueError(f"{path}: plugins must be a non-empty array")

    names: set[str] = set()
    for entry in plugins:
        if not isinstance(entry, dict):
            raise ValueError(f"{path}: every plugin entry must be an object")
        name = require_text(entry, "name", path)
        if name in names:
            raise ValueError(f"{path}: duplicate plugin entry {name!r}")
        names.add(name)
        require_text(entry, "description", path)
        require_text(entry, "category", path)
        source = require_text(entry, "source", path)
        plugin_root = (REPOSITORY_ROOT / source).resolve()
        try:
            plugin_root.relative_to(REPOSITORY_ROOT)
        except ValueError as error:
            raise ValueError(f"{path}: source escapes repository: {source!r}") from error
        if not plugin_root.is_dir():
            raise ValueError(f"{path}: missing plugin source {source!r}")
        validate_plugin_manifest(plugin_root / ".claude-plugin" / "plugin.json", name)


def validate_cross_tool_plugin(plugin_name: str) -> None:
    plugin_root = REPOSITORY_ROOT / plugin_name
    manifest_path = plugin_root / ".codex-plugin" / "plugin.json"
    manifest = validate_plugin_manifest(manifest_path, plugin_name)
    claude_manifest = validate_plugin_manifest(
        plugin_root / ".claude-plugin" / "plugin.json", plugin_name
    )
    if manifest["version"] != claude_manifest["version"]:
        raise ValueError(f"{plugin_root}: Claude and Codex versions differ")
    skills_value = require_text(manifest, "skills", manifest_path)
    skills_root = (plugin_root / skills_value).resolve()
    try:
        skills_root.relative_to(plugin_root)
    except ValueError as error:
        raise ValueError(f"{manifest_path}: skills path escapes plugin") from error
    skill_dirs = sorted(path for path in skills_root.iterdir() if path.is_dir())
    if not skill_dirs:
        raise ValueError(f"{skills_root}: no skill directories")
    for skill_dir in skill_dirs:
        if not (skill_dir / "SKILL.md").is_file():
            raise ValueError(f"{skill_dir}: missing SKILL.md")
        if not (skill_dir / "agents" / "openai.yaml").is_file():
            raise ValueError(f"{skill_dir}: missing agents/openai.yaml")


def main() -> None:
    validate_marketplace()
    for plugin_name in CROSS_TOOL_PLUGINS:
        validate_cross_tool_plugin(plugin_name)
    print("Repository plugin validation passed")


if __name__ == "__main__":
    main()
