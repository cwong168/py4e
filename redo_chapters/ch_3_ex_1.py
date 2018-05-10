'''
Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''

hours = input('Enter Hours worked:',)
rate = input('Enter your Hourly Rate:',)
float_hours = float(hours)
float_rate = float(rate)


if float_hours > 40:
    ot = float_hours - 40
    ot_pay = ot * float_rate * 0.5
    pay = int(hours) * float(rate)
    ot_total = ot_pay + pay
    print('Over time Pay:', ot_total)
else:
    pay = int(hours) * float(rate)
    print('Pay:',pay)
