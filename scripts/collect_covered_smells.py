from doctest import run_docstring_examples
import json
import logging
import argparse
import subprocess
from pathlib import Path
import sys
import time
from typing import Any

BENCHMARK_ROOT = Path().resolve()
ARTIFACTS_DIR = BENCHMARK_ROOT / "artifacts"
DATA_COLLECTOR = BENCHMARK_ROOT / "scripts" / "data_csv_collect.py"
SMELLS_DIR = ARTIFACTS_DIR / "smells"
RAW_SMELLS_DIR = SMELLS_DIR / "raw"
COVERAGE_DIR = ARTIFACTS_DIR / "coverage"
OUTPUT_DIR = SMELLS_DIR / "covered"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


class UTCFormatter(logging.Formatter):
    converter = time.gmtime  # Use UTC instead of local time

    def formatTime(self, record, datefmt=None):  # noqa: ANN001
        return super().formatTime(record, datefmt)


# --- Setup logging ---
def setup_logging():
    """Configure logging to file and console."""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / "smell_coverage_filtering.log"

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = UTCFormatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter("%(message)s")
    console_handler.setFormatter(console_formatter)

    logging.basicConfig(level=logging.DEBUG, handlers=[file_handler, console_handler])


def load_json(file_path: Path) -> dict[str, Any]:
    logging.debug(f"Loading JSON file: {file_path}")
    with file_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    logging.debug(f"Loaded {len(data)} items from {file_path}")
    return data


def is_line_covered(coverage: dict[str, Any], path: Path, line: int) -> bool:
    str_path = str(path)
    if str_path not in coverage["files"]:
        logging.debug(f"Path not found in coverage: {str_path}")
        return False
    covered = line in coverage["files"][str_path]["executed_lines"]
    logging.debug(
        f"Checking coverage for {str_path} line {line}: {'covered' if covered else 'not covered'}"
    )
    return covered


def filter_smells(
    repo_name: str, smells: dict[str, Any], coverage: dict[str, Any]
) -> dict[str, Any]:
    logging.debug(f"Filtering smells for repo: {repo_name}")
    filtered = {}
    for smell_id, smell_data in smells.items():
        original_occs = smell_data["occurences"]
        relative_path = (
            Path(smell_data["path"])
            .resolve()
            .relative_to(BENCHMARK_ROOT / "repositories" / repo_name)
        )
        new_occs = [
            occ for occ in original_occs if is_line_covered(coverage, relative_path, occ["line"])
        ]
        logging.debug(
            f"Smell {smell_id}: {len(new_occs)} / {len(original_occs)} occurrences covered"
        )
        if new_occs:
            smell_data["occurences"] = new_occs
            filtered[smell_id] = smell_data
    logging.debug(f"Total smells after filtering: {len(filtered)}")
    return filtered


def run_data_collector() -> None:
    """Run the data collection script"""
    try:
        if DATA_COLLECTOR.exists():
            logging.info("Starting data collection...")
            result = subprocess.run(
                ["python", str(DATA_COLLECTOR), str(OUTPUT_DIR)],
                check=True,
                capture_output=True,
                text=True,
            )
            logging.debug(f"Data collector output:\n{result.stdout}")
            if result.stderr:
                logging.warning(f"Data collector errors:\n{result.stderr}")
            logging.info("Data collection completed")
        else:
            logging.warning(f"Data collector script not found at {DATA_COLLECTOR}")
            print(f"Warning: Data collector script not found at {DATA_COLLECTOR}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Data collection failed: {e!s}\n{e.stderr}")
    except Exception as e:
        logging.error(f"Error running data collector: {e!s}")


def process_repo(smells_file: Path):
    repo_name = smells_file.stem
    coverage_file = COVERAGE_DIR / f"{repo_name}.json"
    output_file = OUTPUT_DIR / f"{repo_name}.json"

    logging.debug(f"Processing smells file: {smells_file}")
    logging.debug(f"Expected coverage file: {coverage_file}")
    logging.debug(f"Output file will be: {output_file}")

    if not coverage_file.exists():
        logging.debug(f"Coverage file not found for {repo_name}: {coverage_file}")
        return

    logging.info(f"Processing repository: {repo_name}")
    smells = load_json(smells_file)
    coverage = load_json(coverage_file)

    filtered = filter_smells(repo_name, smells, coverage)
    with output_file.open("w", encoding="utf-8") as f:
        json.dump(filtered, f, indent=2)

    logging.info(
        f"Filtered smells written to {output_file} ({len(filtered)}/{len(smells)} smells retained)"
    )


def main():
    parser = argparse.ArgumentParser(description="Filter uncovered smells based on coverage data.")
    parser.add_argument(
        "--repo", type=str, help="Optional: name of a specific repository to process."
    )
    args = parser.parse_args()

    setup_logging()

    if args.repo:
        logging.debug(f"Processing single repository: {args.repo}")
        process_repo(RAW_SMELLS_DIR / f"{args.repo}.json")
    else:
        logging.debug(f"Processing all repositories in {RAW_SMELLS_DIR}")
        for smells_file in RAW_SMELLS_DIR.iterdir():
            process_repo(smells_file)

    run_data_collector()


if __name__ == "__main__":
    main()
