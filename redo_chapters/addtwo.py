'''
To return a result from a function, we use the return statement in our function. 
For example, we could make a very simple function called addtwo that adds two numbers together and returns a result.
'''

def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)