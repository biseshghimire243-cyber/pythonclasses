price = float(input("Enter product price: "))
tax_rate = float(input("Enter tax percentage: "))

tax = price * tax_rate / 100
final_price = price + tax

print("Product Price:", price)
print("Tax Amount:", tax)
print("Final Price:", final_price)