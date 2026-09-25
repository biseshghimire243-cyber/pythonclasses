words = input("Enter words: ").split()

result = []

for word in words:
    first = word[0].lower()

    if word.lower().count(first) == 1:
        result.append(word)

print("Words whose first letter appears once:", result)