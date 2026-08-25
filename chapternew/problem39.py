food = float(input("Enter food amount: "))

tax = food * 13 / 100
service = food * 10 / 100

total = food + tax + service

print("Food Amount:", food)
print("Tax:", tax)
print("Service Charge:", service)
print("Total Bill:", total)