a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

numbers = [a, b, c]
numbers.sort()

print("Median:", numbers[1])