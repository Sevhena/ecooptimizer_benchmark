import json
import time
import logging
from pathlib import Path
import sys
import argparse

import astroid
from astroid import nodes

from typing import Optional

BENCHMARK_ROOT = Path().resolve()
ARTIFACTS_DIR = BENCHMARK_ROOT / "artifacts"
WORKTREE_DIR = BENCHMARK_ROOT / "worktrees"
SMELLS_DIR = ARTIFACTS_DIR / "smells"
COVERED_SMELLS_DIR = SMELLS_DIR / "covered"
ANNOTATED_SMELLS_DIR = SMELLS_DIR / "annotated"


class UTCFormatter(logging.Formatter):
    converter = time.gmtime  # Use UTC instead of local time

    def formatTime(self, record, datefmt=None):  # noqa: ANN001
        return super().formatTime(record, datefmt)


def setup_logging(repo_name: str):
    """Configure logging to file and console."""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    ann_log_dir = log_dir / "annotations"
    ann_log_dir.mkdir(exist_ok=True)
    log_file = ann_log_dir / f"annotations_{repo_name}.log"

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = UTCFormatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter("%(message)s")
    console_handler.setFormatter(console_formatter)

    logging.basicConfig(level=logging.DEBUG, handlers=[file_handler, console_handler])


def get_code_lines(file_path: Path):
    """Read a file and return its lines."""
    with file_path.open(encoding="utf-8") as f:
        return f.readlines()


def write_code_lines(file_path: Path, lines: list):
    """Write lines back to a file."""
    with file_path.open("w", encoding="utf-8") as f:
        f.writelines(lines)


def find_import_insertion_point(lines: list[str]) -> int:
    last_import_line = -1
    in_docstring = False
    in_multi_import = False
    for i, line in enumerate(lines):
        line = line.strip()
        logging.debug(f"Import line: {line}")
        # Skip empty lines, comments, and docstrings before imports
        if not line or line.startswith("#"):
            continue
        if line.startswith('"""'):
            if not line.replace('"""', "", 1).endswith('"""'):
                if in_docstring:
                    logging.debug("Exiting docstring")
                    in_docstring = False
                    last_import_line = i
                else:
                    logging.debug("Entering docstring")
                    in_docstring = True

            continue
        if line.startswith("'''"):
            if not line.replace("'''", "", 1).endswith("'''"):
                if in_docstring:
                    in_docstring = False
                else:
                    in_docstring = True

            continue
        if line.startswith(("from __future__", "import ", "from ")):
            if "(" in line and ")" not in line:
                # If the last import line is a multi-line import, continue
                in_multi_import = True
                continue
            last_import_line = i
            continue
        elif in_multi_import:
            if line.endswith(")"):
                in_multi_import = False
                last_import_line = i
            continue
        elif in_docstring:
            continue
        else:
            break
    return last_import_line + 1  # Insert after the last import


def add_decorator_to_function(
    file_path: Path,
    cc_args: str,
    line_num: int,
    col_num: int,
    tracker: str = "codecarbon",
):
    """Add CodeCarbon decorator to a function."""
    lines = get_code_lines(file_path)

    logging.debug(f"Initial line number: {line_num}")

    # Add import if not present
    if tracker == "codecarbon":
        package = "codecarbon"
        track_import = "EmissionsTracker"
        decorator = "track_emissions"
    else:
        package = "crtracker"
        track_import = "MemoryCPUTracker"
        decorator = "MemoryCPUTracker.track_usage"

    # Add the decorator
    decorator_line = " " * (col_num) + f"@{decorator}({cc_args})\n"
    lines.insert(line_num - 1, decorator_line)

    # Add import if not present
    if not any(
        line.strip().startswith((f"from {package} import {track_import}", f"import {package}"))
        for line in lines
    ):
        import_id = find_import_insertion_point(lines)

        lines.insert(import_id, f"from {package} import {track_import}\n")

    write_code_lines(file_path, lines)
    logging.info(f"Added decorator to function in {file_path} at line {line_num}")


