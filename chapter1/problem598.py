numbers = list(map(int, input("Enter numbers: ").split()))

if len(numbers) < 2:
    print("Need at least two numbers")
else:
    largest_gap = 0

    for i in range(1, len(numbers)):
        gap = abs(numbers[i] - numbers[i - 1])

        if gap > largest_gap:
            largest_gap = gap

    print("Largest gap:", largest_gap)