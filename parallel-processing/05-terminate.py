#!/usr/bin/python3

"""
spawn a new long running process and then terminate it
Introducing Python, ch. 10
"""

import multiprocessing, time, os

def whoami(name):
    print("I'm %s, in process %s" % ( name, os.getpid() ))

def loopy(name):
    whoami(name)
    start = 1
    stop  = 1000
    for num in range(start, stop):
        print("--> Loop number %s of %s." % (num, stop))
        time.sleep(1)

if __name__ == "__main__":
    whoami("main")
    p = multiprocessing.Process(target=loopy, args=("loopy",))
    p.start()
    time.sleep(5)
    p.terminate()
