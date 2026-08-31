text = input("Enter text: ")

letters = ""
digits = ""

for char in text:
    if char.isalpha():
        letters += char
    elif char.isdigit():
        digits += char

print("Letters:", letters)
print("Digits:", digits)