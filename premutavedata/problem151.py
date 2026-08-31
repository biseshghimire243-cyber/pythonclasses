sentence = input("Enter a sentence: ")

words = sentence.split()
unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

print("Without duplicate words:")
print(" ".join(unique_words))