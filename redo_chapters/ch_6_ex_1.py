'''
Exercise 1: Write a while loop that starts at the last character in the string and 
works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.


for char in fruit:
    print(char)

'''

fruit = 'banana'

index = -1
while index < len(fruit):
    letter = fruit[index]
    index = index -1
    print(letter)




