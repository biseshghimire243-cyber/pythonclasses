character = input("Enter one character: ")

if len(character) != 1:
    print("Please enter exactly one character")
elif character.isalpha():
    print("It is an alphabet")
elif character.isdigit():
    print("It is a digit")
else:
    print("It is a special character")