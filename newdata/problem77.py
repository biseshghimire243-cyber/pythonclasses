numbers = [2, 4, 2, 6, 4, 2, 8, 4, 2]

frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

mode = max(frequency, key=frequency.get)

print("Numbers:", numbers)
print("Mode:", mode)
print("Frequency:", frequency[mode])