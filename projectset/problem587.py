words = input("Enter words: ").split()

vowels = "aeiouAEIOU"
count = 0

for word in words:
    vowel_count = 0
    consonant_count = 0

    for character in word:
        if character.isalpha():
            if character in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    if vowel_count > consonant_count:
        count += 1

print("Count:", count)