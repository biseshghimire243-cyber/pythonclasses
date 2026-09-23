numbers = list(map(int, input("Enter numbers: ").split()))

if len(numbers) < 2:
    print("At least two numbers are required.")
else:
    largest_product = numbers[0] * numbers[1]
    best_pair = (numbers[0], numbers[1])

    for i in range(1, len(numbers) - 1):
        product = numbers[i] * numbers[i + 1]

        if product > largest_product:
            largest_product = product
            best_pair = (numbers[i], numbers[i + 1])

    print("Best pair:", best_pair)
    print("Largest product:", largest_product)