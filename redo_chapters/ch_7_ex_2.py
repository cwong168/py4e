'''
Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:

X-DSPAM-Confidence:0.8475

When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line to extract the floating-point number on the line. 
Count these lines and then compute the total of the spam confidence values from these lines. 
When you reach the end of the file, print out the average spam confidence.

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745

Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519
Test your file on the mbox.txt and mbox-short.txt files.
'''

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
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


'''
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        #print(line)
        data = line.find(':')
        #print(data)
        eline = line.find(' ',data)
        print(eline)
        num = line[data +1:eline]
        print(num)
        #new_num = float(num)
        #print(new_num)
print('There were', count, 'subject lines in', fname)
'''
