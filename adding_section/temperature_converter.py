balance = 5000

print("===== BANK ACCOUNT =====")
print("Initial Balance:", balance)

deposit = float(input("Enter deposit amount: "))
balance += deposit

withdraw = float(input("Enter withdrawal amount: "))

if withdraw <= balance:
    balance -= withdraw
    print("Withdrawal successful")
else:
    print("Insufficient balance")

print("Final Balance:", balance)