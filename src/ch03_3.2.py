hrs = input("Enter Hours:")
rate = input("Rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if h <= 40:
    regular_pay = h * r
else:
    regular_pay = 40 * r
    overtime_hours = h - 40
    overtime_pay = overtime_hours * r * 1.5
    gross_pay = regular_pay + overtime_pay
print(gross_pay)
