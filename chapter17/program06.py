text = input("Enter a word: ")

character = input("Enter character to count: ")

count = text.lower().count(character.lower())

print("Character frequency:", count)