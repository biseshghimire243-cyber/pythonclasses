numbers = list(map(int, input("Enter numbers: ").split()))

if not numbers:
    print("No numbers entered.")
else:
    longest = 1
    current = 1

    previous_sum = sum(int(digit) for digit in str(abs(numbers[0])))

    for i in range(1, len(numbers)):
        current_sum = sum(int(digit) for digit in str(abs(numbers[i])))

        if current_sum == previous_sum:
            current += 1
        else:
            current = 1

        longest = max(longest, current)
        previous_sum = current_sum

    print("Longest sequence with equal digit sums:", longest)