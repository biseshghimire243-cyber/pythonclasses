number = input("Enter a number: ")

digits = [int(digit) for digit in number]

digit_sum = sum(digits)

product = 1
for digit in digits:
    product *= digit

difference = product - digit_sum

print("Sum of digits:", digit_sum)
print("Product of digits:", product)
print("Difference:", difference)