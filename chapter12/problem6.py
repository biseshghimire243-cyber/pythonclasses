age = int(input("Enter your age: "))

if age < 18:
    raise Exception("You must be at least 18 years old.")

print("Welcome!")