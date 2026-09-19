sentence = input("Enter a sentence: ")
words = sentence.split()

shortest = min(words, key=len)

print("Shortest word:", shortest)
print("Length:", len(shortest))