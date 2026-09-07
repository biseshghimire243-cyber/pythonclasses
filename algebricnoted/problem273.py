number = int(input("Enter a number: "))

if number >= 0:
    root = int(number ** 0.5)

    if root * root == number:
        print("Perfect square")
        print("Square root:", root)
    else:
        print("Not a perfect square")
else:
    print("Negative numbers cannot be perfect squares.")