'''
If we wanted to extract all of the revision numbers (the integer number at the end of these lines) 
using the same technique as above, we could write the following program:

'''

# Search for lines that start with 'Details: rev='
# followed by numbers and '.'
# Then print the number if it is greater than zero
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9.]+)', line)
    if len(x) > 0:
        print(x)