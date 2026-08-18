numbers = [45, 12, 78, 3, 56, 21]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("Smallest number:", smallest)