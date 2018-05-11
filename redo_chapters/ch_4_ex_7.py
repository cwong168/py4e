'''
Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade 
that takes a score as its parameter and returns a grade as a string.

Score   Grade
> 0.9     A
> 0.8     B
> 0.7     C
> 0.6     D
<= 0.6    F
Program Execution:
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
'''




def computegrade(score):
    grade = (score)
    return grade


score = input('Please enter your score:')
try:
    computegrade(float(score))
    #float_score = float(score)
except:
    print("Please enter a score between 0.0 and 1.0")
    quit()

if float(score) > 1.0:
    print("Please enter a score between 0.0 and 1.0")
elif float(score) >= 0.9:
    print('Your grade is A')
elif float(score) >= 0.8:
    print('Your grade is B')
elif float(score) >= 0.7:
    print('Your grade is C')
elif float(score) >= 0.6:
    print('Your grade is D')
elif float(score) < 0.6:
    print('Your grade is F')