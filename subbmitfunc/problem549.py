numbers = list(map(int, input("Enter numbers: ").split()))

if len(numbers) < 2:
    print("At least two numbers are required.")
else:
    numbers.sort()

    smallest_difference = numbers[1] - numbers[0]
    best_pair = (numbers[0], numbers[1])

    for i in range(1, len(numbers) - 1):
        difference = numbers[i + 1] - numbers[i]

        if difference < smallest_difference:
            smallest_difference = difference
            best_pair = (numbers[i], numbers[i + 1])

    print("Closest pair:", best_pair)
    print("Smallest difference:", smallest_difference)