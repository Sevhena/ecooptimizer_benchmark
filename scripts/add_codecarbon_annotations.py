import json
import time
import logging
from pathlib import Path
import sys
import argparse
from datetime import datetime, timezone
from typing import Optional

# TODO: Update analysis ouput structure to include energy metadata


class UTCFormatter(logging.Formatter):
    converter = time.gmtime  # Use UTC instead of local time

    def formatTime(self, record, datefmt=None):  # noqa: ANN001
        return super().formatTime(record, datefmt)


def setup_logging(repo_name: str):
    """Configure logging to file and console."""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    ann_log_dir = log_dir / "annotations"
    ann_log_dir.mkdir(exist_ok=True)
    log_file = ann_log_dir / f"annotations_{repo_name}.log"

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = UTCFormatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter("%(message)s")
    console_handler.setFormatter(console_formatter)

    logging.basicConfig(level=logging.DEBUG, handlers=[file_handler, console_handler])


def get_code_lines(file_path: Path):
    """Read a file and return its lines."""
    with file_path.open(encoding="utf-8") as f:
        return f.readlines()


def write_code_lines(file_path: Path, lines: list):
    """Write lines back to a file."""
    with file_path.open("w", encoding="utf-8") as f:
        f.writelines(lines)


def add_decorator_to_function(file_path: Path, cc_args: str, line_num: int, col_num: int):
    """Add CodeCarbon decorator to a function."""
    lines = get_code_lines(file_path)

    # Add the decorator
    decorator_line = " " * (col_num) + f"@track_emissions({cc_args})\n"
    lines.insert(line_num - 1, decorator_line)

    # Add import if not present
    if not any(line.strip().startswith("from codecarbon import track_emissions") for line in lines):
        lines.insert(0, "from codecarbon import track_emissions\n")

    write_code_lines(file_path, lines)
    logging.info(f"Added decorator to function in {file_path} at line {line_num}")


def wrap_with_context_manager(
    file_path: Path, cc_args: str, start_line: int, end_line: int, col_num: int
):
    """Wrap code block with CodeCarbon context manager."""
    lines = get_code_lines(file_path)

    # Add context manager around the specified lines
    indent = lines[start_line - 1][
        : len(lines[start_line - 1]) - len(lines[start_line - 1].lstrip())
    ]

    # Insert start before the block
    start_context = f"{indent}with EmissionsTracker({cc_args}) as tracker:\n"
    lines.insert(start_line - 1, start_context)

    # Add proper indentation to the block
    for i in range(start_line, end_line + 1):
        lines[i] = f"    {lines[i]}"

    # Add import if not present
    if not any(
        line.strip().startswith("from codecarbon import EmissionsTracker") for line in lines
    ):
        lines.insert(0, "from codecarbon import EmissionsTracker\n")

    write_code_lines(file_path, lines)
    logging.info(f"Wrapped lines {start_line}-{end_line} in {file_path} with context manager")


def process_smell(smell_data: dict, repo_name: str):
    """Process a single smell and annotate the code accordingly."""
    file_path = Path(smell_data["path"])
    energy_meta = smell_data.get("energyMetadata", {})

    if not file_path.exists():
        logging.warning(f"File not found: {file_path}")
        return

    # Prepare the context manager lines
    file_tag = f"{smell_data['messageId']}_{smell_data['id']}"
    ccarbon_output_file = Path(
        f"results/{repo_name}/{smell_data['symbol']}/{smell_data['id']}.csv"
    ).resolve()
    ccarbon_output_file.parent.mkdir(parents=True, exist_ok=True)

    cc_args = f"project_name='{repo_name}-benchmark', experiment_id='{repo_name}_{file_tag}', output_file='{ccarbon_output_file}'"

    if energy_meta.get("isFunc", False):
        # Function/method case - use decorator
        if energy_meta.get("useOccurences", False):
            for occ in smell_data["occurences"]:
                add_decorator_to_function(file_path, cc_args, occ["line"], occ.get("column", 0))
        else:
            add_decorator_to_function(
                file_path, cc_args, energy_meta["start"], energy_meta.get("col", 0)
            )

        smell_data["occurences"][0]["line"] += 2
        smell_data["occurences"][0]["endLine"] += 2
    else:
        # Non-function case - use context manager

        if energy_meta.get("useOccurences", False):
            occurences = smell_data["occurences"]
            for i in range(len(smell_data["occurences"])):
                wrap_with_context_manager(
                    file_path,
                    cc_args,
                    occurences[i]["line"],
                    occurences[i]["endLine"],
                    occurences[i].get("column", 0),
                )
                smell_data["occurences"][i]["line"] += 2 + i
                smell_data["occurences"][i]["endLine"] += 2 + i
        else:
            logging.info("Wrapping code block with context manager")
            wrap_with_context_manager(
                file_path,
                cc_args,
                energy_meta["start"],
                energy_meta["end"],
                energy_meta.get("col", 0),
            )
            smell_data["occurences"][0]["line"] += 2
            smell_data["occurences"][0]["endLine"] += 2
            smell_data["additionalInfo"]["innerLoopLine"] += 2

    return smell_data


def get_analysis_file_path(repo_name: str, manual_path: Optional[str]):
    """Determine the analysis file path based on inputs."""
    if manual_path:
        return Path(manual_path)
    return Path(f"artifacts/smells/analysis_results_{repo_name}.json")


def main(repo_name: str, smell_id: str, analysis_file: Optional[str]):
    """Main function to process a specific smell."""
    setup_logging(repo_name)
    logging.info(f"Starting annotation for smell {smell_id} in repo {repo_name}")

    # Resolve analysis file path
    analysis_path = get_analysis_file_path(repo_name, analysis_file)
    if not analysis_path.exists():
        logging.error(f"Analysis file not found: {analysis_path}")
        return

    # Load and find specific smell
    try:
        with analysis_path.open(encoding="utf-8") as f:
            smells = json.load(f)
    except Exception as e:
        logging.error(f"Failed to load analysis JSON: {e}")
        return

    target_smell = smells[smell_id]
    if not target_smell:
        logging.error(f"Smell ID {smell_id} not found in analysis data")
        return

    # Process only the specified smell
    try:
        logging.info(f"Processing smell: {target_smell.get('message', 'unknown')}")
        updated_smell_data = process_smell(target_smell, repo_name)

        smells[smell_id] = updated_smell_data
        # Save the updated analysis file
        ann_path = Path("artifacts/smells_annotated") / repo_name / f"report_{smell_id}.json"
        ann_path.parent.mkdir(parents=True, exist_ok=True)
        with ann_path.open("w", encoding="utf-8") as f:
            json.dump(smells, f, indent=4)
        logging.info(f"Updated analysis report saved to {ann_path}")
    except Exception as e:
        logging.error(f"Failed to process smell: {e}")

    logging.info("Annotation completed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Annotate code with CodeCarbon instrumentation for a specific smell."
    )
    parser.add_argument(
        "repo_name", help="Repository name to analyze (used for automatic file path resolution)"
    )
    parser.add_argument("smell_id", help="ID of the smell to annotate")
    parser.add_argument(
        "--analysis-file",
        help="Manual path to analysis JSON file (overrides automatic resolution)",
        default=None,
    )

    args = parser.parse_args()

    main(repo_name=args.repo_name, smell_id=args.smell_id, analysis_file=args.analysis_file)
