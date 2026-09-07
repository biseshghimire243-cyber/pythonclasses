sentence = input("Enter a sentence: ")

words = sentence.split()
count = 0

for word in words:
    clean = word.lower().strip(".,!?")

    if len(set(clean)) < len(clean):
        count += 1

print("Words containing repeated letters:", count)