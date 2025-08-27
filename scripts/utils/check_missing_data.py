#!/usr/bin/env python3
"""
check_emissions.py

Checks emissions/<repo>/<smell_type>/ for the 4 required files for every smell id
listed in configs/selected.yaml, and reports missing data in a summarised way.
"""

import argparse
import sys
import yaml
from pathlib import Path

FILE_TYPES = {
    "carbon_orig": "{id}.csv",
    "carbon_ref": "{id}_refactored.csv",
    "usage_orig": "{id}_usage.csv",
    "usage_ref": "{id}_usage_refactored.csv",
}


def load_smells(path: Path) -> dict:
    with path.open() as f:
        data = yaml.safe_load(f) or {}
    if "smells" in data and isinstance(data["smells"], dict):
        return data["smells"]
    return {}


def classify_missing(present, file_types):
    """present is a set of keys that exist, file_types is the current dict of files to check."""
    all_types = set(file_types.keys())
    missing = all_types - present

    if len(missing) == len(file_types):
        return "all data missing"

    carbon_missing = {"carbon_orig", "carbon_ref"} & all_types
    usage_missing = {"usage_orig", "usage_ref"} & all_types

    if missing == carbon_missing:
        return "only carbon data missing"
    if missing == {"carbon_ref"} & all_types | {"usage_ref"} & all_types:
        return "only refactored data missing"
    if missing == usage_missing and usage_missing:
        return "only usage data missing"
    return "partial data missing: " + ", ".join(sorted(missing))


def check_missing(
    emissions_dir: Path, smells_map: dict[str, dict[str, str]], ignore_usage: bool = False
):
    file_types = dict(FILE_TYPES)
    if ignore_usage:
        file_types.pop("usage_orig")
        file_types.pop("usage_ref")

    report = {}
    for repo, smell_types in sorted(smells_map.items()):
        for smell_type, ids in sorted(smell_types.items()):
            if not ids:
                continue
            smell_dir = emissions_dir / repo / smell_type
            for sid in ids:
                present = set()
                for key, template in file_types.items():
                    fname = template.format(id=sid)
                    fpath = smell_dir / fname
                    if fpath.exists():
                        present.add(key)

                if len(present) == len(file_types):
                    continue  # all present

                category = classify_missing(present, file_types)
                report.setdefault(f"{repo}/{smell_type}", []).append((sid, category))

    return report


def main():
    parser = argparse.ArgumentParser(
        description="Check for missing emissions data (summarised) based on YAML config."
    )
    parser.add_argument(
        "-c",
        "--config",
        default="configs/selected.yaml",
        help="Path to selected.yaml (default: configs/selected.yaml)",
    )
    parser.add_argument(
        "-e", "--emissions-dir", default="emissions", help="Emissions root dir (default: emissions)"
    )
    parser.add_argument(
        "--ignore-usage",
        action="store_true",
        help="Ignore CPU/RAM usage files when checking for missing data",
    )
    args = parser.parse_args()

    config = Path(args.config)
    emissions = Path(args.emissions_dir)

    if not config.exists():
        print(f"Config file not found: {args.config}", file=sys.stderr)
        sys.exit(2)

    if not emissions.exists():
        print("No emissions data found.")

    smells_map = load_smells(config)
    if not smells_map:
        print(f"No 'smells' mapping found in {args.config} or it's empty.", file=sys.stderr)
        sys.exit(3)

    report = check_missing(emissions, smells_map, args.ignore_usage)

    if not report:
        print("All data present ✅")
        sys.exit(0)

    for key in sorted(report):
        print(f"{key}:")
        for sid, category in report[key]:
            print(f"  - {sid}: {category}")

    sys.exit(1)


if __name__ == "__main__":
    main()
