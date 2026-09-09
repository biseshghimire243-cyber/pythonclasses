income = float(input("Enter monthly income: "))
expenses = list(map(float, input("Enter expenses separated by spaces: ").split()))

total_expenses = sum(expenses)
savings = income - total_expenses

print("Total expenses:", total_expenses)
print("Monthly savings:", savings)

if savings > 0:
    print("You are saving money")
elif savings == 0:
    print("Income and expenses are equal")
else:
    print("You are spending more than your income")