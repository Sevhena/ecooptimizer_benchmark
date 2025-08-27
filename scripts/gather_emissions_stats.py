from typing import Optional
import pandas as pd
from pathlib import Path
from statistics import mean, stdev
from collections import defaultdict
import argparse

EMISSIONS_METRIC = ["emissions"]  # Only emissions from carbon files
USAGE_METRICS = ["cpu_percent", "memory_mb"]  # From usage files


def process_file_pair(orig_file, refactored_file, metrics, file_type):
    try:
        df_orig = pd.read_csv(orig_file)
        df_ref = pd.read_csv(refactored_file)

        results = {}
        for metric in metrics:
            if metric in df_orig.columns and metric in df_ref.columns:
                orig_mean = df_orig[metric].dropna().mean()
                ref_mean = df_ref[metric].dropna().mean()
                delta = orig_mean - ref_mean  # positive = savings
                results[metric] = delta

        # Convert memory_mb to memory_gb for consistency
        if file_type == "usage" and "memory_mb" in results:
            results["memory_gb"] = results["memory_mb"] / 1024
            del results["memory_mb"]

        return results
    except Exception as e:
        print(f"⚠️ Error reading {file_type} pair {orig_file.name}: {e}")
        return {}


def fmt(val):
    if isinstance(val, float):
        if abs(val) < 0.001:
            return f"{val:.3e}"
        return f"{val:.3f}"
    return val


def gather_stats(base_dir: Path, output_file: Path, repo: Optional[str] = None):
    savings_by_smell = defaultdict(lambda: defaultdict(list))
    if repo:
        repo_paths = [base_dir / repo]
    else:
        repo_paths = [p for p in base_dir.iterdir() if p.is_dir() and not p.name.startswith("_")]

    for repo_path in repo_paths:
        if not repo_path.is_dir():
            continue

        for smell_path in repo_path.iterdir():
            if not smell_path.is_dir():
                continue

            smell_type = smell_path.name

            # Process carbon emissions files (only emissions metric)
            for orig_file in smell_path.glob("*.csv"):
                if "_refactored" in orig_file.name or "_usage" in orig_file.name:
                    continue

                refactored_file = orig_file.with_name(orig_file.stem + "_refactored.csv")
                if not refactored_file.exists():
                    continue

                results = process_file_pair(
                    orig_file, refactored_file, EMISSIONS_METRIC, "emissions"
                )
                for metric, delta in results.items():
                    savings_by_smell[smell_type][metric].append(delta)

            # Process usage files (cpu_percent and memory_mb)
            for orig_usage_file in smell_path.glob("*_usage.csv"):
                if "_refactored" in orig_usage_file.name:
                    continue

                refactored_usage_file = orig_usage_file.with_name(
                    orig_usage_file.stem + "_refactored.csv"
                )
                if not refactored_usage_file.exists():
                    continue

                results = process_file_pair(
                    orig_usage_file, refactored_usage_file, USAGE_METRICS, "usage"
                )
                for metric, delta in results.items():
                    savings_by_smell[smell_type][metric].append(delta)

    # Prepare final output
    final_metrics = ["emissions", "cpu_percent", "memory_gb"]
    rows = []
    for smell_type, metrics in savings_by_smell.items():
        row = {"Smell Type": smell_type}
        for metric in final_metrics:
            values = metrics.get(metric, [])
            if values:
                row[f"{metric} savings (mean)"] = fmt(mean(values))
                row[f"{metric} savings (stdev)"] = fmt(stdev(values) if len(values) > 1 else 0.0)
            else:
                row[f"{metric} savings (mean)"] = "N/A"
                row[f"{metric} savings (stdev)"] = "N/A"
        rows.append(row)

    df_out = pd.DataFrame(rows).sort_values(by="Smell Type")
    with (base_dir / output_file).open("w") as f:
        print(f"Writing to {output_file.resolve()}")
        f.write("\n=== Carbon and Resource Savings by Smell Type ===\n")
        f.write(df_out.to_markdown(index=False))


def main():
    parser = argparse.ArgumentParser(description="Gather emissions and resource savings stats.")
    parser.add_argument("--input-dir", type=str, default="emissions", help="Base input directory")
    parser.add_argument(
        "--output-file", type=str, default="raw_data.md", help="File to ouput stats."
    )
    parser.add_argument(
        "--repo", type=str, help="Only gather data for this repo (subdir of input-dir)"
    )
    args = parser.parse_args()

    base_dir = Path(args.input_dir)
    gather_stats(base_dir, Path(args.output_file), repo=args.repo)


if __name__ == "__main__":
    main()
