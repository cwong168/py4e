'''
Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come 
from each email address, and print the dictionary.
'''

file = input('Enter file name: ')
fo = open(file)
word_list = dict()

for line in fo:
    arr = line.split()
    for item in arr:
        if '@' in item:
            email = item.replace(";","").replace("<","").replace(">","")
            #print(email) 
            if email in word_list:
                word_list[email] = word_list[email] + 1
            else:
                word_list[email] = 1

print(word_list)