birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter current year: "))

age = current_year - birth_year

if age >= 0:
    print("Your age is:", age)
else:
    print("Invalid birth year.")