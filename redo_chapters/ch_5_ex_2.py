'''
Exercise 2: Write another program that prompts for a list of numbers as above 
and at the end prints out both the maximum and minimum of the numbers instead of the average.
'''

count = 0
total = 0
largest = None
smallest = None

while True:
    val = input('Please enter a number: ')
    if val == 'done' :
        break
    
    try:
        float_val = float(val)
    except:
        print('Invalid input')
        continue
    if largest is None or val > largest:
        largest = val
    if smallest is None or val < smallest:
        smallest = val
    count = count + 1
    total = total + float_val
    

print(total,count,total/count)
print(largest, smallest)