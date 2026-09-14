units = float(input("Enter water units used: "))

if units <= 10:
    bill = units * 10
elif units <= 20:
    bill = 10 * 10 + (units - 10) * 15
else:
    bill = 10 * 10 + 10 * 15 + (units - 20) * 20

print("Water bill:", bill)