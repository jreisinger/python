#!/usr/bin/python3

""" spawn 4 new processes and run say() in them
    Introducing Python, ch. 10
"""

import multiprocessing
import os
import time

def say(what):
    print("Program in process %s (sweet child of %s) says: %s" % 
            (os.getpid(), os.getppid(), what))

if __name__ == "__main__":
    say("I'm the main program")
    for n in range(4):
        p = multiprocessing.Process(
                target=say, 
                args=("I'm function %s" % n,)
                )
        p.start()
