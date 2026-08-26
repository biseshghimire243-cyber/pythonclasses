text = input("Enter a sentence: ")
character = input("Enter character to count: ")

count = text.lower().count(character.lower())

print("Character:", character)
print("Occurrences:", count)