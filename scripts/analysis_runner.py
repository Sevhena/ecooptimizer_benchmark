import os
import time
import sys
import subprocess
import logging
from pathlib import Path
from datetime import datetime, timezone
import concurrent.futures

import yaml

from run_benchmark import SELECTED_YAML

CURRENT_DIR = Path().resolve()

# Configuration
REPO_DIR = (CURRENT_DIR / "repositories").resolve()
ANALYSIS_RESULTS_DIR = (CURRENT_DIR / "artifacts/smells").resolve()
DATA_COLLECTOR = CURRENT_DIR / "scripts/data_csv_collect.py"
REPO_CONFIG_FILE = CURRENT_DIR / "configs/repos.yaml"
SELECTED_REPOS_FILE = CURRENT_DIR / "configs/selected.yaml"

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
ANALYSIS_LOG_DIR = LOG_DIR / "analysis"
ANALYSIS_LOG_DIR.mkdir(exist_ok=True)

logger = logging.getLogger()


def load_yaml(path: Path):
    with path.open() as f:
        return yaml.safe_load(f)


repos_config = load_yaml(REPO_CONFIG_FILE)


class UTCFormatter(logging.Formatter):
    converter = time.gmtime  # Use UTC instead of local time

    def formatTime(self, record, datefmt=None):  # noqa: ANN001
        return super().formatTime(record, datefmt)


def setup_logging():
    """Configure logging to file and console."""
    log_file = ANALYSIS_LOG_DIR / "analysis_monitor.log"

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = UTCFormatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter("%(message)s")
    console_handler.setFormatter(console_formatter)

    logging.basicConfig(level=logging.DEBUG, handlers=[file_handler, console_handler])


def get_existing_repos() -> set[str]:
    """Get list of already analyzed repos"""
    analyzed = set()
    try:
        if ANALYSIS_RESULTS_DIR.exists():
            for f in ANALYSIS_RESULTS_DIR.iterdir():
                if f.name.startswith("analysis_results_") and f.name.endswith(".json"):
                    repo_name = f.name[len("analysis_results_") : -len(".json")]
                    analyzed.add(repo_name)
        logger.debug(f"Found {len(analyzed)} already analyzed repos")
        return analyzed
    except Exception as e:
        logger.error(f"Error getting existing repos: {e!s}")
        return set()


def get_new_repos() -> list[str]:
    """Find repos that haven't been analyzed yet"""
    try:
        analyzed = get_existing_repos()
        new_repos = [
            item.name
            for item in REPO_DIR.iterdir()
            if (
                item.is_dir()
                and item.name != "analysis_results"
                and item.name != ".venv"
                and item.name not in analyzed
            )
        ]
        logger.debug(f"Found {len(new_repos)} new repos to analyze")
        return new_repos
    except Exception as e:
        logger.error(f"Error finding new repos: {e!s}")
        return []


def get_repo_directories(repo_path: str) -> list[str]:
    """Get top-level directories in a repo"""
    try:
        repo = Path(repo_path)
        dirs = [d.name for d in repo.iterdir() if d.is_dir()]
        logger.debug(f"Found {len(dirs)} directories in {repo_path}")
        return dirs
    except Exception as e:
        logger.error(f"Error getting repo directories: {e!s}")
        return []


def run_analysis(repo_name: str) -> None:
    """Run ecooptimizer and wait for completion"""
    try:
        logger.info(f"Starting analysis for repository: {repo_name}")

        repo_config = repos_config.get(repo_name, None)
        if not repo_config:
            logger.error(f"No configuration found for repository: {repo_name}")
            raise ValueError(f"No configuration found for repository: {repo_name}")

        target: str = repo_config.get("target", "")
        exclusions: list = repo_config.get("patterns_to_exclude", [])

        debug_log = (
            ANALYSIS_LOG_DIR
            / f"analysis_{repo_name}_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.log"
        )
        with debug_log.open("w") as log_file:
            process = subprocess.Popen(
                [
                    "ecooptimizer",
                    "-a",
                    "--root",
                    f"repositories/{repo_name}",
                    "--target",
                    f"repositories/{target}",
                    "--exclude",
                    ",".join(exclusions),
                    "--analysis-results-file",
                    f"{ANALYSIS_RESULTS_DIR.relative_to(CURRENT_DIR)}/analysis_results_{repo_name}.json",
                ],
                stdout=log_file,
                stderr=subprocess.STDOUT,
            )
            return_code = process.wait()
            if return_code != 0:
                logger.error(f"Analysis failed with return code {return_code}")
            else:
                logger.info("Analysis completed successfully")
        print("Analysis completed")
    except Exception as e:
        logger.error(f"Analysis failed: {e!s}")
        raise


def run_data_collector() -> None:
    """Run the data collection script"""
    try:
        if DATA_COLLECTOR.exists():
            logger.info("Starting data collection...")
            result = subprocess.run(
                ["python", str(DATA_COLLECTOR), str(ANALYSIS_RESULTS_DIR)],
                check=True,
                capture_output=True,
                text=True,
            )
            logger.debug(f"Data collector output:\n{result.stdout}")
            if result.stderr:
                logger.warning(f"Data collector errors:\n{result.stderr}")
            logger.info("Data collection completed")
        else:
            logger.warning(f"Data collector script not found at {DATA_COLLECTOR}")
            print(f"Warning: Data collector script not found at {DATA_COLLECTOR}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Data collection failed: {e!s}\n{e.stderr}")
        raise
    except Exception as e:
        logger.error(f"Error running data collector: {e!s}")
        raise


def clear_screen():
    """Clear the console screen"""
    os.system("cls" if os.name == "nt" else "clear")


