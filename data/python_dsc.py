#!/usr/bin/env python3
#
# Python data structure cookbook
#

LIST_OF_TUPLES = [
    ('one',   1),
    ('two',   2),
    ('three', 3),
]

LIST_OF_DICTIONARIES = [
    {'one':   1},
    {'two':   2},
    {'three': 3},
]

def print_lot(data, tmpl):
    for name, value in data:
        print(tmpl.format( name, value ))

def print_lod(data, tmpl):
    for dict_item in data:
        for key in dict_item:
            print(tmpl.format( key, dict_item[key] ))

def main():
    tmpl = '{:<10} {}'
    print_lot(LIST_OF_TUPLES, tmpl)
    print_lod(LIST_OF_DICTIONARIES, tmpl)

if __name__ == '__main__':
    main()
