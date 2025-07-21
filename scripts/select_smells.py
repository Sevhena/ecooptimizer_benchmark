from collections import defaultdict
from pathlib import Path
import sys
import time
from typing import Any, Optional
import json
import random
import argparse
import logging
import yaml

# Constants
SELECTED_CONFIG_PATH = Path("configs").resolve() / "selected.yaml"

SMELLS_DIR = Path("artifacts").resolve() / "smells"
COVERED_SMELLS_DIR = SMELLS_DIR / "covered"
SELECTED_SMELLS_DIR = SMELLS_DIR / "selected"

SELECTED_SMELLS_DIR.mkdir(exist_ok=True)

SMELL_COUNT = 6

# Typing alias
Smell = dict[str, Any]
GroupedTree = dict[str, Any]


class UTCFormatter(logging.Formatter):
    converter = time.gmtime  # Use UTC instead of local time

    def formatTime(self, record, datefmt=None):  # noqa: ANN001
        return super().formatTime(record, datefmt)


# --- Setup logging ---
def setup_logging():
    """Configure logging to file and console."""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / "smell_selection.log"

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = UTCFormatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter("%(message)s")
    console_handler.setFormatter(console_formatter)

    logging.basicConfig(level=logging.DEBUG, handlers=[file_handler, console_handler])


def load_smells(path: Path) -> list[Smell]:
    with path.open("r") as f:
        return list(json.load(f).values())


def extract_threshold(smell: Smell) -> Optional[str]:
    """Extract threshold part from the message string, if available."""
    msg = smell.get("message", "")
    if "(" in msg and "/" in msg:
        part = msg.split("(")[-1].split(")")[0]
        if "/" in part and all(p.strip().isdigit() for p in part.split("/")):
            return part
    return None


def group_by(smells: list[Smell], key_func) -> dict[str, list[Smell]]:
    groups = defaultdict(list)
    for smell in smells:
        key = key_func(smell)
        groups[key].append(smell)
    return groups


def build_tree(smells: list[Smell]) -> GroupedTree:
    """
    Builds a nested index tree of smells grouped by:
    threshold -> module -> object.
    Adds depth only as needed to get at least 6 leaf bins.
    """

    def flatten_bins(tree) -> list[list[Smell]]:
        bins = []

        def recurse(t):
            if isinstance(t, list):
                bins.append(t)
            elif isinstance(t, dict):
                for v in t.values():
                    recurse(v)

        recurse(tree)
        return bins

    # Start at threshold level
    level1 = group_by(smells, lambda s: extract_threshold(s) or "no-thresh")
    if len(level1) >= 6:
        return level1

    # Add module level
    level2 = {}
    for thresh, smells1 in level1.items():
        level2[thresh] = group_by(smells1, lambda s: s.get("module", "no-module"))
    if len(flatten_bins(level2)) >= 6:
        return level2

    # Add object level
    level3 = {}
    for thresh, moddict in level2.items():
        level3[thresh] = {}
        for mod, smells2 in moddict.items():
            level3[thresh][mod] = group_by(smells2, lambda s: s.get("obj", "no-obj"))
    return level3


def select_from_tree(tree: GroupedTree, max_instances: int = 6) -> list[Smell]:
    """Selects up to `max_instances` from different bins in the tree."""
    selected = []

    def recurse(t: list | dict) -> list[Smell]:
        if isinstance(t, list):
            return [random.choice(t)]
        else:
            collected = []
            for subtree in t.values():
                collected.extend(recurse(subtree))
            return collected

    if isinstance(tree, list):  # fallback
        return random.sample(tree, min(max_instances, len(tree)))

    top_level_keys = list(tree.keys())
    random.shuffle(top_level_keys)

    for key in top_level_keys:
        smells_from_bin = recurse(tree[key])
        if smells_from_bin:
            selected.append(random.choice(smells_from_bin))
        if len(selected) >= max_instances:
            break

    # Fill in remaining slots randomly from all
    if len(selected) < max_instances:
        all_smells = recurse(tree)
        random.shuffle(all_smells)
        for s in all_smells:
            if s not in selected:
                selected.append(s)
            if len(selected) >= max_instances:
                break

    return selected[:max_instances]


def process_repo(
    repo: str,
    smells_by_repo: dict[str, list[Smell]],
    output: dict[str, dict[str, list[str]]],
    all_selected_smells: dict[str, dict[str, Smell]],
):
    smells = smells_by_repo[repo]
    grouped_by_type: dict[str, list[Smell]] = {}
    for smell in smells:
        grouped_by_type.setdefault(smell["symbol"], []).append(smell)

    output[repo] = {}

    for smell_type, instances in grouped_by_type.items():
        logging.debug(
            f"{repo}: Processing smell type '{smell_type}' with {len(instances)} instances"
        )
        if len(instances) <= SMELL_COUNT:
            logging.warning(
                f"{repo}: Only {len(instances)} instances found for smell type '{smell_type}' (less than 6)"
            )
            selected = instances
        else:
            tree = build_tree(instances)
            selected = select_from_tree(tree)

        output[repo][smell_type] = [s["id"] for s in selected]
        for s in selected:
            all_selected_smells[repo][s["id"]] = s


def defaultdict_to_dict(d: Any) -> Any:
    if isinstance(d, defaultdict):
        d = {k: defaultdict_to_dict(v) for k, v in d.items()}
    elif isinstance(d, dict):
        d = {k: defaultdict_to_dict(v) for k, v in d.items()}
    elif isinstance(d, list):
        d = [defaultdict_to_dict(i) for i in d]
    return d


def update_selected_config(output: dict[str, dict[str, list[str]]]):
    if SELECTED_CONFIG_PATH.exists():
        with SELECTED_CONFIG_PATH.open("r") as f:
            config: dict[Any, Any] = yaml.safe_load(f) or {
                "repos": [repo for repo in output.keys()]
            }
    else:
        config: dict[Any, Any] = {"repos": [repo for repo in output.keys()]}

    config["smells"] = defaultdict_to_dict(output)

    with SELECTED_CONFIG_PATH.open("w") as f:
        yaml.dump(config, f)
    logging.info(f"Updated selected.yaml with {len(output)} repos")


def write_selected_smells(repo_smells: dict[str, dict[str, Smell]]):
    for repo, smells in repo_smells.items():
        out_path = SELECTED_SMELLS_DIR / f"{repo}.json"
        with out_path.open("w") as f:
            json.dump(smells, f, indent=2)
            logging.debug(f"Wrote smells for '{repo}' to {out_path}")
    logging.info(f"Wrote selected smells to {SELECTED_SMELLS_DIR}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=str, help="Filter smells for a specific repo only")
    args = parser.parse_args()

    setup_logging()
    logging.info("Starting smell selection process")

    smells_by_repo: dict[str, list[Smell]] = {}
    for file in COVERED_SMELLS_DIR.glob("*.json"):
        repo = file.stem
        if args.repo and repo != args.repo:
            continue
        smells_by_repo[repo] = load_smells(file)
        logging.debug(f"Loaded {len(smells_by_repo[repo])} smells for {repo}")

    selected_config: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list[str]))
    selected_smells: dict[str, dict[str, Smell]] = defaultdict(dict)

    for repo in smells_by_repo:
        process_repo(repo, smells_by_repo, selected_config, selected_smells)

    update_selected_config(selected_config)
    write_selected_smells(selected_smells)
    logging.info("Smell selection completed")


main()
