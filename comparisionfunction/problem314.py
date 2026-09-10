text = input("Enter a sentence: ")
words = text.split()

count = 0

for word in words:
    word = word.strip(".,!?").lower()
    if word and word[0] == word[-1]:
        count += 1

print("Count:", count)