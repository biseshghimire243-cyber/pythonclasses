numbers = list(map(int, input("Enter numbers: ").split()))

average = sum(numbers) / len(numbers)
count = 0

for num in numbers:
    if num > average:
        count += 1

print("Average:", average)
print("Numbers greater than average:", count)