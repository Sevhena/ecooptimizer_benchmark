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

ROOT_DIR = Path().resolve()
ARTIFACTS_DIR = ROOT_DIR / "artifacts"
WORKTREE_DIR = ROOT_DIR / "worktrees"
PATCHES_DIR = ARTIFACTS_DIR / "patches"
ANNOTATED_SMELLS_DIR = ARTIFACTS_DIR / "smells" / "annotated"
COVERED_SMELLS_DIR = ARTIFACTS_DIR / "smells" / "covered"
SELECTED_REPOS_CONFIG = ROOT_DIR / "configs" / "selected.yaml"

LOG_DIR = Path("logs").resolve()
LOG_DIR.mkdir(exist_ok=True)


class UTCFormatter(logging.Formatter):
    converter = time.gmtime  # Use UTC instead of local time

    def formatTime(self, record, datefmt=None):  # noqa: ANN001
        return super().formatTime(record, datefmt)


def setup_logging():
    """Configure logging to file and console."""
    log_file = LOG_DIR / "patch_creation.log"

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = UTCFormatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter("%(message)s")
    console_handler.setFormatter(console_formatter)

    logging.basicConfig(level=logging.DEBUG, handlers=[file_handler, console_handler])


def load_yaml(path: Path):
    with path.open() as f:
        return yaml.safe_load(f)


# --- Git worktree creation ---
def create_worktree(base_repo: Path, worktree_dir: Path) -> bool:
    try:
        subprocess.run(
            ["git", "worktree", "add", str(worktree_dir), "--force"],
            cwd=base_repo,
            check=True,
            capture_output=True,
            text=True,
        )
        logging.debug(f"Created worktree at {worktree_dir}")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to create worktree: {e.stderr}")
        return False


# --- Run add_annotations.py ---
def add_annotations(repo_name: str, smell_id: str, tracker: str = "codecarbon") -> bool:
    try:
        logging.debug("Adding CodeCarbon annotations")
        subprocess.run(
            [
                sys.executable,
                "scripts/add_annotations.py",
                repo_name,
                smell_id,
                "--tracker",
                tracker,
            ],
            cwd=Path(),
            check=True,
            stdout=subprocess.DEVNULL,
        )
        logging.debug(f"[{smell_id}] Annotation added.")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"[{smell_id}] Annotation failed: {e.stderr}")
        raise Exception(f"Annotation failed for {smell_id}") from e


# --- Run apply_refactor.py ---
def refactor_smell(repo_name: str, smell_id: str, tracker: str = "codecarbon") -> bool:
    try:
        logging.debug(f"Refactoring smell {smell_id} in {repo_name}")
        subprocess.run(
            [
                "ecooptimizer",
                "refactor",
                f"{ANNOTATED_SMELLS_DIR}/{tracker}/{repo_name}.json",
                "--smell-id",
                smell_id,
                "--save-to-original",
                "--log-dir",
                f"{LOG_DIR / 'ecooptimizer' / repo_name}",
            ],
            cwd=(WORKTREE_DIR / repo_name),
            check=True,
            stderr=subprocess.DEVNULL,
        )
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"[{smell_id}] Refactoring failed: {e!s}")
        raise


def fix_refactored_patch_path(
    patch_path_refactored: Path, smell_id: str, symbol: str, tracker: str = "codecarbon"
):
    """Add a refactored tag to the ouput file in the Emissions tracker object in the .patch file."""
    try:
        patch_content = patch_path_refactored.read_text()
        if tracker == "codecarbon":
            fixed_patch_content = patch_content.replace(
                f"{symbol}/{smell_id}.csv", f"{symbol}/{smell_id}_refactored.csv"
            )
        else:
            fixed_patch_content = patch_content.replace(
                f"{symbol}/{smell_id}_usage.csv", f"{symbol}/{smell_id}_usage_refactored.csv"
            )
        patch_path_refactored.write_text(fixed_patch_content)
    except Exception:
        logging.error(f"[{smell_id}] Unable to update refactored .patch file")
        return False

    return True


def create_patch(patch_path: Path, smell_id: str, worktree_path: Path):
    """Create a patch file from the worktree changes."""
    try:
        result = subprocess.run(
            ["git", "diff"], cwd=worktree_path, capture_output=True, text=True, check=True
        )
        if not result.stdout.strip():
            logging.warning(f"[{smell_id}] No changes detected; skipping patch creation.")
            return False
        else:
            patch_path.write_text(result.stdout)
            logging.debug(f"Patch saved to {patch_path}\n")
            return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to create patch: {e.stderr}")
        raise


