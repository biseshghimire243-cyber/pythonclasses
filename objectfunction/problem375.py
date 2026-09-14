numbers = list(map(int, input("Enter numbers: ").split()))
n = int(input("Enter N: "))

expected = n * (n + 1) // 2
actual = sum(numbers)

print("Missing value:", expected - actual)