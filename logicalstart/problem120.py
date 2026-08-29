sentence = input("Enter a sentence: ")

words = sentence.split()
word_lengths = {}

for word in words:
    word_lengths[word] = len(word)

print("===== WORD LENGTHS =====")

for word, length in word_lengths.items():
    print(word, ":", length)