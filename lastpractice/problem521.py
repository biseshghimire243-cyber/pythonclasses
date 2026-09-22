words = input("Enter words: ").split()

best_word = ""
highest_count = -1

for word in words:
    consonants = 0

    for char in word.lower():
        if char.isalpha() and char not in "aeiou":
            consonants += 1

    if consonants > highest_count:
        highest_count = consonants
        best_word = word

print("Word with highest consonant count:", best_word)
print("Consonants:", highest_count)