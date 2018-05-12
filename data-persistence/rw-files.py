#!/usr/bin/env python3

text = """\
Do not meddle in the affairs of wizzards,
for you are crunchy and good with ketchup.\
"""

print("The text has", len(text), "bytes")

filename = "/tmp/wizz.txt"

# Write a text file...
fileobj = open(filename, "wt") # "t" is default. 2nd option is "b"inary
bytes_written = fileobj.write(text)
print(bytes_written, "bytes written to", filename)
fileobj.close()

# Read a text file all lines at once...
fileobj = open(filename, "r") # "r" is default. Other opts: "w", "x", "a"
slurped = fileobj.read()
print(slurped)
fileobj.close()

# Read a text file line by line...
lines = open(filename).readlines() # readlines() is optional
for line in lines:
    print(line)
