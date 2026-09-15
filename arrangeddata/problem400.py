sentence = input("Enter a sentence: ")
words = sentence.split()

best_word = ""

for word in words:
    if len(word) == len(set(word)) and len(word) > len(best_word):
        best_word = word

if best_word:
    print("Longest word:", best_word)
else:
    print("No suitable word found")