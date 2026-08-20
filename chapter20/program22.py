text = input("Enter text: ")

count = 0

for char in text:
    if char.isdigit():
        count += 1

print("Number of digits:", count)