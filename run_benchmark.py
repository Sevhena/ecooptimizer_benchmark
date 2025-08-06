import argparse
import json
import os
import shutil
import subprocess
import logging
import textwrap
from threading import Thread, Event
import yaml
import time
import psutil
from pathlib import Path
from datetime import datetime, timezone
import sys
import csv

# --- Paths ---
BENCHMARK_ROOT = Path().resolve()

WORKTREES_DIR = BENCHMARK_ROOT / "worktrees"
EMISSIONS_DIR = BENCHMARK_ROOT / "emissions"

EMISSIONS_DIR.mkdir(parents=True, exist_ok=True)

ARTIFACTS_DIR = BENCHMARK_ROOT / "artifacts"
PATCHES_DIR = ARTIFACTS_DIR / "patches"
SMELLS_DIR = ARTIFACTS_DIR / "smells" / "annotated"

CONFIGS_DIR = BENCHMARK_ROOT / "configs"
REPOS_YAML = CONFIGS_DIR / "repos.yaml"
SELECTED_YAML = CONFIGS_DIR / "selected.yaml"
DOMAIN_YAML = CONFIGS_DIR / "domains.yaml"

LOG_DIR = BENCHMARK_ROOT / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)


DEFAULT_ITERS = 30

# --- Smell Types ---
ALL_SMELL_TYPES = [
    "long-lambda-expr",
    "long-message-chain",
    "no-self-use",
    "string-concat-loop",
    "too-many-arguments",
    "use-a-generator",
]


class UTCFormatter(logging.Formatter):
    converter = time.gmtime  # Use UTC instead of local time

    def formatTime(self, record, datefmt=None):  # noqa: ANN001
        return super().formatTime(record, datefmt)


def setup_logging():
    """Configure logging to file and console."""
    log_file = LOG_DIR / "benchmark.log"

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = UTCFormatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter("%(message)s")
    console_handler.setFormatter(console_formatter)

    logging.basicConfig(level=logging.DEBUG, handlers=[file_handler, console_handler])


# --- YAML Load ---
def load_yaml(path: Path):
    with path.open() as f:
        return yaml.safe_load(f)


# --- Patch Application ---
def apply_patch(patch_path: Path, repo_path: Path):
    try:
        if not patch_path.exists():
            raise FileNotFoundError(f"Patch file not found: {patch_path}")

        subprocess.run(["git", "apply", str(patch_path)], cwd=repo_path, check=True)
        logging.debug(f"Applied patch: {patch_path.name}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to apply patch: {patch_path.name}")
        raise e
    except FileNotFoundError as e:
        logging.error(f"Patch file not found: {patch_path}")
        raise e


def load_analysis_results(repo_name: str) -> dict[str, dict] | None:
    """Load analysis results for a specific repository."""
    results_file = SMELLS_DIR / f"{repo_name}.json"
    if not results_file.exists():
        logging.error(f"No analysis results found for {repo_name}")
        return None

    with results_file.open() as f:
        return json.load(f)


def monitor_emissions_file(
    initial_lines: int, emissions_csv: Path, stop_event: Event, interval: float = 0.1
):
    """Background process to monitor line count changes in emissions file."""

    dots_printed = 0
    while not stop_event.is_set():  # Check if we should stop
        time.sleep(interval)
        if emissions_csv.exists():
            with emissions_csv.open() as f:
                current_lines = sum(1 for _ in f)
            if current_lines > initial_lines:
                new_lines = current_lines - initial_lines
                dots_to_print = new_lines - dots_printed
                print("." * dots_to_print, end="", flush=True)
                dots_printed += dots_to_print
                initial_lines = current_lines


