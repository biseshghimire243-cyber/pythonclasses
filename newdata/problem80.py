numbers = [2, 7, 11, 15, 3, 6]
target = int(input("Enter target sum: "))

found = False

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):

        if numbers[i] + numbers[j] == target:
            print("Pair:", numbers[i], numbers[j])
            found = True

if not found:
    print("No pair found")