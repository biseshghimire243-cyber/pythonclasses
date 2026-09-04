words = input("Enter words separated by spaces: ").split()

groups = {}

for word in words:
    first = word[0].lower()
    groups.setdefault(first, []).append(word)

for letter in sorted(groups):
    print(letter, ":", groups[letter])