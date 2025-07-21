import json
import re
import argparse
import csv
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

SMELL_INSTANCE_THRESH = 6


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
                raw_data: dict[str, dict] = json.load(f)
                data = [smell for smell in raw_data.values()]

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


def write_csv_statistics(
    output_dir: Path,
    file_stats: defaultdict[Path, defaultdict[str, defaultdict[Optional[str], int]]],
) -> None:
    """Write statistics to CSV files in the output directory"""
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)

    # Initialize summary statistics
    global_smell_counts: defaultdict[str, int] = defaultdict(int)
    global_threshold_counts: defaultdict[tuple[str, str], int] = defaultdict(int)
    repo_stats = defaultdict(dict)

    # Process each file and write individual repo CSV
    for file_path, smells in file_stats.items():
        repo_name = file_path.name.split("_", 3)[2].replace(".json", "")
        csv_path = output_dir / f"{repo_name}.csv"

        # Prepare data for CSV
        rows = []
        total_smells = 0

        for smell_type in ALL_SMELL_TYPES:
            thresholds = smells[smell_type]
            total = sum(thresholds.values())
            total_smells += total

            # Add row for the smell type
            rows.append(
                {
                    "Smell Type": smell_type,
                    "Total Count": total,
                    "Thresholds": ", ".join(
                        f"{k}:{v}" for k, v in thresholds.items() if k is not None
                    )
                    or "N/A",
                }
            )

            # Update global counts
            global_smell_counts[smell_type] += total
            for threshold, count in thresholds.items():
                if threshold is not None:
                    global_threshold_counts[(smell_type, threshold)] += count

        # Add total row
        rows.append({"Smell Type": "TOTAL", "Total Count": total_smells, "Thresholds": "N/A"})

        rows.sort(key=lambda x: x["Total Count"], reverse=True)

        # Write repo CSV
        if rows:
            with csv_path.open("w", newline="") as csvfile:
                fieldnames = ["Smell Type", "Total Count", "Thresholds"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(rows)

            # Store repo stats for summary
            repo_stats[repo_name] = {
                "total_smells": total_smells,
                "smell_types_present": len(
                    [st for st in ALL_SMELL_TYPES if sum(smells[st].values()) > 0]
                ),
                "smell_types_under_threshold": [
                    (st, str(sum(vals.values())))
                    for st, vals in smells.items()
                    if sum(vals.values()) < SMELL_INSTANCE_THRESH
                ],
                "smell_types_missing": [
                    st for st in ALL_SMELL_TYPES if sum(smells[st].values()) == 0
                ],
            }

            # print(repo_stats[repo_name]["smell_types_under_threshold"])

    # Write summary CSV
    summary_path = output_dir / "all.csv"
    with summary_path.open("w", newline="") as csvfile:
        # Write smell type summary
        writer = csv.writer(csvfile)
        writer.writerow(["SUMMARY STATISTICS"])
        writer.writerow([])
        writer.writerow(["Total repos processed:", len(repo_stats)])
        writer.writerow(["Total smells detected:", sum(global_smell_counts.values())])
        writer.writerow([])

        writer.writerow(["SMELL TYPE BREAKDOWN"])
        writer.writerow(["Smell Type", "Total Count"])
        for smell_type in ALL_SMELL_TYPES:
            writer.writerow([smell_type, global_smell_counts.get(smell_type, 0)])

        writer.writerow([])
        writer.writerow(["THRESHOLD BREAKDOWN"])
        writer.writerow(["Smell Type", "Threshold", "Count"])
        for (smell_type, threshold), count in sorted(global_threshold_counts.items()):
            writer.writerow([smell_type, threshold, count])

        writer.writerow([])
        writer.writerow(["REPO BREAKDOWN"])
        writer.writerow(
            [
                "Repository",
                "Total Smells",
                "Smell Types Present",
                "Smell Types Under Threshold",
                "Smell Types Missing",
            ]
        )
        for repo, stats in sorted(
            repo_stats.items(), key=lambda x: x[1]["total_smells"], reverse=True
        ):
            writer.writerow(
                [
                    repo,
                    stats["total_smells"],
                    stats["smell_types_present"],
                    ", ".join([":".join(pair) for pair in stats["smell_types_under_threshold"]]),
                    ", ".join(stats["smell_types_missing"]),
                ]
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
    output_dir = Path("artifacts/stats").resolve()
    smell_state = json_files[0].parent.name

    write_csv_statistics(output_dir / smell_state, file_stats)
    print(f"Statistics written to CSV files in {output_dir}")

    # make_sound()


if __name__ == "__main__":
    main()
