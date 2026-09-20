words = input("Enter words: ").split()

best_word = ""
best_count = 0

for word in words:
    distinct = len(set(word.lower()))

    if distinct > best_count:
        best_count = distinct
        best_word = word

print("Word:", best_word)
print("Distinct characters:", best_count)