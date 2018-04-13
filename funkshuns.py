#!/usr/bin/env python3

# Default argument values are calculated when the function is *defined*, not
# when it is run! Talking about result=[] ...
# ---
# Asterisk (*) does not mean a pointer (Python has no pointers). It groups a
# variable number of positional arguments into a tuple of paramter values.
# Talking about *args ... :-)
def accumulate(*args, result=[], keep_state=True):
    if not keep_state:
        result = [] # clear the list
    for a in args:
        result.append(a)
    print(result)

# keep state of result between function calls
accumulate('a')
accumulate('a')
accumulate('a')

# clear state of result
accumulate('a', keep_state=False)
accumulate('b', 'b', keep_state=False)
