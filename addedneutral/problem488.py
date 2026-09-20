numbers = list(map(int, input("Enter numbers: ").split()))

largest_difference = 0
pair = ()

for i in range(len(numbers) - 1):
    difference = abs(numbers[i] - numbers[i + 1])

    if difference > largest_difference:
        largest_difference = difference
        pair = (numbers[i], numbers[i + 1])

print("Largest adjacent difference:", largest_difference)
print("Pair:", pair)