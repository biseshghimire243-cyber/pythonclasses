numbers = list(map(int, input("Enter numbers: ").split()))

if not numbers:
    print("No numbers entered.")
else:
    longest = 1
    current = 1
    best_value = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current += 1
        else:
            current = 1

        if current > longest:
            longest = current
            best_value = numbers[i]

    print("Value:", best_value)
    print("Longest sequence:", longest)