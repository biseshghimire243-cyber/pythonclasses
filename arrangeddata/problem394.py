sentence = input("Enter a sentence: ")
letter = input("Enter ending letter: ").lower()

words = sentence.split()
count = 0

for word in words:
    if word.lower().endswith(letter):
        count += 1

print("Matching words:", count)