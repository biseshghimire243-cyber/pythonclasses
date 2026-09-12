numbers = list(map(int, input("Enter numbers: ").split()))

largest = numbers[0] * numbers[1]

for i in range(1, len(numbers) - 1):
    product = numbers[i] * numbers[i + 1]

    if product > largest:
        largest = product

print("Largest adjacent product:", largest)