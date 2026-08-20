text = input("Enter a word: ")
character = input("Enter character to check: ")

if text.lower().startswith(character.lower()):
    print("The word starts with that character.")
else:
    print("The word does not start with that character.")