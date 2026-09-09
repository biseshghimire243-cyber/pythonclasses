bill = float(input("Enter bill amount: "))
tip_percent = float(input("Enter tip percentage: "))
people = int(input("Enter number of people: "))

tip = bill * tip_percent / 100
total = bill + tip
per_person = total / people

print("Tip:", round(tip, 2))
print("Total bill:", round(total, 2))
print("Each person pays:", round(per_person, 2))