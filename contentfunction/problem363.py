numbers = list(map(int, input("Enter numbers: ").split()))

best_pair = None
best_difference = -1

for i in range(len(numbers) - 1):
    difference = numbers[i + 1] - numbers[i]

    if difference > best_difference and difference > 0:
        best_difference = difference
        best_pair = (numbers[i], numbers[i + 1])

if best_pair:
    print("Pair:", best_pair)
else:
    print("No increasing pair found")