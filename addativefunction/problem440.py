numbers = list(map(int, input("Enter numbers: ").split()))

total = 0

for number in numbers:
    total += number
    print("Running total:", total)