numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

most_frequent = max(frequency, key=frequency.get)

print("Most frequent number:", most_frequent)
print("Frequency:", frequency[most_frequent])