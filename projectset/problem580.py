numbers = list(map(int, input("Enter numbers: ").split()))

count = 0

for number in numbers:
    if number % 4 == 0:
        count += 1

print("Count:", count)