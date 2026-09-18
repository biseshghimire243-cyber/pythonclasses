numbers = list(map(int, input("Enter numbers: ").split()))

result = []

for number in numbers:
    digits = str(abs(number))

    if len(set(digits)) < len(digits):
        result.append(number)

print("Numbers with repeated digits:", result)