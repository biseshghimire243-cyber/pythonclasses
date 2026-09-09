number = int(input("Enter decimal number: "))
base = int(input("Enter base (2-16): "))

digits = "0123456789ABCDEF"
result = ""

if number == 0:
    result = "0"
else:
    while number > 0:
        result = digits[number % base] + result
        number //= base

print("Converted number:", result)