# --- Create patch for a smell ---
def create_patches(
    smell: tuple[str, str], repo_name: str, base_repo: Path, tracker: str = "codecarbon"
) -> None:
    symbol = smell[0]
    smell_id = smell[1]

    worktree_path = WORKTREE_DIR / repo_name
    worktree_path.parent.mkdir(exist_ok=True)

    patch_path_original = PATCHES_DIR / tracker / repo_name / symbol / smell_id / "original.patch"
    patch_path_refactored = (
        PATCHES_DIR / tracker / repo_name / symbol / smell_id / "refactored.patch"
    )
    failed_patch_path = PATCHES_DIR / tracker / repo_name / "_failed" / f"{symbol}_{smell_id}.patch"
    try:
        if not worktree_path.exists():
            create_worktree(base_repo, worktree_path)

        if not add_annotations(repo_name, smell_id, tracker):
            raise Exception(f"Failed to add annotations for {smell_id} in {repo_name}")

        patch_path_original.parent.mkdir(parents=True, exist_ok=True)
        if not create_patch(patch_path_original, smell_id, worktree_path):
            raise Exception(f"Original patch creation failed for smell {smell_id}")
        logging.debug(f"[{smell_id}] Original patch created at {patch_path_original}")

        refactor_smell(repo_name, smell_id)
        if not create_patch(patch_path_refactored, smell_id, worktree_path):
            raise Exception(f"Refactored patch creation failed for smell {smell_id}")
        if not fix_refactored_patch_path(patch_path_refactored, smell_id, symbol, tracker):
            raise Exception("Path update in refactored .patch failed")

        if failed_patch_path.exists():
            logging.debug(f"[{smell_id}] Removing existing failed patch: {failed_patch_path}")
            failed_patch_path.unlink()

            failed_smells = next((file for file in failed_patch_path.parent.iterdir()), None)
            if not failed_smells:
                failed_patch_path.parent.rmdir()
                logging.debug("No remaining failed patches, _failed directory removed")

    except (KeyboardInterrupt, Exception) as e:
        logging.error(f"[{smell_id}] Patches creation failed: {e}")

        subprocess.run(["git", "restore", "."], cwd=worktree_path, check=True)

        if patch_path_original.exists():
            logging.debug(
                f"[{smell_id}] Cleaning up created patches. Adding original patch to failed patches."
            )
            failed_patch_path.parent.mkdir(parents=True, exist_ok=True)
            patch_path_original.replace(failed_patch_path)

        shutil.rmtree(patch_path_refactored.parent, ignore_errors=True)

        raise e
    finally:
        # Clean up the worktree
        subprocess.run(["git", "restore", "."], cwd=worktree_path, check=True)
        logging.debug(f"[{smell_id}] Worktree cleaned.")


# --- Load smells from analysis results ---
def load_smells(repo_name: str) -> dict[str, dict]:
    path = COVERED_SMELLS_DIR / f"{repo_name}.json"
    if not path.exists():
        logging.error(f"Analysis results not found for repo: {repo_name}")
        return {}
    with path.open() as f:
        smells = json.load(f)
    return smells


