import time
import subprocess
import toml
import logging
from typing import Optional
from pathlib import Path

# Configuration
REPO_DIR = Path("repositories")
ANALYSIS_RESULTS_DIR = Path("analysis_results")
CONFIG_FILE = Path(".ecooptimizer")
LOG_FILE = "analysis_debug.txt"
DATA_COLLECTOR = Path("data_collect.py")

# Setup logging
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "analysis_monitor.log"),
    ],
)
logger = logging.getLogger(__name__)


def load_config() -> dict:
    """Load and parse the TOML config file"""
    try:
        with CONFIG_FILE.open() as f:
            config = toml.load(f)
        logger.debug(f"Successfully loaded config from {CONFIG_FILE}")
        return config
    except Exception as e:
        logger.error(f"Failed to load config: {e!s}")
        raise


def save_config(config: dict) -> None:
    """Save the config file in TOML format"""
    try:
        with CONFIG_FILE.open("w") as f:
            toml.dump(config, f)
        logger.debug(f"Successfully saved config to {CONFIG_FILE}")
    except Exception as e:
        logger.error(f"Failed to save config: {e!s}")
        raise


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


def select_directories_to_exclude(repo_path: str, current_excludes: list[str]) -> list[str]:
    """Prompt user to select directories to exclude"""
    try:
        dirs = [d for d in get_repo_directories(repo_path) if d not in current_excludes]

        if not dirs:
            logger.debug("No directories available to exclude")
            return []

        print(f"\nFound these top-level directories in {repo_path}:")
        for i, d in enumerate(dirs, 1):
            print(f"{i}. {d}")

        print("\nSelect directories to exclude (comma-separated numbers, or 0 for none):")
        selections = input("> ").strip()

        if selections == "0":
            logger.debug("User selected no directories to exclude")
            return []

        selected_indices = [int(s.strip()) - 1 for s in selections.split(",")]
        selected_dirs = [dirs[i] for i in selected_indices if 0 <= i < len(dirs)]
        logger.debug(f"User selected to exclude: {selected_dirs}")
        return selected_dirs
    except (ValueError, IndexError) as e:
        logger.warning(f"Invalid directory selection: {e!s}")
        print("Invalid selection, excluding none")
        return []
    except Exception as e:
        logger.error(f"Error in directory exclusion: {e!s}")
        return []


def update_config_for_repo(
    config: dict, repo_name: str, additional_excludes: Optional[list[str]] = None
) -> None:
    """Update TOML config file for a new repo"""
    try:
        config["root"] = repo_name
        config["target"] = repo_name
        config["analysis_results_file"] = f"analysis_results/analysis_results_{repo_name}.json"

        if additional_excludes:
            current_excludes = config.get("exclude", [])
            current_excludes.extend(additional_excludes)
            config["exclude"] = list(set(current_excludes))
        logger.info(f"Updated config for repo: {repo_name}")
    except Exception as e:
        logger.error(f"Failed to update config: {e!s}")
        raise


def run_analysis() -> None:
    """Run ecooptimizer and wait for completion"""
    try:
        logger.info("Starting analysis...")
        print("Running analysis...")
        with LOG_FILE.open("w") as log_file:
            process = subprocess.Popen(["ecooptimizer"], stdout=log_file, stderr=subprocess.STDOUT)
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
            print("Running data collection...")
            result = subprocess.run(
                ["python3", str(DATA_COLLECTOR), str(ANALYSIS_RESULTS_DIR)],
                check=True,
                capture_output=True,
                text=True,
            )
            logger.debug(f"Data collector output:\n{result.stdout}")
            if result.stderr:
                logger.warning(f"Data collector errors:\n{result.stderr}")
            logger.info("Data collection completed")
            print("Data collection completed")
        else:
            logger.warning(f"Data collector script not found at {DATA_COLLECTOR}")
            print(f"Warning: Data collector script not found at {DATA_COLLECTOR}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Data collection failed: {e!s}\n{e.stderr}")
        raise
    except Exception as e:
        logger.error(f"Error running data collector: {e!s}")
        raise


def main() -> None:
    """Main monitoring function"""
    try:
        logger.info("Starting repository monitoring")
        print("Monitoring for new repos...")

        # Create analysis_results directory if it doesn't exist
        ANALYSIS_RESULTS_DIR.mkdir(exist_ok=True)
        logger.debug(f"Ensured directory exists: {ANALYSIS_RESULTS_DIR}")

        while True:
            try:
                config = load_config()
                current_excludes = config.get("exclude", [])
                logger.debug(f"Current exclude patterns: {current_excludes}")

                new_repos = get_new_repos()
                if new_repos:
                    repo_name = new_repos[0]
                    repo_path = REPO_DIR / repo_name  # noqa: F841
                    logger.info(f"Found new repository: {repo_name}")

                    additional_excludes = []

                    # Uncomment the following lines if you want to prompt for directories to exclude
                    #
                    # additional_excludes = select_directories_to_exclude(
                    #     str(repo_path), current_excludes
                    # )

                    update_config_for_repo(config, repo_name, additional_excludes)
                    save_config(config)

                    run_analysis()
                    run_data_collector()
                else:
                    logger.debug("No new repositories found")
                    print(".", end="", flush=True)
                    time.sleep(10)

            except KeyboardInterrupt:
                logger.info("Monitoring stopped by user")
                print("\nScript stopped by user")
                break
            except Exception as e:
                logger.error(f"Error in main loop: {e!s}", exc_info=True)
                print(f"Error: {e!s}")
                time.sleep(10)  # Prevent tight error loop

    except Exception as e:
        logger.critical(f"Fatal error: {e!s}", exc_info=True)
        print(f"Fatal error: {e!s}")


if __name__ == "__main__":
    main()
