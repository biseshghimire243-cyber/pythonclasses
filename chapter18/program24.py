numbers = [10, 20, 30, 20, 40, 10, 50, 30]

duplicates = []

for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)

print("Duplicate values:", duplicates)