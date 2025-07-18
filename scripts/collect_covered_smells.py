import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
import logging


class UTCFormatter(logging.Formatter):
    converter = time.gmtime  # Use UTC instead of local time

    def formatTime(self, record, datefmt=None):  # noqa: ANN001
        return super().formatTime(record, datefmt)


def setup_logging(repo_name: str):
    """Configure logging to file and console."""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    ann_log_dir = log_dir / "covered_smells"
    ann_log_dir.mkdir(exist_ok=True)
    log_file = (
        ann_log_dir
        / f"covered_smells_{repo_name}_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.log"
    )

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = UTCFormatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter("%(message)s")
    console_handler.setFormatter(console_formatter)

    logging.basicConfig(level=logging.DEBUG, handlers=[file_handler, console_handler])


def load_coverage_data(coverage_path: Path) -> dict[str, set[int]]:
    """Load coverage data and return {file_path: set_of_covered_lines}"""
    coverage_data = {}
    try:
        with coverage_path.open() as f:
            data = json.load(f)

        for file_path, file_data in data["files"].items():
            covered_lines = set()
            # Handle different coverage report formats
            if "executed_lines" in file_data:  # coverage.py format
                covered_lines.update(
                    line_num for line_num, hits in file_data["executed_lines"].items() if hits > 0
                )
            elif "lines" in file_data:  # alternative format
                covered_lines.update(
                    line_num for line_num, hits in file_data["lines"].items() if hits > 0
                )

            coverage_data[file_path] = covered_lines

        logging.info(f"Loaded coverage data for {len(coverage_data)} files")
        return coverage_data

    except Exception as e:
        logging.error(f"Failed to load coverage data: {e}")
        raise


def filter_analysis_results(
    analysis_path: Path, coverage_data: dict[str, set[int]], repo_root: Path
) -> list[dict]:
    """
    Filter analysis results to only include smells in covered code.
    Returns: Filtered analysis results in original format
    """
    filtered_results = []
    try:
        with analysis_path.open() as f:
            analysis_results = json.load(f)

        for smell in analysis_results:
            file_path = str(Path(smell["path"]).relative_to(repo_root))
            logging.debug(f"Processing smell in file: {file_path}")

            # Skip if file wasn't covered at all
            if file_path not in coverage_data:
                logging.debug(f"Skipping smell in uncovered file: {file_path}")
                continue

            covered_lines = coverage_data[file_path]
            covered_occurrences = []

            for occ in smell["occurences"]:
                if occ["line"] in covered_lines:
                    covered_occurrences.append(occ)

            # Only keep smells with at least one covered occurrence
            if covered_occurrences:
                filtered_smell = smell.copy()
                filtered_smell["occurences"] = covered_occurrences
                filtered_results.append(filtered_smell)

        logging.info(
            f"Filtered {len(analysis_results)} smells down to {len(filtered_results)} "
            f"({len(filtered_results) / len(analysis_results):.1%} coverage)"
        )
        return filtered_results

    except Exception as e:
        logging.error(f"Failed to filter analysis results: {e}")
        raise


def run_data_collector() -> None:
    """Run the data collection script"""
    DATA_COLLECTOR = Path("scripts/data_csv_collect.py")
    ANALYSIS_RESULTS_DIR = Path("artifacts/covered_smells")
    try:
        if DATA_COLLECTOR.exists():
            logging.info("Starting data collection...")
            print("Running data collection...")
            result = subprocess.run(
                ["python", str(DATA_COLLECTOR), str(ANALYSIS_RESULTS_DIR)],
                check=True,
                capture_output=True,
                text=True,
            )
            logging.debug(f"Data collector output:\n{result.stdout}")
            if result.stderr:
                logging.warning(f"Data collector errors:\n{result.stderr}")
            logging.info("Data collection completed")
            print("Data collection completed")
        else:
            logging.warning(f"Data collector script not found at {DATA_COLLECTOR}")
            print(f"Warning: Data collector script not found at {DATA_COLLECTOR}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Data collection failed: {e!s}\n{e.stderr}")
        raise
    except Exception as e:
        logging.error(f"Error running data collector: {e!s}")
        raise


def save_filtered_results(results: list[dict], output_path: Path):
    """Save filtered results maintaining original format"""
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w") as f:
            json.dump(results, f, indent=2)
        logging.info(f"Saved filtered results to {output_path}")
    except Exception as e:
        logging.error(f"Failed to save filtered results: {e}")
        raise


def main():
    """Main function with configurable command-line arguments"""
    import argparse

    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Filter code analysis results to only include smells covered by tests",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # Required arguments
    parser.add_argument("analysis_file", type=Path, help="Path to the analysis results JSON file")
    parser.add_argument("coverage_file", type=Path, help="Path to the coverage JSON report")
    parser.add_argument(
        "repo_root", type=Path, help="Root directory of the repository being analyzed"
    )

    # Optional arguments
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("artifacts/covered_smells"),
        help="Output directory for filtered results (default: artifacts/covered_smells/)",
    )
    args = parser.parse_args()

    setup_logging("collect_covered_smells")

    try:
        logging.info("Starting analysis results filtering")
        logging.debug(f"Command-line arguments: {vars(args)}")

        # Set default output path if not specified
        output_path = args.output
        if output_path is None:
            output_path = args.analysis_file.parent / f"covered_{args.analysis_file.name}"
            logging.debug(f"Using default output path: {output_path}")

        # Validate inputs
        if not args.analysis_file.exists():
            raise FileNotFoundError(f"Analysis file not found: {args.analysis_file}")
        if not args.coverage_file.exists():
            raise FileNotFoundError(f"Coverage file not found: {args.coverage_file}")
        if not args.repo_root.exists():
            raise FileNotFoundError(f"Repository root not found: {args.repo_root}")

        # Load coverage data
        coverage_data = load_coverage_data(args.coverage_file)

        # Filter analysis results
        filtered_results = filter_analysis_results(
            args.analysis_file, coverage_data, args.repo_root
        )

        # Save filtered results
        save_filtered_results(filtered_results, output_path)

        logging.info(f"Filtering completed. Results saved to {output_path}")
        return 0

    except Exception as e:
        logging.critical(f"Filtering failed: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    import sys

    sys.exit(main())
