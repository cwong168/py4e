'''
Exercise 6: Rewrite your pay computation with time-and-a-half for overtime 
and create a function called computepay which takes two parameters (hours and rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''

def computepay(hours, rate):
    compute = hours * rate
    return compute

try:
    hours = input('Enter Hours worked:')
    float_hours = float(hours)
    rate = input('Enter your Hourly Rate:')
    float_rate = float(rate)
except:
    print('Please enter numeric input:')
    quit()

if float_hours > 40:
    ot = float_hours - 40
    ot_pay = ot * float_rate * 0.5
    pay = computepay(int(hours), float(rate))
    #pay = int(hours) * float(rate)
    ot_total = ot_pay + pay
    print('Over time Pay:', ot_total)
else:
    pay = computepay(int(hours), float(rate))
    #pay = int(hours) * float(rate)
    print('Pay:',pay)
#except:
#    print('Please enter numeric input:',)