numbers = list(map(int, input("Enter numbers: ").split()))

if numbers:
    smallest_digits = min(len(str(abs(number))) for number in numbers)

    candidates = []

    for number in numbers:
        if len(str(abs(number))) == smallest_digits:
            candidates.append(number)

    print("Largest number with smallest digit count:", max(candidates))
    print("Digit count:", smallest_digits)
else:
    print("No numbers entered.")