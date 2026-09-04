sentence = input("Enter a sentence: ").lower()

words = sentence.split()
frequency = {}

for word in words:
    word = word.strip(".,!?")
    frequency[word] = frequency.get(word, 0) + 1

for word, count in sorted(frequency.items()):
    print(f"{word}: {'*' * count}")