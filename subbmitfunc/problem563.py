numbers = list(map(int, input("Enter numbers: ").split()))

if not numbers:
    print("No numbers entered.")
else:
    longest = 1
    current = 1

    for i in range(1, len(numbers)):
        if numbers[i] == 0 or numbers[i - 1] == 0:
            current = 1
        elif (numbers[i] > 0 and numbers[i - 1] < 0) or \
             (numbers[i] < 0 and numbers[i - 1] > 0):
            current += 1
        else:
            current = 1

        longest = max(longest, current)

    print("Longest alternating sign sequence:", longest)