#!/usr/bin/env python

'''Exercise 2: Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average.'''

def getNumbers():

    numbers = []

    while(True):
        
        val = input('Please enter a number: ')
        if val == 'done' :
            break
        try:
            numbers.append(val)
        except:
            print('Invalid input')
            continue
'''
I think the issue is I have not declear the try and except in the main section
Maybe use the raise valueerror Jimmy showed but how does the array know if the
val is a int or str?
'''

    return numbers

def findLargest(inputs):
    largest = max(inputs)
    return largest

def findSmallest(inputs):
    smallest = min(inputs)
    return smallest

def findTotal(numbers):
    total = 0
    for item in numbers:
        total = total + int(item)

    return total
        
def findAverage(numbers):
    average = 0
    total = 0
    for item in numbers:
        total = total + int(item)

    average = total / len(numbers)

    return average


def main():
    # get numbers
    numbers = getNumbers()

    # find largest in array
    largest = findLargest(numbers)

    # find smallest in array
    smallest = findSmallest(numbers)

    # find total
    total = findTotal(numbers)

    # find average
    average = findAverage(numbers)

    print(largest, smallest, total, average)

main()