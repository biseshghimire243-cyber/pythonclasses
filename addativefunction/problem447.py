numbers = list(map(int, input("Enter numbers: ").split()))

found = False

for i in range(1, len(numbers) - 1):
    if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
        print("First local maximum:", numbers[i])
        print("Position:", i)
        found = True
        break

if not found:
    print("No local maximum found")