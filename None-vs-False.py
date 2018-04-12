#!/usr/bin/env python3

def is_none(thing):
    if thing is None:
        print("it's None  (is)")
    elif thing:
        print("it's True  (boolean)")
    else:
        print("it's False (boolean)")

values = [
    None,
    True,
    False,
    0,
    0.0,
    (),
    [],
    {},
    set(),
]

for value in values:
    print("Checking %5s ... " % (value,), end="")
    is_none(value)
