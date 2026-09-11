number = input("Enter a number: ")

even_digits = []

for digit in number:
    if int(digit) % 2 == 0:
        even_digits.append(int(digit))

if even_digits:
    print("Largest even digit:", max(even_digits))
else:
    print("No even digit found")