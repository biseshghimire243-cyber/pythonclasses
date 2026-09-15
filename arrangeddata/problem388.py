numbers = list(map(int, input("Enter numbers: ").split()))

average = sum(numbers) / len(numbers)
maximum = max(numbers)

count = 0

for number in numbers:
    if average < number < maximum:
        count += 1

print("Average:", average)
print("Maximum:", maximum)
print("Count:", count)