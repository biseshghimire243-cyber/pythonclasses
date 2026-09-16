numbers = list(map(int, input("Enter numbers: ").split()))

result = []

for number in numbers:
    digits = str(abs(number))

    if digits[0] == digits[-1]:
        result.append(number)

print("Numbers with same first and last digit:", result)