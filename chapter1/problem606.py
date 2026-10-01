numbers = list(map(int, input("Enter numbers: ").split()))

result = []

for number in numbers:
    product = 1

    for digit in str(abs(number)):
        product *= int(digit)

    if product % 2 == 0:
        result.append(number)

print("Numbers:", result)