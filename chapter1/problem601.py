words = input("Enter words: ").split()

if words:
    shortest = min(words, key=len)
    print("Shortest word:", shortest)
else:
    print("No words entered")