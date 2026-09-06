sentence = input("Enter a sentence: ")

words = sentence.split()

if words:
    shortest = min(words, key=len)

    print("Shortest word:", shortest)
    print("Length:", len(shortest))
else:
    print("No words entered.")