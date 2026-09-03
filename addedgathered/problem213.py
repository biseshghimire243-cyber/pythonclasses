products = {}

n = int(input("Enter number of products: "))

for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    products[name] = price

expensive = max(products, key=products.get)

print("Most expensive product:", expensive)
print("Price:", products[expensive])