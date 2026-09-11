text = input("Enter a string: ")
vowels = "aeiou"

result = ""

for char in text:
    if char.lower() in vowels:
        result += str(vowels.index(char.lower()) + 1)
    else:
        result += char

print("Result:", result)