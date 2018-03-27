#!/usr/bin/env python3

# Dictionary where values are sets.
# (Set - dictionary without values)
drinks = {
        'martini': {'vodka', 'vermouth'},
        'black russian': {'vodka', 'kahlua'},
        'white russian': {'cream', 'hahlua', 'vodka'},
        'manhattan': {'rye', 'vermouth', 'bitters'},
        'screwdriver': {'orange juice', 'vodka'},
        }

for name, contents in drinks.items():
    # Drinks with vodka but neither cream nor vermouth.
    #if 'vodka' in contents and not ('cream' in contents or 'vermouth' in contents):
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print( "{}: {}".format( name, ", ".join(contents) ) )
