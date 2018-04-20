#!/usr/bin/env python3

def is_palindrome_dq(word):
    """
    using deque, a.k.a. double-ended queue (deque == stack + queue)
    """
    from collections import deque
    dq = deque(word)

    # work from both ends to the middle ...
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False

    return True

def is_palindrome(word):
    """
    using a slice reversal
    """
    reversed_word = word[::-1]
    return word == reversed_word

words = [
    'a',
    'racecar',
    '',
    'radar',
    'bla',
]

for word in words:
    if is_palindrome(word):
        print("'{}' is a palidrome".format(word))
