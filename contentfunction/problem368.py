items = int(input("Enter number of items: "))

total = 0

for i in range(items):
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    total += price * quantity

print("Total price:", total)