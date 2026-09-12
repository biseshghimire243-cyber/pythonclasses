text = input("Enter a string: ")

result = ""

for i in range(0, len(text), 2):
    result += text[i]

print("Result:", result)