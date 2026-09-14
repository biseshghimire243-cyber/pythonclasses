join_year = int(input("Enter joining year: "))
current_year = int(input("Enter current year: "))

experience = current_year - join_year

print("Experience:", experience, "years")

if experience >= 5:
    print("Experienced employee")
else:
    print("Less than 5 years experience")