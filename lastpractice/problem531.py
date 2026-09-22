words = input("Enter words: ").split()

result = []

for word in words:
    if len(word) > 1:
        if word[0].lower() == word[-1].lower():
            result.append(word)

print("Matching words:", result)