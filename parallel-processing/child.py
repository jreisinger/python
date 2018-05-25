#!/usr/bin/python3

"used by 03-fork-exec.py"

import sys, os

print("I'm running in process %s with arg %s" % (os.getpid(), sys.argv[1]))
