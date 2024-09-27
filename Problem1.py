# Justin Kachele
# EGR 125 Homework 2
# Problem 1

number = int(input("Enter number to check if prime: "))

for i in range(2, int(number / 2) + 1):
    if number % i == 0:
        print(number, "is not prime")
        break
else:
    print(number, "is prime")
