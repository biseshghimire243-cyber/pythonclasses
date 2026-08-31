numbers = [15, 42, 8, 73, 29, 61]

unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)

print("Second largest:", unique_numbers[1])