# --- Energy Run + Measurement ---
def run_benchmark(
    repo: str,
    smell_type: str,
    smell_id: str,
    version: str,
    test_cmd: list[str],
    iters: int = DEFAULT_ITERS,
    verbose: bool = False,
):
    """Run benchmark test suite for a given repo smell version."""
    venv_dir = WORKTREES_DIR / repo / ".venv"
    datapoints = 0

    emissions_csv = (
        EMISSIONS_DIR
        / repo
        / smell_type
        / f"{smell_id}{'_refactored' if version == 'refactored' else ''}.csv"
    )
    stats_csv = EMISSIONS_DIR / repo / smell_type / f"{smell_id}_stats.csv"
    stats_csv.parent.mkdir(parents=True, exist_ok=True)

    initial_lines = 0
    if emissions_csv.exists():
        with emissions_csv.open() as f:
            initial_lines = sum(1 for _ in f)

    print("\n     [bench]", end="", flush=True)
    header_written = stats_csv.exists()

    stop_event = Event()
    monitor_thread = Thread(
        target=monitor_emissions_file, args=(initial_lines, emissions_csv, stop_event), daemon=True
    )
    if verbose:
        monitor_thread.start()

    try:
        while datapoints < iters + 1:
            elapsed, avg_cpu, peak_mem = _run_single_test(venv_dir, test_cmd, repo)

            timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H-%M-%S")
            row = [
                timestamp,
                repo,
                smell_type,
                smell_id,
                version,
                iters,
                f"{elapsed:.2f}",
                f"{avg_cpu:.1f}",
                f"{peak_mem:.1f}",
            ]

            with stats_csv.open("a", newline="") as f:
                writer = csv.writer(f)
                if not header_written:
                    writer.writerow(
                        [
                            "timestamp",
                            "repo",
                            "smell_type",
                            "smell_id",
                            "run_type",
                            "iters",
                            "elapsed_sec",
                            "avg_cpu_percent",
                            "peak_memory_mb",
                        ]
                    )
                    header_written = True
                writer.writerow(row)

            # Check how many lines CodeCarbon recorded (excluding header)
            if emissions_csv.exists():
                with emissions_csv.open() as f:
                    datapoints = sum(1 for _ in f) - initial_lines
            else:
                logging.warning(f"No emissions file found: {emissions_csv}")
                raise Exception(f"Emissions file not found for {repo} | {smell_id} | {version}")

            if datapoints < iters:
                logging.debug(
                    f"Only {datapoints} datapoints for {repo} | {smell_id} | rerunning..."
                )
    except KeyboardInterrupt as e:
        raise e
    except Exception as e:
        raise e
    finally:
        if verbose:
            stop_event.set()
            monitor_thread.join(timeout=1.0)

    print(f" [{datapoints} collected]\n", flush=True)
    return True


def _run_single_test(venv_dir: Path, test_cmd: list[str], repo: str):
    """Run a single test iteration and collect system metrics."""
    process = psutil.Process()
    venv_bin = venv_dir / "bin"
    python_path = venv_bin / "python"

    if "-" in test_cmd[0]:
        command = [python_path, *test_cmd]
    else:
        command = test_cmd

    env = os.environ.copy()
    env["VIRTUAL_ENV"] = str(venv_dir)
    env["PATH"] = str(venv_bin) + os.pathsep + env["PATH"]

    console_out_log = LOG_DIR / "bench_console_output.log"

    logging.debug(f"Running test command: {test_cmd} in {repo}")
    start_time = time.time()

    try:
        with console_out_log.open("a") as f:  # append mode
            f.write(f"\n=== New Test Run: {time.ctime()} ===\n")
            subprocess.run(
                command,
                cwd=(WORKTREES_DIR / repo),
                env=env,
                check=True,
                stdout=f,
                stderr=subprocess.STDOUT,
            )
    except Exception as e:
        logging.debug(f"Error raised during testing. Check logs. {e}")

    elapsed = time.time() - start_time
    avg_cpu = process.cpu_percent(interval=0.1)
    mem_mb = process.memory_info().rss / (1024**2)

    return elapsed, avg_cpu, mem_mb


def move_named_subfolders(folder_names: set[str]):
    """
    Move subfolders with specific names into a new UTC-timestamped subfolder,
    unless they are already inside a timestamp-named folder.
    """

    # Prepare destination folder
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")
    destination = EMISSIONS_DIR / timestamp
    destination.mkdir()

    moved = False
    for name in folder_names:
        subfolder = EMISSIONS_DIR / name
        if subfolder.exists():
            shutil.move(str(subfolder), str(destination))
            moved = True

    if not moved:
        destination.rmdir()  # Clean up if nothing was moved


SMELL_TYPES_REF = {
    "crc": "cached-repeated-calls",
    "lec": "long-element-chain",
    "lle": "long-lambda-expr",
    "lmc": "long-message-chain",
    "nsu": "no-self-use",
    "scl": "string-concat-loop",
    "tma": "too-many-arguments",
    "ugen": "use-a-generator",
}


