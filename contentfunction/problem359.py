numbers = list(map(int, input("Enter numbers: ").split()))

count = 0

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        count += 1

print("Count:", count)