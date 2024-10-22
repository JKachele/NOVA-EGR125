# Justin Kachele
# EGR 125 Homework 3
# Problem 1

unit = input("Enter Temperature Unit (F/C): ").upper()
temp = float(input("Enter Temperature Number: "))

if unit == 'F':
    celsius = round((temp - 32) * (5 / 9), 2)
    print(temp, "F is", celsius, "C.")
elif unit == 'C':
    fahrenheit = round((temp * (5 / 9)) + 32, 2)
    print(temp, "C is", fahrenheit, "F.")
else:
    print("Invalid unit")
