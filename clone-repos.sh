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

for i in $(seq 0 $((repo_count - 1))); do
  name=$(yq eval ".repos[$i].name" "$LOCKFILE")
  url=$(yq eval ".repos[$i].url" "$LOCKFILE")
  commit=$(yq eval ".repos[$i].commit" "$LOCKFILE")
  target="$DEST_DIR/$name"

  echo "Cloning $name..."
  git clone "$url" "$target"
  git -C "$target" checkout "$commit"
done

echo "All repositories cloned and checked out to locked commits."
