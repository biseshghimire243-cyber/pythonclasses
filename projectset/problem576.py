words = input("Enter words: ").split()

result = []

for word in words:
    first = word[0].lower()
    last = word[-1].lower()

    if first in "aeiou" and last in "aeiou" and first != last:
        result.append(word)

print("Words starting and ending with different vowels:", result)