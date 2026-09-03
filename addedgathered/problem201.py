liters = float(input("Enter water consumption in liters: "))

if liters <= 1000:
    bill = liters * 0.02
elif liters <= 3000:
    bill = 1000 * 0.02 + (liters - 1000) * 0.04
else:
    bill = 1000 * 0.02 + 2000 * 0.04 + (liters - 3000) * 0.06

print("Water bill:", round(bill, 2))