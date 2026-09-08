numbers = list(map(int, input("Enter sequence: ").split()))

difference = numbers[1] - numbers[0]

for i in range(len(numbers) - 1):
    if numbers[i + 1] - numbers[i] != difference:
        missing = numbers[i] + difference
        print("Missing number:", missing)
        break
else:
    print("No missing number found")