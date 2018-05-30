#!/usr/bin/python3

""" write the current date as a string to a text file
"""

from datetime import date

today       = date.today()
today_str   = today.isoformat()

fout = open("/tmp/today.txt", "w")
print(today_str, file=fout)