def find_statement_insertion_point(
    tree: nodes.Module,
    target_lineno: int,
    target_col_offset: int,
) -> Optional[tuple[int, int]]:
    """
    Find where to insert a statement containing the target node.

    Returns: (lineno, col_offset) where new statement should be inserted
             or None if target is at module level
    """
    target_node = None
    for node in tree.nodes_of_class(nodes.NodeNG):
        if (
            hasattr(node, "lineno")
            and node.lineno == target_lineno
            and hasattr(node, "col_offset")
            and node.col_offset == target_col_offset
        ):
            target_node = node
            break

    if not target_node:
        return None

    current = target_node
    while current.parent:
        logging.debug(
            f"Checking parent node {current.parent.__class__.__name__} of {current.__class__.__name__}"
        )
        if hasattr(current.parent, "body"):
            if not isinstance(current.parent, nodes.Module):
                parent_str = current.parent.as_string().strip().splitlines()
                logging.debug(f"Parent node body: {parent_str}")
                header_stop = next(
                    i for i, line in enumerate(parent_str) if line.strip()[-1] == ":"
                )
                logging.debug(f"Header stop at line {header_stop} for parent node")
                if current.parent.lineno + header_stop >= target_lineno:
                    return (current.parent.lineno, current.parent.col_offset)

            return (current.lineno, current.col_offset)  # type: ignore
        current = current.parent

    return None


def wrap_with_context_manager(
    file_path: Path,
    cc_args: str,
    start_line: int,
    end_line: int,
    is_block: bool = True,
    start_col: Optional[int] = None,
    end_col: Optional[int] = None,
    tab_size: int = 4,
    tracker: str = "codecarbon",
):
    """Wrap code block with CodeCarbon context manager, handling multi-line expressions."""
    lines = get_code_lines(file_path)
    original_indent = lines[start_line - 1][:start_col]
    insertion_line = start_line

    source = file_path.read_text(encoding="utf-8")

    try:
        tree = astroid.parse(source)
    except astroid.AstroidSyntaxError:
        return None

    if is_block:
        is_in_expression = False
    else:
        # If not a block, we need to check if the start and end columns are within the same line
        if start_col is None or end_col is None:
            raise ValueError("start_col and end_col must be provided for non-block expressions")

        # Check if we're in the middle of an expression
        is_sole_assign = False
        for node in tree.nodes_of_class((nodes.AnnAssign, nodes.Assign, nodes.AugAssign)):
            is_sole_assign = (
                node.lineno <= start_line and node.end_lineno >= end_line  # type: ignore
            ) and not isinstance(node.value, nodes.BinOp)

            if is_sole_assign:
                break

        logging.debug(
            f"Checking if expression is sole assignment: {is_sole_assign} for lines {start_line}-{end_line}"
        )

        is_in_expression = (
            not is_sole_assign and not lines[start_line - 1][:start_col].strip() == ""
        )

        logging.debug(
            f"Expression spanning lines {start_line}-{end_line}, is_in_expression={is_in_expression}"
        )

    if is_in_expression:
        # Generate unique variable name
        import uuid

        # Find start of the enclosing expression
        insertion_point = find_statement_insertion_point(tree, start_line, start_col)
        logging.debug(
            f"Insertion point for expression at line {start_line}, column {start_col}: {insertion_point}"
        )
        if not insertion_point:
            logging.error(
                f"Could not find enclosing expression for line {start_line}, column {start_col} in {file_path}"
            )
            return

        insertion_line, insertion_col = insertion_point
        var_name = f"_carbon_wrapped_{uuid.uuid4().hex[:8]}"

        if start_line == end_line:
            # Single line expression - extract it
            code_line = lines[start_line - 1]
            smell_statement = code_line[start_col:end_col].strip()
            new_code_line = code_line[:start_col] + var_name + code_line[end_col:]
            logging.debug(
                f"Extracting single line expression: {code_line.strip()} at line {start_line}"
            )
            lines[start_line - 1] = new_code_line
        else:
            # Multi-line expression - extract the block
            code_block = []
            for i in range(start_line - 1, end_line):
                if i == start_line - 1:
                    code_block.append(lines[i][start_col:].strip())
                elif i == end_line - 1:
                    code_block.append(lines[i][:end_col].strip())
                else:
                    code_block.append(lines[i].strip())

            logging.debug(
                f"Extracting multi-line expression from lines {start_line} to {end_line}: {code_block}"
            )

            smell_statement = " ".join(code_block)

            # Remove the original lines
            for i in range(start_line - 1, end_line):
                if i == start_line - 1:
                    lines[i] = lines[i][:start_col] + var_name + lines[end_line - 1][end_col:]
                else:
                    lines[i] = ""

        lines.insert(
            insertion_line - 1,
            f"{insertion_col * ' '}{var_name} = {smell_statement}\n",
        )
        start_line = insertion_line
        end_line = start_line
        end_column = insertion_col + len(var_name) + len(smell_statement) + 3  # +3 for " = "
        start_column = end_column - len(smell_statement)

    indent = lines[insertion_line - 1][
        : len(lines[insertion_line - 1]) - len(lines[insertion_line - 1].lstrip())
    ]

    # Add import if not present
    if tracker == "codecarbon":
        package = "codecarbon"
        track_import = "EmissionsTracker"
    else:
        package = "crtracker"
        track_import = "MemoryCPUTracker"

    # Insert context manager
    start_context = f"{indent}with {track_import}({cc_args}) as tracker:\n"
    lines.insert(insertion_line - 1, start_context)

    # Indent the block
    logging.debug(f"Indenting lines {start_line}-{end_line} with {tab_size} spaces")
    logging.debug(f"Start line: {lines[start_line].strip()}")
    for i in range(start_line, end_line + 1):
        lines[i] = " " * tab_size + lines[i]

    if not any(
        line.strip().startswith((f"from {package} import {track_import}", f"import {package}"))
        for line in lines
    ):
        import_id = find_import_insertion_point(lines)

        lines.insert(import_id, f"from {package} import {track_import}\n")

    write_code_lines(file_path, lines)
    logging.info(f"Wrapped lines {start_line}-{end_line} in {file_path}")

    if is_in_expression:
        return insertion_line, start_column, end_column  # type: ignore


