distance = float(input("Enter distance in km: "))

if distance <= 2:
    fare = 50
else:
    fare = 50 + (distance - 2) * 25

print("Taxi fare:", round(fare, 2))