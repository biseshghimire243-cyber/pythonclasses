text = input("Enter a sentence: ")

vowels = 0
consonants = 0

for char in text.lower():
    if char in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)