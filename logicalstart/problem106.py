number = int(input("Enter decimal number: "))

digits = "0123456789ABCDEF"
result = ""

if number == 0:
    result = "0"

while number > 0:
    remainder = number % 16
    result = digits[remainder] + result
    number //= 16

print("Hexadecimal:", result)