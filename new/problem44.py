numbers = [45, 12, 78, 23, 9, 56, 34]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("Numbers:", numbers)
print("Smallest number:", smallest)