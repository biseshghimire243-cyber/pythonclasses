sentence = input("Enter a sentence: ")

words = sentence.split()
longest = ""

for word in words:
    clean = word.strip(".,!?").lower()

    if clean == clean[::-1] and len(clean) > len(longest):
        longest = clean

if longest:
    print("Longest palindromic word:", longest)
else:
    print("No palindromic word found.")