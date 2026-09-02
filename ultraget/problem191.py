amount = float(input("Enter shopping amount: "))

if amount >= 10000:
    discount_rate = 20
elif amount >= 5000:
    discount_rate = 15
elif amount >= 2000:
    discount_rate = 10
else:
    discount_rate = 5

discount = amount * discount_rate / 100
final_amount = amount - discount

print("Discount:", discount)
print("Final amount:", final_amount)