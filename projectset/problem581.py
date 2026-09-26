numbers = list(map(int, input("Enter numbers: ").split()))

highest_number = numbers[0]
highest_sum = 0

for number in numbers:
    total = sum(int(digit) for digit in str(abs(number)))

    if total > highest_sum:
        highest_sum = total
        highest_number = number

print("Number:", highest_number)
print("Digit sum:", highest_sum)