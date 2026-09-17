numbers = list(map(int, input("Enter numbers: ").split()))

selected = numbers[::2]

if selected:
    print("Average:", sum(selected) / len(selected))
else:
    print("No numbers found")