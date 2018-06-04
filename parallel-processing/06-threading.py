#!/usr/bin/python3

""" spawn 4 new threads and run say() in them
    Introducing Python, ch. 11
"""

import threading

def say(what):
    print("Program in thread %s says: %s" %
            (threading.current_thread(), what))

if __name__ == "__main__":
    say("I'm the main program")
    for n in range(4):
        p = threading.Thread(
                target=say,
                args=("I'm function %s" % n,)
                )
        p.start()
