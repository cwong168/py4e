'''
For example, if we wanted to read a file and only print out lines which started with the prefix "From:", 
we could use the string method startswith to select only those lines with the desired prefix:
'''


fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)