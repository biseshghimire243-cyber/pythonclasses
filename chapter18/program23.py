numbers = [11, 20, 33, 42, 55, 68, 71]

total = 0

for number in numbers:
    if number % 2 != 0:
        total += number

print("Sum of odd numbers:", total)