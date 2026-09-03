numbers = list(map(int, input("Enter numbers: ").split()))

positive = [num for num in numbers if num > 0]

if positive:
    print("Smallest positive number:", min(positive))
else:
    print("No positive number found.")