#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 3 ]]; then
  echo "Usage: $0 <pattern> <output_dir> <file1.zip> [file2.zip ...]" >&2
  exit 1
fi

PATTERN="$1"
shift
OUTPUT_DIR="$1"
shift  # remove output_dir from $@, so $@ is now only the zip files

if [[ ! -d "$OUTPUT_DIR" ]]; then
  mkdir -p "$OUTPUT_DIR"
fi

for ZIP_FILE in "$@"; do
  if [[ ! -f "$ZIP_FILE" ]]; then
    echo "Warning: skipping '$ZIP_FILE' — not a regular file" >&2
    continue
  fi

  echo "Processing $ZIP_FILE..."

  mapfile -t TO_EXTRACT < <(
    zipinfo -1 "$ZIP_FILE" \
      | grep -i '\.csv$' \
      | grep -i "$PATTERN"
  )

  if [[ ${#TO_EXTRACT[@]} -eq 0 ]]; then
    echo "  No matching CSVs found, skipping."
    continue
  fi

  echo "  Extracting ${#TO_EXTRACT[@]} file(s):"
  printf '    %s\n' "${TO_EXTRACT[@]}"

  unzip -jq "$ZIP_FILE" "${TO_EXTRACT[@]}" -d "$OUTPUT_DIR"
done

echo "Done."
