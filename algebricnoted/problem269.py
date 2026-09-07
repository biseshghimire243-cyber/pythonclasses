products = []

n = int(input("Enter number of products: "))

for i in range(n):
    name = input("Enter product name: ")
    cost = float(input("Enter cost price: "))
    selling = float(input("Enter selling price: "))

    profit = selling - cost
    products.append((name, profit))

if products:
    best = max(products, key=lambda x: x[1])

    print("Most profitable product:", best[0])
    print("Profit:", best[1])