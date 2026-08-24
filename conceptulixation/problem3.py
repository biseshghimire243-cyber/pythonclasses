principal = float(input("Enter loan amount: "))
rate = float(input("Enter annual interest rate: "))
years = int(input("Enter loan period in years: "))

interest = principal * rate * years / 100
total = principal + interest

print("Interest:", interest)
print("Total Payment:", total)