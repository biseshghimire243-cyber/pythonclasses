numbers = [123, 45, 678, 90]

total = 0

for number in numbers:
    while number > 0:
        total += number % 10
        number //= 10

print("Sum of all digits:", total)