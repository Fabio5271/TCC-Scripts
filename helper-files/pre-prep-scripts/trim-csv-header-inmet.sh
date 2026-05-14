#!/usr/bin/env bash
set -euo pipefail

if [[ $# -eq 0 ]]; then
  echo "Usage: $0 <file1.csv> [file2.csv ...]" >&2
  exit 1
fi

for CSV_FILE in "$@"; do
  if [[ ! -f "$CSV_FILE" ]]; then
    echo "Warning: skipping '$CSV_FILE' — not a regular file" >&2
    continue
  fi

  echo "Processing $CSV_FILE..."
  tail -n +9 "$CSV_FILE" > "$CSV_FILE.tmp" && mv "$CSV_FILE.tmp" "$CSV_FILE"
done

echo "Done."
