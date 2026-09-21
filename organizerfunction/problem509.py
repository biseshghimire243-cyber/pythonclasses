words = input("Enter words: ").split()

count = 0

for word in words:
    vowels = 0
    consonants = 0

    for char in word.lower():
        if char.isalpha():
            if char in "aeiou":
                vowels += 1
            else:
                consonants += 1

    if consonants > vowels:
        count += 1

print("Words with more consonants:", count)