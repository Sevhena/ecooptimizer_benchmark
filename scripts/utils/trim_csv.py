#!/usr/bin/env python3
import argparse
import csv
from pathlib import Path
import sys
import fnmatch
import random


def trim_csv_file(csv_file: Path, keep_last_n: int, verbose: bool = False, dry_run: bool = False):
    """Trim a single CSV file to keep last N rows plus header."""
    try:
        # Read all lines
        with csv_file.open("r", newline="") as f:
            reader = csv.reader(f)
            lines = list(reader)

        if len(lines) <= 1:  # Only header or empty file
            if verbose:
                print(f"Skipping {csv_file} - empty or header only")
            return False

        if len(lines) > keep_last_n + 1:  # +1 for header
            if dry_run:
                print(
                    f"[DRY RUN] Would trim {csv_file} from {len(lines) - 1} to {keep_last_n} rows"
                )
                return True

            if verbose:
                print(f"Trimming {csv_file} from {len(lines) - 1} to {keep_last_n} rows")

            rand_start = random.randint(1, max(1, len(lines) - keep_last_n - 1))

            # Keep header + last N rows
            trimmed_lines = [lines[0], *lines[rand_start : rand_start + keep_last_n]]

            # Write back to file
            with csv_file.open("w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(trimmed_lines)
            return True
        elif verbose:
            print(f"No trimming needed for {csv_file} (already has ≤ {keep_last_n} rows)")
        return False
    except Exception as e:
        print(f"Error processing {csv_file}: {e!s}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Trim CSV files to keep last N rows plus headers (no pandas)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--directory", default="emissions", help="Directory containing CSV files to process"
    )
    parser.add_argument(
        "-n",
        "--keep-last",
        type=int,
        default=100,
        help="Number of data rows to keep (excluding header)",
    )
    parser.add_argument("-p", "--pattern", default="*.csv", help="File pattern to match")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show verbose output")
    parser.add_argument(
        "--dry-run", action="store_true", help="Show what would be done without modifying files"
    )

    args = parser.parse_args()

    dir_path = Path(args.directory).resolve()
    if not dir_path.exists():
        print(f"Error: Directory not found: {dir_path}", file=sys.stderr)
        sys.exit(1)

    processed_files = 0
    trimmed_files = 0

    for csv_file in dir_path.rglob("*"):
        if not csv_file.is_file():
            continue

        if fnmatch.fnmatch(str(csv_file), "**/copy/*"):
            continue

        processed_files += 1
        was_trimmed = trim_csv_file(csv_file, args.keep_last, args.verbose, args.dry_run)
        if was_trimmed:
            trimmed_files += 1

    print("\nProcessing complete:")
    print(f"- Scanned directory: {dir_path}")
    print(f"- File pattern: '{args.pattern}'")
    print(f"- Processed files: {processed_files}")
    print(f"- Trimmed files: {trimmed_files}")
    print(f"- Rows kept per file: {args.keep_last}")

    if args.dry_run:
        print("\nNOTE: Dry run mode - no files were modified")


if __name__ == "__main__":
    main()
