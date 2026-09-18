balance = float(input("Enter initial balance: "))
transactions = int(input("Enter number of transactions: "))

for i in range(transactions):
    amount = float(input("Enter transaction amount: "))
    transaction_type = input("Enter type (deposit/withdraw): ").lower()

    if transaction_type == "deposit":
        balance += amount
    elif transaction_type == "withdraw":
        if amount <= balance:
            balance -= amount
        else:
            print("Insufficient balance")

print("Final balance:", balance)