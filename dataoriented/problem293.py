text = input("Enter a string: ")

uppercase = 0
lowercase = 0
digits = 0
symbols = 0

for char in text:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        digits += 1
    else:
        symbols += 1

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Digits:", digits)
print("Symbols:", symbols)