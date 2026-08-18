numbers = [10, 20, 10, 30, 20, 40, 30]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("Original:", numbers)
print("Without duplicates:", unique_numbers)