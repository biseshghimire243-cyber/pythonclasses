def find_maximum(numbers):
    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum


numbers = [25, 67, 12, 89, 45]

print("Maximum number:", find_maximum(numbers))