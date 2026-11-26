#!/bin/sh
set -eu
export LC_ALL=C
for mode in 600 640 644; do
    file="example-$mode"
    : > "$file"
    chmod "$mode" "$file"
    case $(uname -s) in
        Darwin) stat -f '%Lp' "$file" ;;
        Linux) stat -c '%a' "$file" ;;
        *) printf '%s\n' "Unsupported stat variant" >&2; exit 2 ;;
    esac
done
