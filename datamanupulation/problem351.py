text = input("Enter a string: ")
positions = int(input("Enter positions to rotate: "))

positions = positions % len(text)

result = text[positions:] + text[:positions]

print("Rotated string:", result)