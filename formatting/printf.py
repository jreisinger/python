#!/usr/bin/env python3

def printf(format, *args):
    print(format % args)

printf("number %d is written as %s", 42, "forty-two")
