sentence = input("Enter a sentence: ")
minimum = int(input("Enter minimum word length: "))

words = sentence.split()
result = []

for word in words:
    if len(word) >= minimum:
        result.append(word)

print("Result:", " ".join(result))