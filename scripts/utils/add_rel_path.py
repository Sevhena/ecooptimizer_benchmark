from pathlib import Path
import argparse
import json


def load_smells(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    with path.open() as f:
        smells = json.load(f)
    return smells


def dump_smells(path: Path, smells: dict[str, dict]):
    with path.open("w") as f:
        json.dump(smells, f, indent=2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="File or directory")
    args = parser.parse_args()

    path = Path(args.path)
    paths_to_modify = []
    if path.is_file():
        paths_to_modify = [path]

    else:
        for file in path.iterdir():
            paths_to_modify.append(file)

    for file in paths_to_modify:
        repo = file.stem

        smells = load_smells(file)

        benchmark_root = Path(f"repositories/{repo}").resolve()
        for smell in smells.values():
            smell["absolutePath"] = smell["path"]
            smell["path"] = str(Path(smell["absolutePath"]).relative_to(benchmark_root))

        dump_smells(file, smells)


if __name__ == "__main__":
    main()
