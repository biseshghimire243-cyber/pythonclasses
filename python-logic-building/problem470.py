numbers = list(map(int, input("Enter numbers: ").split()))

if numbers:
    largest = max(numbers)
    numbers.remove(largest)

print("After removing largest:", numbers)