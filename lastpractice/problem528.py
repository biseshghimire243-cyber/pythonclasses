words = input("Enter words: ").split()

shortest = ""

for word in words:
    if len(word) == len(set(word.lower())):
        if shortest == "" or len(word) < len(shortest):
            shortest = word

if shortest:
    print("Shortest word with unique characters:", shortest)
else:
    print("No valid word found.")