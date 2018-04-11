#!/usr/bin/env python3

from pprint import pprint

shells = {} # create empty dict

for line in open("/etc/passwd"):
    line = line.rstrip()
    fields = line.split(":")
    shell = fields[-1]
    if shell not in shells: # <-- thiz :-)
        shells[shell] = 1
    else:
        shells[shell] += 1

pprint(shells)
