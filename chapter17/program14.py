def find_minimum(numbers):
    minimum = numbers[0]

    for number in numbers:
        if number < minimum:
            minimum = number

    return minimum


numbers = [25, 67, 12, 89, 45]

print("Minimum number:", find_minimum(numbers))