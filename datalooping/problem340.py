text = input("Enter a string: ")

if not text:
    print("Empty string")
else:
    current_char = text[0]
    current_count = 1
    longest_char = text[0]
    longest_count = 1

    for char in text[1:]:
        if char == current_char:
            current_count += 1
        else:
            current_char = char
            current_count = 1

        if current_count > longest_count:
            longest_count = current_count
            longest_char = current_char

    print("Character:", longest_char)
    print("Count:", longest_count)