vehicle1 = input("Enter first vehicle: ")
price1 = float(input("Enter price of first vehicle: "))

vehicle2 = input("Enter second vehicle: ")
price2 = float(input("Enter price of second vehicle: "))

if price1 < price2:
    print(vehicle1, "is cheaper")
elif price2 < price1:
    print(vehicle2, "is cheaper")
else:
    print("Both vehicles have the same price")