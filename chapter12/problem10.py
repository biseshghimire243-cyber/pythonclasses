balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        raise Exception("Insufficient Balance")

    balance -= amount

    print("Remaining Balance =", balance)

except Exception as e:
    print(e)