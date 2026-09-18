sentence = input("Enter a sentence: ")

words = sentence.split()
frequency = {}

for word in words:
    length = len(word)
    frequency[length] = frequency.get(length, 0) + 1

most_common_length = max(frequency, key=frequency.get)

print("Most frequent word length:", most_common_length)
print("Occurrences:", frequency[most_common_length])