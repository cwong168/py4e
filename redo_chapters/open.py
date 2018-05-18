'''
While the file handle does not contain the data for the file, 
it is quite easy to construct a for loop to read through and count each of the lines in a file:
'''

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)