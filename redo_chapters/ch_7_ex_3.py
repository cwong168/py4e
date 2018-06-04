'''
Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, 
they add a harmless Easter Egg to their program Modify the program that prompts 
the user for the file name so that it prints a funny message when the user types in 
the exact file name "na na boo boo". The program should behave normally for all other files 
which exist and don't exist. Here is a sample execution of the program:

python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt

python egg.py
Enter the file name: missing.tyxt
File cannot be opened: missing.tyxt

python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!
'''

fname = input('Enter the file name: ')
if fname =='na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()
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