def clear_patches(
    repo_name: str, smell_data: Optional[dict] = None, tracker: str = "codecarbon"
) -> None:
    """Clear existing patches for a specific smell or all smells in a repo."""
    annotated_smells_file = ANNOTATED_SMELLS_DIR / f"{repo_name}.json"

    if smell_data:
        patch_path = (
            PATCHES_DIR / tracker / repo_name / smell_data["symbol"] / smell_data["smell_id"]
        )
        if patch_path.exists():
            logging.debug(
                f"Removing patches for smell {smell_data['smell_id']} in repo {repo_name}: {patch_path}"
            )
            shutil.rmtree(patch_path)
        else:
            logging.debug(
                f"No patches found for smell {smell_data['smell_id']} in repo {repo_name}"
            )

        if annotated_smells_file.exists():
            logging.debug(f"Annotated smells file exists: {annotated_smells_file}")
            with annotated_smells_file.open() as f:
                annotated_smells = load_smells(repo_name)
            if smell_data["smell_id"] not in annotated_smells:
                logging.warning(
                    f"Smell {smell_data['smell_id']} not found in annotated smells for repo {repo_name}. Deleting file."
                )
                annotated_smells_file.unlink(missing_ok=True)
            else:
                logging.debug(
                    f"Updating annotated smells file for smell {smell_data['smell_id']} in repo {repo_name}"
                )
                annotated_smells[smell_data["smell_id"]] = smell_data["smells"][
                    smell_data["smell_id"]
                ]
                with annotated_smells_file.open("w") as f:
                    json.dump(annotated_smells, f, indent=4)
        else:
            logging.debug(f"No annotated smells file found for repo {repo_name}")
    else:
        repo_patches_dir = PATCHES_DIR / tracker / repo_name
        if repo_patches_dir.exists():
            logging.info(f"Removing all patches for repo {repo_name}: {repo_patches_dir}")
            shutil.rmtree(repo_patches_dir)
        else:
            logging.debug(f"No patches found for repo {repo_name}")

        # Remove the annotated smells file if it exists
        logging.debug(f"Checking for annotated smells file: {annotated_smells_file}")
        if annotated_smells_file.exists():
            logging.info(
                f"Deleting annotated smells file for repo {repo_name}: {annotated_smells_file}"
            )
            annotated_smells_file.unlink(missing_ok=True)
        else:
            logging.debug(f"No annotated smells file to delete for repo {repo_name}")


ALL_SMELL_TYPES = {
    "crc": "cached-repeated-calls",
    "lec": "long-element-chain",
    "lle": "long-lambda-expr",
    "lmc": "long-message-chain",
    "nsu": "no-self-use",
    "scl": "string-concat-loop",
    "tma": "too-many-arguments",
    "ugen": "use-a-generator",
}


