import argparse
import json
import subprocess
import logging
import yaml
import shutil
import time
import psutil
from pathlib import Path
from datetime import datetime, timezone
import sys

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


DEFAULT_ITERS = 30

# --- Smell Types ---
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


class UTCFormatter(logging.Formatter):
    converter = time.gmtime  # Use UTC instead of local time

    def formatTime(self, record, datefmt=None):  # noqa: ANN001
        return super().formatTime(record, datefmt)


def setup_logging():
    """Configure logging to file and console."""
    log_dir = BENCHMARK_ROOT / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "benchmark.log"

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
        subprocess.run(["git", "apply", str(patch_path)], cwd=repo_path, check=True)
        logging.info(f"Applied patch: {patch_path.name}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to apply patch: {patch_path.name}")
        raise e


def load_analysis_results(repo_name: str) -> dict[str, dict] | None:
    """Load analysis results for a specific repository."""
    results_file = SMELLS_DIR / f"{repo_name}.json"
    if not results_file.exists():
        logging.error(f"No analysis results found for {repo_name}")
        return None

    with results_file.open() as f:
        return json.load(f)


# --- Energy Run + Measurement ---
def run_test_suite(
    repo: str,
    smell_type: str,
    smell_id: str,
    run_type: str,
    test_command: str,
    venv_command: str,
    iters: int,
):
    """Run the benchmark for a smell version: original or refactored."""
    # csv_path = result / f"emissions_{run_type}.csv"
    env_script = f"{venv_command} && {test_command}"

    process = psutil.Process()

    start_time = time.time()
    cpu_percentages = []
    peak_memory = 0

    for _ in range(iters):
        try:
            result = subprocess.run(
                env_script,
                shell=True,
                cwd=(WORKTREES_DIR / repo),
                executable="/bin/bash",
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            cpu = process.cpu_percent(interval=0.1)
            mem = process.memory_info().rss / (1024**2)
            peak_memory = max(peak_memory, mem)
            cpu_percentages.append(cpu)
            print(".", end="", flush=True)
        except Exception as e:
            logging.error(f"Test run failed: {e}")
            return

    elapsed = time.time() - start_time
    avg_cpu = sum(cpu_percentages) / len(cpu_percentages) if cpu_percentages else 0

    # Rename CodeCarbon file
    original_csv = EMISSIONS_DIR / repo / smell_type / f"{smell_id}.csv"
    if original_csv.exists():
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H-%M-%S")
        renamed = Path(str(original_csv).replace(".csv", f"_{timestamp}.csv"))
        shutil.move(original_csv, renamed)
    else:
        logging.warning(
            f"No emissions data found in {EMISSIONS_DIR / repo / smell_type} for {smell_id}"
        )

    logging.info(
        f"[{run_type}] Time: {elapsed:.2f}s | CPU: {avg_cpu:.1f}% | RAM: {peak_memory:.1f}MB"
    )


def run_benchmark(
    repo: str,
    smell_type: str,
    smell_id: str,
    smell_dir: Path,
    version: str,
    test_cmd: str,
    venv_cmd: str,
    iters: int,
):
    datapoints = 0
    while datapoints < iters:
        run_test_suite(repo, smell_type, smell_id, version, test_cmd, venv_cmd, iters)

        # --- Check Emissions Count ---
        orig_csv = list(smell_dir.glob("emissions_original_*.csv"))
        if not orig_csv:
            logging.warning(f"No emissions data for {repo} | {smell_id}")
            continue

        with orig_csv[0].open() as f:
            datapoints = sum(1 for _ in f) - 1

        if datapoints < iters:
            logging.debug(f"Only {datapoints} datapoints collected. Rerunning test suite...")


# --- Entry Point ---
def main():
    parser = argparse.ArgumentParser(description="Run benchmark tests for smells.")
    parser.add_argument("--domain", type=str, help="Benchmark all smells in a domain")
    parser.add_argument("--repo", type=str, help="Benchmark a specific repository")
    parser.add_argument(
        "--smell-types",
        type=list[str],
        default=ALL_SMELL_TYPES,
        help="Benchmark specific smell types",
    )
    parser.add_argument(
        "--smell-id", type=str, help="Benchmark a specific smell ID (must use with --repo)"
    )
    parser.add_argument(
        "--iters", type=int, default=DEFAULT_ITERS, help="Number of iterations to run (default: 30)"
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
            elif smell_dir.name in ALL_SMELL_TYPES and smell_dir.name in args.smell_types:
                smells_to_run[repo][smell_dir.name] = []
                continue
            elif smell_dir.parent.name not in ALL_SMELL_TYPES:
                continue
            smell_id = smell_dir.name
            if args.smellid and repo != args.repo:
                continue
            if args.smellid and smell_id != args.smellid:
                continue
            smells_to_run[repo][smell_dir.parent.name].append(
                (repo, smell_dir.parent.name, smell_id, smell_dir)
            )

    if not smells_to_run:
        logging.warning("No smell instances matched the filters.")
        return

    # --- Confirm Repos ---
    logging.info("\nBenchmarking smells in the following repositories:")
    for repo in sorted({r for r, _, _ in smells_to_run}):
        logging.info(f" - {repo}")
    print()

    # sys.exit(1)

    # --- Execute Benchmarks ---
    for repo, smell_type, smell_id, smell_dir in smells_to_run:
        venv_cmd = repos_config[repo].get("venv_command")
        test_cmd = repos_config[repo].get("test_command")

        if not venv_cmd:
            logging.error(f"{repo} is missing a venv_command in repos.yaml.")
            continue

        repo_dir = WORKTREES_DIR / repo
        if not repo_dir.exists():
            logging.error(f"Missing repo folder: {repo_dir}")
            continue

        logging.info(f"{repo} | {smell_id}")

        # --- Apply and Run Original ---
        for version in ["original", "refactored"]:
            apply_patch(smell_dir / f"{version}.patch", repo_dir)
            run_benchmark(
                repo, smell_type, smell_id, smell_dir, version, test_cmd, venv_cmd, args.iters
            )
            subprocess.run(["git", "restore", "."], cwd=repo_dir)

    print("\n✅ Benchmarking complete.")


if __name__ == "__main__":
    main()
