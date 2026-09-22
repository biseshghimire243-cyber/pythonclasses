numbers = list(map(int, input("Enter numbers: ").split()))

if len(numbers) < 2:
    print("At least two numbers are required.")
else:
    largest_product = numbers[0] * numbers[1]
    best_pair = (numbers[0], numbers[1])

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = numbers[i] * numbers[j]

            if product > largest_product:
                largest_product = product
                best_pair = (numbers[i], numbers[j])

    print("Best pair:", best_pair)
    print("Largest product:", largest_product)