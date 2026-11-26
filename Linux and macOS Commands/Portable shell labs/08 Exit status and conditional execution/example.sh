#!/bin/sh
set -eu
export LC_ALL=C
printf '%s\n' 'tea' 'coffee' > drinks
for pattern in tea water; do
    if grep -q "$pattern" drinks; then printf '0\n'; else printf '%s\n' "$?"; fi
done
if grep -q tea absent 2>/dev/null; then printf '0\n'; else printf '%s\n' "$?"; fi
