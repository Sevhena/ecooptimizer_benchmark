from pathlib import Path
import argparse
import subprocess
import logging
import sys
import json
import shutil
import time
from typing import Optional

import yaml

WORKTREE_DIR = Path("worktrees").resolve()
PATCHES_DIR = Path("artifacts/patches").resolve()
SELECTED_REPOS_CONFIG = Path("configs/selected.yaml").resolve()


class UTCFormatter(logging.Formatter):
    converter = time.gmtime  # Use UTC instead of local time

    def formatTime(self, record, datefmt=None):  # noqa: ANN001
        return super().formatTime(record, datefmt)


# --- Setup logging ---
def setup_logging(log_file: Path) -> logging.Logger:
    log_file.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("create_patches")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    # File handler logs everything
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)
    fh_formatter = UTCFormatter("%(asctime)s - %(levelname)s - %(message)s")
    fh.setFormatter(fh_formatter)

    # Stream handler logs only progress
    # ch = logging.StreamHandler(sys.stdout)
    # ch.setLevel(logging.INFO)
    # ch_formatter = logging.Formatter("%(message)s")
    # ch.setFormatter(ch_formatter)

    logger.addHandler(fh)
    # logger.addHandler(ch)

    return logger


def load_yaml(path: Path):
    with path.open() as f:
        return yaml.safe_load(f)


class ProgressUpdater:
    """Helper class to manage two-line progress updates."""

    def __init__(self, total: int):
        self.total = total
        self.last_message_length = [0, 0]  # Track lengths of both lines
        # Reserve two lines and leave cursor at the second line
        sys.stdout.write("\n\n")
        sys.stdout.flush()

    def update(self, line1: str, line2: str):
        """Update the two progress lines in-place."""
        # Move cursor up 2 lines
        sys.stdout.write("\033[2A")

        # Clear and write line 1
        sys.stdout.write("\r\033[K]")
        sys.stdout.write("\r" + line1)

        # Move to line 2
        sys.stdout.write("\033[1B")

        # Clear and write line 2
        sys.stdout.write("\r\033[K]")
        sys.stdout.write("\r" + line2 + "\n")

        sys.stdout.flush()

        # Update stored lengths
        self.last_message_length = [len(line1), len(line2)]

    def complete(self):
        """Clear progress lines and move cursor below them."""
        # Move cursor up 2 lines
        sys.stdout.write("\033[2A")

        # Clear both lines
        sys.stdout.write("\r" + " " * self.last_message_length[0] + "\033[1B]")
        sys.stdout.write("\r" + " " * self.last_message_length[1] + "\n")

        sys.stdout.flush()


# --- Git worktree creation ---
def create_worktree(base_repo: Path, worktree_dir: Path, logger: logging.Logger) -> bool:
    try:
        subprocess.run(
            ["git", "worktree", "add", str(worktree_dir), "--force"],
            cwd=base_repo,
            check=True,
            capture_output=True,
            text=True,
        )
        logger.debug(f"Created worktree at {worktree_dir}")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to create worktree: {e.stderr}")
        return False


# --- Run add_annotations.py ---
def add_codecarbon_annotations(repo_name: str, smell_id: str, logger: logging.Logger) -> bool:
    try:
        logger.debug("Adding CodeCarbon annotations")
        subprocess.run(
            ["python", "scripts/add_codecarbon_annotations.py", repo_name, smell_id],
            cwd=Path(),
            check=True,
            stdout=subprocess.DEVNULL,
        )
        logger.debug(f"[{smell_id}] Annotation added.")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"[{smell_id}] Annotation failed: {e.stderr}")
        raise Exception(f"Annotation failed for {smell_id}") from e


# --- Run apply_refactor.py ---
def refactor_smell(repo_name: str, smell_id: str, logger: logging.Logger) -> bool:
    try:
        logger.debug(f"Refactoring smell {smell_id} in {repo_name}")
        subprocess.run(
            [
                "ecooptimizer",
                "--root",
                f"repositories/{repo_name}",
                "--refactor-only",
                "--save-to-original",
                "--smells-file",
                f"artifacts/smells_annotated/{repo_name}/report_{smell_id}.json",
                "--smell-id",
                smell_id,
            ],
            cwd=Path(),
            check=True,
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
        )
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"[{smell_id}] Refactoring failed: {e.stderr}")
        raise Exception(f"Refactoring failed for {smell_id}") from e


def fix_refactored_patch_path(patch_path_refactored: Path, smell_id: str, symbol: str) -> None:
    """Add a refactored tag to the ouput file in the Emissions tracker object in the .patch file."""
    patch_content = patch_path_refactored.read_text()
    fixed_patch_content = patch_content.replace(
        f"{symbol}/{smell_id}.csv", f"{symbol}/{smell_id}_refactored.csv"
    )
    patch_path_refactored.write_text(fixed_patch_content)


def create_patch(
    patch_path: Path, smell_id: str, worktree_path: Path, logger: logging.Logger
) -> None:
    """Create a patch file from the worktree changes."""
    try:
        result = subprocess.run(
            ["git", "diff"], cwd=worktree_path, capture_output=True, text=True, check=True
        )
        if not result.stdout.strip():
            logger.warning(f"[{smell_id}] No changes detected; skipping patch creation.")
        else:
            patch_path.write_text(result.stdout)
            logger.debug(f"Patch saved to {patch_path}\n")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to create patch: {e.stderr}")
        raise Exception(f"Patch creation failed for {smell_id}") from e


