base = float(input("Enter base: "))
exponent = int(input("Enter exponent: "))

result = 1

for _ in range(abs(exponent)):
    result *= base

if exponent < 0:
    result = 1 / result

print("Result:", result)