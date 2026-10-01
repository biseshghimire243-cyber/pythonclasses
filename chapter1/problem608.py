text = input("Enter a string: ")

count = 0

for character in text:
    if text.count(character) == 1:
        count += 1

print("Characters appearing once:", count)