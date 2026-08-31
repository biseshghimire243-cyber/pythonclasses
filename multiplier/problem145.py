numbers = [1, 2, 3, 4, 6, 7, 8]

n = 8
expected = n * (n + 1) // 2
actual = sum(numbers)

print("Missing number:", expected - actual)