price1 = float(input("Enter price of Product 1: "))
price2 = float(input("Enter price of Product 2: "))

if price1 < price2:
    print("Product 1 is cheaper")
elif price2 < price1:
    print("Product 2 is cheaper")
else:
    print("Both products have the same price")