numbers = list(map(int, input("Enter numbers: ").split()))

unique_numbers = list(set(numbers))

if len(unique_numbers) >= 2:
    unique_numbers.sort(reverse=True)
    print("Second largest:", unique_numbers[1])
else:
    print("Not enough unique numbers")