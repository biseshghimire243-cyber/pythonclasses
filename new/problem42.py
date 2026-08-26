sentence = input("Enter a sentence: ")

words = sentence.split()
characters = len(sentence.replace(" ", ""))

print("Number of words:", len(words))
print("Number of characters:", characters)