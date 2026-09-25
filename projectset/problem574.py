words = input("Enter words: ").split()

longest = ""

for word in words:
    consonants = 0

    for char in word.lower():
        if char.isalpha() and char not in "aeiou":
            consonants += 1

    if consonants == 3 and len(word) > len(longest):
        longest = word

if longest:
    print("Longest word with exactly three consonants:", longest)
else:
    print("No matching word found.")