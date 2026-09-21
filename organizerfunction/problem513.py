numbers = list(map(int, input("Enter numbers: ").split()))

for number in numbers:
    digits = set(str(abs(number)))
    total = sum(int(digit) for digit in digits)

    print(f"{number} -> Sum of unique digits: {total}")