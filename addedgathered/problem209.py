numbers = list(map(int, input("Enter numbers: ").split()))

total = 0

for i in range(0, len(numbers), 2):
    total += numbers[i]

print("Sum of numbers at odd positions:", total)