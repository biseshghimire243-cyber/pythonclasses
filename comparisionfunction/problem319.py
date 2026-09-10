number = int(input("Enter a number: "))

a, b = 0, 1

while a < number:
    a, b = b, a + b

if a == number:
    print("Fibonacci number")
else:
    print("Not a Fibonacci number")