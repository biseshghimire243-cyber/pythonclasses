sentence = input("Enter a sentence: ")

words = sentence.split()
reversed_words = words[::-1]

print("Reversed sentence:")
print(" ".join(reversed_words))