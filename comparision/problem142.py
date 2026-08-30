price = float(input("Enter product price: "))

discount1 = float(input("Enter first discount percentage: "))
discount2 = float(input("Enter second discount percentage: "))

final1 = price - (price * discount1 / 100)
final2 = price - (price * discount2 / 100)

print("Price with first discount:", final1)
print("Price with second discount:", final2)

if final1 < final2:
    print("First discount gives a better deal")
elif final2 < final1:
    print("Second discount gives a better deal")
else:
    print("Both discounts give the same final price")