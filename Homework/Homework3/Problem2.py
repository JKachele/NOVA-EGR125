# Justin Kachele
# EGR 125 Homework 3
# Problem 2

balance = 0

while(True):
    print("Welcome to the bank!")
    print("1) View Balance")
    print("2) Withdraw Funds")
    print("3) Deposit Funds")
    print("4) Exit")
    sel = int(input("Enter number of selection: "))
    print()

    if sel == 1:
        print("Yout balance is $", balance, sep='')
    elif sel == 2:
        withdraw = float(input("Enter amount to withdraw: "))
        if withdraw > balance:
            print("Warning: Insufficent Funds. Withdraw Declined")
        else:
            balance = round(balance - withdraw, 2)
            print("Withdraw Successful. New balance is $", balance, sep='')
    elif sel == 3:
        deposit = float(input("Enter amount to deposit: "))
        balance = round(balance + deposit, 2)
        print("Deposit Successful. New balance is $", balance, sep='')
    elif sel == 4:
        break;
    else:
        print("Invalid Selection. Try Again")

    print()

print("Have a great day!")
