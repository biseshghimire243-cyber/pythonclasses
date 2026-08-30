a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("First number is largest")
elif b >= a and b >= c:
    print("Second number is largest")
else:
    print("Third number is largest")