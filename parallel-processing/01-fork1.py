#!/usr/bin/python3

"forks child processes until you type 'q' (Programming Python 4th, p. 179)"

import os

def child(newpid):
    print('Hello from child ', os.getpid(), newpid)
    os._exit(0) # else goes back to parent loop -> it's a copy of the orig. proc

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child(newpid)
        else:
            print('Hello from parent', os.getpid(), newpid)
        if input() == 'q': break

parent()
