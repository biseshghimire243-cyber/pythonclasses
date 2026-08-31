numbers = [25, 103, 7, 4567, 82, 99999]

largest = numbers[0]

for number in numbers:
    if len(str(number)) > len(str(largest)):
        largest = number

print("Number with maximum digits:", largest)
print("Number of digits:", len(str(largest)))