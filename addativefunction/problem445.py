words = input("Enter words: ").split()

vowels = set("aeiou")
result = []

for word in words:
    if vowels.issubset(set(word.lower())):
        result.append(word)

print("Words containing all vowels:", result)