def display_menu(new_repos: list[str]) -> None:
    """Display the interactive menu"""
    clear_screen()
    print(f"{green}{'*' * 100}")
    print("REPOSITORY ANALYSIS MENU".center(100))
    print(f"{'*' * 100}{reset}\n")

    options = [
        "1. Analyze all repositories",
        "2. Analyze selected repositories",
        "3. Analyze specific repository",
        f"{'4. Analyze new repositories' + (' (NEW AVAILABLE!)' if new_repos else ' (no new repos)')}",
    ]

    # Grey out option 4 if no new repos
    option_text = options[3]
    if not new_repos:
        option_text = f"\033[90m{option_text}\033[0m"  # Grey color

    for opt in [*options[:3], option_text]:
        print(opt)

    print("\n0. Exit")
    print(f"\n{green}{'*' * 100}{reset}")


def get_user_choice(new_repos: list[str]) -> str:
    """Get and validate user choice"""
    while True:
        try:
            choice = input("\nEnter your choice: ").strip()
            if choice == "0":
                return "exit"
            elif choice == "1":
                return "all"
            elif choice == "2":
                return "selected"
            elif choice == "3":
                return "specific"
            elif choice == "4" and new_repos:
                return "new"
            print("Invalid choice. Please try again.")
        except KeyboardInterrupt:
            return "exit"


def list_repositories() -> list[str]:
    """List all available repositories"""
    return [
        d.name
        for d in REPO_DIR.iterdir()
        if d.is_dir() and d.name not in (".venv", "analysis_results")
    ]


def analyze_all_repos():
    """Process all repositories in parallel (no prompts)."""
    print("Make sure you have properly configured the repositories in repos.yaml.")
    time.sleep(2)
    repos = list_repositories()

    failed_analyses = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(process_repository, repos)

    for repo_name, success in results:
        if not success:
            failed_analyses.append(repo_name)

    if failed_analyses:
        logger.error(
            f"\nFailed to analyze the following repositories:\n- {'- '.join(failed_analyses)}"
        )


def analyze_selected_repos():
    repos = load_yaml(SELECTED_REPOS_FILE).get("repos", [])
    if not repos:
        logger.error(
            "No repositories selected for analysis. Please check your configuration in configs/selected.yaml."
        )
        return

    print("Make sure you have properly configured the repositories in repos.yaml.")
    time.sleep(2)

    failed_analyses = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(process_repository, repos)

    for repo_name, success in results:
        if not success:
            failed_analyses.append(repo_name)

    if failed_analyses:
        logger.error(
            f"\nFailed to analyze the following repositories:\n- {'- '.join(failed_analyses)}"
        )


def analyze_specific_repo():
    """Let user select a specific repository"""
    clear_screen()
    repos = list_repositories()
    print("\nAvailable repositories:")
    for i, repo in enumerate(repos, 1):
        print(f"{i}. {repo}")
    print("\n0. Back to menu")

    while True:
        try:
            choice = int(input("\nSelect repository (number): "))
            if 1 <= choice <= len(repos):
                process_repository(repos[choice - 1])
                break
            elif choice == 0:
                return
            print("Invalid selection")
        except ValueError:
            print("Please enter a number")


def analyze_new_repos(new_repos: list[str]):
    """Process new repositories in parallel (no prompts)."""
    failed_analyses = []

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(process_repository, new_repos)

    for repo_name, success in results:
        if not success:
            failed_analyses.append(repo_name)

    if failed_analyses:
        logger.error(
            f"\nFailed to analyze the following repositories:\n- {'- '.join(failed_analyses)}"
        )


def process_repository(repo_name: str) -> tuple[str, bool]:
    """Wrapper for multiprocessing-safe repo analysis (no prompts)."""
    try:
        run_analysis(repo_name)
        run_data_collector()
        return (repo_name, True)
    except Exception as e:
        logger.error(f"Parallel processing failed for {repo_name}: {e!s}")
        return (repo_name, False)


green = "\033[92m"
reset = "\033[0m"
red = "\033[91m"


def main() -> None:
    """Main monitoring function with interactive menu"""
    setup_logging()
    logger.info(f"{green}\n{'*' * 100}\nSTARTING ANALYSIS RUNNER\n{'*' * 100}{reset}")

    try:
        # Create analysis_results directory if it doesn't exist
        ANALYSIS_RESULTS_DIR.mkdir(parents=True, exist_ok=True)

        last_new_repos = []
        menu_active = True

        while menu_active:
            # Check for new repos
            current_new_repos = get_new_repos()

            # Show notification if new repos appear
            if current_new_repos and not last_new_repos:
                print(
                    f"\n{green}NOTICE: {len(current_new_repos)} new repository(ies) detected!{reset}"
                )
                time.sleep(2)  # Let user see the notification

            # Display menu and get choice
            display_menu(current_new_repos)
            choice = get_user_choice(current_new_repos)

            # Process choice
            if choice == "exit":
                menu_active = False
            elif choice == "all":
                analyze_all_repos()
                continue
            elif choice == "selected":
                analyze_selected_repos()
                continue
            elif choice == "specific":
                analyze_specific_repo()
                continue
            elif choice == "new":
                analyze_new_repos(current_new_repos)
                continue

            last_new_repos = current_new_repos.copy()

            # Brief pause to prevent CPU overload
            time.sleep(0.5)

    except KeyboardInterrupt:
        logger.info(f"{green}\n{'*' * 100}\nMONITORING STOPPED BY USER\n{'*' * 100}{reset}")
    except Exception as e:
        logger.critical(f"{red}\n{'*' * 100}\nCRITICAL ERROR: {e}\n{'*' * 100}", exc_info=True)
        logger.info("*" * 100 + "\n" + reset)
        print(f"Fatal error: {e!s}")
    finally:
        print("\nAnalysis session ended.\n")


if __name__ == "__main__":
    main()
