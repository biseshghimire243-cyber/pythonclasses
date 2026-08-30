balance1 = float(input("Enter first account balance: "))
balance2 = float(input("Enter second account balance: "))

if balance1 > balance2:
    print("Account 1 has more money")
elif balance2 > balance1:
    print("Account 2 has more money")
else:
    print("Both accounts have equal balance")