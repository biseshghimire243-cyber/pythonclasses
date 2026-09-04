text = input("Enter a string: ").lower()

missing = []

for char in "abcdefghijklmnopqrstuvwxyz":
    if char not in text:
        missing.append(char)

print("Missing characters:", missing)