numbers = list(map(int, input("Enter numbers: ").split()))

frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

counts = sorted(set(frequency.values()), reverse=True)

if len(counts) >= 2:
    second_count = counts[1]
    result = [number for number in frequency if frequency[number] == second_count]

    print("Second most common number(s):", result)
    print("Frequency:", second_count)
else:
    print("There is no second most common number.")