#!/usr/bin/env python
import os
from sys import stdin

president_name = None
current_name = None
current_count = 0

for line in stdin:
    line = line.strip()

    president_name, count = line.split('\t', 1)
    count = int(count)

    if current_name == president_name:
        current_count += count
    else:
        if current_name:
            print ('%s\t%s' % (current_name, current_count))
        
        current_name = president_name
        current_count = count

if current_name == president_name:
    print ('%s\t%s' % (current_name, current_count))


