numbers = list(map(int, input("Enter numbers: ").split()))

if len(numbers) < 2:
    print("At least two numbers are required.")
else:
    smallest_difference = abs(numbers[0] - numbers[1])
    best_pair = (numbers[0], numbers[1])

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            difference = abs(numbers[i] - numbers[j])

            if difference < smallest_difference:
                smallest_difference = difference
                best_pair = (numbers[i], numbers[j])

    print("Most balanced pair:", best_pair)
    print("Difference:", smallest_difference)