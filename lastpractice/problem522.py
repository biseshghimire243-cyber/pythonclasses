numbers = list(map(int, input("Enter numbers: ").split()))

result = []

for number in numbers:
    digits = str(abs(number))

    if len(digits) > 1:
        valid = True

        for i in range(len(digits) - 1):
            if digits[i] < digits[i + 1]:
                valid = False
                break

        if valid:
            result.append(number)

print("Numbers with descending digits:", result)