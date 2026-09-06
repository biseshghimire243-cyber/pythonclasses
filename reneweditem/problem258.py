numbers = list(map(int, input("Enter numbers: ").split()))

total = sum(numbers)
left_sum = 0
found = False

for i in range(len(numbers)):
    total -= numbers[i]

    if left_sum == total:
        print("Equilibrium index:", i)
        found = True
        break

    left_sum += numbers[i]

if not found:
    print("No equilibrium index found.")