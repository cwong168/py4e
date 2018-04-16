hours = input('Enter Hours:')
rate = input('Enter Rate:')
try:
    float_hours = float(hours)
    float_rates = float(rate)
except:
    print("Error, please enter numeric input") 
    quit()
    
if float_hours > 40 :
    print("Overtime")
    pay = float(hours) * float(rate)
    overtime = (float_hours - 40.0) * (float_rates * 1.5)
    pay = pay + overtime
else:
    print("Regular")
    pay = float(hours) * float(rate)
print('Pay:', pay)
