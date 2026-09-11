principal = float(input("Enter principal: "))
rate = float(input("Enter annual interest rate (%): "))
years = float(input("Enter years: "))

monthly_rate = rate / 100 / 12
months = int(years * 12)

future_value = principal * (1 + monthly_rate) ** months

print("Future value:", round(future_value, 2))