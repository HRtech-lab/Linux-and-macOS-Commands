#!/bin/sh
set -eu
export LC_ALL=C
mkdir -p a/nested b
touch a/one.csv a/two.txt a/nested/three.csv b/one.csv b/photo.png
for directory in a b; do
    find "$directory" -type f -name '*.csv' -exec sh -c 'for f do printf "1\n"; done' sh {} + | wc -l
done
