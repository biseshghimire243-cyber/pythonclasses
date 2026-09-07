text = input("Enter a string: ")

longest = ""
current = ""

for char in text:
    if char in current:
        current = current[current.index(char) + 1:]

    current += char

    if len(current) > len(longest):
        longest = current

print("Longest substring:", longest)
print("Length:", len(longest))