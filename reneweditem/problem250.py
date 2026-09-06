numbers = list(map(int, input("Enter numbers: ").split()))

peaks = []

for i in range(1, len(numbers) - 1):
    if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
        peaks.append(numbers[i])

print("Local peaks:", peaks)