# --- Entry Point ---
def main():
    parser = argparse.ArgumentParser(description="Run benchmark tests for smells.")
    parser.add_argument("--domain", type=str, help="Benchmark all smells in a domain")
    parser.add_argument("--repo", type=str, help="Benchmark a specific repository")
    parser.add_argument(
        "--smell-types",
        nargs="+",
        default=ALL_SMELL_TYPES,
        help="Benchmark specific smell types",
    )
    parser.add_argument(
        "--exclude",
        nargs="+",
        choices=SMELL_TYPES_REF.keys(),
        help=textwrap.dedent(
            "Exclude certain smell types:\n- "
            + "\n- ".join(f"{k}: {v}" for k, v in SMELL_TYPES_REF.items())
        ),
    )
    parser.add_argument(
        "--smell-id", type=str, help="Benchmark a specific smell ID (must use with --repo)"
    )
    parser.add_argument(
        "--iters", type=int, default=DEFAULT_ITERS, help="Number of iterations to run (default: 30)"
    )
    parser.add_argument(
        "--verbose", action="store_true", help="Enable verbose output with emissions monitoring"
    )
    args = parser.parse_args()

    setup_logging()

    # --- Validate Smell Types ---
    if len(set(args.smell_types) & set(ALL_SMELL_TYPES)) == 0:
        logging.error(
            "No valid smell types specified.\nUse --smell-types to select from following valid smells with a space between each:\n- "
            + "\n- ".join(ALL_SMELL_TYPES)
        )
        sys.exit(1)

    repos_config = load_yaml(REPOS_YAML)
    selected_config = load_yaml(SELECTED_YAML)
    domain_config = load_yaml(DOMAIN_YAML)

    # --- Resolve Target Repos ---
    selected_repos: set[str] = set(selected_config.get("repos", []))
    target_repos: set[str] = set()

    if args.repo:
        if args.repo not in selected_repos:
            logging.error(
                f"Repo {args.repo} not in selected calibration set. "
                + "Make sure the repository is properly added to repos.yaml."
            )
            sys.exit(1)
        target_repos.add(args.repo)

    elif args.domain:
        domain_repos = set(domain_config.get(args.domain.lower(), []))
        target_repos = domain_repos & selected_repos  # Ensure intersection with selected repos
        if not target_repos:
            logging.error(f"No selected repos found for domain '{args.domain}'")
            sys.exit(1)

    else:
        target_repos = selected_repos

    exclusions = [SMELL_TYPES_REF[smell] for smell in args.exclude]

    # --- Smell Filtering ---
    smells_to_run = {}
    for repo in target_repos:
        patch_repo_dir = PATCHES_DIR / repo
        if not patch_repo_dir.exists():
            logging.warning(f"No patches found for {repo}")
            continue

        smells_to_run[repo] = {}

        for smell_dir in sorted(patch_repo_dir.rglob("*")):
            if not smell_dir.is_dir():
                continue
            elif (
                smell_dir.name in ALL_SMELL_TYPES
                and smell_dir.name not in exclusions
                and smell_dir.name in args.smell_types
            ):
                smells_to_run[repo][smell_dir.name] = []
                continue
            elif smell_dir.parent.name not in ALL_SMELL_TYPES:
                continue
            elif smell_dir.parent.name not in smells_to_run[repo]:
                continue
            smell_id = smell_dir.name
            if args.smell_id and repo != args.repo:
                continue
            if args.smell_id and smell_id != args.smell_id:
                continue
            smells_to_run[repo][smell_dir.parent.name].append(
                (repo, smell_dir.parent.name, smell_id, smell_dir)
            )

    if not smells_to_run:
        logging.warning("No smell instances matched the filters.")
        return

    # --- Confirm Repos ---
    logging.info("\nBenchmarking smells in the following repositories:")
    for repo in smells_to_run.keys():
        logging.info(f" - {repo}")

    # --- Execute Benchmarks ---
    raised_error = False
    for repo, smell_items in smells_to_run.items():
        logging.info(f"\nRunning benchmarks for {repo}...")
        logging.info(f"Smell types: {smell_items.keys()}")
        for smell_type, smell_instances in smell_items.items():
            logging.info(f"\n  {smell_type}:")
            for repo, smell_type, smell_id, smell_dir in smell_instances:
                test_cmd = repos_config[repo].get("test_command")

                if not test_cmd:
                    logging.error(f"{repo} is missing a venv in repos.yaml.")
                    continue

                repo_dir = WORKTREES_DIR / repo
                if not repo_dir.exists():
                    logging.error(f"Missing repo folder: {repo_dir}")
                    continue

                logging.info(f"   {smell_id}")

                # --- Apply and Run Original ---
                for version in ["original", "refactored"]:
                    logging.info(f"    [{version}]")
                    try:
                        apply_patch(smell_dir / f"{version}.patch", repo_dir)
                    except FileNotFoundError:
                        logging.debug(
                            f"Patch file not found. Skipping for {repo} | {smell_type} | {smell_id}."
                        )
                        break

                    try:
                        complete = run_benchmark(
                            repo,
                            smell_type,
                            smell_id,
                            version,
                            test_cmd,
                            args.iters,
                            args.verbose,
                        )

                        if not complete:
                            logging.error(
                                f"Failed to run benchmark for {repo} | {smell_type} | {smell_id} | {version}"
                            )
                            break
                    except KeyboardInterrupt:
                        logging.info("Benchmark run interrupted by user.")
                        move_named_subfolders(selected_repos)
                        sys.exit(0)
                    except Exception as e:
                        logging.error(
                            f"Error running benchmark for {repo} | {smell_type} | {smell_id} | {version}: {e}"
                        )
                        raised_error = True
                        continue
                    finally:
                        logging.info(f"    Restoring {repo_dir} to original state...")
                        subprocess.run(["git", "restore", "."], cwd=repo_dir)

    # --- Move Emissions Files ---
    if EMISSIONS_DIR.exists():
        logging.info("\nMoving emissions files to timestamped folder...")
        move_named_subfolders(selected_repos)

    if raised_error:
        logging.error("\n❗ Some benchmarks encountered errors. Please check the logs for details.")
    logging.info("\n✅ Benchmarking complete.")


if __name__ == "__main__":
    main()
