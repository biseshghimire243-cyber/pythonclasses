words = input("Enter words: ").split()

vowels = "aeiouAEIOU"
count = 0

for word in words:
    if word[-1].isalpha() and word[-1] not in vowels:
        count += 1

print("Count:", count)