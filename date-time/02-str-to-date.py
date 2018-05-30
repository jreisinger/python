#!/usr/bin/python3

""" parse a date
"""

from datetime import datetime

fin = open("/tmp/today.txt")
today_str = fin.read()

fmt = "%Y-%m-%d\n"
print( datetime.strptime(today_str, fmt) )