def process_smell(smell_data: dict, repo_name: str, tracker: str):
    """Process a single smell and annotate the code accordingly."""
    file_path = WORKTREE_DIR / repo_name / smell_data["path"]
    logging.debug(f"File path: {file_path}")
    print(f"file path: {file_path}")
    energy_meta = smell_data.get("energyMetadata", {})

    if not file_path.exists():
        logging.warning(f"File not found: {file_path}")
        return

    # Prepare the context manager lines
    file_tag = f"{smell_data['messageId']}_{smell_data['id']}"
    if tracker == "codecarbon":
        output_file = Path(
            f"emissions/{repo_name}/{smell_data['symbol']}/{smell_data['id']}.csv"
        ).resolve()

        args = f"project_name='{repo_name}-benchmark', tracking_mode='process', measure_power_secs=1, experiment_id='{repo_name}_{file_tag}', output_file='{output_file}'"
    else:
        output_file = Path(
            f"emissions/{repo_name}/{smell_data['symbol']}/{smell_data['id']}_usage.csv"
        ).resolve()

        args = f"project_id='{repo_name}-benchmark', experiment_id='{repo_name}_{file_tag}', output_file='{output_file}'"

    if energy_meta.get("isFunc", False):
        # Function/method case - use decorator
        if energy_meta.get("useOccurences", False):
            for occ in smell_data["occurences"]:
                add_decorator_to_function(
                    file_path, args, occ["line"], occ.get("column", 0), tracker
                )
        else:
            add_decorator_to_function(
                file_path, args, energy_meta["start"], energy_meta.get("col", 0), tracker
            )

        smell_data["occurences"][0]["line"] += 2
        smell_data["occurences"][0]["endLine"] += 2
    else:
        # Non-function case - use context manager
        tab_size = 4

        if energy_meta.get("useOccurences", False):
            occurences = smell_data["occurences"]
            for i in range(len(smell_data["occurences"])):
                new_location = wrap_with_context_manager(
                    file_path,
                    args,
                    occurences[i]["line"],
                    occurences[i]["endLine"],
                    False,
                    occurences[i]["column"],
                    occurences[i]["endColumn"],
                    tab_size,
                    tracker,
                )
                if new_location:
                    smell_data["occurences"][i]["line"] = new_location[0]
                    smell_data["occurences"][i]["endLine"] = new_location[0]
                    smell_data["occurences"][i]["column"] = new_location[1]
                    smell_data["occurences"][i]["endColumn"] = new_location[2]

                smell_data["occurences"][i]["line"] += 2 + i
                smell_data["occurences"][i]["endLine"] += 2 + i
                smell_data["occurences"][i]["column"] += tab_size
                smell_data["occurences"][i]["endColumn"] += tab_size
        else:
            logging.info("Wrapping code block with context manager")
            wrap_with_context_manager(
                file_path,
                args,
                energy_meta["start"],
                energy_meta["end"],
                tab_size=tab_size,
                tracker=tracker,
            )
            for i in range(len(smell_data["occurences"])):
                smell_data["occurences"][i]["line"] += 2
                smell_data["occurences"][i]["endLine"] += 2
                smell_data["occurences"][i]["column"] += tab_size
                smell_data["occurences"][i]["endColumn"] += tab_size

            smell_data["additionalInfo"]["innerLoopLine"] += 2

    return smell_data


