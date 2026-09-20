numbers = list(map(int, input("Enter numbers: ").split()))

numbers = sorted(set(numbers))

smallest_difference = None
pair = ()

for i in range(len(numbers) - 1):
    difference = numbers[i + 1] - numbers[i]

    if smallest_difference is None or difference < smallest_difference:
        smallest_difference = difference
        pair = (numbers[i], numbers[i + 1])

if smallest_difference is not None:
    print("Smallest positive difference:", smallest_difference)
    print("Pair:", pair)
else:
    print("Not enough numbers.")