words = input("Enter words: ").split()

longest = ""

for word in words:
    vowels = 0
    consonants = 0

    for char in word.lower():
        if char.isalpha():
            if char in "aeiou":
                vowels += 1
            else:
                consonants += 1

    if vowels > consonants and len(word) > len(longest):
        longest = word

if longest:
    print("Longest word:", longest)
else:
    print("No matching word found.")