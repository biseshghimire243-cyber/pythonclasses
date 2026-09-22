numbers = list(map(int, input("Enter numbers: ").split()))

if len(numbers) < 3:
    print("At least three numbers are required.")
else:
    largest_sum = numbers[0] + numbers[1] + numbers[2]
    best_group = numbers[:3]

    for i in range(1, len(numbers) - 2):
        current_sum = numbers[i] + numbers[i + 1] + numbers[i + 2]

        if current_sum > largest_sum:
            largest_sum = current_sum
            best_group = numbers[i:i + 3]

    print("Best group:", best_group)
    print("Largest sum:", largest_sum)