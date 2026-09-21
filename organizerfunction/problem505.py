numbers = list(map(int, input("Enter numbers: ").split()))

smallest = min(numbers)
largest = max(numbers)

total = 0

for number in numbers:
    if smallest < number < largest:
        total += number

print("Smallest:", smallest)
print("Largest:", largest)
print("Sum between them:", total)