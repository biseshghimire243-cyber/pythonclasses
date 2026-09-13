sentence1 = input("Enter first sentence: ")
sentence2 = input("Enter second sentence: ")

words1 = len(sentence1.split())
words2 = len(sentence2.split())

print("First sentence words:", words1)
print("Second sentence words:", words2)

if words1 > words2:
    print("First sentence has more words")
elif words2 > words1:
    print("Second sentence has more words")
else:
    print("Both have the same number of words")