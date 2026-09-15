principal = float(input("Enter loan amount: "))
rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter loan period in years: "))

monthly_rate = rate / 12 / 100
months = years * 12

if monthly_rate == 0:
    payment = principal / months
else:
    payment = (
        principal * monthly_rate * (1 + monthly_rate) ** months
        / ((1 + monthly_rate) ** months - 1)
    )

print("Monthly payment:", round(payment, 2))