#!/usr/bin/env python3

try:
    score = float(input("Enter score: "))
    if score > 1.0 or score < 0:
        raise ValueError
    if score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    else:
        print('F')
except ValueError:
    print("Bad score")