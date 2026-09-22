numbers = list(map(int, input("Enter numbers: ").split()))

result = []

for number in numbers:
    digits = [int(digit) for digit in str(abs(number))]

    digit_sum = sum(digits)

    digit_product = 1
    for digit in digits:
        digit_product *= digit

    if digit_sum > digit_product:
        result.append(number)

print("Matching numbers:", result)