text1 = input("Enter first word: ")
text2 = input("Enter second word: ")

word1 = sorted(text1.lower().replace(" ", ""))
word2 = sorted(text2.lower().replace(" ", ""))

if word1 == word2:
    print("The words are anagrams")
else:
    print("The words are not anagrams")