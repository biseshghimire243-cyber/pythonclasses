numbers = [10, -5, 20, -8, 15, -3, 7]

positive = 0
negative = 0

for number in numbers:
    if number >= 0:
        positive += 1
    else:
        negative += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)