words = input("Enter words: ").split()

longest = ""

for word in words:
    valid = True

    for i in range(len(word) - 1):
        current_is_digit = word[i].isdigit()
        next_is_digit = word[i + 1].isdigit()

        if current_is_digit == next_is_digit:
            valid = False
            break

    if valid and len(word) > len(longest):
        longest = word

if longest:
    print("Longest alternating word:", longest)
else:
    print("No valid word found.")