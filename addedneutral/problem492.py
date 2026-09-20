numbers = list(map(float, input("Enter numbers: ").split()))

total = 0

for i, number in enumerate(numbers, start=1):
    total += number
    average = total / i

    print(f"After {i} numbers: {average:.2f}")