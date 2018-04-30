'''
Exercise 1:

Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.

Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

'''

def middle(t):
    del t[0]
    del t[3]


letters = ['a', 'b', 'c', 'd', 'e']
t1 = middle(letters)
#t1 = chop
print(letters)
print(t1)

