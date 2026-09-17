numbers = list(map(int, input("Enter numbers: ").split()))

positive = 0
negative = 0

for number in numbers:
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1

if positive == negative:
    print("Positive and negative numbers are balanced")
else:
    print("Positive:", positive)
    print("Negative:", negative)