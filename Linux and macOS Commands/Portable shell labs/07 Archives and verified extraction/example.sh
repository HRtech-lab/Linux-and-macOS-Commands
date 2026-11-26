#!/bin/sh
set -eu
export LC_ALL=C
mkdir input restored
printf %s one > input/first
printf %s second > input/next
(cd input && tar -cf ../example.tar first next)
(cd restored && tar -xf ../example.tar)
for name in first next; do
    cmp "input/$name" "restored/$name"
    wc -c < "restored/$name"
done