def get_analysis_file_path(repo_name: str, tracker: str = "codecarbon"):
    """Determine the analysis file path based on inputs."""
    file_name = f"{repo_name}.json"
    annotated_path = ANNOTATED_SMELLS_DIR / tracker / file_name

    if not annotated_path.exists():
        logging.debug(f"No annotated smells found for {repo_name}, creating new analysis file.")
        return COVERED_SMELLS_DIR / file_name

    logging.debug(f'Existing annotions for "{repo_name}" found. Loading existing file.')
    return annotated_path


def main(repo_name: str, smell_id: str, tracker: str = "codecarbon"):
    """Main function to process a specific smell."""
    setup_logging(repo_name)
    logging.info(f"Starting annotation for smell {smell_id} in repo {repo_name}")

    # Resolve analysis file path
    analysis_path = get_analysis_file_path(repo_name, tracker)
    if not analysis_path.exists():
        logging.error(f"Analysis file not found: {analysis_path}")
        return

    logging.debug(f"Analysis file path: {analysis_path}")

    # Load and find specific smell
    try:
        with analysis_path.open(encoding="utf-8") as f:
            smells = json.load(f)
    except Exception as e:
        logging.error(f"Failed to load analysis JSON: {e}")
        return

    target_smell = smells[smell_id]
    if not target_smell:
        logging.error(f"Smell ID {smell_id} not found in analysis data")
        return

    # Process only the specified smell
    try:
        logging.info(f"Processing smell: {target_smell.get('message', 'unknown')}")
        updated_smell_data = process_smell(target_smell, repo_name, tracker)

        smells[smell_id] = updated_smell_data
        # Save the updated analysis file
        ann_path = ANNOTATED_SMELLS_DIR / tracker / f"{repo_name}.json"
        ann_path.parent.mkdir(parents=True, exist_ok=True)
        with ann_path.open("w", encoding="utf-8") as f:
            json.dump(smells, f, indent=4)
        logging.info(f"Updated analysis report saved to {ann_path}")
    except Exception as e:
        logging.error(f"Failed to process smell: {e}")

    logging.info("Annotation completed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Annotate code with CodeCarbon instrumentation for a specific smell."
    )
    parser.add_argument(
        "repo_name", help="Repository name to analyze (used for automatic file path resolution)"
    )
    parser.add_argument("smell_id", help="ID of the smell to annotate")
    parser.add_argument(
        "--tracker",
        type=str,
        choices=["codecarbon", "usage"],
        default="codecarbon",
        help="Which tracker to annotate with (default: codecarbon)",
    )

    args = parser.parse_args()

    main(repo_name=args.repo_name, smell_id=args.smell_id, tracker=args.tracker)
