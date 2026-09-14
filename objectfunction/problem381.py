text = input("Enter a string: ")

result = ""
previous = ""

for char in text:
    if char != previous:
        result += char
    previous = char

print("Result:", result)