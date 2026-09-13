sentence = input("Enter a sentence: ")
words = sentence.split()

result = {}

for word in words:
    first = word[0].lower()
    result[first] = result.get(first, 0) + 1

print(result)