numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target number: "))

nearest = min(numbers, key=lambda x: abs(x - target))

print("Nearest number:", nearest)
print("Difference:", abs(nearest - target))