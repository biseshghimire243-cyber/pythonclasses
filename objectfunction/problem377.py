word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

count = 0

for a, b in zip(word1, word2):
    if a == b:
        count += 1
    else:
        break

print("Common prefix length:", count)