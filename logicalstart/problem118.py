text = input("Enter text: ")

duplicates = []

for char in text.lower():

    if char == " ":
        continue

    if text.lower().count(char) > 1 and char not in duplicates:
        duplicates.append(char)

print("Duplicate characters:", duplicates)