'''
We can further narrow down the lines that we match using a repeated wild card character in the following example:

'''

# Search for lines that start with From and have an at sign
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line)