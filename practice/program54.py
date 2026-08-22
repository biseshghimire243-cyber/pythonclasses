items = []

for i in range(3):
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    items.append((name, price))

total = 0

print("\nShopping Bill")

for name, price in items:
    print(name, ":", price)
    total += price

print("Total:", total)