numbers = list(map(int, input("Enter numbers: ").split()))

if len(numbers) >= 2:
    numbers.sort()

    product1 = numbers[0] * numbers[1]
    product2 = numbers[-1] * numbers[-2]

    maximum = max(product1, product2)

    print("Maximum product:", maximum)
else:
    print("At least two numbers are required.")