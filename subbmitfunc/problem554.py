words = input("Enter words: ").split()

result = []

for word in words:
    vowels = set()

    for char in word.lower():
        if char in "aeiou":
            vowels.add(char)

    if len(vowels) == 3:
        result.append(word)

print("Words with exactly three different vowels:", result)