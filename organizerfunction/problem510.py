numbers = list(map(int, input("Enter numbers: ").split()))

best_number = None
highest_count = -1

for number in numbers:
    count = 0

    for digit in str(abs(number)):
        if int(digit) % 2 == 0:
            count += 1

    if count > highest_count:
        highest_count = count
        best_number = number

print("Number:", best_number)
print("Even digit count:", highest_count)