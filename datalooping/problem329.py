text = input("Enter a string: ")
character = input("Enter character: ")

first = text.find(character)

if first == -1:
    print("Character not found")
else:
    second = text.find(character, first + 1)

    if second == -1:
        print("Character occurs only once")
    else:
        print("Second occurrence:", second)