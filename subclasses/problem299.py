numbers = list(map(int, input("Enter numbers: ").split()))

largest_gap = 0
pair = None

for i in range(len(numbers) - 1):
    gap = abs(numbers[i + 1] - numbers[i])

    if gap > largest_gap:
        largest_gap = gap
        pair = (numbers[i], numbers[i + 1])

print("Largest gap:", largest_gap)
print("Between:", pair)