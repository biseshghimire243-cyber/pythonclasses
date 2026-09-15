numbers = list(map(int, input("Enter numbers: ").split()))

positive = []
negative = []
zero = []

for number in numbers:
    if number > 0:
        positive.append(number)
    elif number < 0:
        negative.append(number)
    else:
        zero.append(number)

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)