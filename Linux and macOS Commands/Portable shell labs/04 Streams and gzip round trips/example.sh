#!/bin/sh
set -eu
export LC_ALL=C
awk 'BEGIN {for (i=0;i<50;i++) print "sample,18"}' > readings
gzip -c < readings > readings.gz
gzip -dc < readings.gz > restored
cmp readings restored
wc -c < readings
wc -c < restored
