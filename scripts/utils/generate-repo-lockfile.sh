#!/bin/bash

set -e  # Exit on any error

REPO_DIR="repositories"
LOCKFILE="repos.lock.yaml"

# Ensure yq is installed
if ! command -v yq &> /dev/null; then
  echo "'yq' not found. Installing via snap..."
  sudo snap install yq
fi

echo "yq is installed"

# Verify repo directory exists
if [ ! -d "$REPO_DIR" ]; then
  echo "Repository directory '$REPO_DIR' does not exist."
  exit 1
fi

# Start fresh
echo "repos:" > "$LOCKFILE"

# Loop through each Git repo and log its URL and commit
for repo in "$REPO_DIR"/*; do
  if [ -d "$repo/.git" ]; then
    name=$(basename "$repo")
    url=$(git -C "$repo" config --get remote.origin.url)
    commit=$(git -C "$repo" rev-parse HEAD)
    
    echo "  - name: $name" >> "$LOCKFILE"
    echo "    url: $url" >> "$LOCKFILE"
    echo "    commit: $commit" >> "$LOCKFILE"

    echo "Locked $name to $commit"
  fi
done

echo "Lockfile created at $LOCKFILE"
