words = input("Enter words: ").split()

longest = ""

for word in words:
    if len(set(word.lower())) == len(word) and len(word) > len(longest):
        longest = word

if longest:
    print("Longest word with unique characters:", longest)
else:
    print("No word has unique characters.")