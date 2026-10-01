words = input("Enter words: ").split()

vowels = "aeiouAEIOU"
count = 0

for word in words:
    vowel_count = sum(1 for char in word if char in vowels)

    if vowel_count == 2:
        count += 1

print("Count:", count)