word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

common = []

for char in word1:
    if char in word2 and char not in common:
        common.append(char)

print("Common characters:", common)