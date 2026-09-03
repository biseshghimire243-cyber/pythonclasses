password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True

if has_upper and has_lower and has_digit and len(password) >= 8:
    print("Password meets the requirements.")
else:
    print("Password does not meet the requirements.")