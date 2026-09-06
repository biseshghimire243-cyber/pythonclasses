numbers = list(map(int, input("Enter numbers: ").split()))

valleys = []

for i in range(1, len(numbers) - 1):
    if numbers[i] < numbers[i - 1] and numbers[i] < numbers[i + 1]:
        valleys.append(numbers[i])

print("Local valleys:", valleys)