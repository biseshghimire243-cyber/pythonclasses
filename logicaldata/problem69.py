numbers = [10, -5, 20, -15, 30, -8, 40]

positive = []
negative = []

for number in numbers:
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)

print("Positive:", positive)
print("Negative:", negative)