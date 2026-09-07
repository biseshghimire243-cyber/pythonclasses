numbers = list(map(int, input("Enter numbers: ").split()))

frequency = {}

for i in range(len(numbers) - 1):
    pair = (numbers[i], numbers[i + 1])
    frequency[pair] = frequency.get(pair, 0) + 1

if frequency:
    pair = max(frequency, key=frequency.get)

    print("Most common pair:", pair)
    print("Occurrences:", frequency[pair])
else:
    print("Not enough numbers.")