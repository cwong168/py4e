def computepay(hours, rate) :
    if float_hours > 40 :
        pay = float(hours) * float(rate)
        overtime = (float_hours - 40.0) * (float_rates * 0.5)
        pay = pay + overtime
    else:
        print("Regular")
        pay = float(hours) * float(rate)
    return pay

hours = input('Enter Hours:')
rate = input('Enter Rate:')
float_hours = float(hours)
float_rates = float(rate) 

cp_pay = computepay(float_hours,float_rates)

print('Pay:', cp_pay)
