numbers = list(map(int, input("Enter numbers: ").split()))

count = 0

for number in numbers:
    digits = str(abs(number))

    if len(digits) > 1 and digits[0] in digits[1:]:
        count += 1

print("Count:", count)