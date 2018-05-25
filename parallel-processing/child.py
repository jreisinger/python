#!/usr/bin/python3

import sys, os

print("I'm running in process %s with arg %s" % (os.getpid(), sys.argv[1]))
