'''
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
'''


fname = input('Enter the file name:')
fhand = open(fname)
count = 0
total = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        count = count +1
        # find the : in the line
        fa = line.find(':')
        # look at 1 position past the :
        fp = line[fa + 1:]
        # change the number to float
        fn = float(fp)
        # add the total of the numbers and making that total to float
        total = total + fn
        # / the total float number to the number of times it ran
        av = total / count
print('There were', count, 'X-DSPAM-Confidence: lines in', fname)
print('The average is', av)