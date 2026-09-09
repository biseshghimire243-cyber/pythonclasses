number = input("Enter a number: ")

repeated = []

for digit in set(number):
    if number.count(digit) > 1:
        repeated.append(digit)

if repeated:
    print("Repeated digits:", sorted(repeated))
else:
    print("No repeated digits")