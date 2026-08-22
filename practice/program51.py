units = float(input("Enter electricity units: "))

if units <= 50:
    bill = units * 5
elif units <= 100:
    bill = 50 * 5 + (units - 50) * 7
else:
    bill = 50 * 5 + 50 * 7 + (units - 100) * 10

print("Electricity bill:", bill)