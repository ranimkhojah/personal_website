#!/bin/bash
# Script to import publications from BibTeX to Hugo content

set -e  # Exit on error

# Get script directory and project root
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Paths
BIB_FILE="$PROJECT_ROOT/publications.bib"
PUB_DIR="$PROJECT_ROOT/content/publication"
INDEX_FILE="$PUB_DIR/_index.md"

# Check if BibTeX file exists
if [ ! -f "$BIB_FILE" ]; then
    echo "Error: publications.bib not found at $BIB_FILE"
    exit 1
fi

# Preserve _index.md if it exists
if [ -f "$INDEX_FILE" ]; then
    cp "$INDEX_FILE" "$PROJECT_ROOT/_index.md.backup"
fi

# Clear publication directory (remove all subdirectories, keep _index.md)
echo "Clearing old publication folders..."
find "$PUB_DIR" -mindepth 1 -maxdepth 1 -type d -exec rm -rf {} +

# Run Python import script
echo "Importing publications from $BIB_FILE..."
python3 "$SCRIPT_DIR/import_publications.py"

# Restore _index.md if it was backed up
if [ -f "$PROJECT_ROOT/_index.md.backup" ]; then
    mv "$PROJECT_ROOT/_index.md.backup" "$INDEX_FILE"
fi

echo "Publications imported successfully!"
echo "Generated $(find "$PUB_DIR" -mindepth 1 -maxdepth 1 -type d | wc -l) publication(s)"
