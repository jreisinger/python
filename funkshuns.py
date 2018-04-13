#!/usr/bin/env python3

# Default argument values are calculated when the function is *defined*, not
# when it is run! Talking about result=[] ... :-)
def accumulate(arg, result=[], keep_state=True):
    if not keep_state:
        result = [] # clear the list
    result.append(arg)
    print(result)

# keep state of result between function calls
accumulate('a')
accumulate('a')
accumulate('a')

# clear state of result
accumulate('a', keep_state=False)
