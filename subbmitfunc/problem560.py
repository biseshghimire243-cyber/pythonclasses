text = input("Enter a string: ")

found = None

for char in text:
    if text.count(char) == 2:
        found = char
        break

if found:
    print("First character appearing exactly twice:", found)
else:
    print("No character appears exactly twice.")