a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

original_a = a
original_b = b

while b != 0:
    a, b = b, a % b

gcd = a
lcm = abs(original_a * original_b) // gcd

print("LCM:", lcm)