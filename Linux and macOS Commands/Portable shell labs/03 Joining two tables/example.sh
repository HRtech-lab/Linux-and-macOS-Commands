#!/bin/sh
set -eu
export LC_ALL=C
printf '%s\n' 'c 7' 'a 3' 'b 5' | sort > readings
printf '%s\n' 'b 2' 'c 4' 'a 1' | sort > scales
join readings scales | awk '{print $2 * $3}'
