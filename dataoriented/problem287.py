numbers = list(map(int, input("Enter numbers: ").split()))

mode = numbers[0]
highest_count = 0

for number in numbers:
    count = numbers.count(number)

    if count > highest_count:
        highest_count = count
        mode = number

print("Mode:", mode)
print("Frequency:", highest_count)