numbers = list(map(int, input("Enter numbers: ").split()))

unique = sorted(set(numbers))

if len(unique) >= 2:
    print("Second smallest:", unique[1])
else:
    print("Not enough unique numbers")