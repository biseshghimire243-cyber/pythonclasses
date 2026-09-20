numbers = list(map(int, input("Enter numbers: ").split()))

count = 0

for number in numbers:
    digits = str(abs(number))

    if all(digits[i] < digits[i + 1] for i in range(len(digits) - 1)):
        count += 1

print("Numbers with increasing digits:", count)