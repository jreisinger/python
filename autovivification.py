#!/usr/bin/env python3

from pprint import pprint

shells = {}

for line in open("/etc/passwd"):
    line = line.rstrip()
    fields = line.split(":")
    shell = fields[-1]
    if shell not in shells:
        shells[shell] = 1
    else:
        shells[shell] += 1

pprint(shells)
