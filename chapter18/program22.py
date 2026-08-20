numbers = [10, 15, 22, 31, 40, 53, 64]

total = 0

for number in numbers:
    if number % 2 == 0:
        total += number

print("Sum of even numbers:", total)