text = input("Enter a string: ")
character = input("Enter character: ")

first = text.find(character)
last = text.rfind(character)

if first == -1:
    print("Character not found")
else:
    print("First position:", first)
    print("Last position:", last)