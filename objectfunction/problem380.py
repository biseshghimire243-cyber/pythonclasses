numbers = list(map(float, input("Enter numbers: ").split()))

if len(numbers) > 1:
    numbers.remove(max(numbers))
    average = sum(numbers) / len(numbers)
    print("Average:", average)
else:
    print("Need at least two numbers")