sentence = input("Enter a sentence: ")
words = sentence.split()

vowels = "aeiou"

for word in words:
    count = 0

    for char in word.lower():
        if char in vowels:
            count += 1

    print(word, ":", count)