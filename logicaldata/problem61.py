numbers = [45, 12, 78, 23, 9, 67, 34]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

print("Numbers:", numbers)
print("Largest:", largest)
print("Smallest:", smallest)