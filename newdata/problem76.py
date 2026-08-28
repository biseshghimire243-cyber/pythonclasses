numbers = [12, 45, 23, 67, 34, 89, 56]

numbers.sort()

middle = len(numbers) // 2

if len(numbers) % 2 == 1:
    median = numbers[middle]
else:
    median = (numbers[middle - 1] + numbers[middle]) / 2

print("Sorted data:", numbers)
print("Median:", median)