# --- Entrypoint ---
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=str, help="Generate patches for a specific repo")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--type",
        choices=ALL_SMELL_TYPES.keys(),
        help="Generate patches for a specific smell type:\n"
        + "\n- ".join([str(item) for item in ALL_SMELL_TYPES.items()]),
    )
    group.add_argument("--smells", nargs="+", help="Generate patch for a specific smell (id)")
    parser.add_argument(
        "--failed-only",
        action="store_true",
        help="Generate patches only for smells that had previously failed.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Generate patches for all smells in the specified repo or type including overwriting existing ones (DEFAULT: False)",
    )
    parser.add_argument(
        "--tracker",
        choices=["codecarbon", "usage"],
        default="codecarbon",
        type=str,
        help="Which types of annotations to add",
    )
    args = parser.parse_args()

    setup_logging()

    if args.smells and not args.repo:
        logging.error("Please specify a repository with --repo when using --smells")
        sys.exit(1)

    if args.failed_only and args.smells:
        logging.error("Do not use --failed-only when specifying smell ids.")
        sys.exit(1)

    repos_dir = Path("repositories")
    select_repos_config = load_yaml(SELECTED_REPOS_CONFIG)

    if args.type:
        # Filter selected smells to only include the specified type for each repo
        smell_type = ALL_SMELL_TYPES[args.type]
        select_repos_config["smells"] = {
            repo: {
                symbol: smell_ids
                for symbol, smell_ids in repo_items.items()
                if symbol == smell_type
            }
            for repo, repo_items in select_repos_config["smells"].items()
        }

        logging.info(f"Generating patches for smell type: {smell_type}")
        logging.debug(f"Selected smells for type {smell_type}: {select_repos_config['smells']}")

    if args.repo:
        if not args.smells:
            logging.info(f"Generating patches for repo: {args.repo}")
        repo_list: list[str] = args.repo.split(",")
    else:
        logging.info("Generating patches for all selected repositories")

        repo_list = select_repos_config.get("repos", [])

    failed_patches: dict[str, list[str]] = dict()

    for repo_name in repo_list:
        base_repo = repos_dir / repo_name
        if not base_repo.exists():
            logging.error(f"Repository folder not found: {base_repo}")
            continue

        failed_patches[repo_name] = []
        smells = load_smells(repo_name)

        if not smells:
            continue

        smell_meta = []
        smell_map: dict[str, list[str]] = select_repos_config.get("smells", {}).get(repo_name, {})
        if args.failed_only:
            failed_dir = PATCHES_DIR / args.tracker / repo_name / "_failed"
            if not failed_dir.exists():
                logging.debug(f"No smells failed to create patches for repo {repo_name}")
                continue

            logging.info(f"Refactoring failed smells in {repo_name}")

            for file in failed_dir.iterdir():
                smell_type, smell_id = file.stem.split("_")
                if args.type and smell_type != ALL_SMELL_TYPES[args.type]:
                    continue
                smell_meta.append((smell_type, smell_id))
                clear_patches(
                    repo_name,
                    {"symbol": smells[smell_id]["symbol"], "smell_id": smell_id, "smells": smells},
                    args.tracker,
                )
        else:
            if args.smells:
                logging.info(f"Generating patches for smells {args.smells} in repo {repo_name}\n")
                for smell in args.smells:
                    smell_meta.append((smells[smell]["symbol"], smell))
                    clear_patches(
                        repo_name,
                        {"symbol": smells[smell]["symbol"], "smell_id": smell, "smells": smells},
                        args.tracker,
                    )
            elif args.type:
                logging.info(f"Generating patches for smell type {args.type} in repo {repo_name}\n")
                if not smell_map:
                    logging.warning(
                        f"No smells of type '{args.type}' selected for {repo_name}. Skipping patch generation."
                    )
                    continue
                logging.debug(f"Selected smells for {repo_name}: {smell_map}")

                for symbol, smell_ids in smell_map.items():
                    for smell_id in smell_ids:
                        if smell_id in smells:
                            patch_dir = PATCHES_DIR / args.tracker / repo_name / symbol / smell_id
                            if not args.all and patch_dir.exists():
                                logging.debug(
                                    f"Patches already exist for {smell_id} in {repo_name}. Skipping."
                                )
                                continue

                            smell_meta.append((symbol, smell_id))

                            logging.debug(
                                f"Removing existing patches for {smell_id} in {repo_name}"
                            )
                            clear_patches(
                                repo_name,
                                {"symbol": symbol, "smell_id": smell_id, "smells": smells},
                                args.tracker,
                            )
                        else:
                            logging.warning(
                                f"Smell ID {smell_id} not found in analysis results for {repo_name}"
                            )
            else:
                if not smell_map:
                    logging.warning(
                        f"No smells of type '{args.type}' selected for {repo_name}. Skipping patch generation."
                    )
                    continue
                logging.debug(f"Selected smells for {repo_name}: {smell_map}")

                smell_id_list = []
                for _, smell_ids in smell_map.items():
                    smell_id_list.extend(smell_ids)
                logging.debug(f"Smell IDs selected for {repo_name}: {smell_id_list}")
                if not smell_id_list:
                    logging.warning(
                        f"No smells selected for {repo_name}. Skipping patch generation."
                    )
                    continue

                logging.info(f"Generating patches for all smells in {repo_name}\n")

                repo_patch_dir = PATCHES_DIR / args.tracker / repo_name

                smell_meta = [
                    (smell["symbol"], smell_id)
                    for smell_id, smell in smells.items()
                    if smell_id in smell_id_list
                    and (args.all or not (repo_patch_dir / smell["symbol"] / smell_id).exists())
                ]

                if args.all:
                    clear_patches(repo_name, args.tracker)
                else:
                    logging.debug(
                        f"Clearing existing patches for smells in {repo_name} before patch creation"
                    )
                    for smell in smell_meta:
                        clear_patches(
                            repo_name,
                            {"symbol": smell[0], "smell_id": smell[1], "smells": smells},
                            args.tracker,
                        )
        total_smells = len(smell_meta)

        logging.info(f"Patching {total_smells} smells in {repo_name}")

        smells_processed = 0

        for smell in smell_meta:
            try:
                logging.info(
                    f"\n[{repo_name}] [{smells_processed + 1}/{len(smell_meta)}] Patching {smell}..."
                )
                create_patches(smell, repo_name, base_repo, args.tracker)
            except KeyboardInterrupt:
                logging.info("Patch creation interrupted by user.")
                sys.exit(0)
            except Exception as e:
                logging.error(f"Failed to create patch for {smell[1]} in {repo_name}")
                sys.stdout.write("\033[1A")
                logging.debug(f"Exception details: {e}", exc_info=True)
                failed_patches[repo_name].append(smell[1])
            finally:
                smells_processed += 1

    if any(failed_patch for failed_patch in failed_patches.values()):
        logging.warning("Some patches failed to create:")
        for repo, smell_ids in failed_patches.items():
            if smell_ids:
                display_ids = "\n  - ".join(smell_ids)
                logging.warning(f"[{repo}]\n  - {display_ids}")
    else:
        logging.info("All patches created successfully.")


if __name__ == "__main__":
    main()
