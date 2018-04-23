'''Exercise 2: Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average.'''

'''def min(values):
    smallest = None
    for val in values:
        if smallest is None or val < smallest:
            smallest = val
    return smallest

def max(values):
    largest = None
    for val in values:
        if largest is None or val > largest:
            largest = val
    return largest'''

average = 0
count = 0
total = 0
smallest = None
largest = None

while True:
    
    val = input('Please enter a number: ')
    if val == 'done' :
        break
    try:
        
        if smallest is None or int(val) < smallest :
            print("smallest:", smallest)
            smallest = int(val) 
        elif largest is None or int(val) > largest :
            largest = int(val)
            print("largest:", largest)                
    except:
        print('Invalid input')
        continue
    count = count + 1

    total = total + int(val)

    average = total / count

  
print(total ,count, smallest, largest, average)