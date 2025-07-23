#!/bin/bash

set -e  # Exit on error

LOCKFILE="repos.lock.yaml"
DEST_DIR="repositories"

# Ensure yq is installed
if ! command -v yq &> /dev/null; then
  echo "'yq' not found. Installing via snap..."
  sudo snap install yq
fi

echo "yq is installed"

# Ensure target directory exists
mkdir -p "$DEST_DIR"

# Loop through each repo entry in the lockfile and clone
repo_count=$(yq eval '.repos | length' "$LOCKFILE")

# Track failures
failed_repos=()

for i in $(seq 0 $((repo_count - 1))); do
  name=$(yq eval ".repos[$i].name" "$LOCKFILE")
  url=$(yq eval ".repos[$i].url" "$LOCKFILE")
  commit=$(yq eval ".repos[$i].commit" "$LOCKFILE")
  target="$DEST_DIR/$name"

  echo "Processing $name..."

  if [ -d "$target/.git" ]; then
    echo "Repo already exists at $target."

    current_commit=$(git -C "$target" rev-parse HEAD)

    if [ "$current_commit" = "$commit" ]; then
      echo "Repo is already at the correct commit: $commit"
    else
      echo "Repo at wrong commit ($current_commit), fetching and checking out $commit..."
      git -C "$target" fetch --all --quiet
      if ! git -C "$target" checkout "$commit"; then
        echo "Failed to checkout commit $commit in $name"
        failed_repos+=("$name")
      fi
    fi

  else
    echo "Cloning $name..."
    git clone "$url" "$target"
    git -C "$target" checkout "$commit"
  fi
done


echo "All repositories cloned and checked out to locked commits."

sudo apt-get update

sudo apt-get install cmake

# Print summary of any failures
if [ ${#failed_repos[@]} -ne 0 ]; then
  echo ""
  echo "The following repositories failed to clone or checkout:"
  for repo in "${failed_repos[@]}"; do
    echo "  - $repo"
  done
else
  echo ""
  echo "All repositories cloned and checked out successfully!"
fi