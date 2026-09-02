units = float(input("Enter electricity units: "))

if units <= 50:
    bill = units * 5
elif units <= 150:
    bill = 50 * 5 + (units - 50) * 7
elif units <= 250:
    bill = 50 * 5 + 100 * 7 + (units - 150) * 10
else:
    bill = 50 * 5 + 100 * 7 + 100 * 10 + (units - 250) * 12

print("Electricity bill:", bill)