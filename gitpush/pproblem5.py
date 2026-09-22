words = input("Enter words: ").split()

longest = ""

for word in words:
    if len(word) < 2:
        valid = True
    else:
        valid = True

        for i in range(len(word) - 1):
            current_vowel = word[i].lower() in "aeiou"
            next_vowel = word[i + 1].lower() in "aeiou"

            if current_vowel == next_vowel:
                valid = False
                break

    if valid and len(word) > len(longest):
        longest = word

if longest:
    print("Longest alternating word:", longest)
else:
    print("No valid word found.")