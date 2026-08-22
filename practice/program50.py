sentence1 = input("Enter first sentence: ")
sentence2 = input("Enter second sentence: ")

words1 = set(sentence1.lower().split())
words2 = set(sentence2.lower().split())

common = words1.intersection(words2)

print("Common words:", common)