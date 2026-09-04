words = input("Enter words separated by spaces: ").split()

groups = {}

for word in words:
    key = "".join(sorted(word.lower()))
    groups.setdefault(key, []).append(word)

for group in groups.values():
    if len(group) > 1:
        print("Anagram group:", group)