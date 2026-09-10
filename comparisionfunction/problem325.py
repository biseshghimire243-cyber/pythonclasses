price = float(input("Enter original price: "))
taxes = list(map(float, input("Enter tax percentages: ").split()))

final_price = price

for tax in taxes:
    final_price += final_price * tax / 100

print("Final price:", round(final_price, 2))