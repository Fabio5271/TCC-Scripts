#!/bin/bash
# Usage: ./clean_inmet_zip.sh <file.zip>

log() { [[ "$QUIET" == false ]] && echo "$@" || true; }

confirm() {
    read -r -p "Proceed with deletion? [y/N] " resp
    case "$resp" in
        [yY][eE][sS]|[yY]) return 0 ;;
        *) return 1 ;;
    esac
}

set -euo pipefail

QUIET=false
VERBOSE=false
ASK_CONFIRM=true

while getopts "qvy" opt; do
    case "$opt" in
        q) QUIET=true ;;
        v) VERBOSE=true ;;
        y) ASK_CONFIRM=false ;;
        ?) echo "Usage: $0 [-v|-y] <file.zip>" >&2; exit 1 ;;
    esac
done
shift $((OPTIND -1))

if [[ $# -ne 1 ]]; then
    echo "Usage: $0 [-v|-y] <file.zip>" >&2
    exit 1
fi

ZIP_FILE="$(realpath "$1")"

if [[ ! -f "$ZIP_FILE" ]]; then
    echo "Error: file not found: $ZIP_FILE" >&2
    exit 1
fi

mapfile -t TO_DELETE < <(
    zipinfo -1 "$ZIP_FILE" \
        | grep -i '\.csv$' \
        | grep -iv 'INMET_CO_'
)

if [[ ${#TO_DELETE[@]} -eq 0 ]]; then
    echo "Nothing to remove in $ZIP_FILE."
    exit 0
fi

log "Removing ${#TO_DELETE[@]} file(s) from $ZIP_FILE:"
[[ "$QUIET" == false ]] && printf '  %s\n' "${TO_DELETE[@]}"

if [[ "$ASK_CONFIRM" == true ]]; then
    if ! confirm; then
        echo "Aborted."
        exit 0
    fi
fi

zip_flags=("--delete")
[[ "$VERBOSE" == false ]] && zip_flags+=("-q")

zip "${zip_flags[@]}" "$ZIP_FILE" "${TO_DELETE[@]}"

echo "Done!"
