numbers = list(map(int, input("Enter numbers: ").split()))

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

unique = [num for num in numbers if frequency[num] == 1]

print("Elements appearing exactly once:", unique)