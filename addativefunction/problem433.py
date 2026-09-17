numbers = list(map(int, input("Enter numbers: ").split()))

numbers.sort(reverse=True)

if len(numbers) >= 2:
    print("Largest sum of two numbers:", numbers[0] + numbers[1])
else:
    print("Enter at least two numbers")