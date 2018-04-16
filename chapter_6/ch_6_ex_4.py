'''Exercise 4: There is a string method called count that is similar to
the function in the previous exercise. Read the documentation of this
method at https://docs.python.org/3.5/library/stdtypes.html#string-methods
and write an invocation that counts the number of times the letter a
occurs in “banana”'''

''' str.count(sub[, start[, end]])
Return the number of non-overlapping occurrences of substring sub in the 
range [start, end]. Optional arguments start and end are interpreted as in slice notation.'''

'''
word = 'banana'
count = word.count('a')
print(count)
'''


count = 'banana'.count('a')
print(count)