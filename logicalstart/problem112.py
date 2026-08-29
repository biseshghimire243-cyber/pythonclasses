password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:

    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    else:
        has_special = True

score = sum([
    len(password) >= 8,
    has_upper,
    has_lower,
    has_digit,
    has_special
])

if score == 5:
    print("Very Strong Password")
elif score >= 4:
    print("Strong Password")
elif score >= 3:
    print("Medium Password")
else:
    print("Weak Password")