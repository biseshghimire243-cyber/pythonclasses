text = input("Enter a word: ")
character = input("Enter character to check: ")

if text.lower().endswith(character.lower()):
    print("The word ends with that character.")
else:
    print("The word does not end with that character.")