numbers = list(map(int, input("Enter numbers: ").split()))

result = []

for number in numbers:
    digit_sum = sum(int(digit) for digit in str(abs(number)))

    if digit_sum % 2 == 0:
        result.append(number)

print("Numbers with even digit sum:", result)