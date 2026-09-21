numbers = list(map(int, input("Enter numbers: ").split()))

result = []

for number in numbers:
    digits = str(abs(number))

    if len(digits) > 1 and int(digits[0]) > int(digits[-1]):
        result.append(number)

print("Matching numbers:", result)