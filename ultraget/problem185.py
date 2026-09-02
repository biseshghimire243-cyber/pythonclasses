text = input("Enter lowercase letters: ")

letters = set(text)

for char in "abcdefghijklmnopqrstuvwxyz":
    if char not in letters:
        print("Missing alphabet:", char)
        break
else:
    print("All alphabets are present.")