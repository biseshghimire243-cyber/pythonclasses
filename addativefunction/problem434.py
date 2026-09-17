words = input("Enter words: ").split()

count = 0

for word in words:
    if len(word) > 1 and word[0].lower() != word[-1].lower():
        count += 1

print("Count:", count)