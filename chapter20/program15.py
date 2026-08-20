sentence = input("Enter a sentence: ")
word = input("Enter word to count: ")

words = sentence.lower().split()

count = words.count(word.lower())

print("Word appears", count, "time(s).")