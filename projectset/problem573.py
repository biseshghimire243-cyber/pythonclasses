numbers = list(map(int, input("Enter numbers: ").split()))

result = []

for number in numbers:
    digits = str(abs(number))

    first_digit = int(digits[0])
    last_digit = int(digits[-1])

    if first_digit % 2 == 0 and last_digit % 2 != 0:
        result.append(number)

print("Matching numbers:", result)