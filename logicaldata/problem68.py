numbers = [1, 2, 3, 4, 6, 7, 8, 9, 10]

n = 10

expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)

missing = expected_sum - actual_sum

print("Missing number:", missing)