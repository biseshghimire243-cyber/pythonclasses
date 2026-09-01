balance = 50000

amount = float(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid amount")
elif amount > balance:
    print("Insufficient balance")
elif amount % 100 != 0:
    print("Amount must be a multiple of 100")
else:
    balance -= amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)