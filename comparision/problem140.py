product1 = float(input("Enter Product 1 price: "))
product2 = float(input("Enter Product 2 price: "))
product3 = float(input("Enter Product 3 price: "))

cheapest = min(product1, product2, product3)
expensive = max(product1, product2, product3)

print("Cheapest price:", cheapest)
print("Most expensive price:", expensive)

if product1 == product2 == product3:
    print("All products have the same price")