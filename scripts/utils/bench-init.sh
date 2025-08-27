#!/bin/bash

# Check if yq is installed, install if not
check_yq_installed() {
    if ! command -v yq &> /dev/null; then
        echo "yq not found, installing..."
        sudo apt-get update
        sudo apt-get install -y snapd
        sudo snap install yq
        if ! command -v yq &> /dev/null; then
            echo "Failed to install yq. Please install manually: https://github.com/mikefarah/yq#install"
            exit 1
        fi
    fi
}

# Parse command line arguments
FORCE_RECLONE=false
while getopts "f" opt; do
    case $opt in
        f) FORCE_RECLONE=true ;;
        *) echo "Usage: $0 [-f]" >&2
           exit 1 ;;
    esac
done

# Check yq is installed
check_yq_installed

# Verify lock file exists
LOCK_FILE="repos.lock.yaml"
if [ ! -f "$LOCK_FILE" ]; then
    echo "Error: Lock file $LOCK_FILE not found"
    exit 1
fi

# Create repositories directory if needed
REPO_DIR="repositories"
mkdir -p "$REPO_DIR"
cd "$REPO_DIR" || exit

# Initialize variables
FAILED_REPOS=()

# Get the count of repos
REPO_COUNT=$(yq e '.repos | length' ../"$LOCK_FILE")

echo "Starting to clone $REPO_COUNT repositories into $REPO_DIR/..."
echo "------------------------------------------"

# Process each repository
for (( i=0; i<$REPO_COUNT; i++ )); do
    NAME=$(yq e ".repos[$i].name" ../"$LOCK_FILE")
    URL=$(yq e ".repos[$i].url" ../"$LOCK_FILE")
    COMMIT=$(yq e ".repos[$i].commit" ../"$LOCK_FILE")
    
    echo "Processing $NAME..."
    
    # Check if directory exists
    if [ -d "$NAME" ] && [ "$FORCE_RECLONE" = false ]; then
        echo "  Directory $NAME already exists. Skipping..."
        continue
    fi
    
    # Remove directory if force reclone is enabled
    if [ -d "$NAME" ] && [ "$FORCE_RECLONE" = true ]; then
        echo "  Removing existing directory $NAME..."
        rm -rf "$NAME"
    fi
    
    # Clone the repository
    if git clone "$URL" "$NAME" 2>/dev/null; then
        echo "  Cloned successfully."
        
        # Checkout the specific commit
        cd "$NAME" || continue
        if git checkout "$COMMIT" 2>/dev/null; then
            echo "  Checked out commit $COMMIT."
        else
            echo "  ERROR: Failed to checkout commit $COMMIT for $NAME."
            FAILED_REPOS+=("$NAME (checkout failed)")
            cd ..
            continue
        fi
        cd ..
    else
        echo "  ERROR: Failed to clone $NAME."
        FAILED_REPOS+=("$NAME (clone failed)")
        continue
    fi
    
    echo "------------------------------------------"
done

# Print summary
echo ""
echo "Cloning process completed."
if [ ${#FAILED_REPOS[@]} -ne 0 ]; then
    echo "The following repositories failed to clone/checkout:"
    for repo in "${FAILED_REPOS[@]}"; do
        echo "  - $repo"
    done
    exit 1
else
    echo "All repositories were successfully cloned and checked out."
    exit 0
fi