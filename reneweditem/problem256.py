numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target sum: "))

triplets = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == target:
                triplets.append(
                    (numbers[i], numbers[j], numbers[k])
                )

print("Triplets:", triplets)