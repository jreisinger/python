#!/usr/bin/python3

"""
Return free week from now till the end of the year. Input is a file with at
least some lines containing date in RE_DATE format (see below).
"""

import datetime
import re
import sys

# input date format
RE_DATE = re.compile(r'(\d{1,2}\.){2}\s*-\s*(\d{1,2}\.){2}')

if len(sys.argv) < 2:
    print("Usage:", sys.argv[0], "file")
    exit(1)

def _rm_whitespace(string):
    return "".join(string.split())

def _rm_zeros(string):
    return re.sub(r'0(\d)', r'\1', string)

def normalize_date(string):
    out = _rm_whitespace(string)
    out = _rm_zeros(out)
    return out
    
busy = []

for line in open(sys.argv[1]):
    mo = re.search(RE_DATE, line)
    if mo:
        date = normalize_date(mo.group(0))
        #print("[%s]" % date)
        start, end = date.split("-")
        fmt = "%d.%m."
        week = datetime.datetime.strptime(start, fmt).isocalendar()[1]
        #print(start, "->", week)
        busy.append(week)
        
week_now = datetime.date.today().isocalendar()[1]
for w in range(week_now, 53):
    if w not in busy:
        print(w)

