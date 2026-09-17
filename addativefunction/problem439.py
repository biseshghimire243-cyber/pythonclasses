sentence = input("Enter a sentence: ")
vowel = input("Enter a vowel: ").lower()

words = sentence.split()
longest = ""

for word in words:
    if vowel in word.lower() and len(word) > len(longest):
        longest = word

if longest:
    print("Longest matching word:", longest)
else:
    print("No matching word found")