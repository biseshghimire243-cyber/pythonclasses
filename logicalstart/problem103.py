number = int(input("Enter a number: "))

square = number ** 2

if str(square).endswith(str(number)):
    print("Automorphic number")
else:
    print("Not an automorphic number")