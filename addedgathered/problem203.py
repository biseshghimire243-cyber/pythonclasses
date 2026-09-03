numbers = list(map(int, input("Enter numbers: ").split()))

largest = max(numbers)
smallest = min(numbers)

print("Largest number:", largest)
print("Smallest number:", smallest)
print("Largest difference:", largest - smallest)