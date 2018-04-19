#!/usr/bin/env python3

from forecast import daily, weekly

print('Daily forecast:', daily.forecast())
print('Weekly forecast:')
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)
