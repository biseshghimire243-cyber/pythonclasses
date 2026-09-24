words = input("Enter words: ").split()

longest = ""

for word in words:
    valid = True

    for i in range(len(word) - 1):
        if word[i].lower() == word[i + 1].lower():
            valid = False
            break

    if valid and len(word) > len(longest):
        longest = word

if longest:
    print("Longest valid word:", longest)
else:
    print("No valid word found.")