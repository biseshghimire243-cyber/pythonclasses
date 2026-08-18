numbers = [10, -5, 7, -2, 8, -9, 4]

positive = 0
negative = 0

for number in numbers:
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)