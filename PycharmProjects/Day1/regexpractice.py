import re
import os

f = open("C:\postcodes.txt", 'rt')

valid = 0
invalid = 0
# print(f.read())

for postcode in f:
    if postcode.isspace():continue

    postcode = re.sub('[ \t\n]','',postcode)
    postcode = postcode.upper()

    print(f.read())