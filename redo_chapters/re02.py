'''
For example, the caret character is used in regular expressions to match "the beginning" of a line. 
We could change our program to only match lines where "From:" was at the beginning of the line as follows:
'''

# Search for lines that start with 'From'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)