numbers = [1, 2, 3, 4, 5]

positions = int(input("Enter rotation positions: "))

positions = positions % len(numbers)

rotated = numbers[-positions:] + numbers[:-positions]

print("Original:", numbers)
print("Rotated:", rotated)