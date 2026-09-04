isbn = input("Enter ISBN-10: ").replace("-", "").upper()

if len(isbn) == 10:
    total = 0
    valid = True

    for i, char in enumerate(isbn):
        if char == "X" and i == 9:
            value = 10
        elif char.isdigit():
            value = int(char)
        else:
            valid = False
            break

        total += (i + 1) * value

    if valid and total % 11 == 0:
        print("Valid ISBN-10")
    else:
        print("Invalid ISBN-10")
else:
    print("ISBN must contain 10 characters.")