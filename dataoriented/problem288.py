text = input("Enter a string: ")

result = ""

for char in text:
    if not char.isdigit():
        result += char

print("Result:", result)