words = input("Enter words: ").split()

vowels = "aeiouAEIOU"
longest = ""

for word in words:
    if word[0] in vowels and len(word) > len(longest):
        longest = word

if longest:
    print("Longest word:", longest)
else:
    print("No word starts with a vowel")