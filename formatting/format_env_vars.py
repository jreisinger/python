#!/usr/bin/env python3

import os

max_key_len = 0

for k in os.environ.keys():
    length = len(k)
    if length > max_key_len:
        max_key_len = length

for k,v in sorted(os.environ.items()):
    print('{:{align}{width}} --> {}'.format(k,v,align='<',width=max_key_len))
