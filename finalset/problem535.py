numbers = list(map(int, input("Enter numbers: ").split()))

count = 0

for number in numbers:
    digits = str(abs(number))
    repeated = 0

    for digit in set(digits):
        if digits.count(digit) > 1:
            repeated += 1

    if repeated == 2:
        count += 1

print("Numbers with exactly two repeated digits:", count)