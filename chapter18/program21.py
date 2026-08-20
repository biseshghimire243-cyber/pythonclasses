num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

a = num1
b = num2

while b != 0:
    a, b = b, a % b

gcd = a
lcm = abs(num1 * num2) // gcd

print("LCM:", lcm)