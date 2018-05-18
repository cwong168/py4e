'''
We could use line slicing to print all but the last character, 
but a simpler approach is to use the rstrip method which strips whitespace from the right side of a string as follows:
'''

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)