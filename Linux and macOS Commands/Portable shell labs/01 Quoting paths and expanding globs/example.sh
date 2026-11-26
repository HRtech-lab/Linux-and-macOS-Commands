#!/bin/sh
set -eu
export LC_ALL=C
mkdir files
printf %s alpha > "files/first file"
printf %s beta > "files/second file"
printf %s cc > "files/third file"
for file in files/*; do
    wc -c < "$file"
done
