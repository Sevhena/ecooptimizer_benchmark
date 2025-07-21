import os
import json
import concurrent.futures
from pathlib import Path
import time
import logging
from typing import Optional
from collections import defaultdict
import re

# Configuration
TARGETED_SMELLS: set[str] = {
    "cached-repeated-calls",
    "long-element-chain",
    "long-lambda-expr",
    "long-lambda-expression",
    "long-message-chain",
    "no-self-use",
    "string-concat-loop",
    "too-many-arguments",
    "use-a-generator",
}

# Smells that need full function/loop context
FUNCTION_CONTEXT_SMELLS = {"no-self-use", "too-many-arguments"}
LOOP_CONTEXT_SMELLS = {"string-concat-loop"}

ROOT_DIR = Path().resolve()

OUTPUT_DIR: Path = ROOT_DIR / "artifacts" / "extracted_snippets"
SEPARATOR: str = "# " + "=" * 50 + "\n"
MAX_WORKERS: int = os.cpu_count() or 4

# Configure logging (file-only)
LOG_DIR: Path = ROOT_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(LOG_DIR / "snippet_extractor.log")],
)
logger = logging.getLogger(__name__)


class SnippetExpander:
    """Utility class for expanding snippets to include full context"""

    @staticmethod
    def find_function_boundaries(lines: list[str], line_num: int) -> tuple[int, int]:
        """
        Find the start and end lines of a function containing the given line number.
        Returns (start_line, end_line) or (-1, -1) if not found.
        """
        # Look backwards for function def
        start_line = line_num

        # Look forward for function end (track indentation)
        base_indent = len(lines[start_line]) - len(lines[start_line].lstrip())
        end_line = start_line
        for i in range(start_line + 1, len(lines)):
            current_line = lines[i]
            if not current_line.strip():  # Skip empty lines
                continue

            current_indent = len(current_line) - len(current_line.lstrip())
            if current_indent <= base_indent and not current_line[base_indent:].startswith(
                (" ", "\t")
            ):
                end_line = i - 1
                break
        else:
            end_line = len(lines) - 1

        return (start_line + 1, end_line + 1)  # Convert to 1-based

    @staticmethod
    def find_loop_boundaries(lines: list[str], line_num: int) -> tuple[int, int]:
        """
        Find the start and end lines of the outermost loop containing the given line.
        Returns (start_line, end_line) or (-1, -1) if not found.
        """
        # Look backwards for loop start
        start_line = -1
        for i in range(line_num - 1, -1, -1):
            if re.match(r"^\s*(for|while)\s", lines[i]):
                start_line = i
                break

        if start_line == -1:
            return (-1, -1)

        # Look forward for loop end (track indentation)
        base_indent = len(lines[start_line]) - len(lines[start_line].lstrip())
        end_line = start_line
        for i in range(start_line + 1, len(lines)):
            current_line = lines[i]
            if not current_line.strip():  # Skip empty lines
                continue

            current_indent = len(current_line) - len(current_line.lstrip())
            if current_indent <= base_indent and not current_line[base_indent:].startswith(
                (" ", "\t")
            ):
                end_line = i - 1
                break
        else:
            end_line = len(lines) - 1

        return (start_line + 1, end_line + 1)  # Convert to 1-based


