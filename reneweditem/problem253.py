words = input("Enter words separated by spaces: ").split()

if words:
    reversed_words = [word[::-1] for word in words]
    prefix = reversed_words[0]

    for word in reversed_words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]

            if not prefix:
                break

    print("Longest common suffix:", prefix[::-1])
else:
    print("No words entered.")