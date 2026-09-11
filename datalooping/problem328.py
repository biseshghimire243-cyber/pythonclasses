number = int(input("Enter a number: "))

square = number ** 2
digits = len(str(number))

right = square % (10 ** digits)
left = square // (10 ** digits)

if left + right == number:
    print("Kaprekar number")
else:
    print("Not a Kaprekar number")