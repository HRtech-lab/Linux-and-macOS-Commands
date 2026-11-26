#!/bin/sh
set -eu
export LC_ALL=C
printf '%s\n' plum apple pear apple plum apple > fruit.txt
sort fruit.txt | uniq -c | awk '{print $1}'
