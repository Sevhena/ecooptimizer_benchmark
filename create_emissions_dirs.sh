#!/bin/bash

# Base directory
base_dir="emissions"

# Repositories (folder names)
repos=(
  "numpy"
  "scipy"
  "nltk"
  "scikit-learn"
  "django"
  "streamlit"
  "gpiozero"
  "dask"
  "paho.mqtt.python"
)

# Smell types (folder names)
smell_types=(
  "long-lambda-expr"
  "long-message-chain"
  "no-self-use"
  "string-concat-loop"
  "too-many-arguments"
  "use-a-generator"
)

# Create directories
for repo in "${repos[@]}"; do
  for smell in "${smell_types[@]}"; do
    mkdir -p "$base_dir/$repo/$smell"
  done
done

echo "Subdirectories created under '$base_dir/'."
