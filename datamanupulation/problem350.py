text = input("Enter a sentence: ")
words = text.split()

vowels = "aeiou"
highest = 0
result = []

for word in words:
    count = 0

    for char in word.lower():
        if char in vowels:
            count += 1

    if count > highest:
        highest = count
        result = [word]
    elif count == highest:
        result.append(word)

print("Words with maximum vowels:", result)
print("Number of vowels:", highest)