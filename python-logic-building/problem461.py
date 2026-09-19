numbers = list(map(int, input("Enter numbers: ").split()))

if numbers:
    result = numbers[0] + numbers[-1]
    print("Sum:", result)
else:
    print("List is empty")