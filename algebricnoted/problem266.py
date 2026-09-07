principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate: "))
years = int(input("Enter number of years: "))

amount = principal

for year in range(1, years + 1):
    amount += amount * rate / 100
    print("Year", year, ":", round(amount, 2))

interest = amount - principal

print("Total interest:", round(interest, 2))
print("Final amount:", round(amount, 2))