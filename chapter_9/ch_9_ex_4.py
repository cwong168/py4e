'''
Exercise 4: Add code to the above program to figure out who has the most messages in the file.

After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Section [maximumloop]) to find who has the most messages and print how many messages the person has.

'''

def findMax(email_list):
    
    max = 0
    person = ''
    for key,value in email_list.items():
        if value > max:
            max = value
            person = key
            
    return { 'email': person, 'count': max }

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

data = findMax(word_list)

print(data['email'])
print(data['count'])