# --- Create patch for a smell ---
def create_patches(
    smell: tuple[str, str], repo_name: str, base_repo: Path, logger: logging.Logger
) -> None:
    symbol = smell[0]
    smell_id = smell[1]

    worktree_path = WORKTREE_DIR / repo_name
    patch_path_original = PATCHES_DIR / repo_name / symbol / smell_id / "original.patch"
    patch_path_refactored = PATCHES_DIR / repo_name / symbol / smell_id / "refactored.patch"
    try:
        if not worktree_path.exists():
            create_worktree(base_repo, worktree_path, logger)

        if not add_codecarbon_annotations(repo_name, smell_id, logger):
            subprocess.run(["git", "restore", "."], cwd=worktree_path, check=True)
            raise Exception(f"Failed to add annotations for {smell_id} in {repo_name}")

        patch_path_original.parent.mkdir(parents=True, exist_ok=True)
        create_patch(patch_path_original, smell_id, worktree_path, logger)
        logger.debug(f"[{smell_id}] Original patch created at {patch_path_original}")

        refactor_smell(repo_name, smell_id, logger)
        create_patch(patch_path_refactored, smell_id, worktree_path, logger)
        fix_refactored_patch_path(patch_path_refactored, smell_id, symbol)
    except Exception as e:
        logger.error(f"[{smell_id}] Patch creation failed: {e}")
        subprocess.run(["git", "restore", "."], cwd=worktree_path, check=True)
        raise Exception(f"Patch creation failed for {smell_id}") from e
    finally:
        # Clean up the worktree
        subprocess.run(["git", "restore", "."], cwd=worktree_path, check=True)
        logger.debug(f"[{smell_id}] Worktree cleaned.")


# --- Load smells from analysis results ---
def load_smells(repo_name: str, artifacts_dir: Path, logger: logging.Logger) -> dict[str, dict]:
    path = artifacts_dir / f"analysis_results_{repo_name}.json"
    if not path.exists():
        logger.error(f"Analysis results not found for repo: {repo_name}")
        return {}
    with path.open() as f:
        smells = json.load(f)
    return smells


def clear_patches(repo_name: str, smell_id: Optional[str] = None) -> None:
    """Clear existing patches for a specific smell or all smells in a repo."""
    if smell_id:
        patch_path = PATCHES_DIR / repo_name / smell_id
        if patch_path.exists():
            shutil.rmtree(patch_path)
    else:
        repo_patches_dir = PATCHES_DIR / repo_name
        if repo_patches_dir.exists():
            shutil.rmtree(repo_patches_dir)


# --- Entrypoint ---
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=str, help="Generate patches for a specific repo")
    parser.add_argument("--smell", type=str, help="Generate patch for a specific smell (id)")
    args = parser.parse_args()

    log_file = Path("logs/create_patches.log")
    logger = setup_logging(log_file)

    if args.smell and not args.repo:
        logger.error("Please specify a repository with --repo when using --smell")
        sys.exit(1)

    artifacts_dir = Path("artifacts/smells")
    repos_dir = Path("repositories")

    if args.repo:
        if not args.smell:
            logger.info(f"Generating patches for repo: {args.repo}")
        repo_list = [args.repo]
    else:
        logger.info("Generating patches for all selected repositories")

        repo_list = load_yaml(SELECTED_REPOS_CONFIG).get("repos", [])

    failed_patches: dict[str, list[str]] = dict()

    for repo_name in repo_list:
        base_repo = repos_dir / repo_name
        if not base_repo.exists():
            logger.error(f"Repository folder not found: {base_repo}")
            continue

        failed_patches[repo_name] = []
        smells = load_smells(repo_name, artifacts_dir, logger)

        if args.smell:
            logger.info(f"Generating patches for smell {args.smell} in repo {repo_name}\n")
            smell_meta = [(smells[args.smell]["symbol"], args.smell)]
            clear_patches(repo_name, args.smell)
        else:
            logger.info(f"Generating patches for all smells in {repo_name}\n")
            smell_meta = [(smell["symbol"], smell_id) for smell_id, smell in smells.items()]
            clear_patches(repo_name)

        total_smells = len(smell_meta)

        if not args.smell:
            logger.info(f"Patching {total_smells} smells in {repo_name}")

        progress = ProgressUpdater(total=total_smells)
        smells_processed = 0

        for smell in smell_meta:
            try:
                if not args.smell:
                    progress.update(
                        f"Processing smell ({smells_processed + 1}/{total_smells}) : ({smell})",
                        f"Patches failed: {len(failed_patches[repo_name])}",
                    )
                create_patches(smell, repo_name, base_repo, logger)
            except Exception as e:
                logger.error(f"Failed to create patch for {smell[1]} in {repo_name}")
                sys.stdout.write("\033[1A")
                logger.debug(f"Exception details: {e}", exc_info=True)
                failed_patches[repo_name].append(smell[1])
            finally:
                smells_processed += 1

    if any(failed_patch for failed_patch in failed_patches.values()):
        logger.warning("Some patches failed to create:")
        for repo, smell_ids in failed_patches.items():
            logger.warning(f"Repo: {repo}, Smells: {', '.join(smell_ids)}")
    else:
        logger.info("All patches created successfully.")


if __name__ == "__main__":
    main()
