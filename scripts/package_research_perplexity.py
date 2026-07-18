#!/usr/bin/env python3
"""Build or verify Perplexity ZIPs for cross-tool platform plugins."""

from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path
from types import ModuleType


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
PLUGIN_NAMES = (
    "platform-assessment",
    "gpu-research-platform",
    "model-training-ops",
    "inference-testing",
    "research-data-platform",
    "adp-enablement",
)


def load_packager() -> ModuleType:
    path = REPOSITORY_ROOT / "prompt-workflows" / "scripts" / "package_perplexity.py"
    spec = importlib.util.spec_from_file_location("perplexity_packager", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load Perplexity packager: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify committed ZIPs")
    args = parser.parse_args()
    packager = load_packager()

    total = 0
    for plugin_name in PLUGIN_NAMES:
        plugin_root = REPOSITORY_ROOT / plugin_name
        skills_dir = plugin_root / "skills"
        output_dir = plugin_root / "perplexity"
        if args.check:
            total += packager.check(skills_dir, output_dir)
        else:
            total += len(packager.build(skills_dir, output_dir))

    verb = "Verified" if args.check else "Built"
    print(f"{verb} {total} cross-tool Perplexity skill packages")


if __name__ == "__main__":
    main()
