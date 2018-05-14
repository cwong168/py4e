'''
We can use this regular expression in a program to read all the lines in a file and print out anything that looks like an email address as follows:
'''

# Search for lines that have an at sign between characters
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(x)