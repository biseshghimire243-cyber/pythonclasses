units = float(input("Enter electricity units: "))

if units <= 20:
    bill = units * 5
elif units <= 50:
    bill = 20 * 5 + (units - 20) * 7
else:
    bill = 20 * 5 + 30 * 7 + (units - 50) * 10

print("Electricity Bill:", bill)