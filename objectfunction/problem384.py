items = {}

count = int(input("Enter number of items: "))

for i in range(count):
    category = input("Enter category: ").lower()
    items[category] = items.get(category, 0) + 1

print("Items by category:")

for category, total in items.items():
    print(category, ":", total)