number = int(input("Enter a number: "))

number = abs(number)
product = 1

if number == 0:
    product = 0
else:
    while number > 0:
        digit = number % 10
        product *= digit
        number //= 10

print("Product of digits:", product)