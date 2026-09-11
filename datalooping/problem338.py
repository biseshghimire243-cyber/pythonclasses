numbers = list(map(int, input("Enter numbers: ").split()))

unique_numbers = set(numbers)

if unique_numbers:
    average = sum(unique_numbers) / len(unique_numbers)
    print("Unique numbers:", unique_numbers)
    print("Average:", round(average, 2))
else:
    print("No numbers found")