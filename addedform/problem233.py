numbers = list(map(int, input("Enter numbers: ").split()))

unique_numbers = sorted(set(numbers), reverse=True)

if len(unique_numbers) >= 3:
    print("Third largest number:", unique_numbers[2])
else:
    print("Not enough unique numbers.")