numbers = list(map(int, input("Enter numbers: ").split()))

duplicates = []

for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)

print("Repeated numbers:", duplicates)