'''
Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input 
gracefully by printing a message and exiting the program. The following shows two executions of the program:

Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input

Enter Hours: forty
Error, please enter numeric input
'''

 


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
    pay = int(hours) * float(rate)
    ot_total = ot_pay + pay
    print('Over time Pay:', ot_total)
else:
    pay = int(hours) * float(rate)
print('Pay:',pay)
#except:
#    print('Please enter numeric input:',)