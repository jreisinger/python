#!/usr/bin/python3

import unicodedata

common_characters = (
    'DOLLAR SIGN',
    'EURO SIGN',
    'SNOWMAN',
)

for char in common_characters:
    name = char
    value = unicodedata.lookup(name)
    category = unicodedata.category(value)
    print('name="%s", value="%s", category="%s"' % (name, value, category))
