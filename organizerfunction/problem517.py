numbers = list(map(int, input("Enter numbers: ").split()))

best_number = None
largest_difference = -1

for number in numbers:
    digits = [int(digit) for digit in str(abs(number))]

    if len(digits) > 1:
        difference = max(digits) - min(digits)

        if difference > largest_difference:
            largest_difference = difference
            best_number = number

if best_number is not None:
    print("Number:", best_number)
    print("Largest digit difference:", largest_difference)
else:
    print("No suitable number found.")