text = input("Enter text: ")

frequency = {}

for char in text:

    if char != " ":
        frequency[char] = frequency.get(char, 0) + 1

print("\nCharacter Frequency:")

for char, count in frequency.items():
    print(char, ":", count)