age = int(input("Enter your age: "))

if age < 5:
    group = "Toddler"
elif age < 13:
    group = "Child"
elif age < 20:
    group = "Teenager"
elif age < 60:
    group = "Adult"
else:
    group = "Senior Citizen"

print("Age Group:", group)