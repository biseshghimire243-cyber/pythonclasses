numbers = list(map(int, input("Enter numbers: ").split()))

count = 0

for number in numbers:
    if len(str(abs(number))) > 2:
        count += 1

print("Count:", count)