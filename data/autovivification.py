#!/usr/bin/env python3

from pprint import pprint

shells_count = {} # create empty dict

for line in open("/etc/passwd"):
    shell = line.rstrip().split(":")[-1]
    if shell not in shells_count: # <-- thiz :-)
        shells_count[shell] = 0
    shells_count[shell] += 1

pprint(shells_count)
