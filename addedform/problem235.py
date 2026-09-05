text = input("Enter a string: ")

if text:
    character = max(text)

    print("Character:", character)
    print("ASCII value:", ord(character))
else:
    print("String is empty.")