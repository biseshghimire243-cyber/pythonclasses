price = float(input("Enter price per item: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

if quantity >= 20:
    discount = total * 0.20
elif quantity >= 10:
    discount = total * 0.10
elif quantity >= 5:
    discount = total * 0.05
else:
    discount = 0

final_price = total - discount

print("Original total:", total)
print("Discount:", discount)
print("Final price:", final_price)