numbers = list(map(int, input("Enter numbers: ").split()))

unique = sorted(set(numbers))

if len(unique) >= 2:
    result = unique[0] + unique[1]
    print("Sum of two smallest numbers:", result)
else:
    print("Need at least two different numbers")