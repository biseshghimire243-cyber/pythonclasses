numbers = list(map(int, input("Enter numbers: ").split()))

product = 1
found = False

for number in numbers:
    if number > 0:
        product *= number
        found = True

if found:
    print("Product of positive numbers:", product)
else:
    print("No positive numbers found")