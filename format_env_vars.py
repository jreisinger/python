#!/usr/bin/env python3

import os

max_key_len = 0

for k,v in os.environ.items():
    if len(k) > max_key_len:
        max_key_len = len(k)
        continue

for k,v in sorted(os.environ.items()):
    print('{:{align}{width}} => {}'.format(k,v,align='<',width=max_key_len))
