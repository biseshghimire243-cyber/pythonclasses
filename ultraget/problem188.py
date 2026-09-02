a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    print("The sides can form a triangle.")

    if a == b == c:
        print("Type: Equilateral")
    elif a == b or b == c or a == c:
        print("Type: Isosceles")
    else:
        print("Type: Scalene")
else:
    print("The sides cannot form a triangle.")