numbers = list(map(int, input("Enter numbers: ").split()))

if numbers:
    average = sum(numbers) / len(numbers)

    longest = 0
    current = 0

    for number in numbers:
        if number < average:
            current += 1
            longest = max(longest, current)
        else:
            current = 0

    print("Average:", round(average, 2))
    print("Longest sequence below average:", longest)
else:
    print("No numbers entered.")