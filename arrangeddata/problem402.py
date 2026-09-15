numbers = list(map(int, input("Enter numbers: ").split()))

average = sum(numbers) / len(numbers)

closest = numbers[0]
smallest_difference = abs(numbers[0] - average)

for number in numbers:
    difference = abs(number - average)

    if difference < smallest_difference:
        smallest_difference = difference
        closest = number

print("Average:", average)
print("Most balanced number:", closest)
print("Difference from average:", smallest_difference)