#!/usr/bin/env python


def getNumbers():

    numbers = []

    while(True):
        
        val = input('Please enter a number: ')
        if val == 'done' :
            break

        numbers.append(val)

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