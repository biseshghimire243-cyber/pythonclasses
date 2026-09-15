text = input("Enter a string: ")

counts = {}

for char in text:
    counts[char] = counts.get(char, 0) + 1

found = False

for char in text:
    if counts[char] >= 3:
        print("First character appearing at least 3 times:", char)
        found = True
        break

if not found:
    print("No character appears 3 times")