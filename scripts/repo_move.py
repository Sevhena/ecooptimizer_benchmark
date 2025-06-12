from pathlib import Path
import shutil

NOT_VALID_REPOS = {
    "extracted_snippets",
    "analysis_results",
    "repositories",
}


def move_repo(repo: Path, source_dir: Path):
    """Move a repository from source to destination."""
    dest_dir = source_dir / "repositories"
    dest_dir.mkdir(exist_ok=True)

    destination = dest_dir / repo.name
    try:
        shutil.move(repo, destination)
        print(f"Moved {repo} to repositories/")
    except Exception as e:
        print(f"Error moving repository: {e!s}")


def main():
    """Main function to move repositories."""
    source_dir = Path().absolute()
    print(f"Source directory: {source_dir}")
    if not source_dir.exists():
        print(f"Source directory {source_dir} does not exist.")
        return

    for repo in source_dir.iterdir():
        if repo.is_dir() and repo.name not in NOT_VALID_REPOS:
            move_repo(repo, source_dir)


if __name__ == "__main__":
    main()
