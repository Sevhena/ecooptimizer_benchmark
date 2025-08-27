#!/bin/bash

# Usage: ./remove_common_string.sh <directory> <string_to_remove>

set -e

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <directory> <string_to_remove>"
  exit 1
fi

TARGET_DIR="$1"
STRING_TO_REMOVE="$2"

if [[ ! -d "$TARGET_DIR" ]]; then
  echo "Error: '$TARGET_DIR' is not a directory."
  exit 1
fi

cd "$TARGET_DIR"

for file in *"$STRING_TO_REMOVE"*; do
  if [[ -f "$file" ]]; then
    new_name="${file//$STRING_TO_REMOVE/}"
    mv -v -- "$file" "$new_name"
  fi
done
