sentence = input("Enter a sentence: ")
replacement = input("Enter replacement word: ")

words = sentence.split()

for i in range(1, len(words), 2):
    words[i] = replacement

print("Modified sentence:", " ".join(words))