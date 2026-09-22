numbers = list(map(int, input("Enter numbers: ").split()))

frequency = {}

for number in numbers:
    for digit in str(abs(number)):
        frequency[digit] = frequency.get(digit, 0) + 1

if frequency:
    highest = max(frequency.values())

    result = []

    for digit in frequency:
        if frequency[digit] == highest:
            result.append(digit)

    print("Most frequent digit(s):", result)
    print("Frequency:", highest)
else:
    print("No numbers entered.")