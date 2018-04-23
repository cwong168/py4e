fname = input('Enter the file name:')
fhand = open(fname)
for line in fhand:
    strip = line.rstrip()
    print(strip.upper())
