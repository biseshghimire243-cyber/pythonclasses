words = input("Enter words: ").split()

count = int(input("Enter minimum vowel count: "))

result = []

for word in words:
    vowels = 0

    for char in word.lower():
        if char in "aeiou":
            vowels += 1

    if vowels >= count:
        result.append(word)

print("Matching words:", result)