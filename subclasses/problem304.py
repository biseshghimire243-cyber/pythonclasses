text = input("Enter a sentence: ").lower()
words = text.split()

unique_words = set(words)
most_common = None
highest = 0

for word in unique_words:
    count = words.count(word)

    if count > highest:
        highest = count
        most_common = word

print("Most common word:", most_common)
print("Frequency:", highest)