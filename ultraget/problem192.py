text = input("Enter a string: ")

frequency = {}

for char in text:
    if char != " ":
        frequency[char] = frequency.get(char, 0) + 1

sorted_chars = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

if len(sorted_chars) >= 2:
    print("Most frequent:", sorted_chars[0][0])
    print("Second most frequent:", sorted_chars[1][0])
else:
    print("Not enough different characters.")