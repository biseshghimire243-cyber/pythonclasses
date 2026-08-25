text = input("Enter a string: ")

digits = 0
special = 0

for char in text:
    if char.isdigit():
        digits += 1
    elif not char.isalpha() and not char.isspace():
        special += 1

print("Digits:", digits)
print("Special characters:", special)