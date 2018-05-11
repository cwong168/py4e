'''
The function random returns a random float between 0.0 and 1.0 (including 0.0 but not 1.0).
 Each time you call random, you get the next number in a long series. To see a sample, run this loop:
'''


import random

for i in range(10):
    x = random.random()
    print(x)