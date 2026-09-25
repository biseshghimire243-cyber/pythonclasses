numbers = list(map(int, input("Enter numbers: ").split()))

found = None

for number in numbers:
    digits = str(abs(number))

    if all(int(digit) % 2 == 0 for digit in digits):
        found = number
        break

if found is not None:
    print("First number with all even digits:", found)
else:
    print("No matching number found.")