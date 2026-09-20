numbers = list(map(int, input("Enter numbers: ").split()))

if len(numbers) < 2:
    print("Not enough numbers.")
else:
    longest = 1
    current = 1

    for i in range(1, len(numbers) - 1):
        first_diff = numbers[i] - numbers[i - 1]
        second_diff = numbers[i + 1] - numbers[i]

        if second_diff > first_diff:
            current += 1
        else:
            current = 1

        longest = max(longest, current)

    print("Longest increasing difference sequence:", longest)