'''
Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers 
at the end when the user enters "done". Write the program to store the numbers the user enters in a list and 
use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.
'''

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

    print('Maximum:', largest, 'Minimum:', smallest, 'Total:', total, 'Average:', average)

main()

