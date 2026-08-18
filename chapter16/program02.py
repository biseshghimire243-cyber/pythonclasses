numbers = [34, 12, 89, 45, 67, 23]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest number:", largest)