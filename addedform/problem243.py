words = input("Enter words separated by spaces: ").split()

if words:
    prefix = words[0]

    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]

            if not prefix:
                break

    print("Longest common prefix:", prefix)
else:
    print("No words entered.")