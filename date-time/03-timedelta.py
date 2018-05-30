#!/usr/bin/python3

""" When will you be (or when were you) 10,000 days old?
"""

from datetime import date, timedelta

my_bday   = date(1989, 11, 17)
party_day = my_bday + timedelta(days=10000)

print(party_day)
