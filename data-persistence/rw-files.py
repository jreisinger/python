#!/usr/bin/env python3

text = """\
Do not meddle in the affairs of wizzards,
for you are crunchy and good with ketchup.\
"""

print("--> The text has", len(text), "chars")

filename = "/tmp/wizz.txt"

print("--> Write a text file...")
fileobj = open(filename, "wt") # "t" is default. 2nd option is "b"inary
written = fileobj.write(text)
print(written, "chars written to", filename)
fileobj.close()

print("--> Read a text file all lines at once...")
fileobj = open(filename, "r") # "r" is default. Other opts: "w", "x", "a"
slurped = fileobj.read()
print(slurped)
fileobj.close()

print("--> Read a text file line by line...")
lines = open(filename).readlines() # readlines() is optional
for line in lines:
    print(line, end="")
print()

print("--> Write a file by chunks...")
fout = open(filename, "w")
size = len(text)
offset = 0
chunk = 10 # chars
while True:
    if offset > size:
        break
    written = fout.write(text[offset:offset+chunk])
    print("Written", written, "chars")
    offset += chunk
