#!/usr/bin/env python3

# An exception is a class. It is a child of the class Exception.
class UppercaseException(Exception):
    pass

words = ['eeenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        raise UppercaseException(word)
