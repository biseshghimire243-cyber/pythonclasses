numbers = list(map(int, input("Enter numbers: ").split()))

best_number = None
highest_product = -1

for number in numbers:
    product = 1

    for digit in str(abs(number)):
        product *= int(digit)

    if product > highest_product:
        highest_product = product
        best_number = number

print("Number:", best_number)
print("Digit product:", highest_product)