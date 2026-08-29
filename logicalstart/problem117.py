expenses = {
    "Food": 4500,
    "Transport": 2500,
    "Education": 6000,
    "Entertainment": 3000,
    "Shopping": 5500
}

total = sum(expenses.values())

print("===== EXPENSE REPORT =====")

for category, amount in expenses.items():
    percentage = (amount / total) * 100
    print(category, ":", amount, "-", round(percentage, 2), "%")

print("Total Expense:", total)