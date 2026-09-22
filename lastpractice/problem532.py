numbers = list(map(int, input("Enter numbers: ").split()))

if not numbers:
    print("No numbers entered.")
else:
    longest = 1
    current = 1

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current += 1
        else:
            current = 1

        longest = max(longest, current)

    print("Longest increasing sequence:", longest)