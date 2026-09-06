numbers = list(map(int, input("Enter numbers: ").split()))
difference = int(input("Enter required difference: "))

pairs = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if abs(numbers[i] - numbers[j]) == difference:
            pairs.append((numbers[i], numbers[j]))

print("Pairs:", pairs)