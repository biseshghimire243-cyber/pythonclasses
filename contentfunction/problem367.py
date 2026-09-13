text = input("Enter a string: ")

highest = text[0]

for char in text:
    if ord(char) > ord(highest):
        highest = char

print("Character:", highest)
print("ASCII value:", ord(highest))