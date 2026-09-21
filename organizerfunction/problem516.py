words = input("Enter words: ").split()

longest = ""

for word in words:
    vowels = []

    for char in word.lower():
        if char in "aeiou":
            vowels.append(char)

    if len(vowels) == len(set(vowels)):
        if len(word) > len(longest):
            longest = word

if longest:
    print("Longest word:", longest)
else:
    print("No valid word found.")