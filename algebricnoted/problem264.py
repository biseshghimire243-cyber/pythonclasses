numbers = list(map(int, input("Enter numbers: ").split()))

if not numbers:
    print("List is empty.")
else:
    longest = 1
    current = 1
    best_number = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current += 1
        else:
            current = 1

        if current > longest:
            longest = current
            best_number = numbers[i]

    print("Number:", best_number)
    print("Longest consecutive sequence:", longest)