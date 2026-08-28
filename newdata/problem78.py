numbers = [15, -7, 23, -12, 8, -4, 19]

positive = []
negative = []

for number in numbers:
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)

result = positive + negative

print("Original:", numbers)
print("Partitioned:", result)