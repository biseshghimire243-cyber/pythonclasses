numbers = list(map(int, input("Enter numbers: ").split()))

best_number = None
smallest_product = None

for number in numbers:
    product = 1

    for digit in str(abs(number)):
        product *= int(digit)

    if smallest_product is None or product < smallest_product:
        smallest_product = product
        best_number = number

print("Number:", best_number)
print("Smallest digit product:", smallest_product)