text = input("Enter a sentence: ")

spaces = 0

for char in text:
    if char == " ":
        spaces += 1

print("Number of spaces:", spaces)