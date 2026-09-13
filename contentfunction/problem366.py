numbers = list(map(int, input("Enter numbers: ").split()))

increasing = True

for i in range(len(numbers) - 1):
    if numbers[i] >= numbers[i + 1]:
        increasing = False
        break

if increasing:
    print("List is strictly increasing")
else:
    print("List is not strictly increasing")