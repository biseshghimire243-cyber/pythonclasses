principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate: "))
time = float(input("Enter time in years: "))

amount = principal * (1 + rate / 100) ** time
interest = amount - principal

print("Final Amount:", round(amount, 2))
print("Compound Interest:", round(interest, 2))