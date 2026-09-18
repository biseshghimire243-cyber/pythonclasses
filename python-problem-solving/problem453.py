sentence = input("Enter a sentence: ")

words = sentence.split()
result = []

for word in words:
    if len(word) == 5:
        result.append(word)

print("Five-letter words:", result)
print("Count:", len(result))