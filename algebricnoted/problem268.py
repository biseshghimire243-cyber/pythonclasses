amount = float(input("Enter recharge amount: "))

if amount >= 2000:
    bonus = 20
elif amount >= 1000:
    bonus = 15
elif amount >= 500:
    bonus = 10
else:
    bonus = 5

bonus_amount = amount * bonus / 100
total_balance = amount + bonus_amount

print("Bonus:", bonus_amount)
print("Total balance:", total_balance)