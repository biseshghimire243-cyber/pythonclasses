numbers = list(map(int, input("Enter numbers: ").split()))

positive_numbers = set(num for num in numbers if num > 0)

missing = 1

while missing in positive_numbers:
    missing += 1

print("First missing positive integer:", missing)