'''
Exercise 1:

Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.

Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

'''

def chop(t):
    last = len(t) - 1
    del t[last]
    del t[0]
    print(t)
    return None

def middle(t):
    t2 = t[:]
    last = len(t) - 1
    del t2[last]
    del t2[0]

    
    return t2

letters = ['a', 'b', 'c', 'd', 'e']
letters2 = letters[:]


t1 = chop(letters)
t2 = middle(letters2)

#print(t1)
print(t2)

