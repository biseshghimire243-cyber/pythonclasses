numbers = list(map(int, input("Enter numbers: ").split()))

best_number = None
highest_count = -1

for number in numbers:
    odd_count = 0

    for digit in str(abs(number)):
        if int(digit) % 2 != 0:
            odd_count += 1

    if odd_count > highest_count:
        highest_count = odd_count
        best_number = number

print("Number:", best_number)
print("Odd digit count:", highest_count)