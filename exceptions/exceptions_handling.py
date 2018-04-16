#!/usr/bin/env python3

short_list = [1, 2, 3]

while True:
    value = input('Position [q to quit]? ')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])

### The code in except: is run only when there is an error.
###
### except <exceptiontype> as <name>:
    except IndexError      as err:      # index error
        print('Bad index:', position)
    except Exception       as other:    # any other type of error
        print('Something else broke:', other)
