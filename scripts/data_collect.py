import json
import re
import argparse
from collections import defaultdict
from pathlib import Path
from typing import Optional

# Complete list of all known smell types
ALL_SMELL_TYPES = [
    "cached-repeated-calls",
    "long-element-chain",
    "long-lambda-expr",
    "long-message-chain",
    "no-self-use",
    "string-concat-loop",
    "too-many-arguments",
    "use-a-generator",
]


def find_json_files(paths: list[str], recursive: bool = False) -> list[Path]:
    """Find all JSON files from given paths (can be files or directories)"""
    json_files: list[Path] = []
    for path_str in paths:
        path = Path(path_str)
        if path.is_file() and path.suffix.lower() == ".json":
            json_files.append(path)
        elif path.is_dir():
            pattern = "**/*.json" if recursive else "*.json"
            json_files.extend(path.glob(pattern) if not recursive else path.rglob("*.json"))
    return json_files


def analyze_smells(
    json_files: list[Path],
) -> defaultdict[Path, defaultdict[str, defaultdict[Optional[str], int]]]:
    """Analyze JSON files and return statistics grouped by file, smell type, and threshold"""
    file_stats: defaultdict[Path, defaultdict[str, defaultdict[Optional[str], int]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(int))
    )

    for file_path in json_files:
        for smell_type in ALL_SMELL_TYPES:
            file_stats[file_path][smell_type]  # This ensures all types exist

        try:
            with file_path.open() as f:
                data = json.load(f)
                if not isinstance(data, list):
                    data = [data]  # Ensure we're working with a list

                for entry in data:
                    smell_type = entry.get("symbol", "UNKNOWN")
                    message = entry.get("message", "")

                    # Extract threshold information (patterns like (2/2) or (7/6))
                    match = re.search(r"\((\d+/\d+)\)", message)
                    threshold_str = match.group(1) if match else None

                    if smell_type == "long-lambda-expression":
                        smell_type = "long-lambda-expr"
                    elif (
                        smell_type not in ALL_SMELL_TYPES
                        and smell_type not in file_stats[file_path]
                    ):
                        file_stats[file_path][smell_type]
                    elif smell_type == "cached-repeated-calls" and threshold_str == "2/2":
                        continue

                    file_stats[file_path][smell_type][threshold_str] += 1

        except json.JSONDecodeError as e:
            print(f"Error parsing {file_path}: {e}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    return file_stats


def write_statistics(
    output_file: Path,
    file_stats: defaultdict[Path, defaultdict[str, defaultdict[Optional[str], int]]],
) -> None:
    """Write statistics to output file in readable format"""
    with output_file.open("w") as f:
        f.write("Code Smell Statistics (Per File and Smell Type)\n")
        f.write("=============================================\n\n")

        # Initialize summary statistics
        total_files = 0
        global_smell_counts: defaultdict[str, int] = defaultdict(int)
        global_threshold_counts: defaultdict[tuple, int] = defaultdict(int)

        for file_path, smells in sorted(file_stats.items(), key=lambda x: str(x[0])):
            total_files += 1
            f.write(f"File: {file_path}\n\n")

            # Calculate total smells for this file
            total_smells = sum(
                sum(thresholds.values())
                for smell_type, thresholds in smells.items()
                if any(thresholds.values())
            )
            f.write("\t=============================================\n")
            f.write(f"\tTotal Smells: {total_smells}\n")
            f.write("\t=============================================\n\n")

            for smell_type in smells.keys():
                thresholds = smells[smell_type]
                total = sum(thresholds.values())

                if smell_type not in ALL_SMELL_TYPES:
                    global_smell_counts["UNKNOWN"] += total
                else:
                    global_smell_counts[smell_type] += total

                f.write(f"\tSmell type: {smell_type} (Total: {total})\n")

                if any(k is not None for k in thresholds):
                    f.write("\t\tThreshold groupings:\n")
                    for threshold, count in sorted(
                        [(k, v) for k, v in thresholds.items() if k is not None],
                        key=lambda x: int(x[0].split("/")[0]) if x[0] else 0,
                    ):
                        f.write(f"\t\t\t{threshold}: {count}\n")
                        global_threshold_counts[(smell_type, threshold)] += count
                f.write("\n")

            f.write("=" * 50 + "\n\n")

        # Write summary statistics
        f.write("\n\n========== SUMMARY STATISTICS =============\n")
        f.write("============================================\n")
        f.write(f"\tTotal repos processed:\t{total_files}\n")
        f.write(
            f"\tTotal smells detected:\t{sum(global_smell_counts.values()) - global_smell_counts['UNKNOWN']}\n\n"
        )

        f.write("\t======= Smell Type Breakdown ==========\n")
        for smell_type, count in sorted(global_smell_counts.items()):
            f.write(f"\t\t{smell_type}:\t{count}\n")

        f.write("\n")

        f.write("\t========== Repo Breakdown =============\n")
        smells_found = defaultdict(list[str])
        for file_path, smells in file_stats.items():
            repo = file_path.name.split("_", 3)[2].replace(".json", "")
            smells_found[repo] = [
                smell for smell, val in smells.items() if smell in ALL_SMELL_TYPES and val
            ]

        smells_found = dict(sorted(smells_found.items(), key=lambda x: len(x[1]), reverse=True))
        for repo, smells in smells_found.items():
            f.write(f"\t\t{repo}: {len(smells)} smell types\n")
            smells_missing = [smell for smell in ALL_SMELL_TYPES if smell not in smells]
            if smells_missing:
                f.write(
                    f"\t\t\t{len(smells_missing)} smell types not present: {', '.join(smells_missing)}\n"
                )


def make_sound() -> None:
    """Play a notification sound in WSL/zsh"""
    try:
        print("\a", end="", flush=True)
    except Exception:
        pass


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Analyze code smell JSON files/directories and generate statistics",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "inputs",
        nargs="+",
        help="JSON files or directories containing JSON files\n"
        "Example:\n"
        "  python analyzer.py file1.json dir1/ dir2/file2.json",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="smell_statistics.txt",
        help="Output file for statistics (default: smell_statistics.txt)",
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Search directories recursively for JSON files",
    )

    args = parser.parse_args()

    # Find all JSON files
    json_files = find_json_files(args.inputs, args.recursive)

    if not json_files:
        print("No JSON files found in the specified paths")
        return

    print(f"Found {len(json_files)} JSON files to analyze")

    # Analyze and write statistics
    file_stats = analyze_smells(json_files)
    write_statistics(Path(args.output), file_stats)
    print(f"Statistics written to {args.output}")

    make_sound()


if __name__ == "__main__":
    main()
