numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("Original List:", numbers)
print("Without Duplicates:", unique_numbers)