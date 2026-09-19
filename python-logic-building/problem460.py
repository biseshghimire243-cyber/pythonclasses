numbers = list(map(int, input("Enter numbers: ").split()))

count = 0

for number in numbers:
    if 100 <= abs(number) <= 999:
        count += 1

print("Three-digit numbers:", count)