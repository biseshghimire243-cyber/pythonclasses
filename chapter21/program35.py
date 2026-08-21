principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))
time = float(input("Enter time in years: "))

amount = principal * (1 + rate / 100) ** time
interest = amount - principal

print("Compound Interest:", round(interest, 2))
print("Total Amount:", round(amount, 2))