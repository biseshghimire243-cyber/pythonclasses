numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

closest = min(numbers, key=lambda x: abs(x - target))

print("Closest value:", closest)