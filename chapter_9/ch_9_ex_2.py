'''
Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. 
To do this look for lines that start with "From", then look for the third word and keep a running count of each of the days of the week. 
At the end of the program print out the contents of your dictionary (order does not matter).

'''

file = input('Enter file name: ')
fo = open(file)
word_list = dict()

for line in fo:
    arr = line.split()
    
    if len(arr) > 0:
        if arr[0] == 'From':
            day = arr[2]
        
            if day in word_list:
                word_list[day] = word_list[day] + 1
            else:
                word_list[day] = 1

print(word_list)

