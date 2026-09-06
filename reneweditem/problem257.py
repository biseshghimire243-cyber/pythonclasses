numbers = list(map(int, input("Enter numbers: ").split()))

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

majority = None

for num, count in frequency.items():
    if count > len(numbers) // 2:
        majority = num
        break

if majority is not None:
    print("Majority element:", majority)
else:
    print("No majority element found.")