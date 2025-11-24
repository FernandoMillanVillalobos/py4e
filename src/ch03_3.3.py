score = input("Enter Score: ")

try:
    score = float(score)
    if score >= 0.0 and score <= 1.0:
        if score >= 0.9:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
         print("D")
        else:
            print(score, "F")
    else:
        print("Error: score is out or range")
except:
    print("Please enter a number between 0.0 and 1.0")

