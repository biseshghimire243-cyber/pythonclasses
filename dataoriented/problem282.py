text = input("Enter text: ")

numbers = []
current = ""

for char in text:
    if char.isdigit():
        current += char
    else:
        if current:
            numbers.append(current)
            current = ""

if current:
    numbers.append(current)

if numbers:
    print("Longest numeric value:", max(numbers, key=len))
else:
    print("No numeric value found")