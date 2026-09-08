text = input("Enter a sentence: ")

words = text.split()
result = []

for word in words:
    if word:
        result.append(word[0].upper() + word[1:].lower())

print("Title case:", " ".join(result))