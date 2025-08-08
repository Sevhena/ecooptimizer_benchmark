import argparse
import os
import subprocess
import logging
import textwrap
import yaml
import time
from pathlib import Path
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


# --- Energy Run + Measurement ---
def run_benchmark(
    repo: str,
    smell_type: str,
    smell_id: str,
    version: str,
    test_cmd: list[str],
    tracker: str = "codecarbon",
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
        / f"{smell_id}{'' if tracker == 'codecarbon' else '_usage'}{'_refactored' if version == 'refactored' else ''}.csv"
    )
    emissions_csv.parent.mkdir(parents=True, exist_ok=True)

    initial_lines = 0
    if emissions_csv.exists():
        with emissions_csv.open() as f:
            initial_lines = sum(1 for _ in f)

    print("\n     [bench]", end="", flush=True)

    try:
        while datapoints < iters + 1:
            datapoints = _run_single_test(
                venv_dir, test_cmd, repo, emissions_csv, initial_lines, iters, verbose
            )

            # Check how many lines CodeCarbon recorded (excluding header)
            if not emissions_csv.exists():
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

    print(f" [{datapoints} collected]\n", flush=True)
    return True


def _run_single_test(
    venv_dir: Path,
    test_cmd: list[str],
    repo: str,
    emissions_csv: Path,
    initial_lines: int,
    target_points: int,
    verbose: bool = False,
):
    """Run a single test iteration, stopping if emissions file has enough datapoints."""
    venv_bin = venv_dir / "bin"
    python_path = venv_bin / "python"

    if "-" in test_cmd[0]:
        command = [python_path, *test_cmd]
    else:
        command = test_cmd

    env = os.environ.copy()
    env["VIRTUAL_ENV"] = str(venv_dir)
    env["PATH"] = str(venv_bin) + os.pathsep + env["PATH"]

    console_out_log = LOG_DIR / f"bench_console_output_{repo}.log"

    logging.debug(f"Running test command: {test_cmd} in {repo}")

    dots_printed = 0
    datapoints = 0

    try:
        with console_out_log.open("a") as f:  # append mode
            f.write(f"\n\n=== New Test Run: {time.ctime()} ===\n")

            proc = subprocess.Popen(
                command,
                cwd=(WORKTREES_DIR / repo),
                env=env,
                stdout=f,
                stderr=subprocess.STDOUT,
            )

            while proc.poll() is None:
                time.sleep(0.1)

                if emissions_csv.exists():
                    with emissions_csv.open() as ef:
                        current_lines = sum(1 for _ in ef)

                    datapoints = current_lines - initial_lines

                    if verbose:
                        dots_to_print = datapoints - dots_printed
                        if dots_to_print > 0:
                            print("." * dots_to_print, end="", flush=True)
                            dots_printed += dots_to_print

                    if datapoints >= target_points:
                        logging.debug(f"Reached {datapoints} datapoints, stopping test.")
                        proc.terminate()
                        try:
                            proc.wait(timeout=5)
                        except subprocess.TimeoutExpired:
                            proc.kill()
                        break

    except Exception as e:
        logging.debug(f"Error raised during testing. Check logs. {e}")

    return datapoints


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
    parser.add_argument("--repos", nargs="+", help="Benchmark specific repositories")
    parser.add_argument(
        "--smell-types",
        nargs="+",
        choices=SMELL_TYPES_REF.keys(),
        default=SMELL_TYPES_REF.keys(),
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
        "--smell-ids", nargs="+", help="Benchmark a specific smell ID (must use with --repo)"
    )
    parser.add_argument(
        "--iters", type=int, default=DEFAULT_ITERS, help="Number of iterations to run (default: 30)"
    )
    parser.add_argument(
        "--verbose", action="store_true", help="Enable verbose output with emissions monitoring"
    )
    parser.add_argument(
        "--refactor-only",
        action="store_true",
        help="Only run benchmarks for the refactored smell instance.",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        help="Directory name for storing emissions data in emissions folder",
    )
    parser.add_argument(
        "--tracker",
        choices=["codecarbon", "usage"],
        default="codecarbon",
        help="Which types of annotations to add",
    )
    args = parser.parse_args()

    setup_logging()

    smell_types = [SMELL_TYPES_REF[smell] for smell in args.smell_types]

    # --- Validate Smell Types ---
    if len(set(smell_types) & set(ALL_SMELL_TYPES)) == 0:
        logging.error(
            "No valid smell types specified.\nUse --smell-types to select from following valid smells with a space between each:\n- "
            + "\n- ".join(ALL_SMELL_TYPES)
        )
        sys.exit(1)

    if args.smell_ids and not args.repo:
        logging.error("--smell-ids must be used with --repo")
        sys.exit(1)

    if args.repos and args.smell_ids:
        logging.error(
            "Cannot use --smell-ids with --repos. Use the singular version --repo instead"
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

    elif args.repos:
        for repo in args.repos:
            if args.repo not in selected_repos:
                logging.error(f"Repo {repo} not in selected calibration set. Skipping. ")
                continue
            target_repos.add(repo)

    elif args.domain:
        domain_repos = set(domain_config.get(args.domain.lower(), []))
        target_repos = domain_repos & selected_repos  # Ensure intersection with selected repos
        if not target_repos:
            logging.error(f"No selected repos found for domain '{args.domain}'")
            sys.exit(1)

    else:
        target_repos = selected_repos

    if args.exclude:
        exclusions = [SMELL_TYPES_REF[smell] for smell in args.exclude]
    else:
        exclusions = []

    # --- Smell Filtering ---
    smells_to_run = {}
    if args.smell_ids:
        smells_to_run[args.repo] = {}
        for smell_id in args.smell_ids:
            symbol = next(
                smell_type
                for smell_type, ids in selected_config["smells"][args.repo].items()
                if smell_id in ids
            )
            if not smells_to_run[args.repo].get(symbol):
                smells_to_run[args.repo][symbol] = []

            smell_dir = PATCHES_DIR / args.tracker / args.repo / symbol / smell_id
            smells_to_run[args.repo][symbol].append((args.repo, symbol, smell_id, smell_dir))

    else:
        for repo in target_repos:
            patch_repo_dir = PATCHES_DIR / args.tracker / repo
            if not patch_repo_dir.exists():
                logging.warning(f"No patches found for {repo}")
                continue

            smells_to_run[repo] = {}
            for smell_type in smell_types:
                type_dir = patch_repo_dir / smell_type

                if not type_dir.exists() or smell_type in exclusions:
                    continue

                smells_to_run[repo][smell_type] = []

                for smell_dir in type_dir.iterdir():
                    smells_to_run[repo][smell_type].append(
                        (repo, smell_type, smell_dir.name, smell_dir)
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
                if args.refactor_only:
                    versions = ["refactored"]
                else:
                    versions = ["original", "refactored"]

                for version in versions:
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
                            args.tracker,
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

    if raised_error:
        logging.error("\n❗ Some benchmarks encountered errors. Please check the logs for details.")
    logging.info("\n✅ Benchmarking complete.")


if __name__ == "__main__":
    main()
