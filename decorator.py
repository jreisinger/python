#!/usr/bin/env python3

# Decorator allows you to modify an existing function without changing its
# source code. It takes one function as input and returns another function.
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

@document_it
def add_ints(a, b):
    return a + b

print(add_ints(1, 2))
