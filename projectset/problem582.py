words = input("Enter words: ").split()

count = 0

for word in words:
    if any(character.isdigit() for character in word):
        count += 1

print("Words containing digits:", count)