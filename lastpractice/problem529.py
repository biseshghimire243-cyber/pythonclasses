numbers = list(map(int, input("Enter numbers: ").split()))

if len(numbers) < 3:
    print("At least three numbers are required.")
else:
    longest = 2
    current = 2

    previous_difference = numbers[1] - numbers[0]

    for i in range(2, len(numbers)):
        difference = numbers[i] - numbers[i - 1]

        if difference == previous_difference:
            current += 1
        else:
            current = 2

        longest = max(longest, current)
        previous_difference = difference

    print("Longest equal-difference sequence:", longest)