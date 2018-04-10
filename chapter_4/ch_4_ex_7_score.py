def computergrade(hokey) :
    try:
        float_score = float(score)
    except:
        print("Error, Bad Score") 
        quit()
    if float(score) > float(1.0) :
        print("Error, Bad Score")
    elif float(score) >= float(0.9) :
        print("A")
    elif float(score) >= float(0.8) :
        print("B")
    elif float(score) >= float(0.7) :
        print("C")
    elif float(score) >= float(0.6) :
        print("D")
    elif float(score) < float(0.6) :
        print("F")

score = input ('Enter Score:')
computergrade(score)