'''
So now that we see the flaw in the program, we can elegantly fix it using the try/except structure. 
We need to assume that the open call might fail and add recovery code when the open fails as follows:
'''

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
