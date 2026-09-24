numbers = list(map(int, input("Enter numbers: ").split()))

result = []

for number in numbers:
    digits = str(abs(number))

    if len(digits) == len(set(digits)):
        result.append(number)

print("Numbers with no repeated digits:", result)