class SnippetExtractor:
    def __init__(self):
        self.error_log: list[str] = []
        self.processed_files: int = 0
        self.start_time: float = time.time()
        self.expander = SnippetExpander()
        logger.info("SnippetExtractor initialized")

    def normalize_indentation(self, snippet: str) -> str:
        """Remove common indentation from snippet while preserving relative indentation"""
        lines = snippet.splitlines()
        if not lines:
            return ""

        min_indent = min(len(line) - len(line.lstrip()) for line in lines if line.strip())

        return "\n".join(line[min_indent:] if line.strip() else line for line in lines)

    def get_expanded_snippet(
        self, str_path: str, line: int, end_line: int, smell_type: str
    ) -> Optional[str]:
        """Get snippet with expanded context when needed"""

        path_components = list(Path(str_path).parts)
        # Ensure compatibility with old directory structure
        try:
            main_proj_dir_id = path_components.index("ecooptimizer")
            path_components[main_proj_dir_id] = "ecooptimizer_benchmark"
            path_components.insert(main_proj_dir_id + 1, "repositories")
        except ValueError:
            pass

        file_path = Path(*path_components)
        try:
            with file_path.open("r", encoding="utf-8") as f:
                lines = f.readlines()

            if smell_type in FUNCTION_CONTEXT_SMELLS:
                start, end = self.expander.find_function_boundaries(
                    lines, line - 1
                )  # Convert to 0-based
                if start != -1:
                    return "".join(lines[start - 1 : end])  # Convert back to 1-based
            elif smell_type in LOOP_CONTEXT_SMELLS:
                start, end = self.expander.find_loop_boundaries(
                    lines, line - 1
                )  # Convert to 0-based
                if start != -1:
                    return "".join(lines[start - 1 : end])  # Convert back to 1-based

            # Default case - use original snippet
            line = max(1, min(line, len(lines)))
            end_line = max(line, min(end_line, len(lines)))
            return "".join(lines[line - 1 : end_line])

        except Exception as e:
            error_msg = f"Error reading {file_path}: {e!s}"
            logger.error(error_msg, exc_info=True)
            self.error_log.append(error_msg)
            return None

    def process_json_file(self, json_path: Path):
        """Process JSON file with expanded snippet context"""
        try:
            logger.info(f"Processing: {json_path}")

            with json_path.open("r", encoding="utf-8") as f:
                data = json.load(f)

            repo_name = json_path.stem
            repo_output_dir = OUTPUT_DIR / repo_name
            repo_output_dir.mkdir(exist_ok=True, parents=True)

            # Structure: {smell_type: {file_path: [occurrences]}}
            smell_file_map: defaultdict[str, defaultdict[str, list[dict[str, int]]]] = defaultdict(
                lambda: defaultdict(list)
            )

            # Group occurrences by smell type and file
            for entry in data:
                smell_type = entry.get("symbol")
                if smell_type not in TARGETED_SMELLS:
                    continue

                file_path = entry.get("path")
                if not file_path:
                    logger.warning(f"Missing path in {json_path}")
                    continue

                for occ in entry.get("occurences", []):
                    if occ.get("line"):
                        smell_file_map[smell_type][file_path].append(occ)

            # Process each smell type
            for smell_type, file_occurrences in smell_file_map.items():
                output_file = repo_output_dir / f"{smell_type}.py"

                with output_file.open("w", encoding="utf-8") as fh:
                    fh.write(f"# {smell_type} snippets for {repo_name}\n\n")

                    for file_path, occurrences in file_occurrences.items():
                        # Group consecutive occurrences
                        grouped_occurrences = self.group_occurrences(occurrences)

                        fh.write(f"# File: {file_path}\n")

                        for group in grouped_occurrences:
                            if len(group) > 1:
                                line_range = f"Lines {group[0]['line']}-{group[-1]['endLine']}"
                                fh.write(
                                    f"# Occurrences: {line_range} ({len(group)} instances)\n\n"
                                )
                            else:
                                fh.write(f"# Line: {group[0]['line']}\n\n")

                            # Get expanded snippet for the first occurrence in group
                            first_occ = group[0]
                            snippet = self.get_expanded_snippet(
                                file_path,
                                first_occ["line"],
                                first_occ.get("endLine", first_occ["line"]),
                                smell_type,
                            )

                            if snippet:
                                fh.write(self.normalize_indentation(snippet))
                                fh.write("\n\n")

                            fh.write(SEPARATOR)

            self.processed_files += 1
            if self.processed_files % 5 == 0:
                self.print_progress()

        except Exception as e:
            error_msg = f"Error processing {json_path}: {e!s}"
            logger.error(error_msg, exc_info=True)
            self.error_log.append(error_msg)

    def group_occurrences(self, occurrences: list[dict[str, int]]) -> list[list[dict[str, int]]]:
        """Group consecutive or nearby occurrences"""
        if not occurrences:
            return []

        sorted_occ = sorted(occurrences, key=lambda x: x["line"])
        groups = [[sorted_occ[0]]]

        for occ in sorted_occ[1:]:
            last = groups[-1][-1]
            if occ["line"] - last.get("endLine", last["line"]) <= 5:
                groups[-1].append(occ)
            else:
                groups.append([occ])

        return groups

    def print_progress(self):
        """Console progress reporting only"""
        elapsed = time.time() - self.start_time
        print(
            f"\rProcessed {self.processed_files} files | "
            f"Errors: {len(self.error_log)} | "
            f"Elapsed: {elapsed:.1f}s",
            end="",
        )

    def save_error_log(self):
        """Save error log without console output"""
        if self.error_log:
            error_file = OUTPUT_DIR / "extraction_errors.log"
            with error_file.open("w", encoding="utf-8") as f:
                f.write("\n".join(self.error_log))
            logger.info(f"Saved {len(self.error_log)} errors to {error_file}")


def main():
    """Main function with clean console output"""
    print("Starting snippet extraction with expanded context...")
    print(f"Will expand context for: {FUNCTION_CONTEXT_SMELLS | LOOP_CONTEXT_SMELLS}")

    OUTPUT_DIR.mkdir(exist_ok=True)
    extractor = SnippetExtractor()

    analysis_dir = Path("analysis_data/smells/raw")
    json_files = [f for f in analysis_dir.iterdir()]

    print(f"Found {len(json_files)} JSON files to process")
    print(f"Using {MAX_WORKERS} parallel workers...")

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(extractor.process_json_file, jf) for jf in json_files]
        concurrent.futures.wait(futures)

    extractor.print_progress()
    extractor.save_error_log()

    print("\n\nExtraction complete!")
    print(f"Results saved to: {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    main()
