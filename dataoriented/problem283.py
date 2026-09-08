units = float(input("Enter electricity units: "))

if units <= 50:
    bill = units * 5
elif units <= 150:
    bill = 50 * 5 + (units - 50) * 7
else:
    bill = 50 * 5 + 100 * 7 + (units - 150) * 10

fixed_charge = 100
total = bill + fixed_charge

print("Total electricity bill:", total)