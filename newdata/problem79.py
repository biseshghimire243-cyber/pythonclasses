numbers = [10, 20, 30, 40, 50]

positions = int(input("Enter positions to rotate: "))

positions = positions % len(numbers)

rotated = numbers[positions:] + numbers[:positions]

print("Original:", numbers)
print("Left rotated:", rotated)