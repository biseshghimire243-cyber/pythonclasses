words = input("Enter words: ").split()

count = 0

for word in words:
    vowel_count = 0

    for char in word.lower():
        if char in "aeiou":
            vowel_count += 1

    if vowel_count == 1:
        count += 1

print("Words with exactly one vowel:", count)