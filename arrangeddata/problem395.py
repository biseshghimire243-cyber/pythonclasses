numbers = list(map(int, input("Enter numbers: ").split()))

pairs = []

for i in range(len(numbers) - 1):
    if numbers[i] == numbers[i + 1]:
        pairs.append((numbers[i], numbers[i + 1]))

print("Consecutive duplicate pairs:", pairs)