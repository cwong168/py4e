'''Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, 
printing each letter on a separate line, except backwards.'''


fruit = 'banana'
# print(fruit[-1])
index = -1
#length = len(fruit)
#index = length -1
while index < len(fruit) and index != -7:
    letter = fruit[index]
    print(letter)
    
    index = index -1