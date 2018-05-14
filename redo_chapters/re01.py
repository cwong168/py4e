'''
The regular expression library re must be imported into your program before you can use it. 
The simplest use of the regular expression library is the search() function. 
The following program demonstrates a trivial use of the search function.
'''

# Search for lines that contain 'From'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)
