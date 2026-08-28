text = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
result = ""

for char in text:

    if char not in vowels:
        result += char

print("Original:", text)
print("Without vowels:", result)