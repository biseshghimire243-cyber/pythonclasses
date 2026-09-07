text = input("Enter a string: ")

frequency = {}

for char in text:
    if char != " ":
        frequency[char] = frequency.get(char, 0) + 1

count = 0

for char in text:
    if char != " " and frequency[char] == 1:
        count += 1

        if count == 2:
            print("Second non-repeating character:", char)
            break
else:
    print("Second non-repeating character not found.")