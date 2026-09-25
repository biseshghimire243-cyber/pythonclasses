words = input("Enter words: ").split()

frequency = {}

for word in words:
    length = len(word)
    frequency[length] = frequency.get(length, 0) + 1

if frequency:
    highest = max(frequency.values())

    lengths = []

    for length in frequency:
        if frequency[length] == highest:
            lengths.append(length)

    print("Most frequent word length(s):", lengths)
    print("Frequency:", highest)
else:
    print("No words entered.")