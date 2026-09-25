numbers = list(map(int, input("Enter numbers: ").split()))

if len(numbers) < 2:
    print("Not enough numbers.")
else:
    changes = 0
    longest = 0
    current = 0

    for i in range(1, len(numbers)):
        if numbers[i] % 2 != numbers[i - 1] % 2:
            current += 1
            longest = max(longest, current)
        else:
            current = 0

    print("Longest alternating parity changes:", longest)