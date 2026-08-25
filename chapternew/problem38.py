hours = int(input("Enter parking hours: "))

if hours <= 1:
    fee = 50
elif hours <= 3:
    fee = 100
elif hours <= 6:
    fee = 200
else:
    fee = 300

print("Parking Fee:", fee)