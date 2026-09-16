numbers = list(map(int, input("Enter numbers: ").split()))

differences = []

for i in range(len(numbers) - 1):
    differences.append(numbers[i + 1] - numbers[i])

print("Adjacent differences:", differences)